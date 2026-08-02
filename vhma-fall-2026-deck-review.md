# VHMA Fall 2026 — Deck Review & Rebuild Plan

**Deck reviewed:** `VHMAFall2026.pdf`, 63 slides
**Reviewer pass:** every slide read as text and rendered as an image; all load-bearing statistics independently verified
**Date:** 2 August 2026 — five weeks out from VHMA Annual Meeting, Reno, Sept 10–12

---

## 0. What I reviewed, and what I could not

I could not open the Gamma link (`gamma.app` is blocked at this environment's network proxy — the request is refused at the tunnel before it reaches Gamma, so no sharing setting will fix it). To get a true side-by-side, export the AI version from Gamma to PDF and upload it the same way you uploaded this one.

That said, the uploaded PDF appears to already contain **both** registers of slide, interleaved. Two distinct visual languages are clearly present:

- **Hand-built slides** — plain left-aligned text on white, no layout, typos intact. Slides 2, 3, 4, 9, 12, 13, 21, 29, 38, 39, 40, 47(partial), 50, 51, 61.
- **AI/Gamma-built slides** — stat cards, timelines, icon grids, generated charts, consistent green accent. Slides 5, 14, 16, 19, 22, 25, 26, 27, 28, 30, 31, 33, 34, 35, 36, 37, 42, 43, 45, 49, 52, 56, 57, 58, 59.

So the merge you're describing is already half-done. The problem is that it was merged by **accumulation** rather than by **selection** — nothing was cut when something better arrived. That is the single biggest issue with the deck and it drives most of what follows.

---

## 1. Headline judgment

The raw material here is genuinely strong. The Rosie/Zoetis pairing, the trust-ladder case study, "You Already Know How to Do This — You've Hired People Before," the transparency audit, and the horses-to-automobiles parallel are all excellent. Slide 28 is the best slide in the deck and should probably be the spine of the whole talk.

Four things are working against it:

1. **It is the wrong deck for this room.** The title slide says *NVA WEBINAR / JUNE 2026*. This is the NVA webinar being repurposed for VHMA, and it still speaks to veterinarians — clinical accuracy studies, the VIN clinician statement, the veterinarian's oath. **VHMA is practice managers and hospital administrators.** They don't diagnose; they buy, staff, police, budget, and explain. Almost none of the deck is aimed at their actual job.

2. **63 slides is roughly double what the slot supports.** At a typical 45–60 minute conference session with Q&A, you have room for about 32–40 slides at this density.

3. **Six slides are blank or near-blank, one is duplicated, and there are eleven typos** — including one on the second slide and one that renders as a cut-off word. In a talk about rigor and vendor transparency, sloppy slides undercut the argument.

4. **The strongest facts are under-told and the weakest are over-shown.** The single most damning detail of the Zoetis story isn't on the slide. Meanwhile two slides carry 27 and 26 unreadable tiles apiece.

---

## 2. The ten changes that matter most

| # | Change | Why |
|---|---|---|
| 1 | Retitle for VHMA; kill every "NVA Webinar / June 2026" and "Day 1" reference | Slides 1, 57, 58, 59, 63 currently name the wrong event |
| 2 | Cut to ~38 slides | See disposition table, §4 |
| 3 | Add the missing Zoetis detail: Zoetis allegedly **altered the AI report after the clinic reported the error**, apologized, admitted fault, and said it had happened to other Imagyst users | This is the fact that makes the room gasp, and it's the manager's lesson: your audit trail is the vendor's audit trail |
| 4 | Rewrite the Rosie slides — several details are wrong (§3) | It's your opening story; it has to be bulletproof |
| 5 | Build out slide 9, "Model Gap vs Absorption Gap" — currently a naked title followed by two blank slides | Best frame in the deck, entirely unbuilt |
| 6 | Add a **Monday-morning AI policy** slide | The artifact managers photograph and take home; nothing in the deck currently tells them what to *do* |
| 7 | Add an **ROI / what-it-costs** slide | Zero dollar figures in 63 slides for an audience whose job is the P&L |
| 8 | Add a **vendor due-diligence** slide | Direct, actionable payoff to the 6.4% transparency stat |
| 9 | Rebuild slides 42/43 as a two-beat visual reveal instead of 53 tiny tiles | Unreadable past row three of a ballroom |
| 10 | Fix all typos and the two rendering bugs (slides 29, 37) | Credibility |

---

## 3. Fact-check

### Confirmed as stated — use with confidence

| Claim | Slide | Status |
|---|---|---|
| Zoetis lawsuit: Columbia Veterinary Hospital, The Dalles OR; Wasco County Court; ≥$50,000; fraud + Oregon Unlawful Trade Practices Act; Oct 2025 incident; 11-year-old Belgian Tervuren | 7 | Confirmed |
| PetSmart Charities–Gallup: 52% skipped or declined care; 71% cite cost | 52 | Confirmed (n=2,498 owners, fielded Nov 13 2024 – Jan 9 2025) |
| Horses = 80% of work among 8,000 vets (1900) → 10% among 14,000 (1920) | 47, 48 | Confirmed, AVMA *One for the History Books*, JAVMA News, 15 Jul 2013 |
| 71 commercial veterinary AI products audited; 63% disclosed zero validation metrics | 35 | Confirmed, Brundage, *Frontiers in Veterinary Science*, 2026 |
| ACVR/ECVDI position statement, March 2025 | 36 | Confirmed |
| AAVSB scalpel quote, March 2025 | 45 | Confirmed |
| Instinct Science 2026: ~73% report efficiency gains | 26 | Confirmed |

### Wrong or imprecise — must fix

| Slide | Currently says | Should say |
|---|---|---|
| 5, 6 | "A non-biologist tech founder's dog received a fatal prognosis in May 2024" | **Paul Conyngham**, Sydney data engineer, co-founder of Core Intelligence Technologies. Dog is **Rosie, an 8-year-old rescue Staffordshire bull terrier cross**, with aggressive **mast cell cancer**; prognosis 1–6 months |
| 5 | "UNSW, ~$3,000" | Work involved **UNSW *and* the University of Queensland** — naming only UNSW under-credits it |
| 5 | Implies a 2024–2025 arc | Vaccine was administered **over the Christmas break, December 2025**; 75% shrinkage of the hock tumour **within one month** |
| 5 | "3.3M views when the story hit the press" | Unverifiable. Cut it — it's the weakest line on an otherwise strong slide and invites "where's that from?" |
| 7 | Headline: "AI Misdiagnosis Kills 11-Year-Old Dog — Vet Sues" | Accurate but ambiguous — reads as though the vet is being sued. Use **"The Vet Sued the AI Company"** |
| 7 | Omits the confirmatory lab | Cancer was confirmed by the **Oregon State University Veterinary Diagnostic Lab** |
| 22 | "Source: CoVet Q1 2026 Veterinary AI Survey, 120+ veterinary professionals globally" | n≈120 is thin to hang six hero percentages on. Either move to a single line, or replace with Instinct Science 2026 (below), which is better powered |
| 52 | "52% Skipped Care — U.S. pet owners who declined or 71% cite cost as the primary reason" | Broken sentence. Should read: **"52% of U.S. pet owners have skipped or declined recommended care. Of those, 71% cite cost."** |
| 25 | Barrier percentages sum to 88% | Either it's multi-select (say so) or categories are missing (say so). As drawn, a numerate manager will notice |
| 16 | "Hilius.AI" | Verify the spelling and that the practice and "Tom" are comfortable being named on a conference slide |

### Stronger, better-sourced numbers available — recommend swapping in

| Fact | Source | Use it on |
|---|---|---|
| **48%** of general practices use AI in some capacity; **63%** for records/SOAP notes; **38%** for diagnostic support; **91%** adopted or changed at least one technology in the past year | Instinct Science, *2026 State of General Practice Veterinary Care* | Replaces or reinforces slide 19/22 — bigger sample, cleaner provenance |
| Vet tech and assistant turnover runs **25–40% annually** | VHMA / AVMA practice survey data | New "Who does what now" slide — and it's *their* association's data, which lands hard in that room |
| Fewer than **10%** of GPs still run traditional fixed full-time schedules; ~**40%** offer part-time; ~**25%** have four-day weeks | Instinct Science 2026 | Supports the staffing-model argument |
| **Vetology** expanded a public AI validation dashboard to **11 metrics per classifier** across 31 retrained models, April 2026 | Vetology announcement | Perfect counter-beat to slide 43's "THE UNCLAIMED STANDARD" — someone just started claiming it |
| AI scribe economics: ~**1.5 hrs/day** recovered per clinician against **$2–5/DVM/day** software cost | Vendor-reported, triangulated across several 2026 sources | New ROI slide — label clearly as vendor-reported |

### Do not use

- The widely circulated "**average practice misses 22% of calls = $843,000 lost revenue per clinic**" figure. It's vendor marketing and the dollar amount is not defensible for a single clinic. Your own West Coast Animal Hospital numbers are stronger and are first-hand.

---

## 4. Slide-by-slide disposition

**Legend:** KEEP · FIX (copy/design) · MERGE · CUT · BUILD (exists as a stub, needs real content)

| # | Slide | Verdict | Note |
|---|---|---|---|
| 1 | Title | FIX | Wrong event. → "VHMA Annual Meeting · Reno · September 2026" |
| 2 | Outline | FIX | 3 typos: "verinary", "prfofession", stray `]`. Rewrite in manager language |
| 3 | "Before we get started.." | CUT | Empty transition |
| 4 | Asking→action / Unusable→Word Class | FIX | "Word Class" → "World Class". Deserves real design; it's a good three-beat |
| 5 | Rosie's Result | FIX | Corrections in §3. Tighten to 4 bullets |
| 6 | Rosie timeline (2 vets) | KEEP | Strong. The "11 months late" beat is the emotional engine |
| — | **NEW: the oncologist's caution** | BUILD | One dog, one tumour, no controlled trial. Protects you from over-claiming |
| 7 | Zoetis lawsuit | FIX | Add the altered-report allegation. This is the payoff |
| 8 | *blank* | CUT | |
| 9 | Model Gap vs Absorption Gap | BUILD | Naked title. Best unbuilt idea in the deck |
| 10 | *blank* | CUT | |
| 11 | *blank* | CUT | |
| 12 | West Coast Animal Hospital intro | FIX | Raw text. Needs layout. "a AI Receptionist" → "an AI receptionist" |
| 13 | "Can this be done?" → six questions | KEEP | Well-built |
| 14 | Trust ladder, steps 1–4 | KEEP | Excellent — arguably your core manager content |
| 15 | Agenda divider (1 of 3) | KEEP | Good pattern, highlight moves correctly |
| 16 | What changed when the agent took the phones | KEEP | Verify "Hilius.AI" and naming consent |
| 17 | METR task-length chart | FIX | Powerful chart, zero explanation. Add a title and one plain-English line: *"The length of task an AI can finish on its own is doubling roughly every seven months"* |
| 18 | PIMS-centered universe | FIX | "PIMs" → "PIMS" (3×) |
| 19 | The market has moved (47/50/80.5/8.6) | KEEP | Consider adding Instinct's 48% |
| 20 | Infinity loop | FIX | No title. Unclear what it argues |
| 21 | Scribes → action (9 items) | KEEP | |
| 22 | Curiosity → daily workflow (6 stats) | FIX | Sample-size caveat, §3 |
| 23 | Four-quadrant workflow | MERGE | Near-duplicate of 20. Keep one |
| 24 | Agenda divider (2 of 3) | KEEP | |
| 25 | Barriers bar chart | FIX | Sums to 88%; declutter axis (0/10/20/30, not every 2) |
| 26 | Efficiency bar chart | FIX | Declutter axis; lead with the 73% |
| 27 | You do not install an agent | KEEP | |
| 28 | You already know how — you've hired people | KEEP | **Best slide in the deck.** Consider promoting it to the top of Act 3 |
| 29 | "mpare AI to the workflow…" | FIX | Rendering bug — the word "Compare" is cut off. Also deserves to be a real slide |
| 30 | Pets as family (83% / 44%) | KEEP | Two donuts is a lot of ink for two numbers, but it works |
| 31 | Risk tiers (low/review/human) | KEEP | Very strong for this audience |
| 32 | AI in veterinary dictation | FIX | Stock image is generic; unclear which "leading companies" |
| 33 | Clinical results worth knowing | FIX | Three clinical studies aimed at DVMs. For VHMA, compress to one slide framed as *"the evidence your doctors will ask you about"* |
| 34 | Six radiology platforms, 23% SIO detection | KEEP | Devastating and well-sourced. Change the electric-blue box to brand green |
| 35 | Safety cannot be an afterthought | KEEP | |
| 36 | ACVR/ECVDI statement | KEEP | |
| 37 | Baseline is not perfect medicine | FIX | Orphan text "Co" floating on the slide |
| 38 | VIN statement | CUT | Duplicate of 39 |
| 39 | VIN statement + attribution | FIX | Keep this one. Reframe for managers: *this is the disclosure obligation you own* |
| 40 | Don't take candy from strangers | KEEP | Good analogy setup — but it currently has no payoff slide. Add one line landing it |
| 41 | Instacart / Uber / Airbnb logos | FIX | Logos and captions misaligned on three different baselines |
| 42 | How Uber built trust (27 tiles) | FIX | Unreadable. Rebuild as reveal (§6) |
| 43 | Unclaimed standard (26 tiles) | FIX | Same. Add the Vetology April 2026 counter-beat |
| 44 | VAULT / ANI.ML | FIX | "Langage" → "Language" |
| 45 | AAVSB scalpel quote | KEEP | Add the rest of AAVSB's position: transparency, informed consent, client data privacy — all manager duties |
| 46 | Agenda divider (3 of 3) | KEEP | |
| 47 | 1900 → 1920 horses | FIX | Off-brand blue box; make both boxes consistent |
| 48 | Vet count 8,000 → 14,000 | FIX | Weak horizontal bars for two numbers. Make it one big "+75%" |
| 49 | Evolution of the medical record | KEEP | Genuinely great. The hand-writing line is the kicker |
| 50 | "2022" AI images | KEEP | |
| 51 | "Today" AI images | KEEP | Excellent before/after |
| 52 | Why protect what isn't working | FIX | Broken sentence, §3. "Millenials" → "Millennials" |
| 53 | AI black box vs council comic | KEEP | Strong visual |
| 54 | OpenVet lidocaine case | FIX | "surfaced up" → "surfaced"; "reveived" → "received" |
| 55 | Loom embed | CUT | A video thumbnail won't play from a conference deck |
| 56 | Small studies / 12.7M records | FIX | Stray "1" artifact bottom-left. Otherwise a superb closer to the evidence act |
| 57 | What you need to know | FIX | "Day 1" → wrong for a single session |
| 58 | What to practice | FIX | Same. Also entirely clinician-facing — rewrite for managers |
| 59 | Tools to try | FIX | Same "Day 1". Codex, Replit and Bolt are wrong for this room — swap for scheduling, comms and documentation tools a manager would actually pilot |
| 60 | Veterinarian's oath | FIX | Powerful, but VHMA members largely aren't veterinarians. Consider pairing with a line about the practice manager's role, or reframe as "the promise the practice makes" |
| 61 | How will change / Why will not | KEEP | Strong close |
| 62 | Thank you + QR codes | FIX | Uses a personal gmail address. Use your VetIntel address |
| 63 | "Workshop" | FIX | Wrong event tags again |

**Net:** 63 → ~38 slides after 8 cuts, 2 merges, and 8 additions.

---

## 5. New slides to build

### N1 — Model Gap vs Absorption Gap *(replaces the stub at slide 9)*

> **The models are 18 months ahead of your workflows.**
>
> **Model gap** — the distance between the best AI available and the AI you're using. Closing fast, and not your problem to solve.
>
> **Absorption gap** — the distance between the AI you're using and the AI your practice has actually absorbed into policy, training, and daily habit. Widening, and *entirely* your problem to solve.
>
> Every dollar of value in this talk lives in the second gap.

Place immediately after the Rosie/Zoetis pair. It converts two anecdotes into the organizing frame for everything after.

### N2 — Your Monday-Morning AI Policy

Six lines, big type, designed to be photographed:

1. **Inventory.** List every AI tool anyone here already pays for or uses. You will be surprised.
2. **One owner.** Name the person who approves new tools. One person.
3. **Tiers.** Low risk / review required / human required. Write down which is which.
4. **Data.** For each tool: where does client and patient data go, and who has seen the answer in writing?
5. **Disclosure.** Decide what you tell clients, and put it in the consent form.
6. **Review.** Ten calls or ten records a week, first month. Then monthly.

This is the slide the room takes home. Nothing in the current deck does this job.

### N3 — What It Costs, What It Returns

Frame honestly as vendor-reported, then give them the arithmetic to check it themselves:

- Scribe software: roughly **$2–5 per DVM per day**
- Vendor-reported recovery: **1.5–2.5 hours per clinician per day**
- Your check: pick one doctor, one week, time the notes before and after
- The number that actually matters isn't hours saved — it's **what those hours got spent on.** If they went back into the same day's overflow, you bought nothing.

That last line is the one a manager will quote to their owner.

### N4 — Seven Questions Before You Sign

Pays off the 6.4% transparency stat:

1. What are your validation metrics, and where are they published?
2. What data trained this, and does ours join it?
3. What happens to our data if we leave?
4. Who is liable when it's wrong — show me the clause.
5. Can I see a full audit trail of what it did and when?
6. Can you change a report after we've seen it? *(Ask this one because of the Zoetis allegation.)*
7. Who else in my market uses this, and may I call them?

### N5 — Who Does What Now

- 1 CSR elevated to Technician Assistant *(your West Coast example)*
- "We aren't firing people. We are promoting people."
- Tech and assistant turnover runs **25–40% a year** — VHMA's own data
- The honest framing: AI is not reducing your headcount. It is changing which 25–40% of roles you're constantly re-hiring, and what those roles are worth.

### N6 — Someone Just Claimed the Standard

Directly after slide 43. Vetology published a public AI validation dashboard — 11 metrics per classifier across 31 retrained models — in April 2026. One line of takeaway: *"The standard is unclaimed right now. That is a temporary condition, and it changes what you should demand in your next contract."*

---

## 6. Visual system fixes

**Colour.** The deck is green/teal with one grey neutral, and then breaks its own rule three times: electric blue on slides 34 and 47, pink alert on 49, red text on 30 and 52. Pick one accent for "danger/attention" — red — and use green for everything else. Convert both blue boxes to brand green.

**The 27-tile problem (slides 42, 43).** No one past the third row can read a 27-item grid. Rebuild as two beats:
- Beat 1: the Uber grid, all 27 tiles, deliberately small and unreadable, with one line — *"Uber built 30+ safety systems over 15 years."* The unreadability **is** the point.
- Beat 2: the same grid shape for veterinary AI, with 3–4 tiles filled and the rest empty outlines. *"Here is what exists in veterinary AI today."*

That's a visual argument. The current version is a wall of text pretending to be a graphic.

**Charts (25, 26, 48).** All three are Gamma defaults. Axis labels every 2% on slide 25 create 18 gridlines for a 9-bar chart. Reduce to 0/10/20/30. On slide 48, two bars for two numbers is wasted space — make it one large **"8,000 → 14,000 vets (+75%)"** with the automobile image behind it.

**Blank space.** Slides 3, 4, 12, 29, 40, 61 are large type floating in the top-left of an otherwise empty 16:9 frame. That reads as unfinished, not minimal. Either centre them as full-bleed statement slides or give them an image.

**Density.** Slide 28 has six paragraphs of body copy. It's your best content and it's unreadable on screen — it's a script, not a slide. Split into two slides of three, or reduce each to its first sentence and speak the rest.

**Typo sweep.** `verinary` → veterinary · `prfofession` → profession · `Word Class` → World Class · `Onegenetically` → One genetically · `mpare` → Compare · `PIMs` → PIMS · `Langage` → Language · `reveived` → received · `surfaced up` → surfaced · `Millenials` → Millennials · `a AI Receptionist` → an AI receptionist · orphan `Co` on slide 37 · stray `1` on slide 56.

---

## 7. Instructions to hand to whoever edits the deck

Copy the blocks below directly.

### 7a. Global pass

```
Global changes to VHMAFall2026:

1. Replace every instance of "NVA WEBINAR" and "JUNE 2026" with
   "VHMA ANNUAL MEETING" and "RENO · SEPTEMBER 2026". Affects slides 1, 63.
2. Replace every "DAY 1 TAKEAWAYS" eyebrow with "TAKEAWAYS".
   Affects slides 57, 58, 59.
3. Replace the contact address on slide 62 with the VetIntel address.
4. Delete slides 3, 8, 10, 11, 38, 55.
5. Merge slides 20 and 23 into one titled workflow diagram.
6. Fix these typos exactly:
   slide 2  "verinary" -> "veterinary"; "prfofession" -> "profession";
            delete the trailing "]"
   slide 4  "Word Class" -> "World Class"
   slide 5  "Onegenetically" -> "One genetically"
   slide 12 "a AI Receptionist" -> "an AI receptionist"
   slide 18 "PIMs" -> "PIMS" (all instances)
   slide 29 restore the cut-off first word: "Compare AI to the workflow..."
   slide 37 delete the orphan text "Co"
   slide 44 "Langage" -> "Language"
   slide 52 "Millenials" -> "Millennials"
   slide 54 "surfaced up" -> "surfaced"; "reveived" -> "received"
   slide 56 delete the stray "1" at bottom left
7. Colour: convert the electric-blue fills on slides 34 and 47 to the
   deck's brand green. Reserve red strictly for warnings.
8. Charts on slides 25 and 26: reduce x-axis labels to 0/10/20/30 and
   0/10/20/30/40/50. Remove intermediate gridlines.
```

### 7b. Gamma prompts for the new slides

Paste each as a new-card prompt:

```
Slide: "Model Gap vs Absorption Gap"
Two-column comparison, brand green. Left column "MODEL GAP" — the distance
between the best AI available and the AI you use; closing fast; not your
problem to solve. Right column "ABSORPTION GAP" — the distance between the
AI you use and the AI your practice has absorbed into policy, training and
daily habit; widening; entirely your problem to solve. Single bold line
beneath both columns: "Every dollar of value in this talk lives in the
second gap." Minimal, large type, no icons.
```

```
Slide: "Your Monday-Morning AI Policy"
Numbered list of six items, large readable type, designed to be photographed
by an audience. 1 Inventory — list every AI tool anyone already pays for or
uses. 2 One owner — name the single person who approves new tools.
3 Tiers — low risk / review required / human required, written down.
4 Data — where does client and patient data go, answered in writing.
5 Disclosure — what you tell clients, in the consent form.
6 Review — ten calls or records a week for the first month, then monthly.
No icons. High contrast. This is a takeaway artifact, not a decoration.
```

```
Slide: "What It Costs, What It Returns"
Three stat cards then one closing line. Card 1: "$2–5" / "per DVM per day" /
"typical AI scribe software cost". Card 2: "1.5–2.5 hrs" / "per clinician
per day" / "vendor-reported documentation time recovered". Card 3: "1 week" /
"one doctor" / "time the notes before and after — verify it yourself".
Closing line in bold beneath: "The number that matters isn't hours saved.
It's what those hours got spent on." Add a small footnote: "Cost and time
figures are vendor-reported; verify in your own practice."
```

```
Slide: "Seven Questions Before You Sign"
Numbered list, seven items, clean two-column layout, brand green accents.
1 What are your validation metrics, and where are they published?
2 What data trained this, and does ours join it?
3 What happens to our data if we leave?
4 Who is liable when it's wrong — show me the clause.
5 Can I see a full audit trail of what it did and when?
6 Can you change a report after we have seen it?
7 Who else in my market uses this, and may I call them?
Small caption beneath: "Question 6 exists because of the Zoetis case."
```

```
Slide: "Who Does What Now"
Left side: a promotion arrow, "1 CSR elevated to Technician Assistant",
with the pull-quote "We aren't firing people. We are promoting people."
Right side: one large stat "25–40%" labelled "annual turnover, veterinary
technicians and assistants — VHMA/AVMA survey data". Bottom, full width,
bold: "AI is not reducing your headcount. It is changing which roles you
re-hire every year, and what they are worth."
```

```
Slide: "Someone Just Claimed the Standard"
Single centred statement with a small logo lockup. Body: "April 2026 —
Vetology published a public AI validation dashboard: 11 metrics per
classifier, 31 models retrained." Closing line, bold: "The standard is
unclaimed today. That is temporary — and it changes what you should demand
in your next contract."
```

```
Slide: "One Dog, One Tumour"
Quiet, restrained counterpoint slide to follow the Rosie story. Three short
lines: "First personalised cancer vaccine designed for a dog." /
"One dog. One tumour. No controlled trial." / "Veterinary oncologists have
urged caution — and they are right to." Muted palette, lots of white space,
no icons, no stats.
```

### 7c. Rebuild brief for slides 42–43 (needs a designer, not a prompt)

> Build as two consecutive slides sharing an identical grid geometry.
>
> **Slide A** — 27 small tiles, Uber's safety systems, deliberately dense and small. Single headline: *"Uber built 30+ safety systems over 15 years."* Do not enlarge the tiles; the fact that the audience can't read them is the argument.
>
> **Slide B** — the same grid, same position, same tile size, relabelled for veterinary AI. Fill only 3–4 tiles in solid brand green; render the remaining 22–23 as empty outlines. Headline: *"Here is what veterinary AI has built."*
>
> The transition between the two slides carries the entire point. Nothing else should move.

### 7d. Copy corrections for existing slides

```
Slide 5 — replace the Rosie body copy with:

Paul Conyngham, a Sydney data engineer with no biology background, was told
his 8-year-old rescue Staffordshire bull terrier cross Rosie had one to six
months to live — aggressive mast cell cancer.

The pipeline: AI designed the bioinformatics workflow over 300 GB of
sequenced DNA (UNSW and the University of Queensland, ~$3,000), identified
the c-KIT driver mutation, and used AlphaFold to model the resulting
proteins and pick the neoantigens most likely to provoke an immune response.

The result: the vaccine was administered in December 2025. Within one month
the tennis-ball-sized tumour on her hock had shrunk by 75%.

[Delete the "3.3M views" line entirely.]
```

```
Slide 7 — retitle to "The Vet Sued the AI Company" and add a third
section after "What happened":

What the clinic alleges
- Zoetis marketed Vetscan Imagyst as "the world's most capable veterinary
  AI analyzer" without disclosing its limitations.
- Cancer was confirmed by the Oregon State University Veterinary
  Diagnostic Lab.
- Zoetis altered the original AI diagnostic report after clinic staff
  reported the error.
- On a call, Zoetis apologised, admitted fault, and said similar incidents
  had occurred with other Imagyst users.

Closing line, bold: "Your audit trail is only as good as your vendor's."
```

```
Slide 52 — fix the broken sentence. Replace:
  "52% Skipped Care / U.S. pet owners who declined or 71% cite cost as the
   primary reason."
with:
  "52% of U.S. pet owners have skipped or declined recommended veterinary
   care. Of those, 71% cite cost."
  Source line: PetSmart Charities–Gallup, State of Pet Care, 2025
  (n = 2,498 dog and cat owners).
```

```
Slide 17 — add a title and a plain-English caption to the METR chart:
  Title: "The Jobs Are Getting Longer"
  Caption: "The length of task an AI can finish on its own is roughly
  doubling every seven months. This is why last year's answer about what
  AI can't do is already out of date."
```

---

## 8. Two open questions for you

1. **Session length and format.** The Notion record lists this as a workshop with Pawsitive Holdings. If it's genuinely a workshop rather than a keynote, the policy slide (N2) and the vendor questions slide (N4) should become worksheet exercises rather than slides, and the deck should shrink further to leave working time.

2. **Overlap with your co-presenter.** The most likely place two speakers duplicate each other is the "what's coming next" material. Worth a 20-minute call to divide that territory before either deck is finalised.

---

## Sources

- [Oregon veterinary hospital sues tech company over AI misdiagnosis — The Daily Chronicle](https://www.chronline.com/stories/oregon-veterinary-hospital-sues-tech-company-claims-ai-misdiagnosis-led-to-dogs-death,406161)
- [Australian tech founder uses ChatGPT and AlphaFold to design dog cancer vaccine — IBTimes UK](https://www.ibtimes.co.uk/sydney-data-engineer-mrna-cancer-vaccine-dog-1785607)
- [A man used AI to help make a cancer vaccine for his dog – an oncologist urges caution — The Conversation](https://theconversation.com/a-man-used-ai-to-help-make-a-cancer-vaccine-for-his-dog-an-oncologist-urges-caution-278735)
- [52% of U.S. Pet Owners Skipped or Declined Veterinary Care — Gallup](https://news.gallup.com/poll/659057/pet-owners-skipped-declined-veterinary-care.aspx)
- [Veterinarians Say Cost Is the Main Driver of Declined Care — Gallup](https://news.gallup.com/poll/700115/veterinarians-say-cost-main-driver-declined-care.aspx)
- [2026 State of General Practice Veterinary Care — Instinct Science](https://instinct.vet/blog/2026-state-of-general-practice-veterinary-care-overview/)
- [Instinct Science Surveys Show AI Adoption, Staffing Strains in Vet Care — MyChesCo](https://www.mychesco.com/a/news/regional/instinct-science-surveys-show-ai-adoption-staffing-strains-in-vet-care/)
- [Inside CoVet's 2026 Veterinary AI Survey](https://co.vet/post/covet-2026-veterinary-ai-survey/)
- [One for the history books — AVMA / JAVMA News, 15 July 2013](https://www.avma.org/javma-news/2013-07-15/one-history-books)
- [Building a framework for responsible AI in veterinary medicine — AVMA](https://www.avma.org/news/building-framework-responsible-ai-veterinary-medicine)
- [Vetology expands public AI validation dashboard to 11 metrics per classifier — PR Newswire, April 2026](https://www.prnewswire.com/news-releases/vetology-expands-public-ai-validation-dashboard-to-11-metrics-per-classifier-commits-to-ongoing-model-retraining-302730913.html)
- [VetRec launches AI Receptionist — July 2026](https://www.morningstar.com/news/pr-newswire/20260715sf05292/vetrec-launches-ai-receptionist-to-ensure-clinics-never-miss-a-call)
- [The patchwork quilt of state veterinary telehealth laws — AAHA](https://www.aaha.org/newstat/publications/the-patchwork-quilt-of-state-veterinary-telehealth-laws/)
- [Which veterinary AI scribe is most accurate — time savings guide, 2026 (vendor-reported)](https://happydoc.ai/blog/which-veterinary-ai-scribe-is-the-most-accurate-a-2026-guide-to-time-savings-and-documentation-quality)
