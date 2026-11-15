# 01 · Scoring Methodology

**Topic:** How the Wellbeing Index (0–100), its five 20% categories (Side Effects / Health Risks, Nutrition Value, Amazon Ratings, Claims Integrity, Sustainability), the risk tiers and the Quality ROI are calculated.
**Applies to:** Personal care (soaps, shampoos, oils) and supplements.
**Last reviewed:** 2026-11-15

> This tool informs product choice. It does not give medical advice.

---

## 1. What "wellbeing" means here

A product scores well when it **does its job (efficacy) without side effects**, judged on three things:

- **Body impact:** what the ingredients, additives and contaminants do to the person using it, and what they give it.
- **Environment impact:** packaging and ingredients that persist or pollute, such as microplastics and plastic-related chemicals.
- **Trust and experience:** whether the label tells the truth, and how satisfied US buyers are (Amazon ratings).

Every score is built only from the label, the approved sources in `02-approved-sources.md`, and (for Amazon Ratings) the product's amazon.com listing (`02` §8).

---

## 2. Risk tiers for individual ingredients

Every ingredient of concern gets exactly one tier, and **each tier must name the authority behind it**.

| Tier | Meaning | Typical evidence |
|---|---|---|
| **High** | Banned, restricted or prohibited for this use by a regulator in the market of sale, **or** a known human carcinogen (e.g. IARC Group 1) at a realistic exposure, **or** linked to a Class I recall or active import alert | FDA prohibited-ingredient rule, FDA recall, IARC Group 1, EPA hazard finding |
| **Moderate** | Restricted or banned in at least one major jurisdiction, a possible or probable carcinogen (IARC 2A/2B), a known endocrine-disruption concern, or a recognised skin sensitiser | EU/EFSA restriction, IARC 2A/2B, NIH/NIEHS finding |
| **Low** | Permitted, but with a known irritation, allergy or contamination watch-point | FDA guidance, NIH ODS fact sheet |
| **No authoritative data found** | None of the approved sources covers the ingredient | Write exactly: *"No authoritative data found."* |

Rules:

1. **Use the stricter rating when approved sources disagree**, but report the legal status in the market where the product is sold (see the conflict rule in `02-approved-sources.md`).
2. **IARC classifies hazard, not risk.** When a rating rests only on an IARC class, say so, and note the exposure route (e.g. "rinse-off, low exposure").
3. **Allergens are flagged separately** (see section 7) and are not toxicity ratings.
4. Contaminants (e.g. benzene, 1,4-dioxane, heavy metals) are only scored when a recall, import alert or published test result names **this product or batch**. Otherwise they are listed as a *watch-point* with no deduction.

---

## 3. The five categories

> **Structure set by VC feedback (2026-11-15):** five categories, **20% each**. *Update 2026-11-15: Conscious Branding was removed and replaced by Amazon Ratings.* This replaces the earlier five sub-scores (Ingredient Safety, Processing Level, Additives, Nutrition Balance, Claim Integrity). Their rules are kept inside the new categories: ingredient and additive risk → **Side Effects / Health Risks**; processing of supplements → **Nutrition Value**; ethoxylated and persistent ingredients → **Sustainability**.

Each category runs from 0 to 100. None can go below 0 or above 100.

| # | Category | Weight | Measures |
|---|---|---|---|
| 1 | **Side Effects / Health Risks** | 20% | Ingredients and additives that can harm the user |
| 2 | **Nutrition Value (based on ingredients)** | 20% | What the ingredients give the body (supplements) or the skin and hair (personal care) |
| 3 | **Amazon Ratings** | 20% | US buyers' average star rating on amazon.com |
| 4 | **Claims Integrity** | 20% | Whether the label's claims are true and verifiable |
| 5 | **Sustainability** | 20% | Environmental impact of packaging and ingredients |

### 3.1 Side Effects / Health Risks
**Score = average of the Ingredient Risk score (3.1a) and the Additive Risk score (3.1b).** Each flagged ingredient is deducted in exactly one of the two.

#### 3.1a Ingredient Risk
Covers actives, base ingredients and named contaminants. Starts at 100.

| Finding | Deduction |
|---|---|
| High-risk ingredient | −30 |
| Moderate-risk ingredient | −12 |
| Low-risk ingredient | −4 |
| No authoritative data found | 0 (listed; lowers confidence) |

**Position multiplier:** ×1.25 if the ingredient is among the **first five** on the list or is a declared **active ingredient** (round to the nearest whole point; e.g. −4 becomes −5, −12 becomes −15).

