# Validation Plan

IREP applies its own standard to itself: the protocol will be judged on evidence and trajectory, not on declarations. This document specifies how, in stages of increasing evidential weight. **Stage 0 is a demonstration, not a validation** — the distinction is binding and every publication from this project must preserve it.

## Stage 0 — Synthetic demonstration (status: in progress)

**What it is.** A fully documented simulation: synthetic candidate populations with known ("true") competence, into which category-based evaluator bias, credential filtering and time-pressure noise are deliberately injected. Two pipelines run head-to-head on the same population: a conventional screen (category-visible, credential-filtered, time-pressured) and an IREP screen (category-blind, evidence-based, untimed). Outputs: divergence of selected sets, true-competence comparison of selectees, and composition analysis of who each pipeline filters out.

**What it can show.** The mechanism, made visible and reproducible: that under stated bias assumptions, the two pipelines select measurably different people, and which design element accounts for which difference. It also serves as the dry run of the full statistical pipeline (the exact analysis code that will run on real data in Stages 1–3).

**What it cannot show — ever.** That IREP works. The bias is injected by us; detecting it is circular. Any use of Stage 0 outputs as evidence of real-world validity is a misuse of this project's work.

**Deliverable.** `simulation/` — open code, fixed seeds, documented assumptions, and a results notebook labeled "illustrative under stated assumptions."

## Stage 0.5, the crossing point: the premise on real data (status: pilot complete)

Numbered 0.5 deliberately: it slots between the synthetic demonstration and the field stages without renumbering them, and issues that cite "Stages 0 to 3" keep their meaning.

**What it is.** Stage 0 is honest about its circularity: the biases are injected, so detecting them proves nothing. This stage answers that sentence with public longitudinal data no one at this project generated. On 69 seasons of the Lahman Baseball Database, three estimators predict each subject's next season: the subject's reference class only (age bucket, position, playing-time tier: the resume), the subject's own prior record only, and a shrinkage blend. The measured quantity is **n\***: how many observations of the individual it takes before their own record beats their category out of sample, against the value classical shrinkage theory predicts from the variance components.

