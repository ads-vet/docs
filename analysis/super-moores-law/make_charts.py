#!/usr/bin/env python3
"""Generate the three presentation charts (SVG + PNG) from data/models.csv."""
import csv, math, os, datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

# --- palette (dataviz reference instance, light mode, validated) ---
SURFACE   = "#fcfcfb"
INK       = "#0b0b0b"
INK2      = "#52514e"
MUTED     = "#898781"
GRID      = "#e1e0d9"
BASELINE  = "#c3c2b7"
BLUE      = "#2a78d6"   # series 1: premium frontier
ORANGE    = "#eb6834"   # series 2: efficient

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "axes.edgecolor": BASELINE, "axes.linewidth": 0.8,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.labelcolor": INK2, "text.color": INK,
    "axes.titlecolor": INK, "svg.fonttype": "none",
})

rows = []
with open("data/models.csv") as f:
    for r in csv.DictReader(f):
        r["d"] = dt.date.fromisoformat(r["date"])
        r["inp"] = float(r["input_usd_per_1m"]); r["out"] = float(r["output_usd_per_1m"])
        r["bl"] = float(r["blended_usd_per_1m_3to1"])
        r["ctx"] = int(r["context_k_tokens"])
        r["cap"] = float(r["capability_composite_0to1"]) if r["capability_composite_0to1"] else None
        r["idx"] = float(r["intelligence_per_dollar_index_gpt3eq1"]) if r["intelligence_per_dollar_index_gpt3eq1"] else None
        rows.append(r)

def tiercolor(r): return BLUE if r["tier"] == "frontier" else ORANGE

def save(fig, name):
    for ext in ("svg", "png"):
        fig.savefig(f"charts/{name}.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)

os.makedirs("charts", exist_ok=True)

# =====================================================================
# CHART 1 — The Cost Collapse (two-panel log time series, input | output)
# =====================================================================
fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.9), sharey=True)
fig.subplots_adjust(wspace=0.06, top=0.84, bottom=0.10)

ANNOT1 = {  # (model, date) -> (panel, label, dx, dy)
    ("GPT-3 (davinci)", "2020-06-11"): (1, "GPT-3\n$60/M", 8, 8),
    ("GPT-4 (8K)", "2023-03-14"):      (1, "GPT-4\n$60 out", 6, 10),
    ("GPT-4.5 (preview)", "2025-02-27"): (1, "GPT-4.5 $150\n(pulled Jul '25)", -30, 12),
    ("o3", "2025-06-10"):              (1, "o3 −80%\n(Jun '25)", -62, -26),
    ("Claude Opus 4.5", "2025-11-24"): (1, "Opus 4.5 −67%", -108, -4),
    ("DeepSeek-R1", "2025-01-20"):     (1, "DeepSeek R1", -66, -18),
    ("GPT-5.6 Luna", "2026-07-30"):    (1, "Luna −80%\n(Jul '26)", -30, -36),
    ("DeepSeek-V2", "2024-05-07"):     (0, "DeepSeek V2 (price war)", 7, 3),
    ("Gemini 1.5 Flash", "2024-08-12"): (0, "Gemini 1.5\nFlash −78%", -78, -12),
    ("GPT-5.5", "2026-04-23"):         (0, "GPT-5.5 ↑$5\n(premium reversal)", -110, 6),
}

