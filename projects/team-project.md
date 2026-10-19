---
layout: default
title: "Team project: risk identification report"
kicker: Unit 6 status document. Group 3, Pampered Pets case study.
permalink: /projects/team-project/
lo: [1, 2, 3, 4]
prev: { title: "Collaborative Discussion 2", url: "/discussions/discussion-2/" }
next: { title: "Individual project (Unit 11)", url: "/projects/individual-project/" }
---

## The brief

Pampered Pets is a four-person pet food business. It relies on local suppliers, a single old computer, a shared Wi-Fi network and email ordering. The owner had been told that digitalisation could raise demand by 50%, that international sourcing could cut purchase prices by 24%, and that failing to digitalise could lose a third of customers. Group 3 was asked to identify the risks of the business as it stands and the risks digitalisation would introduce, and to recommend a course of action, within 1,000 words.

## The team and how we divided the work

The team was Kaona Hoxha (project lead), Noora Aldsani, Janet Karani and me. Roles were agreed in a [team contract]({{ '/development/team-meetings/' | relative_url }}#team-contract) signed on 24 August 2026, each of the five report sections had a named owner, and we set an internal draft deadline of 30 August, ahead of the official one.

| Section | Owner |
|---|---|
| 1. Decision frame and methodology | Agreed jointly; ISO 31000 framing proposed by Kaona as project lead |
| 2. Current-state risk assessment | **Me** |
| 3. Digitalisation as risk migration | Kaona, who also compiled, edited and controlled the word count |
| 4. The three claims as an interacting scenario | Janet, who also contributed to the final recommendation |
| 5. Recommendation: preserve reversibility | Noora |

## My individual contribution

**Methodology.** I contributed the threat modelling approach and argued that STRIDE should be limited to identities, systems and data flows. STRIDE has nothing useful to say about food safety, staff capacity or supplier economics (Shevchenko *et al.*, 2018), so stretching it across the whole business would have produced a long list of poorly fitting threats. The group adopted this scoping, which is why Section 3 pairs STRIDE threats with separate operational scenarios.

**Section 2, the current-state assessment.** I wrote the baseline the rest of the report compares against: five risks covering data availability and malware, product safety and traceability, supplier, people and premises concentration, fraud, privacy and payment, and strategic inaction. I deliberately included strategic inaction, because securing the current systems does nothing about customers drifting to more convenient competitors. Each risk carries a provisional likelihood and impact on the same scale used for the future state, and a proportionate mitigation.

**Honest scoping of evidence.** I argued that, with no incident, margin or customer data in the case study, ratings should be described as provisional judgements rather than presented with false precision (Aven and Thekdi, 2025). This became a principle of the whole report.

**Review.** I reviewed and commented on the other sections rather than rewriting them.

**What I would do differently.** My first draft used practitioner terminology that had to be simplified at review, and I raised my reservations about how firmly the recommendation was framed at the review stage rather than at planning. Both cost group time. The [reflective piece]({{ '/reflection/' | relative_url }}) analyses this further.

The contract assigned me "current threats, risk evaluation and mitigations", which is the scope of Section 2 as submitted.

## Tutor feedback in brief

The tutor judged criticality the report's strongest area, and singled out the justification for combining ISO 31000, STRIDE and qualitative scenarios, including the recognition of what STRIDE cannot assess, which was the scoping I contributed. The main weaknesses were an undefined likelihood and impact scale, no formal risk register, and mitigations without owners, timescales or residual risk levels, which applies to my section as much as any other. The full feedback and my response are on the [feedback page]({{ '/development/feedback/' | relative_url }}#team-project-risk-identification-report-unit-6).

## The submitted report

The report is reproduced below as submitted. You can also [download the original Word file]({{ '/assets/docs/Group3-Risk-Identification-Report.docx' | relative_url }}).

<div class="artefact" markdown="1">
<p class="artefact-meta">Group 3 (2026). Submitted at the end of Unit 6. My section is Section 2.</p>

**Risk Identification Report. Pampered Pets: selective digitalisation as a resilience strategy**

#### 1. Decision frame and methodology

The decision is which information flows to digitalise without dismantling valuable capabilities. Local supply and personal service are resilience assets; the old computer, shared Wi-Fi and email ordering create exposure. Selective digitalisation should strengthen traceability and customer access while preserving local recoverability, recognising that digital opportunities and risks arise together (Renn, Beier and Schweizer, 2021; Sørensen, 2018).

ISO 31000 provides the decision framework and integrates operational, security and compliance risks (AIRMIC, Alarm and IRM, 2010; Barafort, Mesquida and Mas, 2019). STRIDE is restricted to identities, systems and data flows because it cannot evaluate food safety, capacity or supplier economics (Shevchenko et al., 2018); these require qualitative scenarios. The same likelihood-impact scale is applied to both states for consistent comparison. Without incident, margin, customer or supplier data, ratings remain provisional judgements rather than false precision (Aven and Thekdi, 2025).

#### 2. Current-state risk assessment

- **Data availability and malware.** Likelihood: Medium; Impact: High. Loss or corruption of the warehouse spreadsheet could remove stock visibility; shared Wi-Fi and personal devices provide a malware route. Support and backup status must be verified. Mitigate with a supported endpoint, segregated networks, least-privilege accounts, MFA and tested offline backups (Sutton, 2021).

- **Product safety and traceability.** Likelihood: Medium; Impact: High. Incorrect ingredient, allergen, expiry or batch information could undermine quality control and recalls. Use controlled records, supplier reconciliation, dual checks, recall exercises and a manual fallback. Digitisation may otherwise propagate one error rapidly (Aven and Thekdi, 2025).

- **Supplier, people and premises concentration.** Likelihood: Medium; Impact: High. Local disruption, staff absence or premises loss could affect several functions, although ten-minute supplier access supports recovery. Mitigate through secondary local suppliers, safety stock, cross-training, off-site records, continuity procedures and insurance (Sutton, 2021).

- **Fraud, privacy and payment.** Likelihood: Medium; Impact: Medium-High. Email ordering enables phishing, fraudulent bank-detail changes and excessive data retention. Independent call-back, dual payment approval, data minimisation and deletion schedules are proportionate (ICO, 2020); PCI-DSS applies where cards are accepted (PCI SSC, 2020).

- **Strategic inaction.** Likelihood: Medium and rising; Impact: Medium-High. Securing current systems cannot prevent migration towards convenient competitors. Test this through customer research and a digital pilot.

#### 3. Digitalisation as risk migration

Proposed changes are click-and-collect, authoritative online product information, and cloud inventory and batch traceability, initially retaining in-store payment and local sourcing. This migrates risk from local, manually recoverable failures towards interconnected dependencies (Renn, Beier and Schweizer, 2021; Sørensen, 2018). STRIDE-informed technical threats and wider operational risk scenarios are evaluated below.:

- **Tampering.** Likelihood: Medium; Impact: High. Accidental or unauthorised alteration could corrupt stock decisions, product descriptions and recall evidence simultaneously. Role-based access, dual approval, immutable audit history and supplier reconciliation reduce exposure, but availability cannot compensate for lost integrity (Sutton, 2021).

- **Spoofing/elevation of privilege.** Likelihood: Medium; Impact: High. Stolen staff or administrator credentials could permit safety-critical changes. Use MFA, unique accounts, least privilege, privileged-action alerts and prompt access removal.

- **Denial of service.** Likelihood: Medium; Impact: High. Ransomware, provider failure, account lockout or corrupt synchronisation could disable ordering, fulfilment and traceability. Independent backups, tested export and restoration, contractual recovery requirements and a paper-based degraded mode reduce disruption (Sutton, 2021).

- **Information disclosure/repudiation.** Likelihood: Medium; Impact: Medium. Online ordering creates personal-data exposure and disputes over actions. Minimise collection, restrict access, define deletion periods and retain auditable transaction records (ICO, 2020). A hosted PCI-DSS-compliant provider should be required before online payment (PCI SSC, 2020).

- **Operational and supply-chain amplification.** Likelihood: Medium; Impact: High. Rapid demand could overwhelm four employees, while international sourcing compounds transformation with quality, traceability and recovery risks. Apply order caps and fulfilment thresholds; exclude international sourcing from phase one.

#### 4. The three claims as an interacting scenario

The 50%, 24% and 33% claims may be mutually incompatible. Fifty per cent growth could overload fulfilment and cause customer loss. A 24% purchase-price reduction could weaken traceability and the local identity supporting growth. The relevant question is whether the combined model remains viable under stress because interventions produce interacting consequences (Renn, Beier and Schweizer, 2021).

No case evidence supports a 50% demand uplift. Digitalisation may enable new business models and market access, but its outcome depends on context and implementation rather than the technology alone (Sørensen, 2018). The claim cannot supply Pampered Pets' conversion rate, repeat-purchase behaviour or contribution margin and should be treated as a stress test for capacity, not a forecast (Aven and Thekdi, 2025).

Similarly, 24% is meaningless without total-cost modelling covering freight, duties, currency, working capital, quality failures and disruption. The strength of knowledge matters alongside a calculated risk value (Aven and Thekdi, 2025). The 33% claim lacks segmentation, a churn baseline and competitor evidence. A survey and pilot can test convenience but not validate a predetermined percentage.

#### 5. Recommendation: preserve reversibility

Pampered Pets should digitalise its information flows, not digitalise away its identity. Phase zero should secure the existing environment and document recall, continuity and manual operating procedures. Phase one should pilot click-and-collect, product information and cloud traceability for three to six months, with order caps and in-store payment. Expansion should require agreed thresholds for stock accuracy, packing errors, fulfilment time, complaints, repeat purchases, security incidents and contribution margin.

Small, reversible commitments preserve the ability to expand, redesign or stop as uncertainty is reduced through evidence. This follows ISO 31000's iterative emphasis on monitoring, review and treatment adjustment rather than one-off compliance (AIRMIC, Alarm and IRM, 2010; Barafort, Mesquida and Mas, 2019). Online payment and limited trials with non-critical international suppliers should be separate later decisions, never bundled with the initial pilot. The recommendation is therefore conditional, not pro-technology: proceed only while measured benefits exceed the new concentration, safety and identity risks created by scale.

##### References
AIRMIC, Alarm and IRM (2010) *A structured approach to enterprise risk management and the requirements of ISO 31000*. London: Association of Insurance and Risk Managers in Industry, Alarm and Institute of Risk Management.

Aven, T. and Thekdi, S. (2025) *Risk Science*. 3rd edn. Abingdon: Routledge.

Barafort, B., Mesquida, A.-L. and Mas, A. (2019) ‘ISO 31000-based integrated risk management process assessment model for IT organizations’, *Journal of Software: Evolution and Process*, 31(1), e1984. Available at: <https://doi.org/10.1002/smr.1984>.

Information Commissioner’s Office (ICO) (2020) *Guide to the General Data Protection Regulation (GDPR)*. Available at: <https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/>(Accessed: 30 August 2026).

PCI Security Standards Council (PCI SSC) (2020) *PCI Security Standards Overview*. Available at: <https://www.pcisecuritystandards.org/standards/> (Accessed: 30 August 2026).

Renn, O., Beier, G. and Schweizer, P.-J. (2021) ‘The opportunities and risks of digitalisation for sustainable development: a systemic perspective’, *GAIA – Ecological Perspectives for Science and Society*, 30(1), pp. 23–28. Available at: <https://doi.org/10.14512/gaia.30.1.6>.

Shevchenko, N., Chick, T.A., O’Riordan, P., Scanlon, T.P. and Woody, C. (2018) *Threat Modeling: A Summary of Available Methods*. Pittsburgh, PA: Carnegie Mellon University Software Engineering Institute. Available at: <https://www.sei.cmu.edu/library/threat-modeling-a-summary-of-available-methods/> (Accessed: 30 August 2026).

Sørensen, B.T. (2018) ‘Digitalisation: an opportunity or a risk?’, *Journal of European Competition Law & Practice*, 9(6), pp. 349–350. Available at: <https://doi.org/10.1093/jeclap/lpy038>.

Sutton, D. (2021) *Information Risk Management*. 2nd edn. Swindon: BCS Learning & Development Ltd.

</div>

