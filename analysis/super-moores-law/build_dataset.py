#!/usr/bin/env python3
"""Build the cleaned source dataset for 'The Super Moore's Law of AI'.

Outputs:
  data/models.csv        - one row per model price point (launch or reprice)
  data/price_events.csv  - dated major price cuts / increases

Index methodology (documented in SOURCES.md):
  * blended $/1M tokens = (3*input + 1*output) / 4   (3:1 mix, Artificial Analysis convention)
  * capability_composite (0-1):
      - GPQA Diamond normalized above 25% chance floor: g = (gpqa-25)/75
      - SWE-bench Verified as fraction: s = swe/100
      - composite = mean of available {g, s}
      - pre-GPQA-era models: chained MMLU estimate: k * (mmlu-25)/75,
        k = 0.2281 calibrated so GPT-4 (MMLU 86.4, GPQA 39) matches on both scales
  * intelligence_per_dollar_index = (composite / blended) normalized to GPT-3 (2020) = 1
All prices USD per 1M tokens, standard tier (no batch/cache discounts).
date_accessed for all web sources: 2026-08-02.
"""
import csv, math, os

DATE_ACCESSED = "2026-08-02"
K_MMLU_CHAIN = ((39 - 25) / 75) / ((86.4 - 25) / 75)  # = 0.22801 (GPT-4 splice)

