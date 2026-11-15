"""
Scrape CVS.com personal-care products into a CSV:
    category, product_name, ingredients (pipe-separated), price, url

Setup (once):
    pip install playwright
    playwright install chromium

Run:
    python cvs_ingredients.py                    # all categories, 50 products each
    python cvs_ingredients.py --max 20 --headed  # visible browser (helps if CVS blocks headless)
    python cvs_ingredients.py --only shampoo toothpaste

Output: one CSV per category in ./output/ plus a combined all_products.csv.

CVS changes its site layout from time to time. If a category URL 404s, open
cvs.com, browse to the category and paste the URL into CATEGORIES below.
"""

import argparse
import csv
import json
import random
import re
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

BASE = "https://www.cvs.com"

# Category label -> CVS listing URL (check these in a browser if one returns nothing)
CATEGORIES = {
    "Shampoo":     f"{BASE}/shop/personal-care/hair-care/shampoo",
    "Toothpaste":  f"{BASE}/shop/personal-care/oral-care/toothpaste",
    "Face Care":   f"{BASE}/shop/skin-care/facial-skin-care",
    "Hair Care":   f"{BASE}/shop/personal-care/hair-care",
    "Body Care":   f"{BASE}/shop/skin-care/body-care",
    "Hair Oil":    f"{BASE}/shop/personal-care/hair-care/hair-treatments/hair-oils",
}

FIELDS = ["category", "product_name", "ingredients", "price", "url"]
PRODUCT_LINK = re.compile(r"/shop/[^\"'?#\s]+-prodid-\d+")


def polite_pause():
    time.sleep(random.uniform(1.5, 3.5))


def split_ingredients(text: str) -> str:
    """Split on commas that are not inside parentheses/brackets; join with ' | '."""
    if not text:
        return ""
    text = re.sub(r"^\s*(inactive\s+)?ingredients?\s*[:\-]?\s*", "", text.strip(), flags=re.I)
    parts, buf, depth = [], [], 0
    for ch in text:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    cleaned = [re.sub(r"\s+", " ", p).strip(" .;") for p in parts]
    return " | ".join(p for p in cleaned if p)


def collect_product_urls(page, url: str, limit: int) -> list[str]:
    urls: list[str] = []
    page_no = 1
    while len(urls) < limit:
        target = url if page_no == 1 else f"{url}?page={page_no}"
        try:
            page.goto(target, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(3000)
            for _ in range(6):  # trigger lazy loading
                page.mouse.wheel(0, 2500)
                page.wait_for_timeout(700)
        except PWTimeout:
            break
        found = []
        for href in PRODUCT_LINK.findall(page.content()):
            full = BASE + href
            if full not in urls and full not in found:
                found.append(full)
        if not found:
            break
        urls.extend(found)
        page_no += 1
        polite_pause()
    return urls[:limit]


def extract_jsonld_product(page) -> dict:
    for raw in page.locator('script[type="application/ld+json"]').all_text_contents():
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else data.get("@graph", [data])
        for item in items:
            if isinstance(item, dict) and item.get("@type") == "Product":
                return item
    return {}


def extract_price(page, ld: dict) -> str:
    offers = ld.get("offers")
    if isinstance(offers, list) and offers:
        offers = offers[0]
    if isinstance(offers, dict) and offers.get("price"):
        return f"${float(offers['price']):.2f}"
    for sel in ['[data-testid*="price"]', '[class*="price"]', 'meta[property="product:price:amount"]']:
        loc = page.locator(sel).first
        if loc.count():
            txt = loc.get_attribute("content") or loc.inner_text()
            m = re.search(r"\$?\s*(\d+(?:\.\d{2})?)", txt or "")
            if m:
                return f"${m.group(1)}"
    return ""


def extract_ingredients(page) -> str:
    # Expand an "Ingredients" accordion/tab if there is one
    for label in ("Ingredients", "INGREDIENTS"):
        btn = page.get_by_role("button", name=re.compile(label, re.I)).first
        if btn.count():
            try:
                btn.click(timeout=3000)
                page.wait_for_timeout(800)
            except Exception:
                pass
            break

    # Find text that follows an "Ingredients" heading
    text = page.evaluate(
        """() => {
            const els = [...document.querySelectorAll('h1,h2,h3,h4,h5,button,strong,b,span,div,p,dt')];
            for (const el of els) {
                const own = (el.childNodes.length === 1 ? el.textContent : '').trim();
                if (!/^(inactive\\s+)?ingredients:?$/i.test(own)) continue;
                let n = el.nextElementSibling;
                if (!n && el.parentElement) n = el.parentElement.nextElementSibling;
                while (n) {
                    const t = n.innerText.trim();
                    if (t.length > 15) return t;
                    n = n.nextElementSibling;
                }
            }
            return '';
        }"""
    )
    if text:
        return text

    # Fallback: regex over the visible page text
    body = page.inner_text("body")
    m = re.search(r"Ingredients?\s*:?\s*\n?(.{20,3000}?)(?:\n\s*\n|Warnings|Directions|Details|$)", body, re.S | re.I)
    return m.group(1).strip() if m else ""


def scrape_product(page, url: str, category: str) -> dict:
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(2500)
    ld = extract_jsonld_product(page)
    name = ld.get("name") or (page.locator("h1").first.inner_text() if page.locator("h1").count() else "")
    return {
        "category": category,
        "product_name": name.strip(),
        "ingredients": split_ingredients(extract_ingredients(page)),
        "price": extract_price(page, ld),
        "url": url,
    }


def write_csv(path: Path, rows: list[dict]):
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=50, help="products per category")
    ap.add_argument("--headed", action="store_true", help="show the browser window")
    ap.add_argument("--only", nargs="*", help="subset of categories, e.g. shampoo 'hair oil'")
    ap.add_argument("--out", default="output")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(exist_ok=True)
    wanted = {c.lower() for c in args.only} if args.only else None
    all_rows: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.headed)
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
            viewport={"width": 1366, "height": 900},
            locale="en-US",
        )
        page = ctx.new_page()

        for category, url in CATEGORIES.items():
            if wanted and category.lower() not in wanted:
                continue
            print(f"\n== {category}: {url}")
            urls = collect_product_urls(page, url, args.max)
            print(f"   found {len(urls)} product links")
            rows = []
            for i, purl in enumerate(urls, 1):
                try:
                    row = scrape_product(page, purl, category)
                    rows.append(row)
                    flag = "" if row["ingredients"] else "  (no ingredients found)"
                    print(f"   [{i}/{len(urls)}] {row['product_name'][:60]} {row['price']}{flag}")
                except Exception as e:
                    print(f"   [{i}/{len(urls)}] FAILED {purl}: {e}")
                polite_pause()
            fname = re.sub(r"\W+", "_", category.lower()).strip("_") + ".csv"
            write_csv(out / fname, rows)
            all_rows.extend(rows)

        browser.close()

    write_csv(out / "all_products.csv", all_rows)
    print(f"\nDone. {len(all_rows)} products written to {out.resolve()}")


if __name__ == "__main__":
    main()
