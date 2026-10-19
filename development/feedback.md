---
layout: default
title: Peer and tutor feedback
kicker: Feedback received during the module and what I did with it.
permalink: /development/feedback/
lo: [2]
prev: { title: "Team meetings and process", url: "/development/team-meetings/" }
next: { title: "Skills matrix and PDP", url: "/development/skills-pdp/" }
---

## Peer feedback on Discussion 1

| From | What they said | What I did with it |
|---|---|---|
| Asma Umar | Agreed that digital tools are not neutral, and added that an AI system failing to flag a violation can create a false sense of complete monitoring, so digital evidence should support rather than replace human judgement. | Made this the centre of my summary post, linking it to Aven and Thekdi's (2025) point that absence of signal is not evidence of low risk. |
| Abinel Madzivire | Supported the techno-solutionism argument with Pallí-Asperó *et al.* (2025) on co-creative AI design and Carter (2025) on informational control. | Used the participatory design point to argue in my summary that stakeholder engagement is structural to the risk process (AIRMIC, 2010). |

Both responses are reproduced in full in [Discussion 1]({{ '/discussions/discussion-1/' | relative_url }}#3-peer-responses-i-received).

## Peer feedback on Discussion 2

| From | What they said | What I did with it |
|---|---|---|
| Kaona Hoxha | CVSS v4.0's Threat and Environmental metrics add context but do not remove assessor inconsistency. SSVC is better for prioritisation, but only with governance: an asset inventory linked to business services, recorded rationale, a second reviewer for critical systems and periodic reassessment. | Accepted the challenge that changing frameworks does not by itself fix reliability. My summary post adopted her governance controls and added EPSS as evidence for the exploitation input. |
| Janet Karani | Agreed with both of us, stressed that SSVC outcomes are only as reliable as their inputs, and concluded that CVSS and SSVC work best together. | Revised my conclusion: SSVC as the primary decision mechanism, CVSS kept as the standard technical description, both inside reviewable governance. |

Both responses are reproduced in full in [Discussion 2]({{ '/discussions/discussion-2/' | relative_url }}#3-peer-responses-i-received).

## Feedback within the team

At the review stage, teammates noted that my first draft of Section 2 used practitioner terminology that a non-specialist reader would struggle with. I simplified the section before submission and added "write for the least specialist reader first" to my PDP.

## Tutor feedback

### Team project: risk identification report (Unit 6)

| Criterion | Tutor's main points | My response |
|---|---|---|
| Knowledge and understanding | Strong grasp of operational, cyber, regulatory and supply-chain risks; combining ISO 31000, STRIDE and qualitative scenarios was well justified, including recognising what STRIDE cannot assess. The likelihood and impact scale was not defined, and a formal risk register would have made ratings verifiable. | The STRIDE scoping was my contribution, so this confirmed the value of stating a method's limits. The undefined scale is the weakness I now address first: in Unit 11 every estimate has an explicit range and basis. |
| Application | Analysis closely applied to Pampered Pets, with controls proportionate to a four-person business. Mitigations lacked owners, timescales and residual risk levels, and the cost and staffing of controls were not explained. | My Section 2 mitigations had the same gap. In Unit 11 I gave residual estimates for every control and required a named owner, threshold and evidence for each. |
| Criticality | The strongest area: the three claims were questioned convincingly as interacting effects, and the reversible, pilot-based recommendation was well supported. A side-by-side comparison of the status quo and digitalisation, and more on affordability and acceptable residual risk, would have strengthened the judgement. | I agree. The team argued well but never stated what level of residual risk the owner should accept, which is the decision a risk report exists to support. |
| Structure and presentation | Logical sequence and relevant sources, but visually dense; risks belonged in tables, references on a new page, and there was a punctuation error. | The density came from fitting four sections into 1,000 words. The lesson is that word budgets must include the space a reader needs. |

### Individual project: executive summary (Unit 11)

| Criterion | Tutor's main points | My response |
|---|---|---|
| Knowledge and understanding | Fifteen relevant risks; clear distinction between a quality-threatening event and defective product reaching customers; a clear recovery diagram. Database promotion within a minute does not prove full service recovery, and the two-week disruption threshold needed business justification. | I had noted that the vendor figure covers promotion only, but I did not show how the whole chain meets 60 seconds. A future version needs a timed recovery budget for each step, tied to the business impact that sets the threshold. |
| Criticality | Correlation, weak evidence and sourcing costs were examined. The assumed control reductions needed sensitivity testing, and the correlated scenario used a different procedure from the baseline without supporting code. | I have since written the simulation code, which reproduces the reported results, runs both scenarios with the same procedure, and tests control effectiveness from 0% to 100%. See the [individual project page]({{ '/projects/individual-project/' | relative_url }}#reproducibility-code-added-after-feedback). |
| Use of sources | A wide range of sources, but survey findings do not directly establish company-specific probabilities, and recovery claims needed configuration-specific documentation. | This is the most important criticism. Labelling an input "survey-based" is not the same as justifying the adjustment from a population rate to one firm. I now record the adjustment and its reason for each estimate. |
| Structure and presentation | Tables, chart and diagram communicate well, but repetition and extensive tables made it long for an executive summary. | An executive summary should lead with decisions. Detail belongs in appendices. |
| Academic integrity | Transparent references, labelled judgements and equations, and appropriate acknowledgement of the group report. Code or a workbook was needed for reproducibility, and legal requirements should be separated more carefully from contractual standards and assurance measures. | Code now added. I also accept the legal point: PCI DSS, for example, is a contractual requirement, not law, and should not have sat under the same "mandatory" label as GDPR. |
