---
layout: default
title: "Individual project: quantitative risk assessment and DR design"
kicker: Unit 11 executive summary. Pampered Pets after international expansion.
permalink: /projects/individual-project/
lo: [1, 2, 3, 4]
prev: { title: "Team project (Unit 6)", url: "/projects/team-project/" }
next: { title: "Unit 11 vs Unit 6 evaluation", url: "/projects/evaluation/" }
---

## The brief

By Unit 11 the case had moved on. Rather than following the phased approach our team had recommended, the owner introduced an international supply chain, automated warehouses and a 24/7 online shop in one step, and attracted royal customers. The individual brief asked for a quantitative assessment of the probability of quality-threatening and supply-disrupting events, prioritised recommendations including data protection obligations, and a business continuity and disaster recovery solution meeting recovery time and recovery point objectives of under one minute.

The tutor's feedback and my response are on the [feedback page]({{ '/development/feedback/' | relative_url }}#individual-project-executive-summary-unit-11).

## Key decisions I made

**Method.** I chose a Monte Carlo simulation with calibrated three-point (PERT) estimates over a qualitative matrix, single-point annualised loss expectancy or FAIR. The business had no loss history, so ranges were the honest way to express both the estimate and its uncertainty (Hubbard and Seiersen, 2023), and ordinal matrices cannot be combined or reliably ranked (Cox, 2008).

**Testing my own model.** I ran a correlation sensitivity test (Gaussian copula, ρ = 0.3) because one shock can trigger several events. It lowered the chance of at least one event but raised the chance of two or more quality events: fewer bad years, but worse ones. I concluded that the ranking was more robust than any single percentage and labelled which inputs rested on survey data and which on judgement.

**Legal precision.** The brief referred to a "new GDPR directive". I corrected this (the GDPR is a Regulation, applicable since 2018) and mapped obligations across the UK GDPR, the EU GDPR and Monaco's Law No. 1.565, then treated legal requirements as go-live gates rather than ranked options.

**Proportionate DR.** A one-minute RTO and RPO requires an active-active multi-region design that a four-person business cannot operate, so I recommended managed services through a contracted provider, with lock-in controlled by open standards, open-format exports and a tested exit plan.

## Reproducibility code (added after feedback)

The tutor's feedback asked for simulation code so the results, especially the correlated scenario, could be audited, and for sensitivity testing of the assumed control reductions. I wrote the [Python simulation script]({{ '/assets/code/pampered_pets_monte_carlo.py' | relative_url }}) after receiving feedback; its [full output]({{ '/assets/code/pampered_pets_monte_carlo_output.txt' | relative_url }}) is also published. It was not part of the marked submission.

| Measure | Reported in submission | Reproduced by script |
|---|---|---|
| P(at least one quality event) | 54.6% | 54.6% |
| P(two or more quality events) | 15.0% | 15.0% |
| P(at least one supply event) | 79.3% | 79.3% |
| Correlated (ρ = 0.3), at least one quality event | 46.6% | 46.2% |
| Correlated (ρ = 0.3), at least one supply event | 64.3% | 64.6% |
| Residual, at least one quality event | 25.8% | 25.8% |
| Residual, at least one supply event | 52.2% | 52.2% |

Small differences in the correlated rows are sampling noise from 100,000 iterations.

**Same procedure for both scenarios.** The script runs the independent case through the same Bernoulli and copula procedure as the correlated case, with ρ = 0. It matches the analytic baseline (54.6% and 79.4%), so the difference between the two scenarios is attributable to correlation alone.

**Sensitivity to control effectiveness.** If controls deliver only half their assumed reduction, the probability of at least one quality event rises from 26% to 42%, and of a supply event from 52% to 68%. The ranking of controls is unchanged, but the headline claim that controls "halve" quality risk depends heavily on them working as assumed.

## The submitted executive summary

Reproduced as submitted. You can also [download the original Word file]({{ '/assets/docs/Executive-Summary-Unit11.docx' | relative_url }}).

<div class="artefact" markdown="1">
<p class="artefact-meta">Individual submission, Unit 11</p>


Quantitative Risk Assessment of Digitalisation, the International Supply Chain and Disaster Recovery at Pampered Pets

#### 1. Summary of Findings

