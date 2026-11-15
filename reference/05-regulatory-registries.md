# 05 · Regulatory Registries

**Topic:** How to search and read FDA import alerts, FDA recalls, GRAS notices, the Food Additive Status List, the USDA Organic Integrity Database and the Indian registries, and how to record each check.
**Last reviewed:** 2026-11-14

> Record **every** check, including those that find nothing. "Searched, no match" is evidence; an unrecorded check is not.

---

## 1. FDA recalls

**Where:** https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts
**API:** openFDA enforcement reports. No key is needed for light use.

```
https://api.fda.gov/food/enforcement.json?search=product_description:"protein"+AND+recalling_firm:"BrandName"&limit=10
https://api.fda.gov/drug/enforcement.json?search=product_description:"shampoo"&limit=10
```

- **Supplements and food** → `food/enforcement`
- **OTC drugs** (anti-dandruff shampoo, sunscreen) → `drug/enforcement`
- **Cosmetics:** there is no openFDA enforcement endpoint. Use the FDA recalls page and filter by product type "Cosmetics".
- **Adverse events** for cosmetics and supplements → `food/event` (CAERS). These are reports, **not proof of cause**, and are never the basis of a rating.

**How to read a recall:**

| Field | Meaning |
|---|---|
| **Classification** | **Class I:** reasonable probability of serious harm or death. **Class II:** temporary or medically reversible harm. **Class III:** unlikely to cause harm |
| `status` | Ongoing / Completed / Terminated |
| `reason_for_recall` | E.g. undeclared allergen, benzene, microbial contamination |
| `code_info` | Lot numbers and expiry dates. **Compare these with the lot on the product photo** |
| `distribution_pattern` | Where it was sold |

**Scoring:**
- A Class I recall that covers this product or lot → **cap WI at 20** (`01` §4).
- Class II or III → note it in the report and use the recalled ingredient's risk tier.
- A recall of a *different* product from the same brand → note it as context only.

---

## 2. FDA import alerts

**Where:** https://www.accessdata.fda.gov/cms_ia/ialist.html

An import alert tells FDA field staff that products may be **detained without physical examination (DWPE)**.

| Term | Meaning |
|---|---|
| **Red List** | Firms or products currently subject to DWPE |
| **Green List** | Firms exempt from the alert (they showed compliance) |
| **Yellow List** | Firms under heightened surveillance (some alerts) |
| Industry code **53** | Cosmetics |
| Industry code **54** | Vitamins, minerals, proteins and dietary supplements |

**How to search:** open the alert list, search by country (e.g. India) and by firm or brand name, then open the alert and check the Red List section.

**Scoring:** the firm or product is on the Red List for a safety reason (e.g. mercury, heavy metals, undeclared drug ingredients) → **cap WI at 30**.

---

## 3. GRAS Notice Inventory

**Where:** https://www.fda.gov/food/generally-recognized-safe-gras/gras-notice-inventory

GRAS ("generally recognised as safe") lets an ingredient be used in food without pre-market approval as a food additive.

| FDA response | What it means for us |
|---|---|
| **"FDA has no questions"** | FDA accepts the notifier's GRAS conclusion for the stated use and level → supports a Low or no-concern rating |
| **"Notice does not provide a basis for a GRAS determination"** | FDA was not persuaded → at least **Moderate**, and the reason must be cited |
| **"FDA ceased to evaluate at the notifier's request"** | Withdrawn before a decision → **No authoritative data found** for GRAS status |

