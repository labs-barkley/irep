# The Individual-Referential Evaluation Protocol (IREP)
## An Open Standard for Category-Blind, Trajectory-Rich Assessment in Hiring and Admissions

**Working Paper — v0.1 (Draft for public comment)**
**Barkley Labs**
**Author:** Elodie Aishwarya P. Remoissenet (ORCID 0009-0004-6031-659X)
**Paper DOI:** [assigned on Zenodo deposit] — **Repository DOI:** 10.5281/zenodo.21211409 (this release) — 10.5281/zenodo.21211408 (all versions)
**License:** Specification text under CC BY 4.0 [or CC BY-SA 4.0 — see §8]. Reference implementation under AGPLv3 [or Apache 2.0 — see §8].
**Disclosure:** AI tools were used for drafting assistance under the author's full editorial control. The author is solely accountable for the content, sourcing and originality of this work.

---

## Abstract

Hiring and admissions systems routinely collect category data (name, photograph, age, sex, geography, credentials) at the stage where it does the most documented damage: before evaluation. Social-psychological research shows that category salience activates stereotype threat in candidates and population priors in evaluators; audit studies show that identical files receive divergent outcomes when only the category signal changes; and the large-scale French anonymous-CV experiment shows that the intuitive remedy, masking, can worsen outcomes by removing evaluators' ability to read atypical trajectories in context. This paper specifies an open protocol that resolves the tension by relocating rather than deleting category data: evaluation is category-blind but trajectory-rich; assessment is untimed within a bounded window; demographic and credential data are collected only after the evaluation decision, firewalled from evaluators, and used exclusively for audit, compliance and administration. The protocol treats the individual, not the population, as the reference class, and the individual's trajectory, not a credential snapshot, as the primary evidence of capability. It is published as a free and open standard, with an open implementation guide and reference materials, so that any organization (employer, school, HR vendor, public service) can adopt or build upon it. Access to employment is treated here as a matter of basic equity, not as a market to be enclosed.

---

## 1. Motivation

An employment decision engages one or several lives. Access to work belongs with access to education, literacy and culture among the gateways a society cannot equitably price, yet it is among the least served by commons-type initiatives: education has open access, open courseware and public libraries; hiring infrastructure is almost entirely proprietary, opaque, and optimized for throughput rather than validity.

The scientific problem underneath is a reference-class error. Evaluating an individual by the real or presumed properties of their category (their name's connotations, their age bracket, their alma mater's average) substitutes a population statistic for an individual baseline. This error has been documented across machine learning fairness, behavioral science and organizational psychology, and this paper's author has developed the individual-referential argument in adjacent domains (Remoissenet, 2025–2026). Hiring is the error's most consequential everyday habitat.

The evidence base is decades old. Its non-adoption by the sector is a coordination and incentive failure, not a knowledge gap. An open protocol addresses exactly that failure.

## 2. Evidence base

**2.1 Category salience acts on candidates.** Steele and Aronson (1995) showed that framing a difficult test as diagnostic of intellectual ability depressed the performance of negatively stereotyped groups, and that merely recording one's race on a pre-test form was sufficient to produce the effect. Subsequent replication literature has qualified the effect's magnitude, and this protocol does not treat stereotype threat as explaining group achievement gaps; it relies only on the established directional mechanism: category activation at evaluation time is not neutral.

**2.2 Category signals act on evaluators.** Correspondence audit studies (Bertrand and Mullainathan, 2004, and a large replication literature across countries) show that identical résumés receive materially different callback rates when only the name changes. The evaluator's prior is fed before any evidence of competence is read.

**2.3 Masking alone can backfire.** The French national anonymous-CV experiment (Behaghel, Crépon and Le Barbanchon) found that anonymization worsened outcomes for candidates of immigrant background, plausibly because it removed recruiters' contextual, compensatory reading of atypical trajectories. The French result shows that removing labels alone is not a sufficient remedy; IREP proposes retiming - relocating category data out of evaluation and into a firewalled audit channel - as a testable alternative.

**2.4 Unawareness fails technically.** The algorithmic fairness literature established that removing protected attributes does not remove their influence: category leaks through proxies (name, postal code, institution) (Dwork et al., 2012; Kusner et al., 2017; Barocas et al., 2023). Parts of the fairness literature also use protected attributes to train or calibrate models; IREP adopts a stricter separation for human-run selection: category data may support lawful, firewalled auditing, but never evaluation-stage decisions.

**2.5 Speededness measures stress, not competence.** Psychometric work on test speededness indicates that strict time pressure introduces construct-irrelevant variance: it measures performance under stress rather than the target competency, and penalizes candidates (including highly capable ones) whose performance degrades under artificial time constraints. Untimed or generously bounded assessment improves construct validity where speed is not itself the competency (Messick, 1995; Lu & Sireci, 2007).