for pi, (ax, key, title) in enumerate(zip(axes, ("inp", "out"), ("Input tokens", "Output tokens"))):
    for r in rows:
        ax.scatter(r["d"], r[key], s=42, color=tiercolor(r), zorder=3,
                   edgecolors=SURFACE, linewidths=1.2, alpha=0.95)
    # falling price floor per tier (cheapest offered to date)
    for tier, color in (("frontier", BLUE), ("efficient", ORANGE)):
        pts = sorted([r for r in rows if r["tier"] == tier], key=lambda r: r["d"])
        lo, xs, ys = float("inf"), [], []
        for r in pts:
            lo = min(lo, r[key]); xs.append(r["d"]); ys.append(lo)
        xs.append(dt.date(2026, 8, 2)); ys.append(lo)
        ax.step(xs, ys, where="post", color=color, lw=2, alpha=0.65, zorder=2)
    ax.set_yscale("log")
    ax.set_ylim(0.05, 300)
    ax.set_xlim(dt.date(2020, 1, 1), dt.date(2026, 12, 15))
    ax.set_title(title, fontsize=12, loc="left", pad=8)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_yticks([0.1, 1, 10, 100])
    ax.set_yticklabels(["$0.10", "$1", "$10", "$100"])
    ax.tick_params(length=0)
    for spine in ("top", "right"): ax.spines[spine].set_visible(False)
    for (m, d), (panel, label, dx, dy) in ANNOT1.items():
        if panel != pi: continue
        r = next(r for r in rows if r["model"] == m and r["date"] == d)
        ax.annotate(label, (r["d"], r[key]), textcoords="offset points", xytext=(dx, dy),
                    fontsize=8.2, color=INK2, ha="left", va="bottom", linespacing=1.15)

axes[0].set_ylabel("USD per 1M tokens (log scale)", fontsize=10)
axes[0].annotate("Cheapest capable input token:\n$60 → $0.14   (−99.8%)",
                 xy=(dt.date(2020, 5, 1), 0.115), fontsize=9.5, color=INK,
                 ha="left", va="bottom", fontweight="bold", linespacing=1.4)
axes[1].annotate("Output token, frontier class:\n$60 → $6–30   (−50% to −90%)\nefficient tier: $60 → $0.28–1.20   (−98%+)",
                 xy=(dt.date(2020, 5, 1), 8), fontsize=9.5, color=INK,
                 ha="left", va="top", fontweight="bold", linespacing=1.4)
handles = [Line2D([], [], marker="o", ls="-", color=BLUE, markersize=7, lw=2, label="Premium frontier models"),
           Line2D([], [], marker="o", ls="-", color=ORANGE, markersize=7, lw=2, label="Efficient models"),
           Line2D([], [], ls="-", color=MUTED, lw=2, label="lines = cheapest price to date")]
fig.legend(handles=handles, loc="upper right", frameon=False, fontsize=9,
           bbox_to_anchor=(0.995, 1.00), ncol=1, handlelength=1.6, labelspacing=0.3)
fig.suptitle("API price per 1M tokens, major model releases 2020–2026",
             x=0.005, y=0.98, ha="left", fontsize=13.5, fontweight="bold")
save(fig, "chart1_cost_collapse")

# =====================================================================
# CHART 2 — Intelligence per Dollar (scatter, log-x cost, y capability)
# =====================================================================
# one point per model at its latest price; keep GPT-3 at its 2020 launch price (the anchor)
latest = {}
for r in rows:
    if r["cap"] is None: continue
    if r["model"] == "GPT-3 (davinci)" and r["event"] != "launch": continue
    k = r["model"]
    if k not in latest or r["d"] > latest[k]["d"]:
        latest[k] = r
pts = list(latest.values())

fig, ax = plt.subplots(figsize=(12.6, 6.6))
fig.subplots_adjust(top=0.86)
for r in pts:
    ax.scatter(r["bl"], r["cap"] * 100, s=30 + 8 * math.sqrt(r["ctx"] / 1000), zorder=3,
               color=tiercolor(r), alpha=0.85, edgecolors=SURFACE, linewidths=1.2)