The earlier risk identification report (Group 3, 2026) recommended phased, reversible digitalisation, excluding international sourcing from the first phase and deferring online payment. Ms O’dour has instead introduced an international supply chain, automated warehouses and a 24/7 online shop in one step. This has attracted HRH the King and Prince Albert II of Monaco as customers, but shifts risk from local, manually recoverable failures towards interconnected dependencies (Renn, Beier and Schweizer, 2021).

A Monte Carlo simulation of fifteen risks estimates, without further controls, a **55% probability (90% interval 45–63%)** of at least one quality-threatening event in the first twelve months and a **79% probability (73–85%)** of at least one material supply disruption. The leading drivers are logistics or customs delays (36%), transit temperature or humidity excursions (26%) and fulfilment overload for a four-person team (22%). The prioritised controls in Section 4 reduce these to approximately **26%** and **52%**.

Data protection and feed/import compliance are legal obligations and are ranked first. The one-minute recovery targets require a two-region design in which the shop runs active-active and a single-writer database is promoted automatically on failure; because a four-person business cannot operate it, it should run on Amazon Web Services (AWS) managed services through a contracted managed service provider, with lock-in controlled by open standards and a tested exit plan.

#### 2. Approach

##### 2.1 Risk identification
Risks were identified using the ISO 31000 process (ISO, 2018; Sutton, 2021) across overseas suppliers, transport, automated warehouses, the online shop and customer data. Fifteen were retained, six affecting quality (Q1–Q6) and nine affecting supply or availability (S1–S9), extending the earlier report’s qualitative register to the international operation.

##### 2.2 Choice of method
Monte Carlo simulation with calibrated three-point estimates was selected (Hubbard and Seiersen, 2023) because the international operation has no loss history. Ranges express both the best estimate and its uncertainty, producing the probabilities the client requested while preserving the earlier report’s caution against false precision (Aven and Thekdi, 2024). Qualitative matrices were rejected because ordinal scores cannot be combined and may rank risks incorrectly (Cox, 2008); single-point annualised loss expectancy conceals uncertainty; and FAIR requires loss data the business does not hold.

##### 2.3 Calculations and assumptions
Each risk’s annual probability was estimated as a minimum, most likely and maximum value and modelled as a PERT distribution (Vose, 2008). In each of 100,000 iterations, the probability of at least one event per category was calculated as:

*P(at least one event) = 1 − ∏ (1 − pᵢ)*

Inputs are estimates, not observed incident rates; Tables 1 and 2 show whether each rests on a survey statistic or judgement. Results are reported as the mean with a 90% interval, and a sensitivity run applied correlation (ρ = 0.3) through a Gaussian copula, because one shock can trigger several events (Appendix A). Key assumptions are:

1.  Pampered Pets is a four-person UK business adding overseas suppliers, automated warehouses and customers in the UK, EU and Monaco.

2.  An occurrence affects product quality, delays supply by over two weeks or breaches the online availability tolerance, within the first twelve months, when new processes are least mature.

3.  Risks are independent in the base case; correlation is tested separately.

4.  Survey base rates were adjusted for size, new attack surface and royal profile; where none exist, estimates are labelled as judgement.

5.  The earlier report’s phase-zero controls (MFA, segregated networks, offline backups, controlled records, dual checks, recall exercises) are in place; Section 4 controls are not.

#### 3. Results

Tables 1 and 2 give the inputs and simulated annual probabilities. The 55% quality figure is the probability of a quality-threatening event, not the probability that defective product reaches a customer. S3 is grouped with supply risks because a breach involving royal data could suspend online trading or end the royal relationship.

| **ID** | **Quality risk**                               | **Min / ML / Max (%)** | **Mean (90% interval)** | **Basis**                                           |
|--------|------------------------------------------------|------------------------|-------------------------|-----------------------------------------------------|
| Q1     | Transit temperature or humidity excursion      | 10 / 25 / 45           | 26% (15–37%)            | Judgement; multi-leg routes                         |
| Q2     | Warehouse stock-rotation or mis-pick error     | 5 / 15 / 30            | 16% (9–24%)             | Judgement; new automation                           |
| Q3     | Counterfeit or adulterated product             | 2 / 6 / 15             | 7% (3–11%)              | Elliott (2014)                                      |
| Q4     | Undetected supplier recipe change              | 3 / 8 / 20             | 9% (5–15%)              | Judgement; labelling duty                           |
| Q5     | Deliberate tampering                           | 0.5 / 1 / 3            | 1% (0.6–2%)             | British Standards Institution (2017); royal profile |
| Q6     | Product or batch record error spread digitally | 5 / 12 / 25            | 13% (7–20%)             | Earlier report: medium/high                         |
|        | **At least one quality event**                 |                        | **55% (45–63%)**        |                                                     |

