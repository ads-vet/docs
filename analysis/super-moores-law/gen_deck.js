const pptxgen = require("pptxgenjs");

const INK = "0B0B0B", INK2 = "52514E", MUTED = "898781";
const BLUE = "2A78D6", ORANGE = "EB6834", SURFACE = "FFFFFF";
const TINT_BLUE = "EAF2FC", TINT_ORANGE = "FDEFE9";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.author = "VetIntel Analysis";
pres.title = "The Super Moore's Law of AI";

function baseSlide(title, kicker) {
  const s = pres.addSlide();
  s.background = { color: SURFACE };
  s.addText(title, { x: 0.5, y: 0.28, w: 12.3, h: 0.62, fontSize: 32, bold: true,
    color: INK, fontFace: "Calibri", margin: 0 });
  s.addText(kicker, { x: 0.5, y: 0.92, w: 12.3, h: 0.36, fontSize: 14, italic: true,
    color: INK2, fontFace: "Calibri", margin: 0 });
  return s;
}

function statTile(s, y, h, big, label, accent, tint) {
  s.addShape(pres.ShapeType.roundRect, { x: 9.95, y: y, w: 2.9, h: h,
    fill: { color: tint }, line: { type: "none" }, rectRadius: 0.08 });
  s.addText(big, { x: 10.15, y: y + 0.12, w: 2.5, h: 0.55, fontSize: 27, bold: true,
    color: accent, fontFace: "Calibri", margin: 0 });
  s.addText(label, { x: 10.15, y: y + 0.66, w: 2.55, h: h - 0.78, fontSize: 10.5,
    color: INK2, fontFace: "Calibri", margin: 0, lineSpacingMultiple: 1.05 });
}

function footer(s, text) {
  s.addText(text, { x: 0.5, y: 7.06, w: 12.3, h: 0.3, fontSize: 8.5, color: MUTED,
    fontFace: "Calibri", margin: 0 });
}

// ---------------- Slide 1: The Cost Collapse ----------------
{
  const s = baseSlide("The Cost Collapse", "How quickly has the cost of accessing capable AI fallen?");
  s.addImage({ path: "charts/chart1_cost_collapse.png", x: 0.42, y: 1.45, w: 9.35, h: 4.38 });
  statTile(s, 1.45, 1.55, "−99.25%", "blended price of a capable token: GPT-3 $60.00 (2020) → GPT-5.6 Luna $0.45 per 1M tokens (Jul 2026)", BLUE, TINT_BLUE);
  statTile(s, 3.15, 1.55, "133×", "cheaper in 6 years — before batch (−50%) and cached-input (−90%) discounts, which make it steeper", BLUE, TINT_BLUE);
  statTile(s, 4.85, 1.55, "−80%", "GPT-5.6 Luna price cut on Jul 30, 2026, three weeks after launch — verified via OpenAI + CNBC", ORANGE, TINT_ORANGE);
  s.addText([
    { text: "Read: ", options: { bold: true, color: INK } },
    { text: "every dot is a model's list price at launch or reprice (log scale — each gridline is 10× cheaper). The floor falls relentlessly; premium flagships (GPT-5.5, Fable 5) ticked back up in 2026 even as any fixed capability level kept getting cheaper.", options: { color: INK2 } },
  ], { x: 0.5, y: 6.0, w: 12.3, h: 0.85, fontSize: 12, fontFace: "Calibri", margin: 0, lineSpacingMultiple: 1.1 });
  footer(s, "Prices: official vendor announcements & pricing pages, cross-checked Aug 2, 2026 (OpenRouter, Artificial Analysis, llm-stats, CNBC). Full per-point sources: data/models.csv + SOURCES.md.");
  s.addNotes(
    "Every dot is a published API list price per million tokens; the axis is logarithmic, so each gridline down is 10x cheaper. " +
    "Three things to land. First, the floor: GPT-3 cost $60 per million tokens in 2020; today GPT-5.6 Luna costs 45 cents blended, and DeepSeek serves near-frontier models at 14 cents input. That's a 99%+ collapse in six years. " +
    "Second, the cuts are events, not drift: o3 fell 80% in one day in June 2025, Anthropic cut the Opus tier 67% in November 2025, and OpenAI cut Luna 80% three weeks after launch in July 2026 — that Luna claim is verified against OpenAI's own announcement and CNBC. " +
    "Third, honesty note: premium flagship list prices reversed upward in 2025-26 (GPT-5.2 through 5.5 quadrupled input price; Fable 5 opened a $10/$50 tier). The right mental model: the price of the BEST model is roughly flat-to-up; the price of ANY GIVEN capability level collapses. " +
    "All figures are standard-tier list prices — batch and caching discounts make the real decline steeper."
  );
}