LABELS2 = {   # model -> (dx, dy, label)   dx<0 => right-aligned
    "GPT-3 (davinci)": (-10, 6, "GPT-3 (2020)\nIndex = 1"),
    "GPT-3.5 Turbo": (8, -12, "GPT-3.5 Turbo ('23)"),
    "GPT-4 (8K)": (2, 10, "GPT-4 (2023)\nIndex ≈ 5"),
    "GPT-4o": (6, -18, "GPT-4o ('24)"),
    "GPT-4o mini": (-4, -22, "GPT-4o mini ('24)"),
    "o1": (8, -6, "o1 ('24)"),
    "o3": (4, -24, "o3 (post-cut '25)\nIndex ≈ 220"),
    "GPT-5.6 Sol": (12, -6, "GPT-5.6 Sol ('26)"),
    "GPT-5.6 Luna": (2, 12, "GPT-5.6 Luna ('26)\nIndex ≈ 2,160"),
    "Claude 3 Opus": (-2, 12, "Claude 3 Opus ('24)"),
    "Claude Opus 5": (-26, 13, "Claude Opus 5 ('26)"),
    "Claude Fable 5": (6, -18, "Claude Fable 5 ('26)"),
    "Claude Sonnet 5": (-8, -22, "Claude Sonnet 5 ('26)"),
    "Gemini 2.0 Flash": (10, -4, "Gemini 2.0 Flash ('25)\nIndex ≈ 2,790"),
    "Gemini 3.1 Pro": (-12, 4, "Gemini 3.1 Pro ('26)"),
    "DeepSeek-R1": (8, -12, "DeepSeek R1 ('25)"),
    "DeepSeek-V4-Pro": (-10, -20, "DeepSeek V4-Pro ('26)"),
    "Qwen 3.6 Plus": (-12, 8, "Qwen 3.6 Plus ('26)"),
    "Kimi K3": (-34, 14, "Kimi K3 ('26)"),
    "Grok 4.5": (-14, 6, "Grok 4.5 ('26)"),
    "Llama 3.1 405B (Together)": (8, -14, "Llama 3.1 405B ('24)"),
    "Gemini 1.5 Pro": (8, -12, "Gemini 1.5 Pro ('24)"),
}
for r in pts:
    if r["model"] in LABELS2:
        dx, dy, s = LABELS2[r["model"]]
        ax.annotate(s, (r["bl"], r["cap"] * 100), textcoords="offset points",
                    xytext=(dx, dy), fontsize=8.2, color=INK2, linespacing=1.15,
                    ha="left" if dx >= 0 else "right", va="bottom" if dy >= 0 else "top")

# value frontier (best capability at or below each cost)
srt = sorted(pts, key=lambda r: r["bl"])
best, fx, fy = -1, [], []
for r in srt:
    if r["cap"] * 100 > best:
        best = r["cap"] * 100; fx.append(r["bl"]); fy.append(best)
ax.plot(fx, fy, color=MUTED, lw=1.4, ls=(0, (4, 3)), zorder=2)
ax.annotate("value frontier", (fx[1], fy[1]), textcoords="offset points",
            xytext=(-2, 12), fontsize=8.5, color=MUTED, style="italic")

ax.set_xscale("log")
ax.set_xlim(0.09, 75)
ax.set_ylim(0, 107)
ax.set_xticks([0.1, 0.3, 1, 3, 10, 30])
ax.set_xticklabels(["$0.10", "$0.30", "$1", "$3", "$10", "$30"])
ax.set_xlabel("Blended cost per 1M tokens (3:1 input:output mix, log scale)  →  more expensive", fontsize=10)
ax.set_ylabel("Capability score (composite, 0–100)", fontsize=10)
ax.tick_params(length=0)
for spine in ("top", "right"): ax.spines[spine].set_visible(False)
ax.annotate("best value: top-left", xy=(0.095, 103), fontsize=10, color=INK, fontweight="bold")

handles = [Line2D([], [], marker="o", ls="", color=BLUE, markersize=8, label="Premium frontier"),
           Line2D([], [], marker="o", ls="", color=ORANGE, markersize=8, label="Efficient tier"),
           Line2D([], [], marker="o", ls="", mfc="none", mec=MUTED, markersize=4, label="bubble = 4K context"),
           Line2D([], [], marker="o", ls="", mfc="none", mec=MUTED, markersize=11, label="bubble = 2M context")]
fig.legend(handles=handles, loc="upper right", frameon=False, fontsize=9,
           bbox_to_anchor=(0.995, 0.945), ncol=4, columnspacing=1.2)
fig.suptitle("Capability vs. blended cost — bubble size = context window",
             x=0.005, y=0.975, ha="left", fontsize=13.5, fontweight="bold")
save(fig, "chart2_intelligence_per_dollar")