*Table 1. Quality risks (ML = most likely).*

| **ID** | **Supply and availability risk**           | **Min / ML / Max (%)** | **Mean (90% interval)** | **Basis**                                                                                                         |
|--------|--------------------------------------------|------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| S1     | Logistics or customs delay over two weeks  | 20 / 35 / 55           | 36% (25–47%)            | 43.6% hit by third-party failure (Business Continuity Institute, 2024)                                            |
| S2     | Cyber attack disrupting operations         | 5 / 12 / 25            | 13% (7–20%)             | 43% of UK firms breached, 1% ransomware (Department for Science, Innovation and Technology and Home Office, 2025) |
| S3     | Personal data breach, including royal data | 4 / 10 / 22            | 11% (6–17%)             | 30% of breaches involve third parties (Verizon, 2025)                                                             |
| S4     | Cloud or platform outage (before DR)       | 5 / 15 / 30            | 16% (9–24%)             | Judgement; single region                                                                                          |
| S5     | Warehouse automation failure over 48 hours | 5 / 12 / 25            | 13% (7–20%)             | Judgement; new technology                                                                                         |
| S6     | Import or regulatory stoppage              | 5 / 12 / 25            | 13% (7–20%)             | Import controls (*Regulation (EC) No 1069/2009*, 2009)                                                            |
| S7     | Third-party software compromise            | 3 / 8 / 18             | 9% (5–14%)              | Verizon (2025)                                                                                                    |
| S8     | Key supplier failure                       | 3 / 8 / 15             | 8% (5–12%)              | Business Continuity Institute (2024)                                                                              |
| S9     | Fulfilment overload for four staff         | 10 / 20 / 40           | 22% (13–31%)            | Earlier report; 50% growth claim as stress test                                                                   |
|        | **At least one supply event**              |                        | **79% (73–85%)**        |                                                                                                                   |
|        | **Two or more supply events**              |                        | **43%**                 |                                                                                                                   |

*Table 2. Supply chain and availability risks.*

<figure><img src="{{ '/assets/img/exec-summary-fig1-probabilities.png' | relative_url }}" alt="Bar chart of simulated annual probabilities for fifteen risks with 90% intervals. Logistics or customs delay is highest at 36%, followed by transit temperature excursion at 26% and fulfilment overload at 22%; deliberate tampering is lowest at 1%."><figcaption>Figure 1. Simulated annual probabilities with 90% intervals.</figcaption></figure>

##### 3.1 Critical evaluation
Correlation lowers the probability of at least one event (quality 47%, supply 64%) but raises the chance of two or more quality events from 15% to 18%: fewer bad years, but worse ones, favouring contingency stock alongside prevention. Most inputs are judgements anchored to self-selecting surveys skewed towards larger firms, so the strength of knowledge is low to moderate (Aven and Thekdi, 2024). The ranking is therefore more robust than any single percentage, and it drives the treatment plan: the 36% logistics risk justifies safety stock, the 26% transit risk cold-chain monitoring and the 22% overload risk capacity caps. Probability also ignores impact: tampering is rare but could end the royal relationship, so it is prioritised above its likelihood. The claimed 24% purchase-price saving must be weighed against transport, compliance, monitoring and contingency-stock costs before international sourcing is accepted; the unevidenced 33% customer-loss claim is excluded. The model should be updated quarterly with incident data using Bayesian methods (Hubbard and Seiersen, 2023).

#### 4. Prioritised Recommendations

Recommendations are ordered by legal obligation, impact on royal customers and revenue, and probability reduction relative to cost; **MANDATORY** marks legal requirements. Although the brief refers to a “new GDPR directive”, the GDPR is a Regulation applicable since 2018 (*Regulation (EU) 2016/679*, 2016). UK processing falls under the UK GDPR and the *Data Protection Act 2018*, as amended by the *Data (Use and Access) Act 2025*, EU customers under the EU GDPR, and Monegasque customers under Law No. 1.565, which covers foreign controllers processing residents’ data and permits fines of up to €10 million (CMS, 2024).

