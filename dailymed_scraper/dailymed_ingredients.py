"""
Build personal-care ingredient CSVs from DailyMed (NLM) product labels.

Columns: category, product_name, manufacturer, ingredients, price, dailymed_url, setid
  - ingredients: active ingredients first (with strength), then inactive ones,
    in label order, all in one cell separated by " | ".
  - price: DailyMed publishes no pricing, so this column is left blank to fill in.

Note: DailyMed only holds products that have an FDA-registered label (mostly OTC
drug products such as dandruff shampoos, fluoride toothpastes, sunscreen face and
body products). Plain cosmetics with no drug claim are often not listed.

Run:  python dailymed_ingredients.py [--max 150] [--out output]
"""

import argparse
import csv
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

API = "https://dailymed.nlm.nih.gov/dailymed/services/v2"
NS = {"v3": "urn:hl7-org:v3"}

# category -> (title search terms, title must contain one of, title must NOT contain any of)
CATEGORIES = {
    "Shampoo":    (["shampoo"], ["SHAMPOO"], ["LICE"]),
    "Toothpaste": (["toothpaste"], ["TOOTHPASTE", "TOOTH PASTE"], []),
    "Face Care":  (["face", "facial"], ["FACE", "FACIAL"], ["SHAMPOO", "TOOTHPASTE", "MASK, SURGICAL"]),
    "Hair Care":  (["conditioner", "hair", "scalp"], ["CONDITIONER", "HAIR", "SCALP"],
                   ["SHAMPOO", "HAIR OIL", "REMOVAL", "LICE", "GROWTH", "MINOXIDIL"]),
    "Body Care":  (["body lotion", "body wash", "body cream", "body"], ["BODY"],
                   ["SHAMPOO", "TOOTHPASTE", "LICE"]),
    "Hair Oil":   (["hair oil", "scalp oil"], ["HAIR OIL", "SCALP OIL"], []),
}

# Labels whose titles contain these are allergen extracts or oral/injected drugs, not personal care
NOT_PERSONAL_CARE = ["ALLERGEN", "ALLERGENS", "ALLERGENIC", "DANDER", "INJECTION", "TABLET", "CAPSULE", "PELLET"]


def has_word(text: str, words: list[str]) -> bool:
    return any(re.search(rf"(?<![A-Z]){re.escape(w)}(?![A-Z])", text) for w in words)


FIELDS = ["category", "product_name", "manufacturer", "ingredients", "price", "dailymed_url", "setid"]


def get(url: str, tries: int = 4) -> bytes:
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ingredient-list-builder/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(2 ** attempt)


def search(term: str, limit: int) -> list[dict]:
    out, page = [], 1
    while len(out) < limit:
        q = urllib.parse.urlencode({"title": term, "pagesize": 100, "page": page})
        data = json.loads(get(f"{API}/spls.json?{q}"))
        out.extend(data["data"])
        if not data["data"] or data["metadata"].get("next_page") in (None, "null"):
            break
        page += 1
    return out


def fmt_strength(ing) -> str:
    num = ing.find("v3:quantity/v3:numerator", NS)
    den = ing.find("v3:quantity/v3:denominator", NS)
    if num is None or not num.get("value"):
        return ""
    s = f"{num.get('value')} {num.get('unit', '')}".strip()
    if den is not None and den.get("value"):
        d = den.get("value")
        s += f"/{'' if d == '1' else d + ' '}{den.get('unit', '')}".rstrip()
    return s


def parse_label(setid: str) -> dict | None:
    root = ET.fromstring(get(f"{API}/spls/{setid}.xml"))
    org = root.find(".//v3:author//v3:representedOrganization/v3:name", NS)
    products = root.findall(".//v3:manufacturedProduct/v3:manufacturedProduct", NS)
    names, active, inactive = [], [], []
    for prod in products:
        n = prod.findtext("v3:name", default="", namespaces=NS).strip()
        if n and n not in names:
            names.append(n)
        for ing in prod.findall("v3:ingredient", NS):
            sub = ing.findtext("v3:ingredientSubstance/v3:name", default="", namespaces=NS).strip()
            if not sub:
                continue
            if ing.get("classCode", "").startswith("ACT"):
                st = fmt_strength(ing)
                item = f"{sub} ({st})" if st else sub
                if item not in active:
                    active.append(item)
            elif sub not in inactive:
                inactive.append(sub)
    if not (active or inactive):
        return None
    return {
        "product_name": " / ".join(names[:3]),
        "manufacturer": org.text.strip() if org is not None and org.text else "",
        "ingredients": " | ".join(active + [i for i in inactive if i not in active]),
        "price": "",
        "dailymed_url": f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={setid}",
        "setid": setid,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=150, help="max products per category")
    ap.add_argument("--out", default="output")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    used: set[str] = set()  # each label goes in one category only
    all_rows = []
    for category, (terms, must, never) in CATEGORIES.items():
        hits, seen = [], set()
        for term in terms:
            for h in search(term, args.max * 3):
                # match on the product part only, not the "[MANUFACTURER]" suffix
                t = h["title"].upper().split(" [")[0]
                if h["setid"] in seen or h["setid"] in used:
                    continue
                if not has_word(t, must) or has_word(t, never + NOT_PERSONAL_CARE):
                    continue
                seen.add(h["setid"])
                hits.append(h)
        hits = hits[: args.max * 2]  # extra headroom for labels that dedupe away

        with ThreadPoolExecutor(max_workers=4) as pool:
            parsed = list(pool.map(lambda h: (h, safe_parse(h["setid"])), hits))

        rows, names = [], set()
        for h, row in parsed:
            if not row:
                continue
            key = (row["product_name"].upper(), row["ingredients"])
            if key in names:
                continue
            names.add(key)
            used.add(h["setid"])
            rows.append({"category": category, **row})
            if len(rows) >= args.max:
                break
        rows.sort(key=lambda r: r["product_name"].upper())
        write_csv(out / (re.sub(r"\W+", "_", category.lower()) + ".csv"), rows)
        all_rows.extend(rows)
        print(f"{category}: {len(rows)} products")

    write_csv(out / "all_products.csv", all_rows)
    print(f"Total: {len(all_rows)} -> {out.resolve()}")


def safe_parse(setid: str):
    try:
        return parse_label(setid)
    except Exception as e:
        print(f"  skip {setid}: {e}")
        return None


def write_csv(path: Path, rows: list[dict]):
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