# provider, model, tier, date(price effective), event, in, out, ctx_k,
# mmlu, gpqa, swe, aa_v41, status, capability sources / notes, source URLs
M = [
 # ---------------- OpenAI ----------------
 dict(provider="OpenAI", model="GPT-3 (davinci)", tier="frontier", date="2020-06-11", event="launch",
      inp=60.0, out=60.0, ctx=2, mmlu=43.9, gpqa=None, swe=None, aa=None, status="fact",
      notes="No input/output split ($0.06/1K all tokens). MMLU 5-shot from Hendrycks et al.",
      src="https://arxiv.org/abs/2009.03300; https://the-decoder.com/openai-cuts-prices-for-gpt-3-by-two-thirds/"),
 dict(provider="OpenAI", model="GPT-3 (davinci)", tier="frontier", date="2022-09-01", event="reprice",
      inp=20.0, out=20.0, ctx=2, mmlu=43.9, gpqa=None, swe=None, aa=None, status="fact",
      notes="-67% cut attributed to inference efficiency.",
      src="https://the-decoder.com/openai-cuts-prices-for-gpt-3-by-two-thirds/"),
 dict(provider="OpenAI", model="GPT-3.5 Turbo", tier="efficient", date="2023-03-01", event="launch",
      inp=2.0, out=2.0, ctx=4, mmlu=70.0, gpqa=None, swe=None, aa=None, status="fact",
      notes="Chat API debut; 10x cheaper than davinci. MMLU from GPT-4 tech report.",
      src="https://arxiv.org/abs/2303.08774"),
 dict(provider="OpenAI", model="GPT-3.5 Turbo", tier="efficient", date="2024-01-25", event="reprice",
      inp=0.50, out=1.50, ctx=16, mmlu=70.0, gpqa=None, swe=None, aa=None, status="fact",
      notes="Third GPT-3.5 cut in a year (0125 version).",
      src="https://cointelegraph.com/news/openai-gpt-4-update-price-drop-new-embeddings-models"),
 dict(provider="OpenAI", model="GPT-4 (8K)", tier="frontier", date="2023-03-14", event="launch",
      inp=30.0, out=60.0, ctx=8, mmlu=86.4, gpqa=39.0, swe=None, aa=None, status="fact",
      notes="GPQA 39% = strongest GPT-4 baseline in GPQA paper (few-shot CoT).",
      src="https://arxiv.org/abs/2303.08774; https://arxiv.org/abs/2311.12022"),
 dict(provider="OpenAI", model="GPT-4 Turbo", tier="frontier", date="2023-11-06", event="launch",
      inp=10.0, out=30.0, ctx=128, mmlu=86.5, gpqa=None, swe=None, aa=None, status="mixed",
      notes="Prices fact (DevDay). MMLU ~86.5 unofficial [ESTIMATE].",
      src="https://openai.com/index/new-models-and-developer-products-announced-at-devday/"),
 dict(provider="OpenAI", model="GPT-4o", tier="frontier", date="2024-05-13", event="launch",
      inp=5.0, out=15.0, ctx=128, mmlu=88.7, gpqa=53.6, swe=33.2, aa=None, status="fact",
      notes="Native multimodal. SWE-bench Verified 33.2 from OpenAI's Aug-2024 SWE-bench-Verified post.",
      src="https://openai.com/index/hello-gpt-4o/; https://openai.com/index/introducing-swe-bench-verified/"),
 dict(provider="OpenAI", model="GPT-4o (0806)", tier="frontier", date="2024-08-06", event="reprice",
      inp=2.50, out=10.0, ctx=128, mmlu=88.7, gpqa=53.6, swe=33.2, aa=None, status="fact",
      notes="-50% input / -33% output.",
      src="https://developers.openai.com/api/docs/models/gpt-4o"),
 dict(provider="OpenAI", model="GPT-4o mini", tier="efficient", date="2024-07-18", event="launch",
      inp=0.15, out=0.60, ctx=128, mmlu=82.0, gpqa=40.2, swe=None, aa=None, status="fact",
      notes="Replaced GPT-3.5 Turbo as cheap default.",
      src="https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/"),
 dict(provider="OpenAI", model="o1", tier="frontier", date="2024-12-17", event="launch",
      inp=15.0, out=60.0, ctx=200, mmlu=92.3, gpqa=78.0, swe=48.9, aa=None, status="fact",
      notes="First full reasoning model; reasoning tokens billed as output.",
      src="https://openai.com/index/learning-to-reason-with-llms/"),
 dict(provider="OpenAI", model="GPT-4.5 (preview)", tier="frontier", date="2025-02-27", event="launch",
      inp=75.0, out=150.0, ctx=128, mmlu=None, gpqa=None, swe=None, aa=None, status="fact",
      notes="Most expensive OpenAI model ever; removed from API 2025-07-14.",
      src="https://en.wikipedia.org/wiki/GPT-4.5"),
 dict(provider="OpenAI", model="GPT-4.1", tier="efficient", date="2025-04-14", event="launch",
      inp=2.0, out=8.0, ctx=1000, mmlu=90.2, gpqa=66.3, swe=54.6, aa=None, status="fact",
      notes="API-only; first OpenAI 1M context.",
      src="https://openai.com/index/gpt-4-1/"),
 dict(provider="OpenAI", model="o3", tier="frontier", date="2025-04-16", event="launch",
      inp=10.0, out=40.0, ctx=200, mmlu=None, gpqa=83.3, swe=69.1, aa=None, status="fact",
      notes="GPQA 83.3 = Artificial-Analysis-measured (OpenAI announced 87.7 high-compute).",
      src="https://openai.com/index/introducing-o3-and-o4-mini/; https://artificialanalysis.ai/evaluations/gpqa-diamond"),
 dict(provider="OpenAI", model="o3", tier="frontier", date="2025-06-10", event="reprice",
      inp=2.0, out=8.0, ctx=200, mmlu=None, gpqa=83.3, swe=69.1, aa=30.4, status="fact",
      notes="-80% cut, same model, optimized inference stack.",
      src="https://venturebeat.com/ai/openai-announces-80-price-drop-for-o3-its-most-powerful-reasoning-model"),
 dict(provider="OpenAI", model="GPT-5", tier="frontier", date="2025-08-07", event="launch",
      inp=1.25, out=10.0, ctx=400, mmlu=None, gpqa=85.7, swe=74.9, aa=None, status="fact",
      notes="Unified reasoning; GPQA is thinking-mode figure.",
      src="https://openai.com/index/introducing-gpt-5/"),
 dict(provider="OpenAI", model="GPT-5 mini", tier="efficient", date="2025-08-07", event="launch",
      inp=0.25, out=2.0, ctx=400, mmlu=None, gpqa=None, swe=None, aa=None, status="fact",
      notes="", src="https://openai.com/index/introducing-gpt-5/"),
 dict(provider="OpenAI", model="GPT-5.2", tier="frontier", date="2025-12-10", event="launch",
      inp=1.75, out=14.0, ctx=400, mmlu=92.5, gpqa=92.4, swe=None, aa=None, status="mixed",
      notes="FIRST flagship price increase (+40% vs GPT-5.1). Benchmarks from third-party compilations.",
      src="https://openrouter.ai/openai/gpt-5.2; https://www.vellum.ai/blog/gpt-5-2-benchmarks"),
 dict(provider="OpenAI", model="GPT-5.5", tier="frontier", date="2026-04-23", event="launch",
      inp=5.0, out=30.0, ctx=1000, mmlu=None, gpqa=92.6, swe=None, aa=None, status="mixed",
      notes="Doubled GPT-5.4 pricing. GPQA from secondary sources.",
      src="https://en.wikipedia.org/wiki/GPT-5.5"),
 dict(provider="OpenAI", model="GPT-5.6 Sol", tier="frontier", date="2026-07-09", event="launch",
      inp=5.0, out=30.0, ctx=1050, mmlu=None, gpqa=94.1, swe=96.2, aa=58.9, status="mixed",
      notes="Current flagship. GPQA/SWE third-party (OpenAI's official headline was Terminal-Bench 2.1 88.8).",
      src="https://openai.com/index/gpt-5-6/; https://benchlm.ai/benchmarks/gpqaDiamond; https://llm-stats.com/benchmarks/swe-bench-verified"),
 dict(provider="OpenAI", model="GPT-5.6 Terra", tier="efficient", date="2026-07-09", event="launch",
      inp=2.50, out=15.0, ctx=1050, mmlu=None, gpqa=None, swe=None, aa=None, status="fact",
      notes="Mid tier.", src="https://openai.com/index/gpt-5-6/"),
 dict(provider="OpenAI", model="GPT-5.6 Terra", tier="efficient", date="2026-07-30", event="reprice",
      inp=2.0, out=12.0, ctx=1050, mmlu=None, gpqa=None, swe=None, aa=None, status="fact",
      notes="-20% cut.", src="https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html"),
 dict(provider="OpenAI", model="GPT-5.6 Luna", tier="efficient", date="2026-07-09", event="launch",
      inp=1.0, out=6.0, ctx=1050, mmlu=None, gpqa=None, swe=93.0, aa=None, status="fact",
      notes="High-volume tier. SWE-bench Verified 93.0 via llm-stats.",
      src="https://openai.com/index/gpt-5-6/; https://llm-stats.com/benchmarks/swe-bench-verified"),
 dict(provider="OpenAI", model="GPT-5.6 Luna", tier="efficient", date="2026-07-30", event="reprice",
      inp=0.20, out=1.20, ctx=1050, mmlu=None, gpqa=None, swe=93.0, aa=None, status="fact",
      notes="-80% cut three weeks after launch ('Luna' price cut, verified).",
      src="https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/; https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html"),
 # ---------------- Anthropic ----------------
 dict(provider="Anthropic", model="Claude 2", tier="frontier", date="2023-07-11", event="launch",
      inp=11.02, out=32.68, ctx=100, mmlu=78.5, gpqa=None, swe=None, aa=None, status="fact",
      notes="Token prices are Anthropic's conversion of per-character pricing.",
      src="https://www.anthropic.com/news/claude-2"),
 dict(provider="Anthropic", model="Claude 2.1", tier="frontier", date="2023-11-21", event="reprice",
      inp=8.0, out=24.0, ctx=200, mmlu=78.5, gpqa=None, swe=None, aa=None, status="fact",
      notes="-27% vs Claude 2; first 200K context.",
      src="https://www.anthropic.com/news/claude-2-1"),
 dict(provider="Anthropic", model="Claude 3 Haiku", tier="efficient", date="2024-03-13", event="launch",
      inp=0.25, out=1.25, ctx=200, mmlu=75.2, gpqa=None, swe=None, aa=None, status="fact",
      notes="", src="https://www.anthropic.com/news/claude-3-family"),
 dict(provider="Anthropic", model="Claude 3 Opus", tier="frontier", date="2024-03-04", event="launch",
      inp=15.0, out=75.0, ctx=200, mmlu=86.8, gpqa=50.4, swe=None, aa=None, status="fact",
      notes="First GPT-4-class Claude.", src="https://www.anthropic.com/news/claude-3-family"),
 dict(provider="Anthropic", model="Claude 3.5 Sonnet", tier="frontier", date="2024-06-20", event="launch",
      inp=3.0, out=15.0, ctx=200, mmlu=88.7, gpqa=59.4, swe=None, aa=None, status="fact",
      notes="Oct-2024 'v2' upgrade at same price: GPQA 65.0, SWE-bench 49.0.",
      src="https://www.anthropic.com/news/claude-3-5-sonnet"),
 dict(provider="Anthropic", model="Claude 3.5 Sonnet v2", tier="frontier", date="2024-10-22", event="upgrade",
      inp=3.0, out=15.0, ctx=200, mmlu=None, gpqa=65.0, swe=49.0, aa=None, status="fact",
      notes="Same price, higher capability.",
      src="https://www.anthropic.com/news/3-5-models-and-computer-use"),
 dict(provider="Anthropic", model="Claude 3.7 Sonnet", tier="frontier", date="2025-02-24", event="launch",
      inp=3.0, out=15.0, ctx=200, mmlu=None, gpqa=68.0, swe=62.3, aa=None, status="fact",
      notes="GPQA 68.0 standard mode (84.8 extended thinking).",
      src="https://www.anthropic.com/news/claude-3-7-sonnet"),
 dict(provider="Anthropic", model="Claude Opus 4", tier="frontier", date="2025-05-22", event="launch",
      inp=15.0, out=75.0, ctx=200, mmlu=88.8, gpqa=79.6, swe=72.5, aa=None, status="fact",
      notes="", src="https://www.anthropic.com/news/claude-4"),
 dict(provider="Anthropic", model="Claude Sonnet 4.5", tier="frontier", date="2025-09-29", event="launch",
      inp=3.0, out=15.0, ctx=200, mmlu=None, gpqa=83.4, swe=77.2, aa=None, status="fact",
      notes="", src="https://www.anthropic.com/news/claude-sonnet-4-5"),
 dict(provider="Anthropic", model="Claude Haiku 4.5", tier="efficient", date="2025-10-15", event="launch",
      inp=1.0, out=5.0, ctx=200, mmlu=None, gpqa=None, swe=73.3, aa=None, status="fact",
      notes="", src="https://www.anthropic.com/news/claude-haiku-4-5"),
 dict(provider="Anthropic", model="Claude Opus 4.5", tier="frontier", date="2025-11-24", event="launch",
      inp=5.0, out=25.0, ctx=200, mmlu=None, gpqa=87.0, swe=80.9, aa=None, status="mixed",
      notes="Opus tier -67% price cut. SWE 80.9 fact; GPQA 87.0 [ESTIMATE - unverified].",
      src="https://www.anthropic.com/news/claude-opus-4-5"),
 dict(provider="Anthropic", model="Claude Opus 4.8", tier="frontier", date="2026-05-28", event="launch",
      inp=5.0, out=25.0, ctx=1000, mmlu=None, gpqa=93.6, swe=88.6, aa=56.0, status="mixed",
      notes="SWE via llm-stats; AA v4.1 snapshot conflicts exist (56 vs 61.4 across modes).",
      src="https://llm-stats.com/benchmarks/swe-bench-verified; https://benchlm.ai/benchmarks/artificialanalysis"),
 dict(provider="Anthropic", model="Claude Fable 5", tier="frontier", date="2026-06-09", event="launch",
      inp=10.0, out=50.0, ctx=1000, mmlu=None, gpqa=92.6, swe=95.0, aa=59.9, status="mixed",
      notes="New Mythos-class tier above Opus; premium price point.",
      src="https://www.anthropic.com/claude/fable; https://benchlm.ai/benchmarks/gpqaDiamond"),
 dict(provider="Anthropic", model="Claude Sonnet 5", tier="efficient", date="2026-06-30", event="launch",
      inp=2.0, out=10.0, ctx=1000, mmlu=None, gpqa=None, swe=85.2, aa=57.0, status="mixed",
      notes="Intro pricing through 2026-08-31; list $3/$15 from Sep 1. AA ~57 secondary source.",
      src="https://www.anthropic.com/news/claude-sonnet-5"),
 dict(provider="Anthropic", model="Claude Opus 5", tier="frontier", date="2026-07-24", event="launch",
      inp=5.0, out=25.0, ctx=1000, mmlu=None, gpqa=None, swe=97.0, aa=60.7, status="mixed",
      notes="SWE-bench sources conflict 96.0 vs 97.0 [FLAG]. AA v4.1 #1 (60.7).",
      src="https://llm-stats.com/benchmarks/swe-bench-verified; https://benchlm.ai/benchmarks/artificialanalysis"),
 # ---------------- Google ----------------
 dict(provider="Google", model="Gemini 1.0 Pro", tier="efficient", date="2023-12-13", event="launch",
      inp=0.50, out=1.50, ctx=32, mmlu=71.8, gpqa=None, swe=None, aa=None, status="fact",
      notes="Converted from official per-character pricing.",
      src="https://blog.google/technology/ai/google-gemini-ai/"),
 dict(provider="Google", model="Gemini 1.5 Pro", tier="frontier", date="2024-05-14", event="launch",
      inp=3.50, out=10.50, ctx=1000, mmlu=85.9, gpqa=None, swe=None, aa=None, status="fact",
      notes="<=128K-prompt tier shown; 2x above 128K. 1M context (2M from Jun 2024).",
      src="https://arxiv.org/abs/2403.05530"),
 dict(provider="Google", model="Gemini 1.5 Pro", tier="frontier", date="2024-10-01", event="reprice",
      inp=1.25, out=5.0, ctx=2000, mmlu=85.9, gpqa=None, swe=None, aa=None, status="fact",
      notes="-64% input / -52% output.",
      src="https://developers.googleblog.com/en/updated-production-ready-gemini-models-reduced-15-pro-pricing-increased-rate-limits-and-more/"),
 dict(provider="Google", model="Gemini 1.5 Flash", tier="efficient", date="2024-05-14", event="launch",
      inp=0.35, out=1.05, ctx=1000, mmlu=78.9, gpqa=None, swe=None, aa=None, status="fact",
      notes="", src="https://arxiv.org/abs/2403.05530"),
 dict(provider="Google", model="Gemini 1.5 Flash", tier="efficient", date="2024-08-12", event="reprice",
      inp=0.075, out=0.30, ctx=1000, mmlu=78.9, gpqa=None, swe=None, aa=None, status="fact",
      notes="~-78% cut.",
      src="https://developers.googleblog.com/en/gemini-15-flash-updates-google-ai-studio-gemini-api/"),
 dict(provider="Google", model="Gemini 2.0 Flash", tier="efficient", date="2025-02-05", event="launch",
      inp=0.10, out=0.40, ctx=1000, mmlu=None, gpqa=60.1, swe=None, aa=None, status="fact",
      notes="GA pricing; dropped the 128K tier split.",
      src="https://developers.googleblog.com/en/gemini-2-family-expands/"),
 dict(provider="Google", model="Gemini 2.5 Pro", tier="frontier", date="2025-06-17", event="launch",
      inp=1.25, out=10.0, ctx=1000, mmlu=None, gpqa=86.4, swe=63.8, aa=None, status="fact",
      notes="<=200K tier. GPQA 86.4 independently measured (vendor launch fig 84.0).",
      src="https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/; https://www.vals.ai/benchmarks/gpqa"),
 dict(provider="Google", model="Gemini 2.5 Flash", tier="efficient", date="2025-06-17", event="launch",
      inp=0.30, out=2.50, ctx=1000, mmlu=None, gpqa=78.3, swe=None, aa=None, status="fact",
      notes="GA unified pricing (an input-price INCREASE vs preview $0.15).",
      src="https://developers.googleblog.com/en/gemini-2-5-thinking-model-updates/"),
 dict(provider="Google", model="Gemini 3 Pro", tier="frontier", date="2025-11-18", event="launch",
      inp=2.0, out=12.0, ctx=1000, mmlu=None, gpqa=91.9, swe=76.2, aa=48.0, status="fact",
      notes="Price INCREASE vs 2.5 Pro. HLE 37.5. AA v4.1 = 48.",
      src="https://blog.google/products/gemini/gemini-3/"),
 dict(provider="Google", model="Gemini 3.1 Pro", tier="frontier", date="2026-02-19", event="launch",
      inp=2.0, out=12.0, ctx=2000, mmlu=None, gpqa=94.1, swe=None, aa=46.0, status="mixed",
      notes="Same price as 3 Pro, context doubled to 2M. GPQA via BenchLM Aug-2026 snapshot.",
      src="https://benchlm.ai/benchmarks/gpqaDiamond; https://artificialanalysis.ai/models/comparisons/grok-4-5-vs-gemini-3-1-pro-preview"),
 dict(provider="Google", model="Gemini 3.6 Flash", tier="efficient", date="2026-07-21", event="launch",
      inp=1.50, out=7.50, ctx=1000, mmlu=None, gpqa=None, swe=None, aa=None, status="fact",
      notes="Output 17% cheaper than 3.5 Flash; Flash tier has moved upmarket since 2025.",
      src="https://9to5google.com/2026/07/21/gemini-3-6-flash/"),
 # ---------------- Meta (hosted via Together AI) ----------------
 dict(provider="Meta", model="Llama 2 70B (Together)", tier="efficient", date="2023-07-18", event="launch",
      inp=0.90, out=0.90, ctx=4, mmlu=68.9, gpqa=None, swe=None, aa=None, status="estimate",
      notes="Hosted price ESTIMATE (Together AI, late 2023; archives unavailable).",
      src="https://ai.meta.com/llama/; https://www.together.ai/pricing"),
 dict(provider="Meta", model="Llama 3.1 405B (Together)", tier="frontier", date="2024-07-23", event="launch",
      inp=3.50, out=3.50, ctx=128, mmlu=88.6, gpqa=51.1, swe=None, aa=None, status="fact",
      notes="First open frontier-scale model; Together AI list price.",
      src="https://ai.meta.com/blog/meta-llama-3-1/; https://www.together.ai/pricing"),
 dict(provider="Meta", model="Llama 4 Maverick (Together)", tier="efficient", date="2025-04-05", event="launch",
      inp=0.27, out=0.85, ctx=1000, mmlu=None, gpqa=69.8, swe=None, aa=None, status="fact",
      notes="400B MoE / 17B active, multimodal. GPQA from Meta model card.",
      src="https://ai.meta.com/blog/llama-4-multimodal-intelligence/; https://openrouter.ai/meta-llama/llama-4-maverick"),
 # ---------------- DeepSeek ----------------
 dict(provider="DeepSeek", model="DeepSeek-V2", tier="efficient", date="2024-05-07", event="launch",
      inp=0.14, out=0.28, ctx=128, mmlu=78.5, gpqa=None, swe=None, aa=None, status="fact",
      notes="CNY 1/2 per 1M converted; triggered the China price war.",
      src="https://cyber.fsi.stanford.edu/publication/taking-stock-deepseek-shock"),
 dict(provider="DeepSeek", model="DeepSeek-V3", tier="efficient", date="2024-12-26", event="launch",
      inp=0.27, out=1.10, ctx=64, mmlu=88.5, gpqa=59.1, swe=None, aa=None, status="fact",
      notes="671B MoE / 37B active; ~$5.6M training cost.",
      src="https://arxiv.org/abs/2412.19437"),
 dict(provider="DeepSeek", model="DeepSeek-R1", tier="efficient", date="2025-01-20", event="launch",
      inp=0.55, out=2.19, ctx=64, mmlu=90.8, gpqa=71.5, swe=49.2, aa=None, status="fact",
      notes="o1-class reasoning at ~1/27th o1's output price ('DeepSeek shock').",
      src="https://arxiv.org/abs/2501.12948"),
 dict(provider="DeepSeek", model="DeepSeek-V3.2-Exp", tier="efficient", date="2025-09-29", event="launch",
      inp=0.28, out=0.42, ctx=128, mmlu=None, gpqa=None, swe=None, aa=24.7, status="fact",
      notes="Sparse attention; 'API prices drop 50%+'. AA 24.7 is non-reasoning mode.",
      src="https://venturebeat.com/ai/deepseeks-new-v3-2-exp-model-cuts-api-pricing-in-half-to-less-than-3-cents"),
 dict(provider="DeepSeek", model="DeepSeek-V4-Pro", tier="efficient", date="2026-05-31", event="reprice",
      inp=0.435, out=0.87, ctx=1000, mmlu=None, gpqa=None, swe=80.6, aa=44.0, status="mixed",
      notes="Permanent -75% cut (launch ~$1.74/$3.48 INFERRED). SWE 80.6 = V4-Pro-Max config.",
      src="https://thetechportal.com/2026/05/23/chinas-deepseek-permanently-cuts-prices-of-flagship-v4-pro-ai-model-by-75/; https://artificialanalysis.ai/models/deepseek-v4-pro"),
 dict(provider="DeepSeek", model="DeepSeek-V4-Flash", tier="efficient", date="2026-07-31", event="launch",
      inp=0.14, out=0.28, ctx=1000, mmlu=None, gpqa=None, swe=None, aa=50.0, status="fact",
      notes="AA v4.1 = 50, ~Opus-4.8-class per AA, at ~1% of Opus output price.",
      src="https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash; https://www.caixinglobal.com/2026-08-01/deepseek-releases-official-v4-flash-model-as-chinas-ai-race-intensifies-102470292.html"),
 # ---------------- Mistral ----------------
 dict(provider="Mistral", model="Mixtral 8x7B", tier="efficient", date="2023-12-11", event="launch",
      inp=0.54, out=0.54, ctx=32, mmlu=70.6, gpqa=None, swe=None, aa=None, status="fact",
      notes="First prominent open MoE; aggregator median price.",
      src="https://mistral.ai/news/mixtral-of-experts/"),
 dict(provider="Mistral", model="Mistral Large 2", tier="frontier", date="2024-07-24", event="launch",
      inp=3.0, out=9.0, ctx=128, mmlu=84.0, gpqa=None, swe=None, aa=None, status="fact",
      notes="Cut to $2/$6 in Sep 2024.", src="https://mistral.ai/news/mistral-large-2407/"),
 dict(provider="Mistral", model="Mistral Medium 3", tier="efficient", date="2025-05-07", event="launch",
      inp=0.40, out=2.0, ctx=128, mmlu=None, gpqa=None, swe=None, aa=None, status="fact",
      notes="Vendor claim: ~90% of Claude 3.7 Sonnet at ~8x lower cost.",
      src="https://mistral.ai/news/mistral-medium-3"),
 dict(provider="Mistral", model="Mistral Large 3", tier="efficient", date="2025-12-02", event="launch",
      inp=0.50, out=1.50, ctx=256, mmlu=None, gpqa=44.0, swe=None, aa=None, status="mixed",
      notes="Apache 2.0 open weights, non-reasoning. GPQA ~44 independent eval [approx].",
      src="https://llm-stats.com/models/mistral-large-latest"),
 dict(provider="Mistral", model="Mistral Medium 3.5", tier="efficient", date="2026-04-29", event="launch",
      inp=1.50, out=7.50, ctx=262, mmlu=None, gpqa=None, swe=None, aa=29.9, status="fact",
      notes="Reasoning flagship priced ABOVE Large 3 (counter-trend).",
      src="https://blog.galaxy.ai/model/mistral-medium-3-5"),
 # ---------------- xAI ----------------
 dict(provider="xAI", model="Grok 3", tier="frontier", date="2025-04-09", event="launch",
      inp=3.0, out=15.0, ctx=131, mmlu=None, gpqa=84.6, swe=None, aa=None, status="mixed",
      notes="API launch date. GPQA is xAI-announced (vendor figure).",
      src="https://x.ai/news/grok-3"),
 dict(provider="xAI", model="Grok 4", tier="frontier", date="2025-07-09", event="launch",
      inp=3.0, out=15.0, ctx=256, mmlu=None, gpqa=87.5, swe=None, aa=None, status="mixed",
      notes="GPQA ~87.5 (88.9 Heavy). SWE ~72-75 leaked/unofficial - EXCLUDED.",
      src="https://x.ai/news/grok-4"),
 dict(provider="xAI", model="Grok 4 Fast", tier="efficient", date="2025-09-19", event="launch",
      inp=0.20, out=0.50, ctx=2000, mmlu=None, gpqa=None, swe=None, aa=None, status="fact",
      notes="~98% cost cut vs Grok 4 at near-Grok-4 capability; 2M context.",
      src="https://simonwillison.net/2025/Sep/20/grok-4-fast/"),
 dict(provider="xAI", model="Grok 4.5", tier="frontier", date="2026-07-08", event="launch",
      inp=2.0, out=6.0, ctx=500, mmlu=None, gpqa=None, swe=86.6, aa=54.0, status="fact",
      notes="SWE via llm-stats; AA v4.1 = 54 (#1 agentic tool use).",
      src="https://llm-stats.com/benchmarks/swe-bench-verified; https://www.datacamp.com/blog/grok-4-5"),
 # ---------------- Moonshot (Kimi) ----------------
 dict(provider="Moonshot", model="Kimi K2", tier="efficient", date="2025-07-11", event="launch",
      inp=0.60, out=2.50, ctx=128, mmlu=None, gpqa=None, swe=65.8, aa=None, status="fact",
      notes="1T MoE / 32B active, open weights.",
      src="https://moonshotai.github.io/Kimi-K2/; https://artificialanalysis.ai/models/kimi-k2"),
 dict(provider="Moonshot", model="Kimi K2.5", tier="efficient", date="2026-01-27", event="launch",
      inp=0.60, out=3.0, ctx=256, mmlu=None, gpqa=None, swe=76.8, aa=None, status="fact",
      notes="Multimodal; 'Agent Swarm'.",
      src="https://www.codecademy.com/article/kimi-k-2-5-complete-guide-to-moonshots-ai-model"),
 dict(provider="Moonshot", model="Kimi K3", tier="frontier", date="2026-07-16", event="launch",
      inp=3.0, out=15.0, ctx=1000, mmlu=None, gpqa=None, swe=93.4, aa=57.1, status="fact",
      notes="2.8T params, largest open-weight model ever; open challenger pricing UP into frontier tier.",
      src="https://artificialanalysis.ai/articles/kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5; https://llm-stats.com/benchmarks/swe-bench-verified"),
 # ---------------- Alibaba (Qwen) ----------------
 dict(provider="Alibaba", model="Qwen2.5-Max", tier="frontier", date="2025-01-28", event="launch",
      inp=1.60, out=6.40, ctx=32, mmlu=None, gpqa=None, swe=None, aa=None, status="fact",
      notes="Launched mid-DeepSeek-shock.", src="https://x.com/Alibaba_Qwen/status/1884995327318782086"),
 dict(provider="Alibaba", model="Qwen3-235B", tier="efficient", date="2025-04-28", event="launch",
      inp=0.70, out=2.80, ctx=128, mmlu=None, gpqa=71.1, swe=None, aa=None, status="fact",
      notes="Apache 2.0; hybrid thinking modes; Alibaba Cloud price.",
      src="https://qwenlm.github.io/blog/qwen3/"),
 dict(provider="Alibaba", model="Qwen 3.6 Plus", tier="efficient", date="2026-04-20", event="launch",
      inp=0.325, out=1.95, ctx=1000, mmlu=None, gpqa=87.8, swe=78.8, aa=None, status="mixed",
      notes="Open-weight workhorse tier; benchmarks via 2026 aggregators.",
      src="https://openrouter.ai/qwen/qwen3.6-plus; https://codersera.com/blog/qwen-3-5-complete-guide-2026/"),
 dict(provider="Alibaba", model="Qwen 3.7 Max", tier="frontier", date="2026-05-19", event="launch",
      inp=2.50, out=7.50, ctx=1000, mmlu=None, gpqa=92.4, swe=80.4, aa=46.0, status="fact",
      notes="List price (50% promo exists - modeled at list).",
      src="https://artificialanalysis.ai/models/qwen3-7-max"),
]

