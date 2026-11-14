# 06 · Label-Reading Guide

**Topic:** How to read product photos (front and back), ingredient order, serving sizes and nutrition or supplement panels, and what to do when a label can't be read.
**Last reviewed:** 2026-11-14

> **Golden rule:** if a label can't be read, **say so; never guess.** Write `[UNREADABLE: <what and where>]`, or `[NOT AVAILABLE: <what>]` when a web source doesn't publish it.
> The product **is still scored** from what is known, with the ⚠️ "Full ingredient list not available" warning (`01` §4, Missing data).
>
> **Common case:** brand and retailer websites often publish only "key ingredients" (e.g. three herbs), not the full list. Record them as known ingredients, mark the rest `[NOT AVAILABLE: full ingredient list not published online]`, and ask for a back-label photo to complete the score.

---

## 1. Input scenarios

| Scenario | What the user gives | What we do |
|---|---|---|
| **A. Photos** | Front and back photos of both products | Extract all 10 fields below from the images |
| **B. Typed details** | A web link or barcode for each product | Identify the product, fetch its label text **from a US sale website**, and mark the source as "web label" |
| **C. Hybrid** | Photos plus links or barcodes | Read the photos first, then fill gaps from the web label (**US sale websites only**). **If they conflict, the photo wins**, and the difference is noted |

### Guardrails (demo)
- 🇺🇸 **US sale websites only.** Every online lookup (label, ingredients, claims, price, link or barcode) uses only websites that sell the product **in the United States**. See the allowed list in `02-approved-sources.md` §7.
  - ✅ For example: the brand's US site (e.g. headandshoulders.com/en-us, srisritattvausa.com), wholefoodsmarket.com, amazon.com, walmart.com, target.com, cvs.com, walgreens.com.
  - ❌ Not allowed: sites selling outside the US, such as a brand's India site (srisritattva.com), bigbasket.com, 1mg.com, apollopharmacy.in, flipkart.com, nykaa.com, or amazon.in.
  - If a user sends a non-US link, identify the product, then look it up on a US sale website. If no US site carries it, say: *"This product isn't listed on a US sale website, so I can only use the label photos you send."*
- **Product universe:** products sold in the US at **Whole Foods Market**, or **Sri Sri Tattva** products sold in the US (e.g. srisritattvausa.com, Amazon.com).
- **Market:** US. Prices are in **USD**, and US rules (FDA, USDA) give the legal status.
- **In scope:** personal care (soaps, shampoos, oils) and supplements.
- Out-of-scope product → reply: *"This demo covers personal care and supplements from Whole Foods and Sri Sri Tattva. I can still read the label, but the scoring hasn't been validated for this product."*
- **Compare like with like** (shampoo with shampoo, protein powder with protein powder). If the categories differ, say so and compare only the sub-scores that apply.

---

## 2. The 10 fields to extract

| # | Field | Where it is | Notes |
|---|---|---|---|
| 1 | **Brand and product name** | Front | Include the variant (e.g. "Chocolate", "Anti-Hairfall") |
| 2 | **Net quantity** | Front, bottom | mL, g, fl oz, oz, count. Needed for Quality ROI |
| 3 | **Price** | Typed by the user, or from a shelf photo or web listing | Note the currency and date |
| 4 | **Claims** | Front and back: badges, seals, slogans | Every claim goes to `03` |
| 5 | **Ingredients, in order** | Back | Exact spelling; keep brackets and percentages |
| 6 | **Active ingredients** | "Drug Facts" box (US OTC) or "Composition" (Ayurvedic) | Name and strength |
| 7 | **Nutrition or Supplement Facts panel** | Back or side | Serving size, servings per container, nutrients, %DV |
| 8 | **Allergens and warnings** | Back | "Contains:", "May contain", caution statements |
| 9 | **Regulatory identifiers** | Back or bottom | FSSAI licence (14 digits), AYUSH/drug licence no., NDC (US OTC), certifier name, veg/non-veg mark, organic seals |
| 10 | **Batch / lot, manufacturing and expiry dates, manufacturer and country** | Bottom, crimp or neck | Lot is needed to check recalls |

Record each field with a **confidence** mark: ✅ read clearly · ⚠️ partly read (state which part) · ❌ unreadable.

---

## 3. Reading the ingredient list

