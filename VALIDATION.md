# Validation Plan

IREP applies its own standard to itself: the protocol will be judged on evidence and trajectory, not on declarations. This document specifies how, in four stages of increasing evidential weight. **Stage 0 is a demonstration, not a validation** — the distinction is binding and every publication from this project must preserve it.

## Stage 0 — Synthetic demonstration (status: in progress)

**What it is.** A fully documented simulation: synthetic candidate populations with known ("true") competence, into which category-based evaluator bias, credential filtering and time-pressure noise are deliberately injected. Two pipelines run head-to-head on the same population: a conventional screen (category-visible, credential-filtered, time-pressured) and an IREP screen (category-blind, evidence-based, untimed). Outputs: divergence of selected sets, true-competence comparison of selectees, and composition analysis of who each pipeline filters out.

**What it can show.** The mechanism, made visible and reproducible: that under stated bias assumptions, the two pipelines select measurably different people, and which design element accounts for which difference. It also serves as the dry run of the full statistical pipeline (the exact analysis code that will run on real data in Stages 1–3).

**What it cannot show — ever.** That IREP works. The bias is injected by us; detecting it is circular. Any use of Stage 0 outputs as evidence of real-world validity is a misuse of this project's work.

**Deliverable.** `simulation/` — open code, fixed seeds, documented assumptions, and a results notebook labeled "illustrative under stated assumptions."

## Stage 1 — Retrospective re-scoring (target: first real-data result)

Partner practitioners (recruiters, headhunters, employers) re-screen past, closed hiring pipelines under IREP rules, on a lawful basis (anonymized records, data-processing agreement, GDPR legal basis documented before any transfer). Endpoints: (a) divergence between IREP-selected and actually-selected sets; (b) where post-hire performance data exists, comparison of both selected sets against realized performance. Limitations stated in advance: survivorship (performance data exists only for those actually hired), and site selection effects.

## Stage 2 — Parallel-pipeline pilot

On live, real hiring: candidates consent to dual screening (conventional and IREP, run independently and blind to each other); the hiring decision follows one pipeline per pre-registered assignment; divergence and downstream outcomes are tracked. This is the correspondence-study design brought inside the funnel. Requires: candidate consent flows, evaluator firewalling, and a pre-registered analysis plan (OSF).

## Stage 3 — Randomized controlled trial (with academic partners)

Randomization at the requisition or site level, university lab partnership, ethics committee approval, OSF pre-registration, and longitudinal follow-up of hire performance and retention. This is what moves IREP from GitHub into the literature.

## Cross-cutting rules

1. **No scraped, purchased or non-consented human data. None.** Real candidate data enters only through partners with a documented lawful basis and a data-processing agreement. A project about evaluative dignity does not get to be casual about the dignity of its own data subjects.
2. **Pre-registration before real data.** Analysis plans for Stages 1–3 are pre-registered (OSF) before data access.
3. **"Different" before "better."** The honest near-term claim is that IREP selects *differently*, and in ways traceable to documented design choices. "Better" requires longitudinal performance data and will take the time it takes — the protocol is judged on its trajectory, as it preaches (spec P6).
4. **Negative and null results are published.** Same repository, same prominence.
5. **Stage 4 of the protocol is the instrument.** IREP's own post-decision measurement layer is the data-collection infrastructure for its validation — implementers who adopt the protocol are, by design, equipped to contribute evidence.

## What partners get

Pilot sites: the reference implementation, analysis support, and co-authorship on resulting publications where contribution warrants it. Labs: a pre-built field-experiment infrastructure and an open, citable protocol. Everyone: the results, free, forever.

## Contact

Open an issue tagged `pilot-site`, `research-partner`, or see CALL_FOR_COLLABORATORS.md.
