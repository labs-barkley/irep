# Changelog

All notable changes to the IREP specification and repository.

## [0.2.0] - unreleased (comment window)
### Added
- spec/IREP-v0.2.md: the v0.1 text plus three sections. §8 Selection (issues #10, #6, #3): two layers, a pre-registered aggregation rule, a pre-registered threshold, allocation on evidence, an exploration band set by a pre-registered error estimator with a logged seeded draw, disclosure. §9 The evaluation view (issue #7, with the defaults of issue #2): authorised attributes and their representation, residual re-identification risk, rare trajectories, a worked example. §10 Items (issue #8): anchoring, ambiguous signals and the not-assessable state, the two-lever comparison arm and the rule on validity claims, a worked item.
- VALIDATION.md Stage 2b: Falsification, the 2x2 of issue #5 as a written design. Difference is the primary outcome, observable for every candidate; quality is read only among hires and in the score-independent exploration arm. The design is written; it has not been run.
- ROADMAP.md: the registry (issues #4, #9, #15): entry schema, trust tiers and what each permits an organisation to say, three blocking preconditions, the regulatory clock. A roadmap: nothing about the registry ships in this release.
- GLOSSARY.md: Aggregation rule, Not assessable, Exploration band, Evaluation view.
- evidence/bibliography.md: entries for the sources cited by the new texts, two 2026 studies of LLM screening, and the evaluations of NYC Local Law 144; a new section, "External review", lists Baelde (2026) as a critique, not an endorsement, outside the sourcing policy.
### Changed
- VALIDATION.md Stage 2: the stage-shift test (issue #12). Cross-cutting rule 5: the differential-prediction test runs on the composite of spec §8.2, states its direction hypothesis in advance, and covers age and disability (issue #13).
- Spec numbering in v0.2: "Open questions for the collective" is §11 (§8 in v0.1) and "Conclusion" is §12 (§9 in v0.1). spec/IREP-v0.1.md keeps its own numbering and is not modified.
- README.md and LICENSE.md point to §11 of the v0.2 spec for the open questions and the licence choice. README.md and llms.txt link spec/IREP-v0.2.md, with v0.1 cited as the deposited version. README status: v0.2 is a draft for public comment, with no DOI before its release.
- llms.txt (root and docs/), AGENTS.md and evidence/bibliography.md read "IREP's stated scope" where they read "IREP v0.1's stated scope". The scope itself is unchanged: hiring and admissions.
- IREP-STARTER.md, USING-IREP-WITH-AI.md and CONTRIBUTING.md point to the v0.2 spec; GLOSSARY.md "Allocation layer" points to spec §8. README: status badge in v0.2, Roadmap section aligned with ROADMAP.md.
- AGENTS.md and the Claude skill aligned with spec §8 to §10: an assistant drafts item levels against the rubric and never ranks candidates; comparison belongs to the allocation layer.
### External review
- Baelde (2026): version DOI 10.5281/zenodo.22112323, concept DOI 10.5281/zenodo.22112322 (all versions). Cited as a critique, not an endorsement. Tracked in issues #10 to #15. Response: docs/responses/2026-08-baelde-different-to-better.md. VALIDATION.md stages 1-4 revised; implementation guide gains the operational logging triad; glossary gains the evaluation/allocation layer distinction.
- Issue #1 of the companion repository labs-barkley/irep-crossing-point (Baelde, era non-stationarity) is cited as a critique. It belongs to that repository and is not addressed in this release.

## [0.1.3] - 2026-08-26
### Added
- VALIDATION.md Stage 0.5: the crossing point. The protocol's premise tested on real public longitudinal data (69 seasons, Lahman Baseball Database); pilot result stated with its conditions (upper bound, floor-conditional, single domain); companion repository referenced (publication pending). Numbered 0.5 so Stages 0-3 keep their meaning in existing issue references.
- Cross-cutting rule 1 amended alongside Stage 0.5, and stated here so the change is dated rather than discovered by git blame: the no-non-consented-human-data rule gains one sentence saying why the Lahman source is not an exception to it (published, licensed CC BY-SA, aggregate performance statistics of a public profession, no private attributes, no scraping). The rule itself is unchanged for candidate data.
- VALIDATION.md intro reads "in stages" rather than "in four stages" (Stage 0.5 exists), and Stage 1's target is retitled "first real-data result on the protocol itself" to keep the premise/protocol distinction exact.
- README (Status): the registry framing from issue #4 surfaced; the registry is the measurement infrastructure and what makes conformance third-party verifiable, the badge is proof of enrollment.
### Changed
- README: the Stage 0 circularity sentence now points at Stage 0.5 as its first real-data answer.
- llms.txt (root and docs) and AGENTS.md: the premise-vs-protocol distinction stated where validity claims are scoped.
- spec/IREP-v0.1.md: References section title no longer says citations are to be completed (the deposit is done, DOIs minted); the self-citation uses the canonical name form.
- README (Acknowledgments): non-endorsement stated once in the section chapeau; Ph.D. punctuated.

## [0.1.2] - 2026-08-24
### Changed
- EU AI Act wording aligned with the Digital Omnibus (in force 27 July 2026): the Annex III classification is unchanged, the obligations now apply from 2 December 2027 (2 August 2030 for public authorities), and IREP's rule is stated as independent of that timeline. Applied in README.md, AGENTS.md, USING-IREP-WITH-AI.md, GLOSSARY.md, principles/05_human_decides.md, ai/skills/claude/irep-evaluation/SKILL.md, evidence/bibliography.md, llms.txt, the site, and as an editorial note in the repository copy of spec/IREP-v0.1.md (the deposited v0.1 is unmodified).
- Canonical one-line definition unified across llms.txt, .zenodo.json, CITATION.cff and the site (three variants had drifted apart).
- llms.txt: principles P1-P7 corrected to P1-P10.
- docs/ re-synced with the deployed site; the mirror had been a generation behind since July.
- README: duplicate "For recruiters and talent teams" section removed.
### Added
- Coverage and citations (README) and External commentary (llms.txt): third-party writing that references IREP, listed as commentary and never as validation evidence.
- Practitioner commentary section in evidence/bibliography.md, explicitly outside the sourcing policy.
- Acknowledgments (README): scoped credit for the trajectory-field re-identification objection (k-anonymity), tracked as issue #2.
- AGENTS.md: agents must not present third-party commentary as validation, and must flag extensions beyond IREP v0.1's scope of hiring and admissions.

## [0.1.1] - 2026-07-06
### Changed
- Stage 4 reworded: firewalled audit channel (lawful, voluntary, at or after application; analytically unavailable until decisions are finalized) - enables lawful stage-by-stage audits including non-selected candidates; Art. 9 GDPR note added.
- P1 stated in full: individual = unit of interpretation; role = standard of decision; population = instrument of audit.
- "Masking alone backfires" softened to "can backfire"; Behaghel interpretation flagged as interpretation; fairness-literature position restated as IREP''s own separation rule.
- "non-commercial" replaced by "non-proprietary, not-for-sale" everywhere (commercial implementation is expressly permitted).
- Licenses clarified: docs CC BY 4.0; demonstration code Apache-2.0 (interim).
### Added
- P8 (accommodation without disclosure), P9 (declared tool conditions), P10 (independent scoring).
- DATA-GOVERNANCE.md, IMPLEMENTATION-GUIDE.md, CODE_OF_CONDUCT.md, SECURITY.md, DCO.md, NOTICE, issue templates.
- simulation/ablation_study.py (single-factor scenarios).

## [0.1.0] - 2026-07-05
Initial public release.