# open_weights: yes = weights publicly downloadable at release (incl. Llama-license and
# Mistral research-license weights); unverified = license not confirmed in this research.
EVENTS = [
 ("2022-09-01","OpenAI","GPT-3 davinci","$60 -> $20 per 1M (-67%), first major cut","https://the-decoder.com/openai-cuts-prices-for-gpt-3-by-two-thirds/"),
 ("2023-03-01","OpenAI","GPT-3.5 Turbo","Chat API launch at $2 flat: 90% below davinci","https://openai.com/blog/introducing-chatgpt-and-whisper-apis"),
 ("2023-11-06","OpenAI","GPT-4 Turbo","Launch at $10/$30: 3x/2x cheaper than GPT-4, 16x context","https://openai.com/index/new-models-and-developer-products-announced-at-devday/"),
 ("2023-11-21","Anthropic","Claude 2.1","$11.02/$32.68 -> $8/$24 (-27%)","https://www.anthropic.com/news/claude-2-1"),
 ("2024-01-25","OpenAI","GPT-3.5 Turbo (0125)","$1.00/$2.00 -> $0.50/$1.50","https://cointelegraph.com/news/openai-gpt-4-update-price-drop-new-embeddings-models"),
 ("2024-05-07","DeepSeek","DeepSeek-V2","Launch at ~$0.14/$0.28 ignites China price war (Alibaba cut up to 97%)","https://cyber.fsi.stanford.edu/publication/taking-stock-deepseek-shock"),
 ("2024-05-13","OpenAI","GPT-4o","Launch at $5/$15: -50% vs GPT-4 Turbo at higher capability","https://openai.com/index/hello-gpt-4o/"),
 ("2024-08-06","OpenAI","GPT-4o (0806)","$5/$15 -> $2.50/$10 (-50%/-33%)","https://developers.openai.com/api/docs/models/gpt-4o"),
 ("2024-08-12","Google","Gemini 1.5 Flash","$0.35/$1.05 -> $0.075/$0.30 (~-78%)","https://developers.googleblog.com/en/gemini-15-flash-updates-google-ai-studio-gemini-api/"),
 ("2024-10-01","Google","Gemini 1.5 Pro","$3.50/$10.50 -> $1.25/$5.00 (-64%/-52%)","https://developers.googleblog.com/en/updated-production-ready-gemini-models-reduced-15-pro-pricing-increased-rate-limits-and-more/"),
 ("2025-01-20","DeepSeek","DeepSeek-R1","o1-class reasoning at $0.55/$2.19 (~1/27th of o1 output price)","https://arxiv.org/abs/2501.12948"),
 ("2025-06-10","OpenAI","o3","$10/$40 -> $2/$8 (-80%), same model, optimized inference","https://venturebeat.com/ai/openai-announces-80-price-drop-for-o3-its-most-powerful-reasoning-model"),
 ("2025-09-19","xAI","Grok 4 Fast","Near-Grok-4 capability at $0.20/$0.50 vs $3/$15 (~-98%)","https://simonwillison.net/2025/Sep/20/grok-4-fast/"),
 ("2025-09-29","DeepSeek","DeepSeek-V3.2-Exp","API prices cut 50%+ to $0.28/$0.42 via sparse attention","https://venturebeat.com/ai/deepseeks-new-v3-2-exp-model-cuts-api-pricing-in-half-to-less-than-3-cents"),
 ("2025-11-24","Anthropic","Claude Opus 4.5","Opus tier $15/$75 -> $5/$25 (-67%)","https://www.anthropic.com/news/claude-opus-4-5"),
 ("2025-12-10","OpenAI","GPT-5.2","COUNTER-TREND: flagship price INCREASE $1.25/$10 -> $1.75/$14 (+40%)","https://openrouter.ai/openai/gpt-5.2"),
 ("2026-04-23","OpenAI","GPT-5.5","COUNTER-TREND: flagship at $5/$30, 4x GPT-5.1 input price in 5 months","https://en.wikipedia.org/wiki/GPT-5.5"),
 ("2026-05-31","DeepSeek","DeepSeek V4-Pro","Permanent -75% cut to $0.435/$0.87 (1M-context frontier model)","https://thetechportal.com/2026/05/23/chinas-deepseek-permanently-cuts-prices-of-flagship-v4-pro-ai-model-by-75/"),
 ("2026-07-30","OpenAI","GPT-5.6 Luna","$1.00/$6.00 -> $0.20/$1.20 (-80%) three weeks after launch; Terra -20%","https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html"),
 ("2026-07-31","DeepSeek","DeepSeek V4-Flash","~Opus-4.8-class (AA 50) at $0.14/$0.28 - 'race to zero'","https://www.axios.com/2026/08/01/deepseek-model-cheap-ai-price-war"),
]