- **Self-affirmed GRAS** (a firm's own conclusion, never notified) is **not** in the inventory. Report: *"GRAS status self-determined; not reviewed by FDA."*
- GRAS applies to **specific uses and levels**. Check that the product's use matches.
- GRAS covers **food**. Dietary ingredients in supplements follow DSHEA (new dietary ingredient notifications) instead.

---

## 4. Food Additive Status List

**Where:** https://www.fda.gov/food/food-additives-petitions/food-additive-status-list

It lists the regulatory status of additives in alphabetical order. Each entry gives the CFR section and any limits. Key points:

- A CFR reference such as **21 CFR 172.xxx** means an approved food additive with conditions of use.
- **GRAS** or **GRAS/FS** means GRAS, or GRAS for a specific use.
- Some entries are marked as **prohibited** or have had their authorisation revoked (e.g. BVO, Red No. 3). Check the notes.
- Colour additives are covered separately in 21 CFR Parts 73/74.

Also check **Substances Added to Food**: https://www.fda.gov/food/food-additives-petitions/substances-added-food-formerly-eafus

---

## 5. USDA Organic Integrity Database (OID)

**Where:** https://organic.ams.usda.gov/integrity/

**How to search:**
1. Search for the **operation name** (the brand, manufacturer or "distributed by" name on the label), or for the certifier named under "Certified organic by …".
2. Open the operation's record and check:

| Field | What to look for |
|---|---|
| **Status** | **Certified** = valid. **Suspended / Revoked / Surrendered** = not valid |
| **Certifier** | Must match the certifier on the label |
| **Scope** | Crops / Livestock / Wild crops / **Handling** (manufacturers need Handling) |
| **Products** | The product category should be listed |
| **Effective date / anniversary date** | Certification must be current |

3. Download the certificate if one is available.

**Claim status:**
- Operation certified, product listed → **Verified**
- Operation certified, product not listed → **Unverifiable**
- Not found, or status not Certified, but the USDA seal is shown → **False**

**Imports:** under the Strengthening Organic Enforcement rule (compliance from March 2024), imported organic products need an NOP Import Certificate, and most handlers in the supply chain must be certified.

---

## 6. Other US lookups

| Registry | Use | URL |
|---|---|---|
| **DailyMed** (NLM) | Confirm the OTC "Drug Facts" for anti-dandruff shampoos: active ingredient and strength | https://dailymed.nlm.nih.gov |
| **NIH Dietary Supplement Label Database** | Compare a supplement label with its registered version | https://dsld.od.nih.gov |
| **FDA warning letters** | Firm-level enforcement (e.g. disease claims, contamination) | https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/warning-letters |
| **eCFR** | The current text of the rules cited | https://www.ecfr.gov |

---

## 7. India

| Registry | Use | URL |
|---|---|---|
| **FSSAI FoSCoS** | Check the 14-digit FSSAI licence or registration number on food or supplement labels: name, address and validity must match | https://foscos.fssai.gov.in |
| **Jaivik Bharat** | Verify Indian organic food claims and logos | https://jaivikbharat.fssai.gov.in |
| **FSSAI notifications and advisories** | Bans, standards, recalls (FSSAI Food Recall Procedure Regulations 2017). There is no searchable public recall database, so search FSSAI advisories and press releases | https://www.fssai.gov.in |
| **CDSCO**† | Registration of imported cosmetics (Cosmetics Rules 2020) | https://cdsco.gov.in |
| **State AYUSH licensing**† | The Ayurvedic manufacturing licence number printed on the label | https://ayush.gov.in |

† = proposed source; see `02` §5.

---

## 8. Barcodes and web links

- A **barcode (GTIN/EAN)** identifies the product, not its safety. Prefix 890 = issued by GS1 India; 00–13 = GS1 US. The prefix shows where the barcode was registered, **not** where the product was made.
- Use the barcode or link only to **identify** the product and fetch the official label from a **US sale website** (the brand's US site or a US retailer; see `02` §7). Never use a non-US sale site, even if its link was given. Ratings still come only from approved sources.
- If the web label and the photo label differ, **trust the photo** (the product in hand) and note the difference.

---

## 9. Check log template

Paste this into every report (`07-output-template.md`, section 6).

| # | Registry | Query used | Date searched | Result | Effect on score |
|---|---|---|---|---|---|
| 0 | Ingredient pull check (`06` §6) | `source URL` | YYYY-MM-DD | PASS / PARTIAL / FAIL (checks _) | Warning / confidence |
| 1 | FDA Recalls / openFDA | `brand + product type` | YYYY-MM-DD | No match / Recall Class _ (lot _) | None / Cap _ |
| 2 | FDA Import Alerts | `firm, country` | | | |
| 3 | GRAS / Food Additive Status List | `ingredient` | | | |
| 4 | USDA OID | `operation name` | | Certified / Not found | Claim status |
| 5 | FSSAI FoSCoS | `licence no.` | | Valid / Invalid | Claim status |
| 6 | DailyMed / DSLD | `product name` | | | |

---

## 10. NIH and FDA APIs for label pulls (process steps 1 and 3)

> Use these **official label APIs before any shopping website**. They return the registered label, including the full ingredient list, so the ingredient pull check (`06` §6) can usually PASS. None needs a key for light use. **Check the exact parameters against each API's documentation before building**, and cache every response with its date, so a demo never depends on a live call.

### 10.1 Which API for which product

| Product type | First source | Second source | If neither has it |
|---|---|---|---|
| **OTC drug** (anti-dandruff shampoo, sunscreen, medicated soap): has a "Drug Facts" box | **DailyMed** (NIH/NLM) | openFDA drug label | Back-label photo |
| **Dietary supplement**: has a "Supplement Facts" panel | **NIH Dietary Supplement Label Database (DSLD)** | Brand's US site | Back-label photo |
| **Cosmetic** (most shampoos, soaps, oils), e.g. Sri Sri Tattva Protein Shampoo | **No US government database lists cosmetic formulas** | Designated product page / brand's US site (`02` §7) | **Back-label photo** (required for a PASS) |

### 10.2 DailyMed: OTC drug labels (NIH/NLM)

| Call | Purpose |
|---|---|
| `GET https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name=head%20and%20shoulders` | Find labels (SPLs) by name; returns `setid`, title and version date |
| `GET https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{setid}.xml` | The full label: active ingredient and strength, **inactive ingredients**, warnings, directions |
| `GET https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{setid}/ndcs.json` | NDC codes for the label (to match a barcode) |

- **Read:** the active ingredient and its strength; the full inactive list, in label order.
- **Record:** `setid`, version date and URL as the source (e.g. Head & Shoulders Classic Clean: `f28a55cf-eb42-4a0d-a4a3-2bae72b58ac8`).
- **Pitfall:** one brand has many labels (Classic Clean, 2-in-1, "with Vitamin E"). Check 2 of the pull check (right variant) must match the title exactly.

### 10.3 Dietary Supplement Label Database (DSLD): supplement labels (NIH ODS)

| Call | Purpose |
|---|---|
| `GET https://api.ods.od.nih.gov/dsld/v9/search-filter?q=<brand product>` | Search labels; returns DSLD IDs |
| `GET https://api.ods.od.nih.gov/dsld/v9/label/{id}` | The full label: Supplement Facts rows (amount, %DV), **other ingredients**, serving size, claims, label images |

- **Pitfall:** DSLD keeps old label versions. Use the newest entry date, and compare it with the product photo if one is available.

### 10.4 Supporting NIH APIs (for steps 4 and 6)

| API | Use | Example call |
|---|---|---|
| **PubChem PUG REST** | Match an INCI or label name to a chemical identity and synonyms, to look it up in `04` | `GET https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/sodium%20laureth%20sulfate/synonyms/JSON` |
| **ODS fact sheets API** | Upper Limits and safety notes for Nutrition Balance | `https://ods.od.nih.gov/api/` |
| **RxNorm (RxNav)** | Standardise the names of OTC active ingredients | `GET https://rxnav.nlm.nih.gov/REST/drugs.json?name=pyrithione%20zinc` |

### 10.5 Related FDA API

| Call | Purpose |
|---|---|
| `GET https://api.fda.gov/drug/label.json?search=openfda.brand_name:"head and shoulders"&limit=5` | Second source for OTC labels: `active_ingredient`, `inactive_ingredient` fields |
| `GET https://api.fda.gov/drug/enforcement.json?search=...` | Recalls (see §1) |

### 10.6 Recording an API pull

Add each pull to the check log (§9) and to the product record's `pull_check` (`06` §7):

```yaml
pull_check:
  status: PASS | PARTIAL | FAIL
  source: dailymed | dsld | openfda | product_page | photo
  source_url: "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/<setid>.xml"
  source_id: "<setid or DSLD id>"
  label_version_date: YYYY-MM-DD
  pulled_at: YYYY-MM-DD
  checks_failed: []
```
