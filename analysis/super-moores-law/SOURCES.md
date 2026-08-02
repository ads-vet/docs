# The Super Moore's Law of AI — Sources, Methodology & Assumptions

Research compiled and all URLs accessed on **2026-08-02**. Per-data-point source URLs
are in `data/models.csv` (column `sources`) and `data/price_events.csv`.

## 1. What each number is

Every row in `data/models.csv` carries a `status` flag:

| Flag | Meaning |
|---|---|
| `fact` | Published by the vendor (pricing page, launch post, model card, paper) or a primary press report of the announcement. |
| `mixed` | Prices are published facts; one or more benchmark figures come from third-party compilations (llm-stats, BenchLM, Artificial Analysis, Vellum) rather than the vendor. |
| `estimate` | Explicitly estimated (flagged in `notes`); e.g., Llama 2 70B hosted pricing. |

Calculated columns (`blended_usd_per_1m_3to1`, `capability_composite_0to1`,
`intelligence_per_dollar_index_gpt3eq1`) are **calculated values**, derived only from
the columns to their left using the formulas below.

## 2. Price conventions

- All prices are **USD per 1M tokens, standard tier** — no batch (−50%), cache
  (−90% reads), or off-peak discounts. Using discounts would make every decline steeper,
  so the headline numbers are conservative.
- **Blended price = (3 × input + 1 × output) / 4** — the 3:1 convention used by
  Artificial Analysis. GPT-3 had no input/output split; $60/M applies to both.
- Meta sells no first-party API; Llama rows use **Together AI** hosted list prices
  (host named in the row). Hosted prices vary ±2–3× across providers.
- Tiered pricing (Gemini ≤/> 200K prompts, Grok >128K surcharge) uses the **base tier**.
- Chinese-lab CNY prices converted at the widely reported USD list equivalents.
- **Reasoning-token caveat:** o-series, GPT-5+, Claude thinking modes and Gemini 2.5+
  bill hidden reasoning tokens as output. Cost *per task* therefore fell less than cost
  *per token* for reasoning models. Epoch AI and MIT price actual tokens consumed; our
  token-price series does not attempt this adjustment (documented limitation).

## 3. Capability composite (Slide 2 y-axis)

No single benchmark spans 2020→2026 (MMLU saturates ~90% by 2024; GPQA Diamond starts
2023 and is saturating ~94% in 2026; SWE-bench Verified starts 2024). We therefore use:

- **g = (GPQA Diamond − 25) / 75** — normalized above the 25% four-choice chance floor.
- **s = SWE-bench Verified / 100.**
- **composite = mean of the available {g, s}** (both where both exist).
- **Pre-GPQA models (2020–2023):** chained MMLU estimate
  `k × (MMLU − 25) / 75` with **k = 0.228**, calibrated at GPT-4 — the only strong model
  with credible scores on both scales (MMLU 86.4 → 0.819; GPQA 39 → 0.187). These rows are
  flagged `mmlu_chained[E]` in `capability_basis` and are **estimates**.

Known limitations (deliberate, disclosed):
1. Mixing GPQA-only and GPQA+SWE models introduces ±5-point noise; for 2026 frontier
   models the two agree within a few points.
2. SWE-bench is agent-scaffold dependent; where configs conflict we use the figure from
   llm-stats' leaderboard and flag vendor-config outliers (e.g. DeepSeek "V4-Pro-Max").
3. GPQA Diamond has 198 questions (±3.5pp run noise) and is saturating in 2026 — the
   composite therefore *understates* recent capability gains.
4. We did **not** splice Artificial Analysis Intelligence Index versions: v2/v3/v4.0/v4.1
   are mutually incomparable (same model scores differ by 10–20 points across versions).
   AA v4.1 values (Aug 2026 snapshot) are included as a reference column only.
5. Vendor-announced vs independently measured scores diverge (o3 GPQA: 87.7 announced,
   83.3 AA-measured). We prefer independent measurements where available.

## 4. Intelligence-per-Dollar Index (GPT-3 2020 = 1)

`index = (composite / blended price) ÷ (0.0575 / $60.00)`

GPT-3's composite (0.0575) is the chained-MMLU estimate from its published 43.9% 5-shot
MMLU (Hendrycks et al. 2020). The denominator anchor is therefore itself an estimate —
the *ratios among modern models* are unaffected by it; the *absolute* "×GPT-3" multiples
scale with it. A GPT-3 composite 20% higher/lower shifts every headline multiple
~20% the other way; the doubling-time conclusion (~6–9 months vs 24) is robust to this.

Models with no defensible capability score (e.g. DeepSeek V4-Flash, Grok 4 Fast, GPT-5
mini, Gemini 3.6 Flash) are priced in the dataset but **excluded from the index** —
several would likely *raise* the efficient-tier envelope if scored, so the headline is
again conservative.

**Tier definition:** "premium frontier" vs "efficient" reflects **price positioning at
release**, not capability. Budget-priced open frontier models (DeepSeek R1, V4-Pro,
Mistral Large 3) are classed efficient; that is what makes the two envelopes meaningfully
different, and it is disclosed here.