OPEN = {'Llama 2 70B (Together)': 'yes', 'Llama 3.1 405B (Together)': 'yes', 'Llama 4 Maverick (Together)': 'yes', 'DeepSeek-V2': 'yes', 'DeepSeek-V3': 'yes', 'DeepSeek-R1': 'yes', 'DeepSeek-V3.2-Exp': 'yes', 'DeepSeek-V4-Pro': 'yes', 'DeepSeek-V4-Flash': 'unverified', 'Mixtral 8x7B': 'yes', 'Mistral Large 2': 'yes', 'Mistral Large 3': 'yes', 'Qwen3-235B': 'yes', 'Qwen 3.6 Plus': 'unverified', 'Kimi K2': 'yes', 'Kimi K2.5': 'unverified', 'Kimi K3': 'yes'}

def blended(inp, out):
    return (3 * inp + out) / 4.0

def capability(row):
    """Composite capability 0-1. Returns (value, basis)."""
    g = (row["gpqa"] - 25) / 75 if row["gpqa"] is not None else None
    s = row["swe"] / 100 if row["swe"] is not None else None
    if g is not None and s is not None:
        return (g + s) / 2, "gpqa+swe"
    if g is not None:
        return g, "gpqa"
    if s is not None:
        return s, "swe"
    if row["mmlu"] is not None:
        return K_MMLU_CHAIN * (row["mmlu"] - 25) / 75, "mmlu_chained[E]"
    return None, "none"

