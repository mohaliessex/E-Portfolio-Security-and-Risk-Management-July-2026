---
layout: default
title: "Unit 8: Implementing quantitative risk models"
kicker: Unit 8 of 12
permalink: /units/unit-08/
lo: [2, 3]
prev: { title: "Unit 7: Quantitative modelling", url: "/units/unit-07/" }
next: { title: "Unit 9: BC and DR", url: "/units/unit-09/" }
---

The unit applied Monte Carlo simulation and Bayes' theorem to real problems, including project management and safety estimation (Eckstein and Riedmueller, 2002), and asked for a critical appraisal of quantitative techniques. The seminar covered building and appraising a quantitative risk model.

### What the unit set out to teach

On completing the unit I should be able to:

- Select the most appropriate modelling technique to use in a given situation.
- Create a QR model of a real-world situation.
- Provide a critical appraisal of the use of QR techniques.

## Artefact: peer responses in Discussion 2

- **To Asma Umar:** I agreed that differences in metrics such as Attack Vector, User Interaction and Scope show how standard criteria are interpreted differently, but argued that CVSS should be retained for communication and interoperability, with SSVC providing the contextual decision layer.
- **To Kaona Hoxha:** I agreed that the core weakness is reproducibility rather than the scoring concept, and that asset criticality, exposure and compensating controls belong in prioritisation, and questioned whether SSVC should fully replace CVSS given its value as a common technical language.

[Read both responses in full in Discussion 2]({{ '/discussions/discussion-2/' | relative_url }}#2-my-peer-responses-unit-8)

## Seminar: Quantitative risk modelling

*18 September 2026.* The seminar contrasted a deterministic calculation (a 10% chance of a £100,000 ransomware loss gives a £10,000 risk) with models that carry uncertainty ranges, interdependencies and output distributions. It compared deterministic formulas, Monte Carlo simulation, Bayesian networks, event tree analysis and regression, and worked through a FAIR-based Monte Carlo model of ransomware against a hospital's electronic health records (Mazumdar, 2026e).

**How I used it.** The contrast between one number and a distribution is why my executive summary uses Monte Carlo simulation with PERT ranges and reports 90% intervals rather than a single annualised loss expectancy.

## Learning note

Writing these responses moved me away from my own initial position. In both, I found myself defending CVSS for communication while arguing for SSVC for decisions, which is closer to a "both, for different jobs" view than the replacement I had proposed.