**Pilot result, stated with its conditions.** The individual record overtakes the reference class at 1.89 prior seasons for a slow, composite metric (95% cluster-bootstrap CI [1.71, 2.15]) and below one season for a fast-stabilising one; n\* tracks signal-to-noise within the domain. The crossing sits later than the analytic prediction in every era window tested, and it is an upper bound: outcome censoring (subjects who collapse out of the sample are the ones the individual record predicts better) inflates it, and the gap is floor-conditional, shrinking from +0.69 at a 50 PA exposure floor to +0.25 at 300 PA. Full pre-registration, amendments log, limitations and one-command reproduction live in the companion repository: [github.com/labs-barkley/irep-crossing-point](https://github.com/labs-barkley/irep-crossing-point), archived as DOI [10.5281/zenodo.22125148](https://doi.org/10.5281/zenodo.22125148).

**What it can show.** That the protocol's premise (evaluate the individual against their own record, not their category) holds on real, outcome-linked, longitudinal data at a measurable threshold, in the domain where the strongest public baseline (Marcel-class forecasting) and the most hostile statistical readership exist.

**What it cannot show, ever.** Anything about hiring. Baseball supplies hundreds of observations per subject; a hiring file supplies a handful. Nothing here touches IREP's pipeline stages, rubrics, or firewalled measurement. And a single domain cannot establish that n\* transfers: the confirmatory test is a second domain with a different noise structure (Dog Aging Project application in preparation; hypotheses frozen before any data access). This stage validates a premise, not the protocol: it tests the estimator claim, not the causal effect of the protocol on hire quality. For the latter, see Baelde (2026), DOI 10.5281/zenodo.22112322, and `docs/responses/2026-08-baelde-different-to-better.md`.

## Stage 1 — Retrospective re-scoring (target: first real-data result on the protocol itself)

Partner practitioners (recruiters, headhunters, employers) re-screen past, closed hiring pipelines under IREP rules, on a lawful basis (anonymized records, data-processing agreement, GDPR legal basis documented before any transfer). Endpoints: (a) divergence between IREP-selected and actually-selected sets; (b) where post-hire performance data exists, comparison of both selected sets against realized performance. Limitations stated in advance: survivorship (performance data exists only for those actually hired), and site selection effects.

**Ceiling, stated plainly (Baelde 2026, §2.2; issue #14).** Under a deterministic historical decision rule the selection propensity is exactly 0 or 1, so the half of the disagreement region that carries the protocol's claim is empty by construction. Stage 1 deliverables are therefore divergence and composition, never value. One documented fissure: where the historical pipeline logged screener identity and file assignment across screeners was quasi-random, examiner-severity designs identify a local effect on marginal candidates, because the propensity is then strictly between 0 and 1 on part of the region. A condition on the historical data, not a repair of the general case.

## Stage 2 — Parallel-pipeline pilot

On live, real hiring: candidates consent to dual screening (conventional and IREP, run independently and blind to each other); the hiring decision follows one pipeline per pre-registered assignment; divergence and downstream outcomes are tracked. This is the correspondence-study design brought inside the funnel. Requires: candidate consent flows, evaluator firewalling, and a pre-registered analysis plan (OSF).

**Two exploration designs, two estimands (Baelde 2026, §2.3; issue #11).** Randomising the tie-break among near-equal scores identifies a threshold-local effect; advancing a fraction of candidates independently of their score identifies the response of the reclassified population, which is the quantity the protocol makes a claim about. Both are pre-registered separately as what they are, with part of the exploration budget reserved for score-independent advancement. Regression discontinuity at the threshold is the fallback if deliberate exploration is refused, valid only with a continuous logged score, a mechanical pre-committed cutoff, mass near it, and no evaluator manipulation.

**Outcome hierarchy (Baelde 2026, §3.1; issue #12), pre-registered.** Primary: survival at 12 months, split by voluntary and involuntary separation. Then: a pre-registered binary manager judgement at 6 months; objective role-specific output where it genuinely exists; ratings with rater fixed effects as secondary only, given their near-circularity for a debiasing protocol; 30 and 90 day milestones as secondary endpoints never promoted to substitutes.

**Stage shift.** Blinding one stage can move discrimination to the first stage where category data becomes visible again (Åslund & Nordström Skans 2012; Neumark 2024). Group gaps are therefore compared stage by stage, from screening to offer, never at the masked stage alone.

## Stage 2b — Falsification (issue #5)

The 2x2 of issue #5 becomes a named design between Stage 2 and Stage 3. Cells: A, unconstrained evaluation with categorical data visible; B, pre-registered rubric with categorical data visible; C, unconstrained evaluation with categorical data masked (the French experiment); D, the protocol. Design: the same applicant files are assessed by independent evaluator panels, one per cell, on a documented lawful basis and with the candidates' consent; at most one cell's decisions are executed.

*Primary outcome (difference), observable for every candidate.* Per cell, the gap in scores and in selection rates between groups, read through the firewalled audit channel (Stage 4 of the protocol), and between candidates with and without the ambiguous signals of spec §10.2.

*Falsifier.* If masking widens the gap under the rubric (D against B) by the mechanism that widens it under unconstrained evaluation (C against A), the protocol's central claim fails, and that result is published with the same prominence.

*Secondary outcome (quality), observable only where a hire happens.* The outcome hierarchy of Stage 2 (issue #12), measured among the hires of the executed cell and in the score-independent exploration arm of spec §8.4. The outcomes of rejected candidates are never imputed, and no benchmark claims to know them (selective labels, Lakkaraju et al. 2017). This design measures "different"; "better" needs the exploration arm and the sample sizes of the registry (cross-cutting rule 3; issue #4).

*Required conditions.* The applicant-pool score distribution is logged before any decision, otherwise the range-restriction dispute of the structured-interview literature applies to this design (Sackett, Berry, et al. 2023). The "blinding harms" pattern documented in three randomised experiments (a field experiment with firms, Behaghel, Crépon & Le Barbanchon 2015; a trial with public-service recruiters, Hiscox et al. 2017; a laboratory experiment, Werner, Grundmann & Rockenbach 2026) is stated in advance as expected in C, and D is claimed to avoid it. The stage-shift test of Stage 2 applies to every cell.

## Stage 3 — Randomized controlled trial (with academic partners)

Randomization at the requisition or site level, university lab partnership, ethics committee approval, OSF pre-registration, and longitudinal follow-up of hire performance and retention. This is what moves IREP from GitHub into the literature. Pre-registered to claim divergence, composition and process metrics: the power analysis in Baelde (2026, Appendix A) shows retention-based evidence needs on the order of a thousand hires per arm before clustering, out of reach at firm level; retention claims are deferred to the registry (issue #15).

## Cross-cutting rules

1. **No scraped, purchased or non-consented human data. None.** Real candidate data enters only through partners with a documented lawful basis and a data-processing agreement. A project about evaluative dignity does not get to be casual about the dignity of its own data subjects. Stage 0.5 is the one exception in kind and it is not an exception to consent: the Lahman Baseball Database is the published, licensed (CC BY-SA) statistical record of a public profession, aggregate performance figures only, with no private attributes and no scraping.
2. **Pre-registration before real data.** Analysis plans for Stages 1–3 are pre-registered (OSF) before data access.
3. **"Different" before "better."** The honest near-term claim is that IREP selects *differently*, and in ways traceable to documented design choices. "Better" requires longitudinal performance data and will take the time it takes — the protocol is judged on its trajectory, as it preaches (spec P6).
4. **Negative and null results are published.** Same repository, same prominence.
5. **Stage 4 of the protocol is the instrument.** IREP's own post-decision measurement layer is the data-collection infrastructure for its validation — implementers who adopt the protocol are, by design, equipped to contribute evidence. The audit set includes differential prediction (Cleary 1968) alongside selection rates: whether the rubric score predicts the outcome with the same intercept and slope across groups. The test runs on the composite score of spec §8.2, not predictor by predictor (Dahlke & Sackett 2022). The direction of any miscalibration is stated in advance as a hypothesis, informed by the documented over-prediction pattern of cognitive tests (Berry & Zhao 2015). Age and disability are covered alongside ethnicity and gender (Lippens, Vermeiren & Baert 2023). Equal selection rates with unequal calibration is the invisible failure mode, and the firewalled channel collects exactly the data this test needs at the time it needs it; the stated caveat is that estimating on hires alone conditions on a collider, and range-restriction corrections there are at best partial (Baelde 2026, §3.2; issue #13).

## What partners get

Pilot sites: the reference implementation, analysis support, and co-authorship on resulting publications where contribution warrants it. Labs: a pre-built field-experiment infrastructure and an open, citable protocol. Everyone: the results, free, forever.

## Contact

Open an issue tagged `pilot-site`, `research-partner`, or see CALL_FOR_COLLABORATORS.md.

## Reference

Baelde, M. (2026). From "Different" to "Better": What It Would Take to Show That a Hiring Protocol Works. Zenodo working paper. DOI [10.5281/zenodo.22112322](https://doi.org/10.5281/zenodo.22112322). Response: `docs/responses/2026-08-baelde-different-to-better.md`.