# GPT-3 anchor
gpt3 = M[0]
c0, _ = capability(gpt3)
anchor = c0 / blended(gpt3["inp"], gpt3["out"])   # intelligence per dollar of GPT-3

os.makedirs("data", exist_ok=True)
with open("data/models.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["provider","model","tier","open_weights","date","event","input_usd_per_1m","output_usd_per_1m",
                "blended_usd_per_1m_3to1","context_k_tokens","mmlu","gpqa_diamond",
                "swe_bench_verified","aa_index_v4_1","capability_composite_0to1","capability_basis",
                "intelligence_per_dollar_index_gpt3eq1","status","notes","sources","date_accessed"])
    for r in M:
        b = blended(r["inp"], r["out"])
        c, basis = capability(r)
        idx = (c / b) / anchor if c is not None else None
        w.writerow([r["provider"], r["model"], r["tier"], OPEN.get(r["model"], "no"), r["date"], r["event"],
                    r["inp"], r["out"], round(b, 4), r["ctx"] * 1000,
                    r["mmlu"] or "", r["gpqa"] or "", r["swe"] or "", r["aa"] or "",
                    round(c, 4) if c is not None else "", basis,
                    round(idx, 1) if idx is not None else "",
                    r["status"], r["notes"], r["src"], DATE_ACCESSED])

