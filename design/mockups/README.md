# App mockups: Know Your Product

Five phone screens (390 px wide) showing the demo flow with the real Sample 1 data (Head & Shoulders Classic Clean vs Sri Sri Tattva Protein Shampoo, `reference/08-sample-comparisons.md`).

**Live, clickable version:** https://claude.ai/artifact/86ZUi3VH4YJ8JsTKCJTQe7 (private until shared from its Share menu)

| # | Screen | File | Process-flow step |
|---|---|---|---|
| 1 | Add two products (scan, label photo or link) | `Main.dc.html` | 1 · Get the label |
| 2 | Ingredient pull check: H&S Partial, Sri Sri Tattva Failed, with "photograph the back label" | `PullCheck.dc.html` | 3 · Ingredient pull check |
| 3 | Wellbeing comparison: 77 vs 79, five categories, Amazon ratings left out, value for money | `Compare.dc.html` | 4–7 · Scores and Quality ROI |
| 4 | Ingredients and claims, switchable per product | `Details.dc.html` | 4–5 · Risk check and claims |
| 5 | Verdict: Comparable, pick by need, who should be careful, in-store tip | `Verdict.dc.html` | 8 · Verdict |

- `canvas.json` is the canvas layout. The `.dc.html` files are Design Component pages for the Claude Design canvas; they load `support.js` from the canvas, so open them through the live link above rather than directly in a browser.
- Look: Inter body, Space Grotesk headings, deep teal (#0F6E5C) accent; amber for warnings, red for failures; blue (H&S) and orange (Sri Sri Tattva) in charts.
