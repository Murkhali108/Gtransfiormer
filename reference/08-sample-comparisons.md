# 08 · Sample Comparisons

**Topic:** Worked examples that set the standard for finished reports.
**Last reviewed:** 2026-11-14

> **Sample 1 uses real products** (the problem statement's use case), built from **public web labels only** (Scenario B in `06`). It shows how the tool handles a label that isn't fully published: it **does not guess**.
> **Samples 2 and 3 use made-up products** (Brands C–F) to show the full method; their registry results are illustrative.
> Ratings marked † assume the proposed EU source in `02` §5 is approved.

| # | Products | Market | Shows |
|---|---|---|---|
| 1 | **Head & Shoulders Classic Clean vs Sri Sri Tattva Protein Shampoo** (real) | US label / India | A real web-label evaluation; a product that is **not scored** because its full ingredient list isn't public; a fit-for-purpose check |
| 2 | Protein powder: whey vs plant (fictional) | US ($) | A false claim, a missing DSHEA disclaimer, an organic seal verified in the OID |
| 3 | Hair oil: Ayurvedic blend vs pure coconut (fictional) | India (₹) | A partly unreadable label → Provisional score; a "chemical-free" claim |

---

# Sample 1: Head & Shoulders Classic Clean vs Sri Sri Tattva Protein Shampoo

**Date:** 2026-11-14 · **Category:** Personal care · **Input:** Web label / search (no photos) · **Confidence:** Low
**Status:** ⏳ **Incomplete.** The verdict is held until the missing label data arrives (see "What we still need").

> **Read this first**
> - Both evaluations come from **public web labels**. The brand pages could not be opened directly from this session, so the facts below come from search results that quote DailyMed (the official US register of OTC drug labels, run by NIH) and the brands' own pages. Every fact is cited.
> - **Head & Shoulders formulas differ by country and variant.** The label used here is the **US "Classic Clean" shampoo** (DailyMed set ID `f28a55cf-eb42-4a0d-a4a3-2bae72b58ac8`), the only full official label found. An Indian pack may differ.
> - This is not a judgement of either brand's safety. It is not medical advice.

## ⚡ Quick answer (so far)
- **Head & Shoulders Classic Clean:** provisional **68 / 100 🟡**. It contains an FDA-recognised anti-dandruff active, so it does the anti-dandruff job.
- **Sri Sri Tattva Protein Shampoo:** **Not scored.** Its full ingredient list isn't published online; only three "key ingredients" are. We won't guess the rest.
- **For dandruff:** only Head & Shoulders has a recognised anti-dandruff active. **For dry hair without dandruff:** we can't say which is better until we see Sri Sri Tattva's full back label.

| | Head & Shoulders Classic Clean | Sri Sri Tattva Protein Shampoo |
|---|---|---|
| **Wellbeing Index** | 68 / 100 🟡 **(Provisional)** | **Not scored**: full ingredient list needed |
| **Quality ROI** | Needs price | Needs price |
| **Does the job it's bought for?** | Dandruff: **Yes** (pyrithione zinc 1%) | Dandruff: No active declared · Dry hair: unclear |
| **Biggest concern** | Zinc pyrithione (banned in EU cosmetics†), fragrance, two harsh surfactants first on the list | Unknown: the full formula isn't published |

## 1. Product snapshot

### Head & Shoulders Classic Clean Anti-Dandruff Shampoo (US label)
- **Maker:** Procter & Gamble · **Type:** OTC drug (US) · NDC prefix 37000-071 [DailyMed]
- **Net quantity / price:** sold in sizes including 13.5 fl oz and 28.2 fl oz [retailer listings]. **Price: not supplied.**
- **Claims on the brand page:** "Paraben Free", "24/7 Dandruff Protection", "for daily use" [headandshoulders.com]
- **Active ingredient:** **Pyrithione zinc 1%** (anti-dandruff) [DailyMed; H-E-B listing]
- **Inactive ingredients, in the order on the brand page:** 1. Water, 2. Sodium Lauryl Sulfate, 3. Sodium Laureth Sulfate, 4. Cocamidopropyl Betaine, 5. Sodium Xylenesulfonate, 6. Zinc Carbonate, 7. Fragrance, 8. Sodium Chloride, 9. Dimethicone, 10. Guar Hydroxypropyltrimonium Chloride, 11. Piroctone Olamine, 12. Glycerin, 13. Trihydroxystearin [headandshoulders.com, quoted in search results]
- **Also on the DailyMed label (position not confirmed):** Niacinamide, Polyquaternium-76, Neosetophoma Cerealis Extract, Blue 1, Red 33 [DailyMed]
- **Unreadable / unconfirmed:** `[NOT CONFIRMED: the full DailyMed inactive list could not be opened; the published list may contain further items such as preservatives]`
- **Allergens:** none of the major allergens in the confirmed list

### Sri Sri Tattva Protein Shampoo, for dry to normal hair (200 mL)
- **Maker:** Sri Veda Sattva Pvt Ltd (named on retailer pages) · **Market:** India
- **Net quantity / price:** 200 mL. **Price: not supplied.**
- **Claims:** "Ayurvedic", "natural ingredients" [srisritattva.com]; "Nourishes hair & reduces hair loss" [1mg]; "Provides strength & shine", "for dry to normal hair" [BigBasket]; "complies with all the safety and quality standards laid down by the AYUSH Ministry" [one retailer listing]
- **Key ingredients (as published):** Green gram, Fenugreek, Chickpea extract [srisritattva.com; Swadesii; Garuda Life]
- **Full ingredient list:** `[NOT AVAILABLE ONLINE: no retailer or brand page publishes the complete INCI list; one retailer says it appears only on the pack]`
- **Licence number (AYUSH/drug licence):** `[NOT AVAILABLE ONLINE]`

## 2. Ingredient risk check

| Product | Ingredient | Position | Tier | Why (plain language) | Authority |
|---|---|---|---|---|---|
| H&S | **Pyrithione zinc** | **active** | Moderate† | Approved by the FDA for dandruff at 1–2% in rinse-off shampoos. Banned in EU cosmetics since 2022 as a reproductive-toxicity hazard. In a shampoo it's rinsed off, so contact is short | [FDA, 21 CFR 358.710]; [EU Reg. 2021/1902]† |
| H&S | Sodium lauryl sulfate | #2 | Low | Can irritate skin and eyes with long contact | [PubChem] |
| H&S | Sodium laureth sulfate | #3 | Low | Mild irritant; possible 1,4-dioxane traces (no product test found → watch-point only) | [PubChem]; [EPA] |
| H&S | Cocamidopropyl betaine | #4 | Low | Occasional contact allergy | [FDA, allergens in cosmetics] |
| H&S | Fragrance | #7 (additive) | Moderate | Undisclosed mixture; a common cause of cosmetic allergy | [FDA, MoCRA / allergens in cosmetics] |
| H&S | Blue 1, Red 33 | end (additive) | Low | FDA-listed colour additives; rare allergy | [FDA, 21 CFR 74] |
| H&S | Piroctone olamine | #11 | No authoritative data found | Antifungal; no rating from a core approved source (EU limits it in cosmetics†) | — |
| H&S | Neosetophoma cerealis extract | unconfirmed | No authoritative data found | — | — |
| H&S | Zinc carbonate, niacinamide, glycerin, dimethicone, guar HPTC, polyquaternium-76 | — | Not flagged | — | — |
| SST | Green gram, fenugreek, chickpea extract | unknown | Not flagged | Plant extracts; no concern found. Chickpea is a legume, so people with legume allergies may want to check | — |
| SST | **Everything else** | — | **Cannot rate** | Full list not published | — |

**Watch-points (not scored):** 1,4-dioxane (H&S, from SLES): no product test or recall found.

## 3. Claim verification

| Product | Claim | Status | What we found |
|---|---|---|---|
| H&S | Anti-dandruff (Drug Facts use) | Consistent | Pyrithione zinc 1% is within the FDA monograph range for rinse-off products (21 CFR 358.710) |
| H&S | "Paraben Free" | Consistent* | No parabens in the confirmed list (*the list may be incomplete) |
| H&S | "24/7 Dandruff Protection" | Unverifiable (−10) | No legal definition; no study cited |
| SST | "Ayurvedic" | Unverifiable (−10) | No AYUSH licence number seen online. A licence on the pack would make this Consistent |
| SST | "Natural ingredients" | Unverifiable (−10) | "Natural" has no legal definition for cosmetics |
| SST | "Nourishes hair & reduces hair loss" | Unverifiable (−10) | No evidence in approved sources |
| SST | "Provides strength & shine" | Unverifiable (−10) | No evidence in approved sources |
| SST | "Complies with AYUSH standards" | Unverifiable | AYUSH is a proposed source† and no licence was seen |
| SST | "Protein shampoo" | Unverifiable | Protein sources (green gram, chickpea) are named, but their amounts are unknown |

## 4. Wellbeing Index

| Sub-score | Weight | Head & Shoulders | Sri Sri Tattva |
|---|---|---|---|
| Ingredient Safety | 35% | 70 | Insufficient data |
| Processing Level | 15% | 50 (P3: ethoxylated SLES) | Insufficient data |
| Additives | 15% | 59 *(provisional)* | Insufficient data |
| Nutrition Balance (skin and hair) | 20% | 70 | Insufficient data |
| Claim Integrity | 15% | 90 | 60 |
| **Wellbeing Index** | | **68 (Provisional)** (68.35) | **Not scored** |
| Caps | | None found | — |

- **H&S Ingredient Safety:** SLS −5, SLES −5, CAPB −5 (Low ×1.25, top five), pyrithione zinc −15 (Moderate ×1.25, active) = **70**
- **H&S Additives:** 7 confirmed additives (sodium xylenesulfonate, zinc carbonate, fragrance, sodium chloride, trihydroxystearin, Blue 1, Red 33) −21; fragrance −12; Blue 1 −4; Red 33 −4 = **59**. Provisional, because unconfirmed items could lower it
- **H&S Nutrition Balance:** SLS (#2) −20, SLES (#3) −10; conditioning agents (dimethicone, guar) come before the first preservative-type ingredient (piroctone olamine) = **70**
- **H&S Claim Integrity:** "24/7" −10 = **90**
- **Sri Sri Tattva:** under `01` §4, a product with no full ingredient list gets no Wellbeing Index. Scoring only the three key ingredients would make the product look cleaner than the evidence allows

**Quality ROI:** not calculated. Prices weren't supplied, and the two products would need the same currency.

## 5. Verdict (held)

**Better choice for the household:** ⏳ **Not decided yet.** One product can't be scored.

**What we can already say**
- **If someone has dandruff:** Head & Shoulders contains an FDA-recognised anti-dandruff active (pyrithione zinc 1%). Sri Sri Tattva doesn't declare one.
- **Head & Shoulders trade-offs:** it starts with two strong cleansers (SLS, SLES), and it contains fragrance and an active that the EU no longer allows in cosmetics†. Rinse it off well.
- **Sri Sri Tattva:** its herbal "protein" ingredients raise no concern, but its claims are unverified and the rest of its formula is unknown.

**Who should be careful**
- 🤧 **Allergies / sensitive skin:** Head & Shoulders has fragrance and cocamidopropyl betaine. Sri Sri Tattva is unknown; chickpea and green gram are legumes.
- 👶 **Children:** keep both out of the eyes. No child-specific concern found in approved sources.
- 🤰 **Pregnancy:** No authoritative data found from US or Indian regulators on rinse-off pyrithione zinc in pregnancy. The EU classification is a hazard classification†.

### What we still need to finish this comparison
1. A **photo of the back label** of Sri Sri Tattva Protein Shampoo: the full ingredient list and the AYUSH or drug licence number.
2. The **Head & Shoulders variant and pack you would actually buy** (Indian packs differ from the US label used here): a front and back photo.
3. **Prices and pack sizes** for both, in the same currency, to work out Quality ROI.

**In-store tip:** On any "Ayurvedic" shampoo, turn the bottle over. A licence number and a full ingredient list should be printed there. If they aren't, the claims can't be checked.

### Sources and checks

| # | Source | What it gave | Date |
|---|---|---|---|
| 1 | DailyMed (NLM/NIH): *Head and Shoulders Classic Clean, pyrithione zinc shampoo*, set ID f28a55cf-eb42-4a0d-a4a3-2bae72b58ac8. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f28a55cf-eb42-4a0d-a4a3-2bae72b58ac8 | Active ingredient, NDC, partial inactive list | 2026-11-14 (via search) |
| 2 | Head & Shoulders US product page: https://www.headandshoulders.com/en-us/products/classic-clean-shampoo | Inactive list order, "Paraben Free", "24/7" claims | 2026-11-14 (via search) |
| 3 | H-E-B listing: https://www.heb.com/product-detail/head-shoulders-classic-clean-dandruff-shampoo/10662535 | "Pyrithione Zinc (1 %)" | 2026-11-14 (via search) |
| 4 | Sri Sri Tattva product page: https://www.srisritattva.com/products/protein-shampoo-for-dry-to-normal-hair-200ml | Key ingredients, "Ayurvedic", "natural" | 2026-11-14 (via search) |
| 5 | Tata 1mg: https://www.1mg.com/otc/sri-sri-tattva-protein-shampoo-nourishes-hair-reduces-hair-loss-otc330764 | "Nourishes hair & reduces hair loss" | 2026-11-14 (via search) |
| 6 | BigBasket: https://bigbasket.com/pd/40262406/sri-sri-tattva-protein-shampoo-for-dry-to-normal-hair-provides-strength-shine-200-ml | "Strength & shine", "dry to normal hair" | 2026-11-14 (via search) |
| 7 | FDA, 21 CFR 358.710 (anti-dandruff actives): https://www.ecfr.gov/current/title-21/section-358.710 | Pyrithione zinc 1–2% rinse-off | — |
| 8 | FDA recalls / openFDA drug enforcement | Not yet searched for this product | To do |

Retailer pages (3, 5, 6) are used **only to identify the product and its label text**. They are never the basis of a risk rating.

---

# Sample 2: Brand C Whey Protein (Chocolate) vs Brand D Organic Plant Protein

**Date:** 2026-11-14 · **Market:** US (Whole Foods) · **Category:** Supplement · **Input:** Hybrid · **Confidence:** High

## ⚡ Quick answer
**Brand D** is the clear winner (87 vs 75): no additives, and its organic seal checks out. Brand C is better value per dollar, but one of its claims is false.

| | Brand C Whey | Brand D Plant |
|---|---|---|
| **Wellbeing Index** | 75 / 100 🟡 | 87 / 100 🟢 |
| **Quality ROI** | 1237.0 | 1109.5 |
| **Does the job?** | Yes (24 g protein) | Yes (21 g protein) |
| **Biggest concern** | "Natural flavor" claim is false; 3 sweeteners/flavours | Sodium 21% DV per scoop |

## 1. Product snapshot

### Brand C Whey Protein, Chocolate
- **Net quantity / price:** 2 lb (907 g) · $54.99 ($6.06 per 100 g)
- **Claims:** "24 g protein per serving", "Builds lean muscle", "Natural chocolate flavor", "Gluten-free"
- **Ingredients:** 1. Whey Protein Concentrate (Milk), 2. Whey Protein Isolate (Milk), 3. Cocoa Powder (processed with alkali), 4. Maltodextrin, 5. Natural and Artificial Flavors, 6. Xanthan Gum, 7. Soy Lecithin, 8. Sucralose, 9. Acesulfame Potassium
- **Supplement Facts (1 scoop, 33 g):** 130 kcal · protein 24 g · added sugars 1 g (2% DV) · sodium 130 mg (6% DV) · saturated fat 1 g (5% DV)
- **Allergens:** **Milk, soy**
- **DSHEA disclaimer:** ❌ not on the label

### Brand D Organic Plant Protein, Unflavored
- **Net quantity / price:** 18 oz (510 g) · $39.99 ($7.84 per 100 g)
- **Claims:** "USDA Organic", "Non-GMO Project Verified", "Vegan", "Heavy-metal tested"
- **Ingredients:** 1. Organic Pea Protein, 2. Organic Brown Rice Protein, 3. Organic Pumpkin Seed Protein
- **Supplement Facts (1 scoop, 30 g):** 120 kcal · protein 21 g · added sugars 0 g · sodium 480 mg (21% DV) · saturated fat 0.5 g (3% DV)
- **Allergens:** None of the major allergens
- **Certifier:** "Certified organic by [Certifier X]"

## 2. Ingredient risk check

| Product | Ingredient | Position | Tier | Why | Authority |
|---|---|---|---|---|---|
| C | Maltodextrin | #4 (additive) | Low | High-glycaemic filler | [FDA, GRAS] |
| C | Natural and artificial flavors | #5 (additive) | Low | Composition not disclosed | [FDA, 21 CFR 101.22] |
| C | Sucralose | #8 (additive) | Low | WHO advises against non-sugar sweeteners for weight control | [WHO 2023]; [FDA] |
| C | Acesulfame potassium | #9 (additive) | Low | As above | [WHO 2023]; [FDA] |
| D | Brown rice protein | #2 | Watch-point | Rice can carry inorganic arsenic; no product test result published | [FDA, arsenic in rice] |

## 3. Claim verification

| Product | Claim | Status | What we found |
|---|---|---|---|
| C | "24 g protein" | Consistent | Matches the panel |
| C | "Builds lean muscle" | **Missing required statement** (−15) | Structure/function claim without the FDA disclaimer (21 CFR 101.93) |
| C | "Natural chocolate flavor" | **False** (−40) | The ingredient list says "Natural **and Artificial** Flavors" |
| C | "Gluten-free" | Consistent | No gluten grains listed; no test certificate |
| D | "USDA Organic" | **Verified** | *Illustrative:* operation found in the USDA OID, status Certified, Handling scope, certifier matches the label |
| D | "Non-GMO Project Verified" | Unverifiable (−10) | Private certifier, not an approved source. Organic certification already excludes GMOs |
| D | "Vegan" | Consistent | All ingredients are plant-derived |
| D | "Heavy-metal tested" | Unverifiable (−10) | No results, lab or limits published |

## 4. Wellbeing Index

| Sub-score | Weight | Brand C | Brand D |
|---|---|---|---|
| Ingredient Safety | 35% | 100 | 100 |
| Processing Level | 15% | 25 (P4) | 50 (P3) |
| Additives | 15% | 65 | 100 |
| Nutrition Balance | 20% | 100 | 85 |
| Claim Integrity | 15% | 45 | 80 |
| **Wellbeing Index** | | **75** (75.25) | **87** (86.5) |

- **C Additives:** 6 additives −18; maltodextrin −5 (Low ×1.25, top five); flavours −4; sucralose −4; ace-K −4 = **65**
- **D Nutrition Balance:** sodium 21% DV −15 = **85**

| | Brand C | Brand D |
|---|---|---|
| Price per 100 g | $6.06 | $7.84 |
| **Quality ROI** | **1237.0** | **1109.5** |

## 5. Verdict
**Better choice:** Brand D (**clear winner**, a 12-point gap).
**Trade-offs**
- Brand C costs less per gram and has a bit more protein per scoop, but uses sweeteners and flavours and makes a false "natural flavor" claim.
- Brand D has more sodium. Two scoops a day gives about 42% of the daily sodium value.

**Who should be careful**
- 🤧 **Allergies:** Brand C contains **milk and soy**.
- 👶 **Children:** protein powders are made for adults; follow the label. No child-specific data in approved sources.
- 🤰 **Pregnancy:** No authoritative data found for these products. Ask a doctor before starting supplements.
- 🧂 **Watching salt:** Brand D, 480 mg sodium per scoop.

**In-store tip:** Read the flavour line on the back, not the front. "Natural and artificial flavors" means the front claim isn't the whole story.

---

# Sample 3: Brand E Herbal Hair Oil vs Brand F Pure Coconut Oil

**Date:** 2026-11-14 · **Market:** India · **Category:** Personal care · **Input:** Photos · **Confidence:** Medium (part of Brand E's label is unreadable)

## ⚡ Quick answer
**Brand F** is the clear winner (100 vs 85, provisional): one ingredient and no misleading claims. Neither product has evidence from an approved source that it reduces hair fall.

| | Brand E Herbal | Brand F Coconut |
|---|---|---|
| **Wellbeing Index** | 85 / 100 🟢 **(Provisional)** | 100 / 100 🟢 |
| **Quality ROI** | 94.4 | 238.1 |
| **Does the job?** | Oiling: yes · Hair fall: unclear | Oiling: yes |
| **Biggest concern** | "Chemical-free" claim; unreadable ingredients | None found |

## 1. Product snapshot

### Brand E Herbal Hair Oil
- **Net quantity / price:** 200 mL · ₹180 (₹90.00 per 100 mL)
- **Claims:** "Ayurvedic", "Reduces hair fall", "Chemical-free"
- **Ingredients:** 1. Sesamum Indicum (Sesame) Oil, 2. Paraffinum Liquidum (Light Liquid Paraffin), 3. Eclipta Alba (Bhringraj) Extract, 4. Emblica Officinalis (Amla) Extract, 5. Bacopa Monnieri (Brahmi) Extract, 6. Parfum, **[UNREADABLE: glare covers about 2 lines after "Parfum"]**
- **Identifiers:** Ayurvedic manufacturing licence no. printed (✅ read)
- **Allergens:** **Sesame**

### Brand F Pure Coconut Oil
- **Net quantity / price:** 500 mL · ₹210 (₹42.00 per 100 mL)
- **Claims:** "100% pure", "Edible grade"
- **Ingredients:** 1. Cocos Nucifera (Coconut) Oil
- **Identifiers:** FSSAI licence no. (14 digits) ✅

## 2. Ingredient risk check

| Product | Ingredient | Position | Tier | Why | Authority |
|---|---|---|---|---|---|
| E | Sesame oil | #1 | Low (allergen) | Sesame is a major food allergen; caution on skin for people allergic to it | [FDA, FASTER Act] |
| E | Light liquid paraffin | #2 | Low | Highly refined cosmetic-grade mineral oil is IARC Group 3 (not classifiable) | [IARC] |
| E | Parfum | #6 (additive) | Moderate | Undisclosed mixture; allergy trigger | [FDA] |
| E | [Unreadable lines] | — | — | Not rated. **We did not guess** | — |
| F | Coconut oil | #1 | — | No concern found | — |

## 3. Claim verification

| Product | Claim | Status | What we found |
|---|---|---|---|
| E | "Ayurvedic" | Consistent | Licence number printed; AYUSH verification is pending approval of that source† |
| E | "Reduces hair fall" | Unverifiable (−10) | No evidence in approved sources |
| E | "Chemical-free" | **Misleading** (−25) | Every ingredient is a chemical, and this product includes mineral oil and fragrance |
| F | "100% pure" | Consistent | Single ingredient |
| F | "Edible grade" | Verified | *Illustrative:* FSSAI licence valid on FoSCoS, name matches |

## 4. Wellbeing Index

| Sub-score | Weight | Brand E | Brand F |
|---|---|---|---|
| Ingredient Safety | 35% | 90 | 100 |
| Processing Level | 15% | 75 (P2) | 100 (P1) |
| Additives | 15% | 85 *(provisional)* | 100 |
| Nutrition Balance (skin and hair) | 20% | 100 | 100 |
| Claim Integrity | 15% | 65 | 100 |
| **Wellbeing Index** | | **85 (Provisional)** (85.25) | **100** |

- **E Ingredient Safety:** sesame −5, paraffin −5 (Low ×1.25, top five) = **90**
- **E Additives:** 1 readable additive −3; parfum −12 = **85**. The unreadable lines may hold more additives, so the score could fall
- **E and F Nutrition Balance:** leave-on oils whose first ingredient is a nourishing oil (+5, capped at **100**); no harsh surfactants or drying alcohols
- A score of 100 means **no deductions were found by this method**. It doesn't mean "perfect" or "medically proven"

| | Brand E | Brand F |
|---|---|---|
| Price per 100 mL | ₹90.00 | ₹42.00 |
| **Quality ROI** | **94.4** | **238.1** |

## 5. Verdict
**Better choice:** Brand F (**clear winner**, a 15-point gap, and more than twice the value per rupee).
**Trade-offs**
- Brand E adds herbal extracts that some people prefer, but its hair-fall claim is unproven in approved sources and "chemical-free" is misleading.
- **Ask for a clearer photo** of Brand E's back label to finish the score.

**Who should be careful**
- 🤧 **Allergies:** Brand E contains **sesame** and fragrance. Anyone sensitive to coconut should patch-test Brand F.
- 👶 **Children:** No authoritative data found for these products.
- 🤰 **Pregnancy:** No authoritative data found for these products.

**In-store tip:** A "chemical-free" label is a marketing line. Turn the bottle over and count the ingredients.

---

> *These samples are for training and illustration. They are not medical advice. Sample 1 reflects public web labels as of the date shown; formulas change and vary by market, so check the pack in hand. Samples 2 and 3 use fictional products.*