**2.6 Introspection is not evidence; audits are.** Two convergent literatures ground the protocol's preference for architectural over attitudinal debiasing. Cognitive and social neuroscience shows that social category encoding is fast and partially automatic, occurring before deliberate judgment (Ito and Urland, 2003; Amodio, 2014): a category does not need to be endorsed to be processed. And the introspection literature (Nisbett and Wilson, 1977; Pronin et al., 2002) shows that people cannot reliably access the causes of their own judgments and systematically locate bias in others rather than themselves. Together these establish that an evaluator's declared impartiality has no evidential value, and that debiasing must operate on the information architecture (what reaches the evaluator, and when) and on decision audits (Stage 4), not on declarations, awareness or training alone. The same rigor cuts the other way: the protocol explicitly repudiates neuromyth-based instruments (left/right-brain typologies, learning styles (Pashler et al., 2008), triune-brain framings) and takes no position on contested individual-level measures such as the IAT (Oswald et al., 2013); IREP audits decisions, never evaluators' inner states. The transversal claim, stated plainly: the way we believe we evaluate and the way evaluation actually proceeds are different processes, and selection systems must be designed for the second.

## 3. The protocol

IREP specifies four sequential stages and ten binding principles.

**Stage 1 — Category-blind, trajectory-rich screening.** The evaluation file contains competencies, work products, verified accomplishments and the full narrative shape of the candidate's trajectory. It excludes: name, photograph, age or birth date, sex or gender, nationality or citizenship status, address and geographic origin, and credential labels used as filters (institution names may be replaced by descriptors of what was done there). Geographic or modality constraints (on-site, hybrid, remote) are resolved by candidate self-attestation against the posted requirement (a binary "I accept the stated conditions"), not by disclosure of location.

**Stage 2 — Untimed structured assessment.** Candidates passing screening complete an assessment within a bounded window (for example, 24 hours from start) but with no per-item time pressure. Exercises are field-appropriate and, where the construct allows, deliberately open: designed to reveal reasoning, judgment and cognitive approach rather than convergence on a single keyed answer. Where "no right answer" formats are used, scoring rubrics must be pre-registered, behaviorally anchored and validated (see §6); unvalidated "cognitive profiling" is prohibited, as it manufactures new categories, which is the very error this protocol exists to eliminate.

**Stage 3 — Decision on evidence.** Selection decisions are made on Stage 1–2 evidence only, by evaluators who have had no access to category data, with documented rationale per decision.

**Stage 4 — Firewalled measurement.** Category and demographic data may be collected, where lawful and voluntary, through a separate, firewalled audit channel at or after application; they are technically inaccessible to evaluators and analytically unavailable until the decision is finalized, which is what makes stage-by-stage audits of the full pipeline (including non-selected candidates) statistically possible; lawfulness depends on the applicable legal basis, safeguards and governance. Special-category data within the meaning of Art. 9 GDPR requires an appropriate legal basis, an explicit purpose and dedicated governance (see DATA-GOVERNANCE.md). Administrative and legal data are collected at contracting through the same firewall. These data serve three purposes exclusively: contracting and compliance; legally mandated declarations; and equity auditing, that is, statistical testing of whether the pipeline systematically disadvantages any group at any stage. Audit findings feed process correction, never individual re-evaluation.

**Binding principles.**
P1. The individual is the reference class; the population is the audit instrument.
P2. Blindness applies to category labels, never to trajectory richness.
P3. Time pressure is excluded unless speed is the competency being hired.
P4. Every scoring instrument must be validated and pre-registered; no emergent categorization of candidates.
P5. Evaluation and measurement are separated organizationally, technically and temporally.
P6. Trajectory outweighs snapshot: evidence of slope (progression, learning velocity, evolution between works) is weighted above evidence of state (a credential obtained at one point in time). The evaluative question is not only "compared to what?" but "compared to when?".
P7. Full auditability by design: decisions, rubrics and pipeline statistics are logged in a form sufficient for internal review and for regulatory conformity assessment.
P8. Accommodation without disclosure: candidates may request reasonable accommodations through a separate operational channel; evaluators receive only the accommodation outcome necessary to conduct the assessment, never diagnostic or disability information.
P9. Declared tool conditions: every assessment states which tools, including AI systems, are permitted; where AI use is allowed, assessment evaluates judgment, verification and process — not undisclosed authorship.
P10. Independent scoring: at least two evaluators score independently, blind to each other's scores, under a pre-registered disagreement rule; arbitrations are logged and inter-rater agreement is reported. At high volume, double scoring is mandatory for final selection; earlier stages may use calibrated audit samples plus all borderline or disputed cases.

**P1, stated in full.** The individual is the unit of interpretation; the role's explicit, evidence-relevant requirements are the standard of decision; the population is the instrument of audit. IREP does not evaluate candidates "against themselves" in place of a standard — it evaluates role-relevant evidence read through the individual's trajectory, and refuses to let category averages or prestige proxies substitute for that evidence.

## 4. Scope and extensions

The protocol is written for employment selection and is directly transposable to university and program admissions, where credential snapshots and category signals play an analogous filtering role. It is deliberately implementation-agnostic: it can run on paper, on existing ATS platforms reconfigured to comply, or on the reference implementation.

## 5. Regulatory positioning