## 5. Headline numbers on the slides (all calculated from the dataset)

| Claim | Calculation |
|---|---|
| Token price −99.25% (133×) | GPT-3 $60.00 blended (2020) → GPT-5.6 Luna $0.45 blended (Jul 2026) |
| Cheapest capable input token −99.8% | $60 → $0.14 (DeepSeek V2 May 2024 / V4-Flash Jul 2026) |
| Intelligence/$ ≈ 2,800× (efficient) | Gemini 2.0 Flash (Feb 2025): composite 0.468 at $0.175 blended → 2,793× |
| Intelligence/$ ≈ 2,160× (Luna) | GPT-5.6 Luna post-cut: composite 0.930 at $0.45 blended |
| Intelligence/$ ≈ 300× (frontier) | Grok 4.5 (Jul 2026): composite 0.866 at $3.00 blended → 301× |
| Doubling time ~6.4 mo (efficient) | 6.13 years GPT-3→envelope 2,793×: 6.13×12 / log2(2793) |
| Doubling time ~8.9 mo (frontier) | 6.13×12 / log2(301) |
| Moore's Law comparison ≈ 8× | 2^(6.13/2) over the same window |

Note the efficient-tier envelope has been **flat since Feb 2025**: since then the value
frontier has moved by adding capability at low prices (Luna: 93-point composite at $0.45)
rather than by cutting the floor price further.

## 6. The "Luna" claim — verification

**VERIFIED.** "Luna" = **GPT-5.6 Luna**, the cost-efficient tier of OpenAI's GPT-5.6
family (Sol / Terra / Luna), GA July 9, 2026. On **July 30, 2026** OpenAI cut Luna's
price **80%**: $1.00/$6.00 → **$0.20/$1.20** per 1M tokens (Terra −20%; Sol unchanged;
Luna flex tier $0.10/$0.60). Confirmed via OpenAI's announcement ("Advancing the
price-performance frontier with GPT-5.6") and independent coverage (CNBC, VentureBeat,
Forbes, Quartz, The Decoder, Simon Willison) plus pricing trackers (OpenRouter,
Artificial Analysis). Distinct from OpenAI's earlier ~80% o3 cut (June 10, 2025).

## 7. Corroborating literature (constant-capability cost decline)

| Source | Finding | URL |
|---|---|---|
| Epoch AI (Mar 2025) | Price to reach a fixed benchmark score fell 9×–900×/year (median ~50×/yr; GPT-4-level GPQA ~40×/yr) | https://epoch.ai/data-insights/llm-inference-price-trends |
| a16z "LLMflation" (Nov 2024) | ~10×/year; GPT-3-class capability: $60/M (2021) → $0.06/M (2024) = 1,000× in 3 years | https://a16z.com/llmflation-llm-inference-cost/ |
| Stanford HAI AI Index 2025 | GPT-3.5-class query cost fell >280× in ~18 months ($20/M Nov 2022 → $0.07/M Oct 2024) | https://hai.stanford.edu/ai-index/2025-ai-index-report |
| MIT FutureTech "The Price of Progress" (Nov 2025) | 5–10×/year at constant benchmark performance; ~3×/yr from algorithmic efficiency alone | https://arxiv.org/abs/2511.23455 |

Our 6–9-month doubling (≈2.5–4×/year on capability-per-dollar) is *more conservative*
than these constant-capability estimates because benchmark saturation caps measured
capability growth at the top.

## 8. Honest counter-trends (shown, not hidden)

- **Flagship list prices rose in 2025–26**: GPT-5.2 (+40%, Dec 2025) → GPT-5.4 → GPT-5.5
  ($5/$30, 4× GPT-5.1's input price); Gemini 3 Pro +60% input vs 2.5 Pro; Claude Fable 5
  established a $10/$50 tier; Gemini Flash tier moved upmarket 3×; Kimi K3 and Qwen 3.7
  Max priced above their predecessors; GPT-4.5 briefly listed at $75/$150.
- The *frontier of capability* got more expensive even as *any fixed capability level*
  kept collapsing in price. Both are true; the deck says so.
- Anthropic Sonnet 5's $2/$10 is intro pricing (reverts to $3/$15 on Sep 1, 2026).

## 9. Research-access caveats

Official pricing pages (openai.com, docs.anthropic.com, ai.google.dev, api-docs.deepseek.com,
mistral.ai, x.ai, platform.moonshot.ai) returned HTTP 403 to this environment's fetcher;
2026 prices were cross-verified across 3+ independent trackers/press reports each
(OpenRouter, Artificial Analysis, llm-stats, BenchLM, pricepertoken, CloudZero, CNBC,
VentureBeat, 9to5Google, Caixin, Axios) plus official announcement posts surfaced via
search. Everything after Dec 2025 rests on those corroborated secondary snapshots.
Items that could not be corroborated are flagged in `notes` (e.g. Claude Opus 5
SWE-bench 96.0 vs 97.0 source conflict; DeepSeek V4-Pro launch price inferred).