| **\#** | **Recommendation and key controls**                                                                                                                                                                                                                                                                                                                                                               | **Risks**      | **Before → after**                   | **Status**           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--------------------------------------|----------------------|
| 1      | **Data protection:** DPIA (Art. 35); processor contracts (Art. 28); encryption and least privilege (Art. 32); segregated royal data; 72-hour breach process (Art. 33); IDTA or standard contractual clauses and transfer risk assessments for overseas warehouse and logistics data (Information Commissioner’s Office, 2026); tokenised PCI DSS payments (PCI Security Standards Council, 2024). | S3             | 11% → 5%                             | MANDATORY            |
| 2      | **Feed and import compliance:** audited suppliers, certificates of analysis, batch traceability, and the earlier report’s dual checks and recall exercises extended overseas, under EU feed law and its assimilated GB equivalents (*Regulation (EC) No 767/2009*, 2009; *Regulation (EC) No 1069/2009*, 2009).                                                                                   | Q3, Q4, Q6, S6 | Q3 7→3%; Q4 9→4%; Q6 13→5%; S6 13→5% | MANDATORY            |
| 3      | **Disaster recovery** (Section 5) through a managed service provider.                                                                                                                                                                                                                                                                                                                             | S4             | 16% → 1%                             | BUSINESS REQUIREMENT |
| 4      | **Cold-chain monitoring:** data loggers, goods-in inspection, quarantine.                                                                                                                                                                                                                                                                                                                         | Q1             | 26% → 11%                            | High                 |
| 5      | **Cyber resilience:** OT/IT segmentation, MFA, EDR, patching, immutable backups; Cyber Essentials Plus and an ISO/IEC 27001 roadmap; supplier security clauses (Boyens *et al.*, 2022).                                                                                                                                                                                                           | S2, S7         | S2 13→5%; S7 9→5%                    | High                 |
| 6      | **Capacity:** order caps, fulfilment thresholds, cross-training, surge fulfilment contract.                                                                                                                                                                                                                                                                                                       | S9             | 22% → 11%                            | High                 |
| 7      | **Automation assurance:** first-expired-first-out rules, parallel running, manual fallback, vendor SLA.                                                                                                                                                                                                                                                                                           | Q2, S5         | Q2 16→5%; S5 13→5%                   | Medium               |
| 8      | **Royal order protocol:** tamper-evident packaging, final quality check, PAS 96 threat assessment.                                                                                                                                                                                                                                                                                                | Q5             | 1% → 0.7%                            | Medium               |
| 9      | **Supply diversification:** dual sourcing, alternative routes, four to six weeks’ safety stock.                                                                                                                                                                                                                                                                                                   | S1, S8         | S1 36→26%; S8 8→5%                   | Medium               |

*Table 3. Prioritised recommendations; residual estimates are judgements, conditional on controls being implemented and effective (Appendix A).*

The mandatory controls are go-live gates: transfer safeguards before overseas data sharing, a DPIA and access controls before customer data is processed, PCI DSS validation before payments go live, and supplier approval and traceability before the first international shipment. Each control needs a named owner, a threshold and retained evidence; ISO/IEC 27001 and Cyber Essentials Plus demonstrate rather than constitute compliance.

#### 5. Business Continuity and Disaster Recovery

##### 5.1 Requirements
The requirements translate into a recovery time objective (RTO) and recovery point objective (RPO) under one minute with 24/7/365 availability, achievable only with a multi-site strategy in which the application runs active-active across two regions (AWS, 2021). A premises disaster would not stop the cloud-hosted shop; the realistic threats are region failure, cyber attack and failure of a third party such as the payment provider, now critical because online payment is required.

##### 5.2 Proposed design
<figure><img src="{{ '/assets/img/exec-summary-fig2-dr-architecture.png' | relative_url }}" alt="Two-region cloud architecture diagram with an active-active application tier behind a global load balancer and a single-writer database replicated to a secondary region."><figcaption>Figure 2. Proposed two-region architecture: active-active application tier, single-writer database.</figcaption></figure>

