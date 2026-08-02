# The Super Moore's Law of AI

Source-backed, presentation-ready analysis of how AI model capability rose while API
prices collapsed, 2020 → August 2026. Compiled 2026-08-02.

## Headline findings

| # | Takeaway | Number |
|---|---|---|
| 1 | Total cost decline | Capable-token blended price $60 → $0.45 per 1M (−99.25%, 133×); GPT-3-class capability ~1,000× cheaper |
| 2 | Capability per dollar | ~2,800× GPT-3 (best-value tier); ~300× (premium frontier) |
| 3 | Doubling time | ~6.5 months (value tier) / ~9 months (frontier) — vs Moore's Law's 24 months (≈8× over the period) |

The reported **80% "Luna" price cut is verified**: GPT-5.6 Luna, cut $1.00/$6.00 →
$0.20/$1.20 per 1M tokens on 2026-07-30 (OpenAI announcement + CNBC et al.).

## Contents

| Path | What it is |
|---|---|
| `slides/super-moores-law.pptx` | 3-slide executive deck + open-weight appendix slide, with embedded speaker notes (PDF alongside) |
| `slides/speaker_notes.md` | Standalone speaker notes |
| `charts/*.svg` / `charts/*.png` | The four charts (3 core + open-weight catch-up), editable SVG + 200-dpi PNG |
| `data/models.csv` | Cleaned dataset: 74 model price points × 10 providers, with prices, context, benchmarks, open-weights license flag, per-row sources, fact/estimate flags |
| `data/price_events.csv` | 20 dated major price cuts / increases with sources |
| `SOURCES.md` | Methodology, assumptions, index construction, caveats, literature |
| `build_dataset.py` | Reproducibly regenerates `data/*.csv` and the headline numbers |
| `make_charts.py` | Regenerates all charts from `data/models.csv` |
| `gen_deck.js` | Regenerates the PPTX (pptxgenjs) |

## Reproduce

```bash
python3 build_dataset.py   # writes data/*.csv, prints headline numbers
python3 make_charts.py     # writes charts/*.{svg,png}
node gen_deck.js           # writes slides/super-moores-law.pptx
```
