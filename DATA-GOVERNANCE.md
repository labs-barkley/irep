# Data Governance

The protocol's credibility rests on this document as much as on the spec. It defines how data flows through an IREP implementation and what implementers must guarantee. It is normative: an implementation that violates it is not IREP.

## The two channels

**Evaluation channel.** Carries competencies, work products, verified accomplishments and trajectory shape. Never carries: name, photograph, age or birth date, sex or gender, nationality or citizenship status, address or geographic origin, credential labels used as filters, marital status, disability or health information. Evaluators have access to this channel only.

**Audit channel.** Carries category and demographic data, collected where lawful and voluntary, at or after application. Three guarantees are binding: (1) *technical inaccessibility* — evaluators cannot reach this channel (separate systems or access controls, not policy promises); (2) *analytical unavailability* — no joins between channels until the selection decision is finalized; (3) *purpose limitation* — contracting, legally mandated declarations, and stage-by-stage equity audits only. Audit findings correct the process; they never re-evaluate individuals.

## Special-category data (Art. 9 GDPR)

Data revealing racial or ethnic origin, health, disability, sexual orientation and other Art. 9 categories are prohibited from processing by default. An implementer collecting them for equity audits must document: the legal basis and applicable exception, the explicit purpose, voluntariness (refusal must be free of any consequence for the candidate), retention limits, and access governance. Where a lawful basis cannot be established, the audit runs on the categories that remain lawful — a smaller audit is acceptable; an unlawful one is not.

## Accommodations (P8)

Accommodation requests flow through a third, operational channel. Evaluators receive only the operational outcome ("this assessment is administered with extended window X" / "in format Y"), never the reason, diagnosis or disability information. Accommodation data is never joined to evaluation or audit data at individual level.

## Candidate rights

Candidates can access the rationale of decisions concerning them (Stage 3 documentation), request correction of factual errors in their evaluation file, withdraw audit-channel consent at any time without consequence, and are informed at collection of every purpose. Data minimization applies throughout: if a field is not required by the current stage, it is not collected at that stage.

## Retention

Evaluation-channel data: retained per applicable employment law, then deleted. Audit-channel data: aggregated for audit statistics, individual-level records deleted on a documented schedule. Accommodation data: deleted after the assessment concludes, keeping only the operational fact that an accommodation was provided.

## For research partners

Validation studies (VALIDATION.md Stages 1–3) additionally require: a data-processing agreement, documented lawful basis before any transfer, OSF pre-registration before data access, and anonymization or pseudonymization at source. No scraped, purchased, or non-consented human data enters this project — under any circumstances.