// ---------------- Slide 2: Intelligence per Dollar ----------------
{
  const s = baseSlide("Intelligence per Dollar", "How many times more capability does one dollar buy today?");
  s.addImage({ path: "charts/chart2_intelligence_per_dollar.png", x: 0.42, y: 1.42, w: 9.35, h: 4.66 });
  statTile(s, 1.42, 1.5, "2,790×", "more intelligence per dollar than GPT-3 — best-value model (Gemini 2.0 Flash, Feb 2025)", ORANGE, TINT_ORANGE);
  statTile(s, 3.07, 1.5, "2,160×", "GPT-5.6 Luna (Jul 2026): 93-point capability at $0.45 per 1M tokens", ORANGE, TINT_ORANGE);
  statTile(s, 4.72, 1.5, "≈300×", "even the premium frontier tier (Grok 4.5, Claude Opus 5) buys ~300× more capability per dollar", BLUE, TINT_BLUE);
  s.addText([
    { text: "Index method: ", options: { bold: true, color: INK } },
    { text: "capability = composite of GPQA-Diamond (normalized above the 25% chance floor) and SWE-bench Verified; pre-2023 models chained from MMLU at the GPT-4 overlap. Index = capability ÷ blended $/1M tokens, GPT-3 (2020) = 1. Estimates flagged in the dataset; benchmark saturation makes recent gains conservative.", options: { color: INK2 } },
  ], { x: 0.5, y: 6.22, w: 12.3, h: 0.75, fontSize: 10.5, fontFace: "Calibri", margin: 0, lineSpacingMultiple: 1.1 });
  footer(s, "Benchmarks: vendor model cards, GPQA paper (Rein et al. 2023), llm-stats/BenchLM Aug-2026 snapshots; AA Intelligence Index versions NOT mixed. Methodology: SOURCES.md §3–4.");
  s.addNotes(
    "This is the value map: capability up the y-axis, blended cost across the x-axis on a log scale, bubble size is the context window. Best value is top-left. " +
    "The capability score is a documented composite: GPQA-Diamond — PhD-level science questions, normalized above the 25% guessing floor — averaged with SWE-bench Verified, the standard real-world coding benchmark. Older models that predate those tests are chained in from MMLU at the GPT-4 overlap point and flagged as estimates. " +
    "GPT-3 sits bottom-right: index 1. GPT-4 in 2023 bought 5x more intelligence per dollar. Today's value frontier — DeepSeek V4-Pro, Qwen 3.6, GPT-5.6 Luna — sits top-left at 1,000 to 2,800x. One dollar buys roughly three orders of magnitude more measured capability than in 2020, and about 300x more even if you insist on a premium frontier model. " +
    "Caveat to volunteer if asked: benchmarks are saturating at the top, so if anything this understates recent gains; and reasoning models bill hidden thinking tokens, so per-task costs fall somewhat less than per-token prices."
  );
}

// ---------------- Slide 3: The Super Moore's Law ----------------
{
  const s = baseSlide("The Super Moore's Law", "AI doesn't literally follow Moore's Law — but capability per dollar is currently compounding ~3× faster than Moore's pace.");
  s.addImage({ path: "charts/chart3_super_moores_law.png", x: 0.42, y: 1.42, w: 9.35, h: 4.60 });
  statTile(s, 1.42, 1.5, "1  −99%+", "total cost decline: $60 → $0.45 per 1M blended tokens (133×); GPT-3-class capability ~1,000× cheaper (a16z)", BLUE, TINT_BLUE);
  statTile(s, 3.07, 1.5, "2  ~2,800×", "improvement in capability per dollar since GPT-3 (best-value tier); ≈300× at the premium frontier", ORANGE, TINT_ORANGE);
  statTile(s, 4.72, 1.5, "3  ~6–9 mo", "doubling time of AI capability per dollar — vs 24 months for the Moore's Law benchmark (≈8× over the same six years)", BLUE, TINT_BLUE);
  s.addText([
    { text: "Corroboration: ", options: { bold: true, color: INK } },
    { text: "Epoch AI: constant-capability inference prices fell 9–900×/yr (median ~50×). a16z: ~10×/yr. Stanford HAI: GPT-3.5-class cost fell 280× in 18 months. MIT FutureTech: 5–10×/yr. Our 6–9-month doubling is the conservative end.", options: { color: INK2 } },
  ], { x: 0.5, y: 6.18, w: 12.3, h: 0.7, fontSize: 11, fontFace: "Calibri", margin: 0, lineSpacingMultiple: 1.1 });
  footer(s, "Index envelopes computed from data/models.csv (best index achieved to date, per tier). Moore's Law line: 2× every 24 months from Jun 2020. Literature: SOURCES.md §7.");
  s.addNotes(
    "The hero chart: the orange line is the best intelligence-per-dollar available at each moment; blue restricts to premium frontier models; the gray dashed line is what Moore's Law — doubling every two years — would have delivered from the same 2020 starting point: about 8x by now. " +
    "The observed curves delivered roughly 2,800x and 300x. That is a doubling every 6.5 months for the value tier and every 9 months at the frontier — three to four times faster than the Moore's Law benchmark. We are explicitly NOT claiming AI follows Moore's Law; we're using it as the familiar yardstick for 'fast'. " +
    "The milestones carry the capability side of the story: 2K context to 1-2 million, text-only to multimodal and agentic, 44% on MMLU to 94% on PhD-level GPQA and 97% on real coding tasks. " +
    "Three takeaways, right rail: costs down 99%+, capability per dollar up ~2,800x, doubling every 6-9 months. External literature (Epoch, a16z, Stanford HAI, MIT) measures the same phenomenon at 10-50x per year for constant capability — our numbers are the conservative end. " +
    "Strategic close for VetIntel: anything we build on today's model prices gets ~2x cheaper or ~2x smarter within a year — design products assuming the intelligence budget keeps compounding."
  );
}

pres.writeFile({ fileName: "slides/super-moores-law.pptx" }).then(() => console.log("deck written"));
