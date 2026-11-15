# Process Flow: Know Your Product, Wellbeing Comparison

This is the pipeline from raw input to the finished comparison report, in nine steps. It was designed by working backwards from the output; it runs forwards from step 1.

```mermaid
flowchart TD
    R[/"Raw input: 2 products as photos, web link or barcode, plus price"/] --> S1
    S1["1. Get the label (US sale websites only)"] --> S2
    S2["2. Extract the label fields"] --> S3
    S3{"3. Ingredient pull check"}
    S3 -- "FAIL: re-pull or ask for photo" --> S1
    S3 -- "PASS / PARTIAL / FAIL with no re-pull possible (score with ⚠️ warning)" --> S4 & S5 & S6
    S4["4. Score ingredients and packaging"] --> S7
    S5["5. Verify the claims"] --> S7
    S6["6. Research brand giving"] --> S7
    S7["7. Calculate the Wellbeing Index and Quality ROI"] --> S8
    S8["8. Decide the verdict"] --> S9
    S9[/"9. Write the comparison report"/]
```

## Steps

| # | Step | Input | Output | Reference file |
|---|---|---|---|---|
| 1 | **Get the label** | **Raw input:** two products as photos (front and back), a web link or barcode, or both; a price for each | Label images or label text, pulled in this order: **official NIH label APIs** (DailyMed for OTC drugs, the Dietary Supplement Label Database for supplements), then the **designated product page or other US sale website**, then a **back-label photo** (needed for cosmetics). Source address and date recorded | `reference/05` §10, `reference/06` §1, `reference/02` §7 |
| 2 | **Extract the label fields** | Label images or text (1) | A product record: brand, variant, size, price, claims, full ingredient list in order, active ingredients, nutrition panel, allergens, identifiers, lot number, **packaging, owning company**, unreadable parts | `reference/06` §2–5 |
| 3 | **Ingredient pull check** | The product record (2) | PASS / PARTIAL / FAIL, the checks that failed, and the next step. **FAIL → back to step 1** (re-pull or photo). If neither is possible, score with the ⚠️ warning | `reference/06` §6 |
| 4 | **Score ingredients and packaging** | The checked ingredient list and packaging (3), the flagged-ingredient list, approved sources, FDA recalls and import alerts | A risk tier and authority per ingredient, allergens, watch-points, any score caps → **Side Effects / Health Risks, Nutrition Value, Sustainability** scores | `reference/01` §3.1, 3.2, 3.5; `reference/04`, `reference/02`, `reference/05` |
| 5 | **Verify the claims** | Claims and the checked ingredient list (3), the key-terms registry, official registries | A status per claim → **Claims Integrity** score; new terms added to the glossary | `reference/03`, `reference/05` |
| 6 | **Research brand giving** | The owning company (from the label), company filings and reports | Giving as a % of net profit, Verified or Self-reported → **Conscious Branding** score (or "not yet researched" → left out, with a warning) | `reference/01` §3.3, `reference/02` §8, `reference/05` §11 |
| 7 | **Calculate the Wellbeing Index and Quality ROI** | 5 category scores at 20% each (4, 5, 6), caps, price and net quantity in USD | Wellbeing Index 0–100 with band, provisional flag and confidence; Quality ROI | `reference/01` §3–6 |
| 8 | **Decide the verdict** | Both indexes and the gap, Quality ROI, caps, the fit-for-purpose check, incomplete-list warnings, allergens and care groups | The better choice and how strongly (clear winner / leans toward / comparable), trade-offs, who should be careful, in-store tip | `reference/01` §7–8 |
| 9 | **Write the report** | Everything above, plus the source log | The finished comparison report | `reference/07` (examples in `reference/08`) |

## Notes
- **The weakest link is steps 1 → 3.** Every score depends on getting the real ingredient list. Step 3 is the gate that stops a "key ingredients only" pull from reaching the score.
- **Steps 4, 5 and 6 are independent** and can run in parallel; step 7 needs all three. Step 6 (brand giving) depends only on the owning company, so it can be researched once per brand and cached.
- **Use official APIs first.** DailyMed and the Dietary Supplement Label Database return registered full labels (`reference/05` §10). Cosmetics have no government label database, so they need a back-label photo.
- **Price is a raw input.** Without it, step 7 can't calculate Quality ROI.