- **Traffic:** CDN, WAF and DDoS protection, and an anycast load balancer that health-checks both regions and shifts traffic without DNS delay.

- **Application:** stateless containers on a fully managed service (for example AWS Fargate) in both regions, avoiding in-house server administration.

- **Data:** Aurora PostgreSQL Global Database. Only the primary region accepts writes; the secondary serves reads and is promoted to writer on failure, with an effective RPO of about one second and promotion in under a minute (AWS, no date).

- **Corruption:** replication copies ransomware damage instantly, so immutable cross-account backups are essential.

- **Assurance:** quarterly end-to-end failover tests against ISO 22301 (ISO, 2019) and NIST SP 800-34 (Swanson *et al.*, 2010), since the vendor figure covers database promotion only. A test passes only if detection, traffic shift, promotion, reconnection and a test order complete within 60 seconds, losing no more than 60 seconds of committed transactions; replication lag is alarmed well below that limit. The earlier report’s paper-based fallback is retained for warehouse operations (Sutton, 2021).

##### 5.3 Platform recommendation
AWS is recommended because its published database recovery figures support both targets, and hosting in its UK and EU regions keeps the shop’s data within the UK and EEA. This reduces but does not remove international transfers: data shared with overseas partners still needs the safeguards in Recommendation 1, and AWS’s US parentage belongs in the transfer risk assessment. A four-person firm cannot run this design, so a managed service provider should be contractually bound to both 60-second targets, with testing, reporting and remedies for breach, as the earlier report advised. Azure and Google Cloud should be included in a competitive quote; a SaaS platform is acceptable only with contractual RTO and RPO commitments. The one-minute changeover is a per-incident target; annual availability (for example 99.99%, about 53 minutes a year) is a separate commitment, and both belong in the contract. A live second region roughly doubles hosting cost, which should be weighed against revenue lost per minute.

##### 5.4 Vendor lock-in
Lock-in arises from proprietary interfaces, data formats and contracts (Opara-Martins, Sahandi and Tian, 2016). It is controlled through containers and infrastructure as code (Terraform or OpenTofu), a PostgreSQL-compatible database (although Aurora’s replication is proprietary), nightly open-format exports held outside the provider, and a tested exit plan. The EU Data Act also obliges providers to facilitate switching (*Regulation (EU) 2023/2854*, 2023). Full multi-cloud is not recommended, as its cost and complexity exceed the firm’s capability.

#### 6. Conclusion

First-year probabilities of 55% for a quality-threatening event and 79% for supply disruption are high, largely because expansion was taken in one step, but the prioritised controls halve the quality figure to 26% and cut supply disruption by a third, to 52%. Meeting the mandatory data protection and feed requirements first, then the managed DR design and cold-chain monitoring, gives a defensible basis for reassuring royal customers. Reinstating the earlier report’s reversibility, expanding international sourcing only as measured thresholds are met, remains the most effective treatment, with the model updated quarterly.

#### References

Aven, T. and Thekdi, S. (2024) *Risk science: an introduction*. 2nd edn. Abingdon: Routledge. Available at: https://doi.org/10.4324/9781003494317

AWS (2021) *Disaster recovery of workloads on AWS: recovery in the cloud*. Available at: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html (Accessed: 4 October 2026).

AWS (no date) *Amazon Aurora Global Database*. Available at: https://aws.amazon.com/rds/aurora/global-database/ (Accessed: 4 October 2026).

Boyens, J. *et al.* (2022) *Cybersecurity supply chain risk management practices for systems and organizations*. NIST SP 800-161r1. Gaithersburg, MD: National Institute of Standards and Technology. Available at: https://doi.org/10.6028/NIST.SP.800-161r1

British Standards Institution (2017) *PAS 96:2017 Guide to protecting and defending food and drink from deliberate attack*. London: British Standards Institution. Available at: https://www.gov.uk/government/publications/guide-to-protecting-and-defending-food---and-drink-from-deliberate-attack (Accessed: 11 October 2026).

Business Continuity Institute (2024) *Latest BCI report reveals escalating supply chain disruptions drive increased tier mapping and insurance uptake*. Available at: https://thebci.org/news/supply-chain-disruptions-drive-increased-tier-mapping-and-insurance-uptake.html (Accessed: 4 October 2026).

