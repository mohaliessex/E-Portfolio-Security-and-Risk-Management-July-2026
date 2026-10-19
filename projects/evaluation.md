---
layout: default
title: "Evaluation: the Unit 11 project against the Unit 6 status report"
kicker: How the final individual project compares with the team's earlier status document.
permalink: /projects/evaluation/
lo: [1, 3]
prev: { title: "Individual project (Unit 11)", url: "/projects/individual-project/" }
next: { title: "Summary of learning outcomes", url: "/development/learning-outcomes/" }
---

The Unit 6 team report was the status document: a qualitative identification of Pampered Pets' risks before digitalisation and of the risks digitalisation would bring. The Unit 11 executive summary was written after the scenario changed. This page compares the two and judges how well the earlier work held up.

## What changed between the two documents

| Dimension | Unit 6 status report (team) | Unit 11 final project (individual) |
|---|---|---|
| Scenario | Small local business considering digitalisation | Business already expanded internationally, with automated warehouses, a 24/7 online shop and royal customers |
| Question | Which information flows should be digitalised, and what risks follow? | How likely are quality and supply events in year one, what should be done first, and how can recovery meet one-minute objectives? |
| Framework | ISO 31000, with STRIDE limited to identities, systems and data flows | ISO 31000 for identification, Monte Carlo simulation for analysis |
| Risk expression | Ordinal likelihood and impact, explicitly provisional | PERT three-point estimates, means with 90% intervals, correlation sensitivity test |
| Scope of risks | Ten risks across current and future state | Fifteen risks, six quality and nine supply or availability |
| Legal treatment | GDPR via ICO guidance; PCI DSS where cards are taken | UK GDPR, EU GDPR, Monaco Law No. 1.565, feed and import law, PCI DSS v4.0.1, framed as go-live gates |
| Continuity | Paper-based degraded mode and tested backups | Two-region active-active design, managed service provider, lock-in controls |
| Recommendation | Phased, reversible digitalisation; international sourcing excluded from phase one | Prioritised controls, with reversibility reinstated as the most effective treatment |

## What carried forward

The Unit 6 report proved more useful than I expected, even though the client did not follow it. Four elements carried directly into Unit 11.

- **The baseline controls.** The phase-zero controls in the team report (MFA, segregated networks, offline backups, controlled records, dual checks and recall exercises) became an explicit assumption of the simulation, so the Unit 11 probabilities measure the risk that remains after them.
- **The claims as stress tests.** The team decided that the 50% growth claim was a capacity stress test rather than a forecast. In Unit 11 that became risk S9, fulfilment overload for four staff, one of the three leading drivers at 22%.
- **The register.** Several Unit 11 risks extend Section 2, which I wrote: product and batch record errors (Q6) come from the traceability risk, and the data breach risk (S3) from the fraud, privacy and payment risk.
- **The epistemic stance.** Unit 6 described ratings as provisional judgements. Unit 11 kept that honesty in quantitative form by reporting intervals, labelling each input's basis and rating the strength of knowledge as low to moderate.

## What the status report missed

The Unit 6 report had weaknesses that only became visible in Unit 11.

- **No way to aggregate.** Ordinal ratings could tell the owner which risks mattered most, but not the probability that *something* would go wrong. That was exactly the question in Unit 11, and answering it required rebuilding the analysis rather than extending it (Cox, 2008).
- **Thin legal analysis.** A single line on GDPR and PCI DSS was adequate for a local shop but not for cross-border processing of royal customers' data. Unit 11 needed jurisdiction-by-jurisdiction analysis.
- **Continuity was assumed, not designed.** "Tested backups and a paper fallback" set no recovery objectives. Unit 11 had to translate one-minute RTO and RPO targets into an architecture, an assurance test and a contract.
- **Interdependence was named but not modelled.** The team report argued that the three claims interact. Unit 11's correlation test showed what interaction does to the numbers: fewer bad years, but worse ones.

## My judgement

The status report was sound for its question, and its central recommendation of small, reversible commitments survived a change of client strategy that it had advised against. That is a fair test of risk advice. Its main limitation was that qualitative work cannot be extended into quantitative work without being rebuilt, so in future I would record ranges and their basis from the outset, even in a qualitative report, so that a later quantitative stage can reuse them.

<div class="pending" markdown="1">
**To add:** the tutor's feedback on the Unit 6 report, and a sentence on whether that feedback shaped the Unit 11 submission.
</div>