#### 3.1b Additive Risk
Additives are preservatives, colours, fragrance or flavour, sweeteners, fillers, emulsifiers, thickeners, opacifiers, pH adjusters, hydrotropes and chelators added for function rather than for the product's purpose. Ingredients that serve the product's purpose (surfactants, oils, conditioners, humectants such as glycerin or panthenol, protein sources) are not additives. Starts at 100.

| Finding | Deduction |
|---|---|
| Each additive (load) | −3 |
| Plus: High-risk additive | −30 |
| Plus: Moderate-risk additive | −12 |
| Plus: Low-risk additive | −4 |

The position multiplier applies to the **risk** deductions, not to the −3 load.

### 3.2 Nutrition Value (based on ingredients)
The checks differ because a supplement nourishes the body from inside and a personal-care product nourishes the skin or hair from outside. Starts at 100.

#### 3.2a Supplements: dietary nutrition
Based on one serving, with % Daily Value (%DV) from the label.

| Finding | Deduction |
|---|---|
| Added sugars >10% DV | −15 (>20% DV: −30) |
| Sodium >20% DV | −15 |
| Saturated fat >20% DV | −10 |
| Any nutrient above the NIH ODS Tolerable Upper Intake Level at the suggested daily use | −30 |
| Proprietary blend that hides individual amounts | −15 |
| **Processed** formula: protein isolates or extracts with few additives (adapted from the NOVA classification as described by FAO, 2019) | −5 |
| **Ultra-processed** formula: isolates plus flavours, sweeteners or other cosmetic additives | −15 |
| Fibre ≥10% DV | +5 |

#### 3.2b Personal care: skin and hair nourishment
Does the formula **balance cleansing with nourishment**, or strip and dry the skin or hair? This is the tool's own label-based rubric, not a risk rating.

**Nourishing ingredients** are plant oils and butters, humectants (glycerin, panthenol, aloe), proteins and amino acids, ceramides, and conditioning agents (silicones, guar hydroxypropyltrimonium chloride, polyquaterniums).

| Finding | Deduction |
|---|---|
| Harsh anionic surfactant (a sulfate or sulfonate, e.g. SLS, SLES, ammonium lauryl sulfate, olefin sulfonate) among the first 3 ingredients | −20 for the first, −10 for each additional one |
| Drying alcohol (alcohol denat., SD alcohol, isopropyl alcohol) among the first 5 ingredients | −15 |
| Nourishing ingredients appear only **after the first preservative**, so likely ≤1% (a "label-dressing" amount) | −10 |
| **No** nourishing ingredient anywhere on the list | −20 |
| Leave-on product (oil, lotion, cream) whose first ingredient is a nourishing oil, butter or humectant | +5 |

### 3.3 Amazon Ratings
**Definition:** how satisfied US buyers are with the product, from its average star rating on **amazon.com**. It reflects the "does its job" half of wellbeing as buyers experience it.

**Source:** the product's **amazon.com** listing only (a US sale website; not amazon.in or other Amazon country sites). Record the **ASIN**, the **average star rating**, the **number of ratings** and the **date read**. Keep a screenshot for the demo.

| Average rating (out of 5) | Score |
|---|---|
| 4.5 – 5.0 | 100 |
| 4.0 – 4.4 | 80 |
| 3.5 – 3.9 | 60 |
| 3.0 – 3.4 | 40 |
| Below 3.0 | 20 |

**Rules**
1. **Match the listing.** It must be the same product, variant and size. If Amazon pools ratings across sizes or variants, say so in the report.
2. **Few ratings:** 10–49 ratings → score with ⚠️ *"few ratings"* and Medium confidence. **Fewer than 10 ratings** → too few to score; treat as no rating.
3. **No amazon.com listing, or not yet looked up** → leave the category out; the other four categories are rescaled to 25% each, with the ⚠️ warning below.
4. **Ratings are opinions, not safety evidence.** They never change an ingredient's risk tier, a claim's status or a cap. A review describing a reaction may prompt a check of FDA recalls and adverse-event reports (`05` §1), but the review itself is not cited as evidence.
5. **Don't scrape Amazon.** Record ratings by hand from the listing, or through an Amazon API your account is licensed to use.

> ⚠️ **Amazon rating not available for <Product>.** This score uses the other four categories at 25% each. Needed: the product's amazon.com listing (ASIN, stars, number of ratings).