Where an implementation constitutes an AI system intended for recruitment or selection within Annex III of the EU AI Act, it is high-risk. IREP can also be run entirely without AI. Its requirements on validated instruments (P4), separation of functions (P5) and auditability (P7) can support conformity-by-design, but do not themselves establish conformity: implementers remain responsible for determining applicability, completing the relevant risk-management, documentation, human-oversight and monitoring obligations, and demonstrating compliance. The same architecture serves GDPR data-minimization: category data is not collected until it has a lawful, specified purpose.

## 6. Limitations and known risks

Three risks are named openly. First, psychometric risk: open-ended assessment without rigorous validation can smuggle categories back in through scorer subjectivity; the validation requirement (P4) is therefore binding, not advisory. Second, gaming risk: any published standard can be optimized against; longitudinal, artifact-based evidence is harder to fabricate than credentials, but not immune, and implementations should include verification steps. Third, displacement risk: removing the credential filter shifts weight onto work products and assessments, which can advantage candidates with more free time; the bounded-window design and reasonable-load requirements on assessment length mitigate but do not eliminate this, and it must be monitored in the Stage 4 audit.

The protocol also does not claim that individual evaluation dissolves structural inequality. It claims something narrower and testable: that no candidate should be answered for by the average of a category, at the moment of evaluation, in either direction.

## 7. Governance and the commons model

IREP is published as a commons, in explicit resistance to the financialization of access to employment. The intended structure is a non-profit vehicle (association or foundation, jurisdiction to be determined) acting as steward of the specification, with development conducted in the open by a volunteer and institutionally supported collective. Sustainability is expected from grants, foundations and public digital-commons funding, with donations as a complement; the protocol and tooling are free of charge, permanently. Commercial actors, including HR software vendors, are welcome and encouraged to implement the standard in their own products; enclosure of the standard itself is not.

## 8. Open questions for the collective (v0.1 → v1.0)

Licensing: CC BY 4.0 maximizes adoption of the specification; CC BY-SA adds share-alike protection. For the reference implementation, AGPLv3 protects against proprietary capture; Apache 2.0 maximizes vendor adoption. The choice encodes the project's theory of change and is put to the founding collective. Also open: the validation methodology and instrument library for Stage 2; the minimal audit statistics set for Stage 4; the admissions-specific profile; and the conformity-assessment cookbook for the EU AI Act.

## 9. Conclusion

The research has been available for decades. What has been missing is not evidence but an implementable, free, auditable standard that any organization can adopt without a vendor, a license fee, or an act of faith. This paper is that standard's first draft, offered to a collective that does not yet exist, in the conviction that the right to be evaluated as oneself, and not as one's category, should never have been for sale.

---

## References (to be completed with full citations before deposit)

- Steele, C. M., & Aronson, J. (1995). Stereotype threat and the intellectual test performance of African Americans. *Journal of Personality and Social Psychology*, 69(5), 797–811.
- Bertrand, M., & Mullainathan, S. (2004). Are Emily and Greg more employable than Lakisha and Jamal? A field experiment on labor market discrimination. *American Economic Review*, 94(4), 991–1013.
- Behaghel, L., Crépon, B., & Le Barbanchon, T. (2015). Unintended effects of anonymous résumés. *American Economic Journal: Applied Economics*, 7(3), 1–27.
- Dwork, C., Hardt, M., Pitassi, T., Reingold, O., & Zemel, R. (2012). Fairness through awareness. *Proceedings of ITCS 2012*, 214–226.
- Kusner, M. J., Loftus, J., Russell, C., & Silva, R. (2017). Counterfactual fairness. *Advances in Neural Information Processing Systems 30*.
- Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning: Limitations and Opportunities.* MIT Press.
- Lu, Y., & Sireci, S. G. (2007). Validity issues in test speededness. *Educational Measurement: Issues and Practice*, 26(4), 29–37.
- Messick, S. (1995). Validity of psychological assessment. *American Psychologist*, 50(9), 741–749.
- Nisbett, R. E., & Wilson, T. D. (1977). Telling more than we can know. *Psychological Review*, 84(3), 231–259.
- Pronin, E., Lin, D. Y., & Ross, L. (2002). The bias blind spot. *Personality and Social Psychology Bulletin*, 28(3), 369–381.
- Ito, T. A., & Urland, G. R. (2003). Race and gender on the brain. *Journal of Personality and Social Psychology*, 85(4), 616–626.
- Amodio, D. M. (2014). The neuroscience of prejudice and stereotyping. *Nature Reviews Neuroscience*, 15(10), 670–682.
- Oswald, F. L., Mitchell, G., Blanton, H., Jaccard, J., & Tetlock, P. E. (2013). Predicting ethnic and racial discrimination: A meta-analysis of IAT criterion studies. *Journal of Personality and Social Psychology*, 105(2), 171–192.
- Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest*, 9(3), 105–119.
- The broader annotated evidence base (cognitive mechanisms, foundations, audit-study replications) is maintained at evidence/bibliography.md.
- Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex III (high-risk systems: employment).
- Remoissenet, E. A. P. (2025–2026). Prior works on reference-class error and individual longitudinal baselines. Zenodo, DOI 10.5281/zenodo.20060327; *The Normative Trap*, DOI 10.5281/zenodo.20516821.