### Order means amount
- **Food and supplements (US):** listed in descending order of weight (21 CFR 101.4).
- **Cosmetics (US):** descending order of predominance, **except** that ingredients at **1% or less** may be listed in any order after those above 1%, and **colour additives may be listed last** in any order (21 CFR 701.3).
- **India (food):** descending order of weight or volume at the time of manufacture (FSSAI Labelling & Display Regulations 2020).
- **Practical rule:** the first 3–5 ingredients make up most of the product. A "hero" plant extract listed after the preservative (e.g. after phenoxyethanol, usually ≤1%) is present only in a **tiny amount**.

### Names to recognise
- **Cosmetics** use **INCI** names: *Aqua* = water, *Parfum* = fragrance, *Butyrospermum Parkii* = shea, *Cocos Nucifera* = coconut, *Sesamum Indicum* = sesame, *CI 42090* = FD&C Blue 1.
- **Ayurvedic** labels may use Sanskrit names with a botanical name: *Bhringraj* (Eclipta alba), *Amla* (Emblica officinalis), *Brahmi* (Bacopa monnieri), *Tila taila* (sesame oil).
- "-eth" or "PEG-" means **ethoxylated** (a 1,4-dioxane watch-point; Processing Level P3).
- "-paraben", "-isothiazolinone", "DMDM", "quaternium-15", "urea" (imidazolidinyl/diazolidinyl) → check `04`.
- "Fragrance", "parfum" or "aroma" is **one word that can hide many chemicals**.

### Compound ingredients
`Chocolate chips (sugar, cocoa butter, soy lecithin)`: list the sub-ingredients separately for scoring.

---

## 4. Reading the panels

### US Nutrition Facts (food)
1. **Serving size** first. All numbers are per serving.
2. **Servings per container.** Multiply if a person uses more.
3. **%DV:** 5% or less is low; 20% or more is high (FDA rule of thumb).
4. **Added sugars** has its own line and %DV.

### US Supplement Facts (21 CFR 101.36)
- Shows the **serving size** (e.g. "1 scoop (33 g)") and the amount and %DV of each dietary ingredient.
- **Proprietary blend:** only the total blend weight is required, not the amount of each ingredient → deduct under Nutrition Balance (`01` §3.4).
- `†` means "Daily Value not established".
- Compare the dose with **NIH ODS Upper Limits** at the **suggested daily use** (e.g. 2 scoops a day = 2 × panel).

### India nutrition information (FSSAI 2020)
- Given **per 100 g or 100 mL** and usually **per serve**, with %RDA per serve.
- **Green dot in a square = vegetarian; brown triangle in a square = non-vegetarian.**
- Health supplements must carry **"NOT FOR MEDICINAL USE"**.

### US Drug Facts (OTC anti-dandruff shampoo)
- **Active ingredient** and strength (e.g. "Pyrithione zinc 1%"), **purpose**, uses, warnings, directions, then **inactive ingredients**.
- The active and its strength must match 21 CFR 358.710 (see `03` §E).

---

## 5. Photo-reading tips

| Problem | What to do |
|---|---|
| **Glare or reflection** | Read the clear parts; mark the glare zone `[UNREADABLE: glare, lines 3–4 of ingredients]` |
| **Curved bottle; text wraps out of view** | Mark it as cut off: `[UNREADABLE: list continues beyond image edge]`. Ask for a side photo |
| **Very small font** | Read only what is certain; do not complete partial words from memory |
| **Several languages** | Use the English (or Hindi, if clear) panel; note the language |
| **Sticker over the original label** (imports) | Read both; the importer's sticker is the legal label for that market |
| **Blurry digits** (licence, lot, %) | Mark as ⚠️. Never round or infer a number |
| **Front and back from different variants** | Flag it and ask the user to confirm |

**Never:** guess an ingredient from the brand's other products, fill in a "typical" formula, or take the list from memory.

---

## 6. Hand-off to scoring

After extraction, build this record per product, then follow `01` → `03`/`04`/`05` → `07`.

```yaml
product: "<brand> <name> <variant>"
category: personal_care | supplement
market: US | India
net_qty: { value: 340, unit: mL }
price: { value: 390, currency: INR, date: 2026-11-14 }
claims: ["...", "..."]
actives: [{ name: "Pyrithione zinc", strength: "1%" }]
ingredients: ["Water", "Sodium Laureth Sulfate", "..."]
panel: { serving: "33 g", per_serving: { protein_g: 24, added_sugars_g: 2, sodium_mg: 130 } }
allergens: ["milk", "soy"]
identifiers: { fssai: "", ayush_licence: "", ndc: "", certifier: "", lot: "", expiry: "" }
unreadable: ["ingredients after 'Fragrance' (glare)"]
source: photo | web | hybrid
```