CMS (2024) *The new Monegasque data protection law*. Available at: https://cms.law/en/mco/publication/the-new-monegasque-data-protection-law (Accessed: 4 October 2026).

Cox, L.A. (2008) ‘What’s wrong with risk matrices?’, *Risk Analysis*, 28(2), pp. 497–512. Available at: https://doi.org/10.1111/j.1539-6924.2008.01030.x

*Data Protection Act 2018*, c. 12. Available at: https://www.legislation.gov.uk/ukpga/2018/12/contents (Accessed: 4 October 2026).

*Data (Use and Access) Act 2025*, c. 18. Available at: https://www.legislation.gov.uk/ukpga/2025/18/contents (Accessed: 11 October 2026).

Department for Science, Innovation and Technology and Home Office (2025) *Cyber security breaches survey 2025*. Available at: https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2025/cyber-security-breaches-survey-2025 (Accessed: 4 October 2026).

Elliott, C. (2014) *Elliott Review into the integrity and assurance of food supply networks: final report*. London: HM Government. Available at: https://www.gov.uk/government/publications/elliott-review-into-the-integrity-and-assurance-of-food-supply-networks-final-report (Accessed: 11 October 2026).

Group 3 (2026) Risk Identification Report. *Security and Risk Management*. Unpublished group report submitted to the University of Essex Online.

Hubbard, D.W. and Seiersen, R. (2023) *How to measure anything in cybersecurity risk*. 2nd edn. Hoboken, NJ: Wiley. Available at: https://www.oreilly.com/library/view/how-to-measure/9781119892304/ (Accessed: 11 October 2026).

Information Commissioner’s Office (2026) *A guide to international transfers*. Available at: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/a-guide-to-international-transfers (Accessed: 11 October 2026).

ISO (2018) *ISO 31000:2018 Risk management: guidelines*. Geneva: International Organization for Standardization. Available at: https://www.iso.org/standard/65694.html (Accessed: 11 October 2026).

ISO (2019) *ISO 22301:2019 Security and resilience: business continuity management systems: requirements*. Geneva: International Organization for Standardization. Available at: https://www.iso.org/standard/75106.html (Accessed: 11 October 2026).

Opara-Martins, J., Sahandi, R. and Tian, F. (2016) ‘Critical analysis of vendor lock-in and its impact on cloud computing migration: a business perspective’, *Journal of Cloud Computing*, 5(1), article 4. Available at: https://doi.org/10.1186/s13677-016-0054-z

PCI Security Standards Council (2024) *Payment Card Industry Data Security Standard v4.0.1*. Wakefield, MA: PCI Security Standards Council. Available at: https://www.pcisecuritystandards.org/document_library/ (Accessed: 11 October 2026).

*Regulation (EC) No 767/2009 of the European Parliament and of the Council of 13 July 2009 on the placing on the market and use of feed* (2009) *Official Journal* L 229, 1 September, pp. 1–28. Available at: http://data.europa.eu/eli/reg/2009/767/oj (Accessed: 4 October 2026). GB assimilated version available at: https://www.legislation.gov.uk/eur/2009/767/contents (Accessed: 11 October 2026).

*Regulation (EC) No 1069/2009 of the European Parliament and of the Council of 21 October 2009 laying down health rules as regards animal by-products and derived products not intended for human consumption* (2009) *Official Journal* L 300, 14 November, pp. 1–33. Available at: http://data.europa.eu/eli/reg/2009/1069/oj (Accessed: 4 October 2026). GB assimilated version available at: https://www.legislation.gov.uk/eur/2009/1069/contents (Accessed: 11 October 2026).

*Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data (General Data Protection Regulation)* (2016) *Official Journal* L 119, 4 May, pp. 1–88. Available at: http://data.europa.eu/eli/reg/2016/679/oj (Accessed: 4 October 2026).

*Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act)* (2023) *Official Journal* L, 22 December. Available at: http://data.europa.eu/eli/reg/2023/2854/oj (Accessed: 4 October 2026).

Renn, O., Beier, G. and Schweizer, P.-J. (2021) ‘The opportunities and risks of digitalisation for sustainable development: a systemic perspective’, *GAIA – Ecological Perspectives for Science and Society*, 30(1), pp. 23–28. Available at: https://doi.org/10.14512/gaia.30.1.6

