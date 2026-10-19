---
layout: default
title: "Unit 11: Future trends in security and risk management"
kicker: Unit 11 of 12
permalink: /units/unit-11/
lo: [1, 2, 3, 4]
prev: { title: "Unit 10: DR implementation", url: "/units/unit-10/" }
next: { title: "Unit 12: The great debate", url: "/units/unit-12/" }
---

The unit reviewed emerging trends in the field, including machine learning for autonomous cyber defence (Ridley, McCloskey and Mountain, 2018), behavioural operations (Fahimnia *et al.*, 2019), reputational risk and options theory, and frameworks for selecting a risk management approach (Marks, 2019). The individual project was submitted this unit.

### What the unit set out to teach

On completing the unit I should be able to:

- Describe the main emerging trends in the field.
- Explain their potential impact on research.
- Recommend which you think will be most influential.

## Artefact: individual executive summary

A Monte Carlo assessment of fifteen risks estimated, without further controls, a 55% probability of at least one quality-threatening event and a 79% probability of at least one material supply disruption in the first year, reduced to about 26% and 52% by the prioritised controls. The summary also mapped data protection obligations across three jurisdictions and designed a disaster recovery solution for one-minute objectives.

[Read the full executive summary]({{ '/projects/individual-project/' | relative_url }})

<figure><img src="{{ '/assets/img/exec-summary-fig1-probabilities.png' | relative_url }}" alt="Bar chart of simulated annual probabilities for fifteen risks with 90% intervals."><figcaption>Simulated annual probabilities with 90% intervals, from the individual project.</figcaption></figure>

## Artefact: Module Wiki entry on future trends

<div class="artefact" markdown="1">
<p class="artefact-meta">Module Wiki entry, Unit 11: future trends in security and risk management</p>

Machine learning (ML) is the thread running through most of the Unit 11 readings. Varshney and Alemzadeh (2017) define safety in ML as minimising both the risk and the uncertainty of harms. This closely mirrors definitions of security risk that combine consequences with uncertainty (Amundrud, Aven and Flage, 2017). The parallel matters: ML systems can be assessed with the same risk tools as any other asset, and ML failures are risk events, not only technical faults.

The readings show ML entering security in three ways.

- **Autonomous defence.** Ridley, McCloskey and Mountain (2018) describe reinforcement learning agents that monitor applications and can isolate or patch compromised systems without waiting for an analyst.
- **Recommender systems.** Techniques developed for e-commerce (Aggarwal, 2016) are now used to advise on security practice and to direct analysts' attention.
- **Trust in ML itself.** Adversarial ML treats the algorithm as the attack surface, through data poisoning, evasion, model stealing and data extraction (Vassilev *et al.*, 2024). Wing (2020) frames the response as trustworthy AI: robustness, fairness, accountability, and the question of how a model and its data can be shown to satisfy a stated property.

Three other trends compete for influence. Enterprise risk management (ERM) argues that all risks, not only those easy to quantify, should be managed as a portfolio across the organisation (Fraser and Simkins, 2016). DevSecOps builds security into the delivery pipeline through dependency scanning, static and dynamic testing, and container testing (Carter, 2017). The NSA's Science of Security initiative identified five hard problems, including security metrics and human behaviour, that still lack rigorous foundations (Nicol *et al.*, 2012).

**My assessment.** The trends are not independent. Autonomous defence and recommender systems are only as good as the models behind them. ERM and DevSecOps are the governance and delivery channels through which AI risk will be managed. The hard problems of metrics and human behaviour return as the problems of measuring model risk and keeping humans meaningfully in the loop. I therefore treat the security and governance of ML, meaning adversarial ML and trustworthy AI, as the trend most likely to reshape the field, and this is the position I take in the Unit 12 debate.
</div>

## Learning note

Building the simulation taught me more than reading about it. The hardest part was not the code but deciding what each input rested on, and then admitting in the report that most inputs were judgements. Labelling the basis of every estimate felt like weakening my own work at first; I now think it is what made the work defensible.