### 3.4 Claims Integrity
Every front and back claim is checked against `03-key-terms-registry.md` and the registries in `05-regulatory-registries.md`. Starts at 100.

| Status | Meaning | Deduction |
|---|---|---|
| **Verified** | Confirmed in an official registry (e.g. USDA Organic Integrity Database) | 0 |
| **Consistent** | Not registry-checked, but matches the ingredient list and its legal definition | 0 |
| **Unverifiable** | No legal definition, or no certificate or test found in approved sources | −10 |
| **Misleading** | Technically arguable but likely to create a false impression (e.g. "chemical-free") | −25 |
| **False** | Contradicted by the label, ingredients or a registry | −40 |
| **Missing required statement** | A statement the law requires is absent (e.g. the FDA disclaimer on a supplement structure/function claim) | −15 |

### 3.5 Sustainability
Environmental impact of the **packaging** and of **ingredients that persist or pollute**. This category answers the brief's questions on plastic, BPA and the environment. Starts at 100.

| Finding | Points | Authority / basis |
|---|---|---|
| Primary packaging: glass, aluminium, paper or carton | 0 | — |
| Recyclable plastic: PET (#1) or HDPE (#2) | −5 | Resin code on pack |
| Plastic, resin code not shown | −10 | — |
| Hard-to-recycle plastic: PVC (#3), PS (#6), other (#7, e.g. polycarbonate), multi-layer pouch or sachet | −15 | Resin code on pack |
| BPA-containing packaging (polycarbonate #7, epoxy-lined can) | −10 more | FDA; EFSA (see `04` §2.2) |
| Plastic microbeads in a rinse-off product | −30 (and the prohibited-ingredient cap) | Microbead-Free Waters Act 2015 (FDA) |
| PFAS ingredient ("perfluoro-", "polyfluoro-", PTFE) | −25 | EPA; FDA |
| Ethoxylated ingredient ("-eth", "PEG-"): 1,4-dioxane and aquatic-toxicity watch-point | −5 each, max −15 | EPA |
| Persistent synthetic polymer (silicones such as dimethicone, polyquaterniums, acrylates copolymers) | −5 each, max −15 | EPA (persistence) |
| Refill, concentrate or reduced-packaging format offered | +5 | — |
| Verified USDA Organic certification | +5 | USDA OID |
| EPA Safer Choice certified product | +5 | EPA Safer Choice |

- Environmental **claims** ("eco-friendly", "biodegradable") are judged in Claims Integrity, not here.
- If the packaging can't be seen or isn't described, make no packaging deduction and note *"packaging not confirmed"*.

---

## 4. Weights and the Wellbeing Index

**Wellbeing Index (WI) = average of the five category scores** (each weighted 20%), rounded to a whole number (halves round up, e.g. 81.5 → 82).

| Category | Weight |
|---|---|
| Side Effects / Health Risks | 20% |
| Nutrition Value (based on ingredients) | 20% |
| Amazon Ratings | 20% |
| Claims Integrity | 20% |
| Sustainability | 20% |
| **Total** | **100%** |

The same weights apply to **both** supplements and personal care.

### Hard caps (these override the computed score)

| Condition | WI capped at |
|---|---|
| Active Class I recall covering this product or lot | 20 |
| Recall for an undeclared major allergen covering this product | 20 |
| Contains an ingredient prohibited for this product type in the market of sale | 30 |
| Product or firm on an active FDA import alert (Red List) for a safety reason | 30 |

### Missing data: always rate, always warn

Every product gets a Wellbeing Index, even when data is missing. When data is missing, the score comes with a clear warning.

0. **Check the ingredient pull first.** Before any scoring, run the ingredient pull check in `06-label-reading-guide.md` §6. It confirms the right product, the full list (not just "key ingredients"), and a plausible formula (water and a cleanser in a shampoo, for example). **FAIL** → re-pull from the designated page or ask for a back-label photo. Score with the warning only if neither works.
1. **Never guess.** If part of the label can't be read or isn't published, say so (`[UNREADABLE: …]` / `[NOT AVAILABLE: …]`). Never fill the gap from memory or from a "typical" formula.
2. **Score from what is known.**
   - **Side Effects, Nutrition Value, Sustainability:** deduct only for known ingredients and packaging.
   - **Nutrition Value (supplements):** if the nutrition or supplement panel is missing, leave the category out and rescale the others.
   - **Amazon Ratings:** if there is no amazon.com listing, it hasn't been looked up, or it has fewer than 10 ratings, leave the category out and rescale the others (§3.3).
   - When a category is left out, the remaining categories share 100% equally (four categories → 25% each).
3. **Add the warning** to the score wherever it appears (quick answer, score table, verdict):

   > ⚠️ **Full ingredient list not available.** This score is based on <N> known ingredients (<source, e.g. "key ingredients from the brand website">). Ingredients we could not see may raise or lower it.

   Label the WI **Provisional** and show **data coverage**, e.g. *"3 known ingredients (key ingredients only)"* or *"13 of an estimated 18+ ingredients"*. Use the Amazon Ratings warning (§3.3) when the rating is missing.
4. **The warning affects the verdict wording.** If the higher-scoring product has an incomplete ingredient list, drop the verdict one level ("Clear winner" → "Leans toward"; "Leans toward" → "Comparable") and add *"pending the full label"*.
5. **Say what would complete the score**, e.g. a photo of the back label or the product's amazon.com listing.

**Confidence:**
- **High:** full label read, all ingredients covered by sources, and an Amazon rating with 50 or more ratings.
- **Medium:** 1–3 ingredients with no authoritative data, a minor unreadable section, or an Amazon rating based on 10–49 ratings.
- **Low:** the ingredient pull check failed, the full ingredient list is not available, a category was left out, or more than 3 ingredients are not covered by sources.

---

## 5. Bands

| WI | Band | Plain-language label |
|---|---|---|
| 80–100 | 🟢 Green | Strong choice |
| 60–79 | 🟡 Yellow | Good, with caveats |
| 40–59 | 🟠 Amber | Fair; use with care |
| 0–39 | 🔴 Red | Weak; prefer an alternative |

---

## 6. Quality ROI

> Problem statement: *"Quality ROI = Wellbeing Index / price / qty × 100."*

Read literally (WI ÷ price ÷ qty), a bigger pack would score worse, so the tool uses **WI per unit price**:

```
Price per 100   = Price ÷ (Net quantity in mL or g) × 100
Quality ROI     = WI ÷ Price per 100 × 100
```

- Compare ROI **only between products in the same currency and unit** (mL with mL, g with g).
- Higher ROI means more wellbeing per dollar.
- ROI is a **tie-breaker and value signal only**. It never overrides a safety cap.
- *Assumption to confirm with the project owner:* "qty" means net quantity in 100 mL or 100 g units.

**Example:** WI 80, $8.99 for 13.5 fl oz (399 mL) → price per 100 mL = $2.252 → ROI = 80 ÷ 2.252 × 100 ≈ **3,552**.

---

## 7. Efficacy, allergens and care groups (shown, not scored)

- **Fit-for-purpose check:** does the product contain an ingredient recognised by a regulator for the job it is bought for? Example: anti-dandruff actives in the FDA OTC monograph (21 CFR 358.710). If not, the verdict must say so even when the WI is higher.
- **Allergens:** flag the 9 US major food allergens (milk, egg, fish, crustacean shellfish, tree nuts, peanuts, wheat, soy, sesame) and the FSSAI-declared allergens wherever they appear, including in topical products.
- **Care groups:** children, pregnancy and breastfeeding, known allergies. Name a group only when an approved source supports it.

---

## 8. Comparing two products

| WI gap | Verdict wording |
|---|---|
| ≥10 points | "**Clear winner:** Product X" |
| 5–9 points | "**Leans toward** Product X" |
| <5 points | "**Comparable.**" Break the tie by Side Effects / Health Risks, then Claims Integrity, then Quality ROI |

A capped product can never win against an uncapped one.

---

## 9. Worked arithmetic (personal care, illustrative product)

| Category | Score | Weight | Points |
|---|---|---|---|
| Side Effects / Health Risks | 64.5 (Ingredient Risk 70, Additive Risk 59) | 20% | 12.9 |
| Nutrition Value (skin and hair) | 70 | 20% | 14.0 |
| Amazon Ratings | 100 (4.6 stars from 12,000 ratings) | 20% | 20.0 |
| Claims Integrity | 90 | 20% | 18.0 |
| Sustainability | 75 | 20% | 15.0 |
| **WI** | | | **79.9 → 80 (Green)** |

- **Nutrition Value:** SLES and SLS are both among the first 3 ingredients (−20, −10); conditioning agents come before the first preservative (no deduction) = 70.
- **Sustainability:** plastic bottle with no resin code (−10), one ethoxylated surfactant (−5), two persistent polymers (−10) = 75.

See `08-sample-comparisons.md` for full examples.