# =====================================================================
# CHART 3 — The Super Moore's Law (hero: index envelopes vs Moore's Law)
# =====================================================================
def envelope(sel):
    pts = sorted([r for r in rows if r["idx"] is not None and sel(r)], key=lambda r: r["d"])
    hi, xs, ys = 0, [], []
    for r in pts:
        if r["idx"] > hi:
            hi = r["idx"]; xs.append(r["d"]); ys.append(hi)
    xs.append(dt.date(2026, 8, 2)); ys.append(hi)
    return xs, ys

fig, ax = plt.subplots(figsize=(12.6, 6.2))
xe, ye = envelope(lambda r: True)                      # best value available (any tier)
xf, yf = envelope(lambda r: r["tier"] == "frontier")   # premium frontier only

ax.step(xe, ye, where="post", color=ORANGE, lw=2.6, zorder=3)
ax.step(xf, yf, where="post", color=BLUE, lw=2.6, zorder=3)

# Moore's law reference: double every 2 years from GPT-3
t0 = dt.date(2020, 6, 11)
mx = [t0 + dt.timedelta(days=30 * i) for i in range(75)]
my = [2 ** ((d - t0).days / 365.25 / 2) for d in mx]
ax.plot(mx, my, color=MUTED, lw=2, ls=(0, (5, 4)), zorder=2)

ax.set_yscale("log")
ax.set_ylim(0.7, 9000)
ax.set_xlim(dt.date(2020, 3, 1), dt.date(2027, 5, 1))
ax.set_yticks([1, 10, 100, 1000])
ax.set_yticklabels(["1×", "10×", "100×", "1,000×"])
ax.set_ylabel("Intelligence per dollar (GPT-3, 2020 = 1×, log scale)", fontsize=10)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.tick_params(length=0)
for spine in ("top", "right"): ax.spines[spine].set_visible(False)

# direct end labels (identity not by color alone)
ax.annotate("Best-value model:  ≈2,800× GPT-3\n(doubles every ~6.5 months)", xy=(xe[-1], ye[-1]),
            textcoords="offset points", xytext=(6, 8), fontsize=9.5, color=ORANGE,
            fontweight="bold", va="bottom", linespacing=1.3)
ax.annotate("Premium frontier model:  ≈300× GPT-3\n(doubles every ~9 months)", xy=(xf[-1], yf[-1]),
            textcoords="offset points", xytext=(6, -4), fontsize=9.5, color=BLUE,
            fontweight="bold", va="top", linespacing=1.3)
ax.annotate("Moore's Law pace\n(2× every 2 years) ≈ 8×", xy=(mx[-1], my[-1]),
            textcoords="offset points", xytext=(-40, 16), fontsize=9.5, color=INK2, linespacing=1.25)

# milestones on the lines + free-text era notes
ONLINE = [
    (dt.date(2020, 6, 11), 1.0, "GPT-3\n2K context, text-only,\n44% MMLU", (-8, 14)),
    (dt.date(2023, 3, 14), 5.0, "GPT-4: multimodal input,\nMMLU 86%", (10, -34)),
    (dt.date(2024, 8, 12), 1304, "1M-token context\ngoes mainstream", (-76, 12)),
]
for d, v, txt, (dx, dy) in ONLINE:
    ax.scatter([d], [v], s=26, color=INK2, zorder=4, marker="D")
    ax.annotate(txt, (d, v), textcoords="offset points", xytext=(dx, dy),
                fontsize=8.2, color=INK2, linespacing=1.2)
ax.annotate("2025: reasoning models,\nopen-weight price war", xy=(dt.date(2024, 11, 1), 38),
            fontsize=8.2, color=INK2, linespacing=1.2)
ax.annotate("2026 frontier: 94% GPQA-Diamond, 97% SWE-bench,\n1–2M context, agentic + multimodal",
            xy=(dt.date(2024, 11, 15), 5300), fontsize=8.2, color=INK2, linespacing=1.2)

ax.set_title("Intelligence per dollar has doubled every 6–9 months — Moore's Law expects 24",
             loc="left", fontsize=13.5, fontweight="bold", pad=10)
save(fig, "chart3_super_moores_law")
print("done")
