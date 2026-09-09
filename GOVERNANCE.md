# Governance

## Purpose

IREP exists to keep one thing out of the market: the standard by which human beings are evaluated for access to work and education. Access to employment is treated here as a matter of basic equity — like access to education, literacy and culture — and the protocol is therefore free of charge, permanently, for everyone including commercial implementers.

## Current stewardship (bootstrap phase)

- **Steward:** Barkley Labs (initiator), acting as temporary custodian of the specification.
- **Decision rule during bootstrap:** proposals via issues/PRs; the steward merges, documenting rationale publicly. No private channels for protocol decisions.

## Target structure

A non-profit vehicle (association loi 1901 or foundation; jurisdiction and form to be decided with the founding collective) holding:

1. the specification and the project name and identity,
2. the reference implementation,
3. the conformity/audit tooling.

Funding: grants, foundations, public digital-commons programs (e.g., European NGI-type funds), and donations. No paid tiers, no dual licensing of the spec, no sale.

## Principles that bind any future governance

- The specification remains free and openly licensed. Enclosure of the standard is out of scope, forever.
- Commercial implementation is welcome; capture is not.
- Protocol changes require public rationale and must cite evidence (see `evidence/bibliography.md` contribution rules).
- The project practices what it specifies: contributions are evaluated on their content, with maintainer decisions documented.

## Stewardship, succession and handoff

IREP is currently maintained by a single steward. That is a weakness, stated here rather than hidden, and the governance below exists to make the project survive it.

**The steward is temporary by design.** The role is custodial, not proprietary: the steward merges, documents rationale in public, and holds no rights over the specification beyond those any contributor holds. Stewardship transfers to the founding collective as soon as one exists, and the current steward's stated objective is to make that transfer happen, not to delay it.

**Handoff triggers.** Stewardship passes to the maintainers of record, by their own decision, in any of these cases: the steward resigns; the steward is unreachable for ninety consecutive days on public channels; a founding collective is constituted and accepts the transfer; or the maintainers of record decide, by simple majority, that the steward is no longer able to act. No trigger requires the steward's consent to take effect.

**Maintainers of record.** Listed in `MAINTAINERS.md`, with their scope. Maintainers are promoted from contributors on the basis of merged work, never appointed by announcement. There is no chief and no board during the bootstrap phase.

## Dormancy

A project with one steward can go quiet. This section defines what quiet means and what it does not mean.

The project is **dormant** when no maintainer has merged, reviewed or responded on public channels for ninety consecutive days. Dormancy is a state, not an end: the specification remains published, licensed and citable, and the DOIs continue to resolve.

During dormancy, anyone may open an issue titled "Dormancy" to establish the fact. If no maintainer of record responds within thirty days of that issue, any contributor with prior merged work may declare themselves acting maintainer by opening a pull request adding themselves to `MAINTAINERS.md`, with a public rationale. That pull request stands as accepted if no maintainer of record objects within a further thirty days.

Dormancy never converts into private ownership. A dormant IREP is a published standard without an active maintainer, which is a normal state for a specification and not a licence for anyone to enclose it.

## Fork

Forking is expected, permitted and, in some circumstances, encouraged.

The specification is openly licensed and may be forked at any time, by anyone, for any reason, including disagreement with the steward. A fork is not a hostile act; it is the mechanism by which a standard that has stopped serving its purpose gets corrected.

Two conditions apply, and they concern honesty rather than permission. A fork must not present itself as IREP: it takes its own name and states, once and visibly, that it derives from IREP and at which version. And a fork must carry forward the licence it received, so that what was open stays open downstream.

If a fork becomes the more active project, the steward of record undertakes to say so in this repository and to point here toward it. A standard that is kept alive elsewhere has still done its job.

## Open governance questions (for the founding collective)

- Legal form and jurisdiction.
- Licensing: CC BY 4.0 vs CC BY-SA 4.0 for the spec; AGPLv3 vs Apache 2.0 for code.
- Trademark policy for "IREP-compliant" claims and a lightweight self-assessment/conformity checklist.
- Composition of a scientific committee for Stage 2 instrument validation (psychometrics, I/O psychology, ML fairness, employment law).

## Contact

commons@irepprotocol.org — the shared mailbox of the collective. There is no chief and no owner behind this address; mail is read by the steward(s) of record, and protocol decisions still happen only in public issues.
