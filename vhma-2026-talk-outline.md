# VHMA 2026 — Talk Outline (Reno, Sept 10–12)

Working outline for Adam's VHMA / Pawsitive Intelligence 2026 workshop. Built from the VMG One
session arc ([AI adoption strategy for veterinary practices](https://app.notion.com/p/39efed47878c8133b44efc0b677bd583))
and re-aimed at hospital managers.

Every stat below is dated and linked. **Check the Evidence Bank before putting a number on a slide** —
two of these are older than they feel.

Related Notion records:
- Event: [VHMA / Pawsitive Intelligence 2026](https://app.notion.com/p/391fed47878c81098ce7e57e055c3688)
- Announcement: [VHMA, Pawsitive Holdings to present AI workshop](https://app.notion.com/p/391fed47878c8132a570e1307e5ce810)

---

## 0. The brief we have to hit

From the VHMA / Pawsitive Holdings press release (FR, 2026-02-06), the workshop promises three things:

1. **How AI is evolving** — the pace argument.
2. **What to expect in the coming years** — the forecast.
3. **How to foster an "AI-first" culture** — the playbook.

That's the contract with the room. The outline below maps every block to one of those three, and
anything that maps to none of them gets cut.

### Logistics on record

- **Event:** VHMA Annual Meeting & Conference, Grand Sierra Resort, Reno, NV. Event record has
  2026-09-09 → 2026-09-12; press release bills the workshop Sept 10–12.
- **Co-presenter:** Pawsitive Intelligence / Pawsitive Holdings.
- **Audience:** hospital managers and administrators — *not* primarily owners or DVMs. This is the
  single biggest change from the VMG version.
- **Adam's flights:** booked. Hotel status: check needed.

### Open questions blocking the final draft

- [ ] **Slot length and format.** One 90-minute workshop, a multi-session track across Sept 10–12,
      or keynote plus breakout? The run-of-show below assumes 90 minutes with cut-downs.
- [ ] **Division of labour with Pawsitive** — who owns which blocks?
- [ ] **Room setup** — can attendees get hands on keyboards, or is it theatre-style? Determines
      whether the hands-on workshop blocks from the VMG version survive.
- [ ] **Naming.** Event record still carries the UMHL-vs-VHMA/Pawsitive caveat. Resolve before
      anything goes external.
- [ ] **Pre-session survey.** The VMG session used 3–5 questions on real client/team situations.
      Worth repeating — VHMA already agreed to a joint survey with us, so there may be a shortcut.

---

## 1. The spine

One sentence the whole talk hangs off:

> **The tools are no longer the hard part. The hard part is that your team's habits, your vendor
> contracts, and your clients' expectations are all changing at different speeds — and the manager is
> the only person in the building positioned to sequence that.**

That framing is deliberately manager-shaped. Owners hear "AI strategy." Managers hear "who does what
on Monday." Stay on the Monday side.

| Beat | Promise it satisfies | The move |
| --- | --- | --- |
| Today's AI is the worst it will ever be | How AI is evolving | Reset the pace assumption |
| Adoption is not depth, and depth is where the money is | What to expect | Show the gap between "we have a scribe" and Small Door |
| AI-first is a management practice, not a purchase | AI-first culture | Give them the playbook |

---

## 2. Run of show — 90 minute default

### Cold open — 0:00–0:05

Open on the room, not the tech. Ask for hands: *who here has a scribe in the building?* Most hands go
up. Then: *who could tell me, right now, what percentage of your medical records go through it?*

The hands drop. **That gap is the talk.** Name it out loud and promise to close it.

> Do not open with a definition of AI. This room has heard it. The press release promises evolution,
> expectation and culture — none of those need a definition slide.

### Block A — The pace — 0:05–0:20

The exponential framing, carried over from VMG. Core line: **today's AI is the worst it will ever be.**

- Ground it in vet-specific evidence rather than generic AI curves. The vet-med adoption record has
  gone from pilot announcements → teaching hospitals → PIMS-native agents inside roughly eighteen
  months. That's the curve, and it's all in our own story archive.
- Manager-specific twist the VMG version didn't need: **the pace argument is a budgeting argument.**
  If capability doubles and price falls on the timescales we're seeing, a three-year software
  commitment signed today is a bet on a market that won't exist. Say that plainly — it lands hard
  with the people who sign the contracts.

### Block B — The landscape — 0:20–0:40

The "help me make sense of the vendor flood" block. Do **not** present logo soup. Present four
layers, because layers survive new entrants and logos don't:

1. **Documentation / scribes** — the layer almost everyone has already bought. CoVet, ScribbleVet,
   VetRec.
2. **Diagnostics** — imaging and cytology. Vetology, Radimal, Zoetis Vetscan Imagyst, MediCapture
   aiScope.
3. **The PIMS itself** — the layer that just started moving. Provet Agents, Lupa Pets, CoVet↔Merlin.
4. **Open tooling** — OpenVet's VetClaw library, 51 open-source veterinary AI skills. The existence
   of this layer is the point: capability is becoming a commodity.

Payoff line for the block: **even the practices that adopted early are using a fraction of full
capability.** Then hand them the depth question — Block C.

> Worth demoing one "I didn't know it could do that" moment here if the room allows it. The VMG
> session used AI driving a browser inside a live PIMS. One early moment of genuine surprise buys
> attention for the rest of the session.

### Block C — Depth beats adoption — 0:40–0:50

The Small Door block. **95% of their medical records generated through CoVet**, after two years of
collaboration, across 13 East Coast locations with 24/7 telemedicine.

How to use it: the number is not impressive because it's big. It's impressive because it's
*saturated*. A practice at 95% has stopped treating the tool as an option — the workflow, training,
QA and expectations all got rebuilt around it. A practice at 30% has a subscription.

Then the manager question, which is the real content of this block: **what did the last 40 points
cost them?** Two years of collaboration, not a procurement decision. Walk the room through what
saturation actually requires:

- A default that is on, not opt-in.
- Someone who owns record quality and reviews samples.
- A named path for the DVM who hates it.
- Retraining when the model changes under you.

### Block D — Where it breaks — 0:50–1:03

The honesty block, and the most valuable ten minutes in the talk. Radiology is the perfect case
because the evidence genuinely conflicts.

Put two facts on one slide:

- **Murdoch University** studied six AI radiograph interpretation tools and rated performance
  **"low to moderate"** — contradicting several more favourable studies. Vendors pushed back,
  stressing the tools are decision support, not replacements.
- **Vetology**, in the same season, expanded its **public** AI validation dashboard from four metrics
  per classifier to eleven, and committed to ongoing retraining.

The synthesis — the single most useful sentence a manager will hear all day:

> **You cannot evaluate these tools from the marketing. But one vendor in this category publishes its
> validation data per classifier, in public. That is the question you ask every vendor now: where is
> your validation data, and how often do you retrain?**

That converts a scary study into a purchasing checklist. It also earns credibility with the skeptics
in the room, which makes Block F land.

Second half of the block — the other failure modes, carried from VMG: data leaks, hallucinated
authority (the fabricated-case-law pattern), and clients recording consults on their own devices.

### Block E — The floor is moving — 1:03–1:15

The Provet block, and the freshest thing in the talk.

Provet (Nordhealth) launched what it bills as the **first all-in-one veterinary PIMS built for AI
agents** (2026-07-10). The framing in their own release is the part managers need: *"unlike
third-party solutions or PIMS with bolt-on AI modules,"* the native Provet Agents run with full
context on a clinic's records, performance, operations, customer communications, inventory and
permissions.

Why this matters more to a manager than to a vet:

- **The integration tax may be temporary.** Much of the current stack is bolt-ons stitched to a PIMS.
  If the PIMS absorbs that layer, today's careful integration work becomes tomorrow's redundancy.
- **Permissions become the whole ballgame.** An agent with context on inventory, comms and
  performance is an agent that can *act*. Who approves what it does? That's a management question,
  not an IT question, and nobody else in the building is going to answer it.
- **It is not just Provet.** Lupa Pets raised a $20M Series A to expand exactly this — AI agents
  inside a practice-management system. Two independent bets on the same thesis is a trend.

Practical takeaway: **ask every PIMS vendor what their agent roadmap is before you renew.** Pair it
with the Block A budgeting argument.

### Block F — AI-first culture — 1:15–1:27

The playbook block. This is what the press release actually sold, so it cannot be rushed.

**Start with the reframe.** AI as promotion, not replacement — the "Becky" framing from the VMG
session. Offload clerical and after-hours volume so your strongest people do the work only they can
do. Line worth stealing verbatim from a prior speaker: *"It didn't replace my team, it allowed me to
promote them."*

**Then the workforce argument, which is new for this audience.** The scribe layer is now installed at
the schools:

- UC Davis School of Veterinary Medicine adopted ScribbleVet for its clinical facilities.
- Tuskegee — the first HBCU veterinary program — adopted it for its teaching hospital this month,
  explicitly to expose students to tools they'll meet in practice.
- On the corporate side, AmeriVet has been rolling ScribbleVet across its 213-hospital network.

So: **your next new grad has already been trained on an AI scribe.** If your hospital is still
debating whether to turn one on, that is now a recruiting and onboarding problem, not a technology
problem. For a room of managers who own hiring, this is the most actionable slide in the deck.

**Then the structural advantage.** Independent practices can out-manoeuvre consolidators here,
because the roles consolidators built middle-management layers for — analytics, recruitment,
marketing — are precisely what these tools do well. An independent can move on a market signal in a
week.

**Then close the block with sequencing.** Low-risk entry points that produce a visible win fast:
inbox triage, rebuilding the employee handbook, competitive intelligence on the practice down the
road. Get one "I didn't know it could do that" moment inside the building and momentum does the rest.

### Close — 1:27–1:30

The client-side shift, held to the end because it reframes everything behind it.

Pet owners are already arriving with AI-researched questions. The trajectory points toward a large
share of inbound contact being AI-mediated on both ends within a couple of years. Add the existential
thread — Walgreens moving on bloodwork, Chewy on prescriptions.

The closing frame: **practices that are unclear about their identity will struggle. Relationship-driven
ones won't.** And the manager is the person who builds or erodes that relationship, appointment by
appointment.

Last line should hand them one thing to do on Monday. Candidate: *go find out what percentage of your
records go through your scribe. That number is your AI strategy, and right now you don't know it.*
Callback to the cold open, closes the loop.

### Cut-downs

| If the slot is | Keep | Cut |
| --- | --- | --- |
| 60 min | Cold open, A (short), B, C, D, F | E folds into B as two slides; close compressed |
| 45 min | Cold open, C, D, F | A becomes one slide; B becomes the four-layer diagram only; E cut |
| Multi-session | A+B as session 1, C+D as session 2, E+F as session 3 | Nothing — add the hands-on agent-building blocks from the VMG version |

---

## 3. Evidence Bank

Dated by **publication date**, not by when it landed in our archive. Check the date column before
saying "recently" on stage.

| Fact | Published | Source | Use it for |
| --- | --- | --- | --- |
| Small Door: 95% of medical records via CoVet, 13 locations, 2 years in | **2025-04-04** | [Story](https://app.notion.com/p/392fed47878c81dbbde5f5f4142219ee) · co.vet | Block C — depth vs adoption |
| Murdoch: six AI radiograph tools "low to moderate" | **2026-05-08** | [Story](https://app.notion.com/p/391fed47878c81a89057dccbeffbf97d) · VIN News | Block D — the honest counterweight |
| Vetology: public validation dashboard 4 → 11 metrics per classifier | **2026-04-03** | [Story](https://app.notion.com/p/391fed47878c8161a956d96063dcf1c4) · PR Newswire | Block D — the purchasing checklist |
| Provet: first all-in-one PIMS built for AI agents | **2026-07-10** | [Story](https://app.notion.com/p/39cfed47878c8157a78ecdffae75dc6e) · Nordhealth | Block E — the floor is moving |
| Lupa Pets: $20M Series A for PIMS AI agents | 2026-07 | [Story](https://app.notion.com/p/396fed47878c81ee89e2e164e90f8b3f) | Block E — second bet on the thesis |
| ScribbleVet at UC Davis | **2025-12-12** | [Story](https://app.notion.com/p/391fed47878c81e4b956f3c521d64e95) | Block F — schools are training on it |
| ScribbleVet at Tuskegee (first HBCU vet program) | **2026-07-16** | [Story](https://app.notion.com/p/3a1fed47878c81749a40e3455e843893) · Instinct | Block F — freshest school proof point |
| AmeriVet rolling ScribbleVet to 213 hospitals | **2025-07-25** | [Story](https://app.notion.com/p/392fed47878c812abee1d8c7fd5b7608) | Block F — corporate scale |
| OpenVet VetClaw: 51 open-source vet AI skills | ⚠️ see caveat | [Story](https://app.notion.com/p/391fed47878c816c8a6fe4c1c4748909) | Block B — capability commoditising |
| CoVet ↔ MWI Merlin PIMS integration | 2026-07 | [Story](https://app.notion.com/p/391fed47878c8124b11ac34ed6ce1a31) | Block B — scribe becoming a hub |
| VetRec at Texas A&M | 2026-07 | [Story](https://app.notion.com/p/392fed47878c816fba9acc3763520d19) | Block F — second school data point |

### Caveats — read before slide-building

- **The Small Door number is vendor-published and ~15 months old.** Source is co.vet, CoVet's own
  site. Still the best saturation data point in vet med, but say "as of last year" and attribute it
  to CoVet, or get a refresh. There is also an unverified signal in our archive that **Small Door and
  Bond Vet have merged** — it appears as a Fountain Report email subject line, not a confirmed story.
  **Verify before mentioning Small Door on stage at all.**
- **OpenVet / VetClaw carries a published date of 2016-03-20 in the archive, which is certainly
  wrong** — a 51-skill AI library did not ship in 2016, and the source is a 2026 newsletter PDF. Use
  the fact, not the date, and log a data-quality fix.
- **Murdoch and Vetology are five weeks apart**, not simultaneous. "In the same season" is accurate;
  "the same week" is not.
- **Tuskegee's own source gives no separate go-live date** — the 2026-07-16 date is the publication
  date used as a proxy. Fine for stage use, don't over-specify.

---

## 4. Manager-specific material

Things this audience needs that the VMG owner-heavy room did not:

- **Who owns the tool.** Every AI tool in a hospital needs a named human owner. Managers are usually
  it by default and rarely by decision. Make that explicit.
- **The QA loop.** Sampling records for quality, and what to do when the model changes under you
  without notice.
- **The holdout DVM.** A concrete script for the associate who refuses. Not "get buy-in" — an actual
  sequence.
- **Consent and recording.** Clients recording consults; staff pasting patient data into consumer
  chatbots. Policy language, not vibes.
- **Contract hygiene.** Renewal length, data portability, what happens to your records if the vendor
  is acquired. Ties directly to Blocks A and E.

---

## 5. Interaction

The cold-open hand-raise, then two more:

- After Block C: *table exercise, three minutes* — what percentage of your records go through your
  scribe, and what's the single thing stopping it from being higher?
- After Block D: *show of hands* — who has ever asked a vendor for validation data? Expect near-zero.
  That silence is the teaching moment.

---

## 6. VetIntel tie-in

Keep it light. This is a VHMA workshop, not a product pitch, and the room will punish a pitch.

- The landscape map in Block B exists because we maintain the underlying data. Say that once, in
  passing.
- Offer the "break glass" framing from the VMG session — practices worried about client erosion to
  Chewy/Walgreens can monitor it in data rather than guess. Offer, don't sell.
- Capture the room: usable quotes, and manager feedback on data/AI/workflow needs. That's the event
  record's stated goal, and it's worth more than a slide of ours.

---

## 7. To do before the draft deck

- [ ] Confirm slot length, format, and the split with Pawsitive
- [ ] Verify the Small Door / Bond Vet merger before using Small Door
- [ ] Refresh or re-attribute the 95% figure
- [ ] Fix the OpenVet published date in the Stories archive
- [ ] Build the four-layer landscape diagram (Block B)
- [ ] Build the Murdoch-vs-Vetology single slide (Block D)
- [ ] Draft the 3–5 question pre-session survey; check whether the VHMA joint survey can carry it
- [ ] Decide on the live demo and whether the room supports it
- [ ] Confirm hotel