with open("data/price_events.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["date","provider","model","event","source","date_accessed"])
    for e in EVENTS:
        w.writerow([e[0], e[1], e[2], e[3], e[4], DATE_ACCESSED])

# Console summary of headline numbers used on slides
def idx_of(name, date=None):
    for r in M:
        if r["model"] == name and (date is None or r["date"] == date):
            c, _ = capability(r)
            return (c / blended(r["inp"], r["out"])) / anchor
    return None

import datetime as dt
def years_between(d1, d2):
    a = dt.date.fromisoformat(d1); b = dt.date.fromisoformat(d2)
    return (b - a).days / 365.25

luna = idx_of("GPT-5.6 Luna", "2026-07-30")
flash20 = idx_of("Gemini 2.0 Flash")
opus5 = idx_of("Claude Opus 5")
grok45 = idx_of("Grok 4.5")
yrs = years_between("2020-06-11", "2026-07-30")
print(f"GPT-3 blended: ${blended(60,60):.2f}, capability {c0:.4f}")
print(f"Luna idx: {luna:.0f}x | Gemini 2.0 Flash idx: {flash20:.0f}x | Opus 5 idx: {opus5:.0f}x | Grok 4.5 idx: {grok45:.0f}x")
print(f"Elapsed GPT-3 -> Luna cut: {yrs:.2f} yrs")
for label, v in [("efficient envelope (Gemini 2.0 Flash)", flash20), ("Luna", luna), ("frontier (Grok 4.5)", grok45), ("frontier (Opus 5)", opus5)]:
    print(f"  doubling time via {label}: {12 * yrs / math.log2(v):.1f} months")
print(f"Moore's law over same period: {2 ** (yrs / 2):.1f}x")
print(f"Luna blended: ${blended(0.20, 1.20):.3f} vs GPT-3 $60  -> {60 / blended(0.20, 1.20):.0f}x cheaper ({100 * (1 - blended(0.20, 1.20) / 60):.2f}% decline)")
