# Speaker Notes — The Super Moore's Law of AI

(Also embedded in the PPTX notes pane. Target: ~1 minute per slide.)

## Slide 1 — The Cost Collapse

Every dot is a published API list price per million tokens; the axis is logarithmic, so
each gridline down is 10× cheaper. Three things to land:

1. **The floor.** GPT-3 cost $60 per million tokens in 2020; today GPT-5.6 Luna costs
   $0.45 blended, and DeepSeek serves near-frontier models at $0.14 input. That is a
   99%+ collapse in six years.
2. **The cuts are events, not drift.** o3 fell 80% in one day (June 2025); Anthropic cut
   the Opus tier 67% (November 2025); OpenAI cut Luna 80% three weeks after launch
   (July 30, 2026) — the Luna claim is verified against OpenAI's own announcement and CNBC.
3. **Honesty note.** Premium flagship list prices reversed upward in 2025–26 (GPT-5.2 →
   5.5 quadrupled input price; Claude Fable 5 opened a $10/$50 tier). The right mental
   model: the price of the *best* model is roughly flat-to-up; the price of *any given
   capability level* collapses.

All figures are standard-tier list prices — batch (−50%) and caching (−90%) discounts
make the real decline steeper.

## Slide 2 — Intelligence per Dollar

This is the value map: capability up, blended cost across (log scale), bubble = context
window. Best value is top-left.

The capability score is a documented composite: GPQA-Diamond (PhD-level science,
normalized above the 25% guessing floor) averaged with SWE-bench Verified (real GitHub
coding tasks). Models predating those benchmarks are chained in from MMLU at the GPT-4
overlap point and flagged as estimates.

GPT-3 sits bottom-right at index 1. GPT-4 (2023) bought 5× more intelligence per dollar.
Today's value frontier — DeepSeek V4-Pro, Qwen 3.6, GPT-5.6 Luna — sits at 1,000–2,800×.
One dollar buys roughly three orders of magnitude more measured capability than in 2020,
and ~300× more even if you insist on a premium frontier model.

If asked: benchmarks are saturating at the top, so this *understates* recent gains; and
reasoning models bill hidden thinking tokens, so per-task costs fall somewhat less than
per-token prices.

## Slide 3 — The Super Moore's Law

The orange line is the best intelligence-per-dollar available at each moment; blue
restricts to premium frontier models; the gray dashed line is what Moore's Law (2× every
two years) would have delivered from the same 2020 start: about 8× by now.

The observed curves delivered ~2,800× and ~300× — a doubling every ~6.5 months for the
value tier and ~9 months at the frontier, i.e. roughly 3× faster than the Moore's Law
yardstick. We are explicitly **not** claiming AI follows Moore's Law; it is the familiar
benchmark for "fast."

The milestones carry the capability story: 2K → 1–2M token context, text-only →
multimodal and agentic, 44% MMLU → 94% GPQA-Diamond and 97% SWE-bench.

**Three takeaways:** (1) costs down 99%+; (2) capability per dollar up ~2,800×
(best-value) / ~300× (frontier); (3) doubling every ~6–9 months vs Moore's 24.
External literature (Epoch AI, a16z, Stanford HAI, MIT FutureTech) measures the same
phenomenon at 10–50×/year for constant capability — our figures are the conservative end.

**Strategic close:** anything built on today's model prices gets ~2× cheaper or ~2×
smarter within a year — design products assuming the intelligence budget keeps compounding.
