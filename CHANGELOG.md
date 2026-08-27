# Changelog

All notable changes to the IREP specification and repository.

## Unreleased (v0.2-dev)
### External review
- Baelde (2026), DOI 10.5281/zenodo.22112323, tracked in issues #10 to #15. Response: docs/responses/2026-08-baelde-different-to-better.md. VALIDATION.md stages 1-4 revised; implementation guide gains the operational logging triad; glossary gains the evaluation/allocation layer distinction.
### What v0.2 waits on
- The threshold decision text finalised in the spec (issue #10 closed or stabilised).
- The exploration-design and outcome-hierarchy revisions settled (issues #11, #12).
- A comment window for the external reviewer before the release is cut.
- v0.1 on Zenodo is immutable and stays as is; the v0.2 DOI mints at release time through the existing integration.

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