Sutton, D. (2021) *Information risk management: a practitioner’s guide*. 2nd edn. Swindon: BCS Learning & Development. Available at: https://learning.oreilly.com/library/view/~/9781780175751 (Accessed: 11 October 2026).

Swanson, M. *et al.* (2010) *Contingency planning guide for federal information systems*. NIST SP 800-34 Rev. 1. Gaithersburg, MD: National Institute of Standards and Technology. Available at: https://doi.org/10.6028/NIST.SP.800-34r1

Verizon (2025) *2025 Data breach investigations report*. Available at: https://www.verizon.com/business/resources/reports/dbir/ (Accessed: 4 October 2026).

Vose, D. (2008) *Risk analysis: a quantitative guide*. 3rd edn. Chichester: Wiley. Available at: https://wiley-vch.de/en/areas-interest/finance-economics-law/risk-analysis-978-0-470-51284-5 (Accessed: 11 October 2026).

#### Appendix A: Simulation Parameters

**PERT sampling.** For minimum *a*, most likely *m* and maximum *b*: α = 1 + 4(m − a)/(b − a); β = 1 + 4(b − m)/(b − a); p = a + (b − a) × Beta(α, β). The PERT mean is (a + 4m + b)/6.

**Aggregation.** In each iteration, P(at least one) = 1 − ∏(1 − pᵢ) was calculated across the sampled probabilities; the mean and the 5th and 95th percentiles of this quantity are reported. For the sensitivity test, event occurrence was simulated as Bernoulli draws driven by correlated standard normal variables (Gaussian copula, ρ = 0.3 between all pairs).

| **ID** | **Risk**                                       | **Inherent Min / ML / Max (%)** | **Residual Min / ML / Max (%)** |
|--------|------------------------------------------------|---------------------------------|---------------------------------|
| Q1     | Transit temperature or humidity excursion      | 10 / 25 / 45                    | 4 / 10 / 20                     |
| Q2     | Warehouse stock-rotation or mis-pick error     | 5 / 15 / 30                     | 2 / 5 / 10                      |
| Q3     | Counterfeit or adulterated product             | 2 / 6 / 15                      | 1 / 3 / 7                       |
| Q4     | Undetected supplier recipe change              | 3 / 8 / 20                      | 1 / 3 / 8                       |
| Q5     | Deliberate tampering                           | 0.5 / 1 / 3                     | 0.3 / 0.6 / 1.5                 |
| Q6     | Product or batch record error spread digitally | 5 / 12 / 25                     | 2 / 5 / 10                      |
| S1     | Logistics or customs delay over two weeks      | 20 / 35 / 55                    | 15 / 25 / 40                    |
| S2     | Cyber attack disrupting operations             | 5 / 12 / 25                     | 2 / 5 / 10                      |
| S3     | Personal data breach, including royal data     | 4 / 10 / 22                     | 2 / 4 / 9                       |
| S4     | Cloud or platform outage (before DR)           | 5 / 15 / 30                     | 0.5 / 1 / 3                     |
| S5     | Warehouse automation failure over 48 hours     | 5 / 12 / 25                     | 2 / 5 / 10                      |
| S6     | Import or regulatory stoppage                  | 5 / 12 / 25                     | 2 / 5 / 10                      |
| S7     | Third-party software compromise                | 3 / 8 / 18                      | 2 / 4 / 9                       |
| S8     | Key supplier failure                           | 3 / 8 / 15                      | 2 / 5 / 10                      |
| S9     | Fulfilment overload for four staff             | 10 / 20 / 40                    | 5 / 10 / 20                     |

*Table A1. Inherent and residual (post-control) three-point estimates.*

| **Measure**                   | **Base case (independent)** | **Correlated (ρ = 0.3)** | **Residual, independent** |
|-------------------------------|-----------------------------|--------------------------|---------------------------|
| P(at least one quality event) | 54.6%                       | 46.6%                    | 25.8%                     |
| P(two or more quality events) | 15.0%                       | 18.3%                    | 2.9%                      |
| P(at least one supply event)  | 79.3%                       | 64.3%                    | 52.2%                     |
| P(two or more supply events)  | 42.5%                       | 36.8%                    | 13.9%                     |

*Table A2. Aggregate results under base, correlated and residual scenarios.*

</div>

