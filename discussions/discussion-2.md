---
layout: default
title: "Collaborative Discussion 2: CVSS and its alternatives"
kicker: Units 7 to 9. Reading, Wunder et al. (2024), CVSS scoring inconsistencies.
permalink: /discussions/discussion-2/
lo: [1, 2, 3]
prev: { title: "Collaborative Discussion 1", url: "/discussions/discussion-1/" }
next: { title: "Team project (Unit 6)", url: "/projects/team-project/" }
---

The discussion asked which characteristics of the Common Vulnerability Scoring System (CVSS) Wunder *et al.* (2024) criticise, whether the critique is justified, and which alternative should replace CVSS. This discussion sat closest to my day-to-day work, where CVSS scores are the default language for reporting vulnerabilities. Original files: [initial post]({{ '/assets/docs/D2-Initial-Post.docx' | relative_url }}), [response to Asma]({{ '/assets/docs/D2-Peer-Response-Asma.docx' | relative_url }}), [response to Kaona]({{ '/assets/docs/D2-Peer-Response-Kaona.docx' | relative_url }}).

## How my thinking developed

I began by arguing that the Stakeholder-Specific Vulnerability Categorization (SSVC) should replace CVSS for prioritisation. In my responses to Asma and Kaona I agreed that CVSS still has value as a shared technical language. The most useful challenge came from Kaona, with Janet agreeing: SSVC is not automatically more consistent, because a decision tree is only as reliable as its inputs. My summary therefore moved from "change the framework" to "govern the inputs", adding an asset inventory linked to business services, documented rationale, second review for critical systems and exploit-likelihood data such as EPSS.

## 1. Initial post (Unit 7)

<div class="artefact" markdown="1">
<p class="artefact-meta">Posted Saturday 3 October 2026</p>

Wunder et al. (2024) criticizes several characteristics of the Common Vulnerability Scoring System (CVSS), particularly its **subjectivity, complexity and inconsistency between assessors**. Although CVSS provides a standardized framework for describing vulnerability severity, the authors demonstrate that different users can interpret and apply its metrics differently. This is problematic because apparently precise numerical scores can give organizations a false sense of objectivity when the underlying metric selection may depend on the individual assessor (Wunder et al., 2024). The authors’ findings therefore question whether CVSS scores are sufficiently reliable for making vulnerability-prioritization decisions.

I agree with this criticism to a significant extent. CVSS is useful as a common language for communicating the technical severity of vulnerabilities, but severity and priority are not necessarily the same thing. For example, a vulnerability with a high CVSS score may not represent an immediate organizational risk if the affected system is isolated or well protected. Conversely, a vulnerability with a lower technical score could require urgent attention if it affects a critical business system. The CVSS framework itself recognizes the importance of environmental and threat-related factors, but these require additional assessment by the organization (FIRST, 2024). Consequently, relying on the numerical score alone can be misleading.

One alternative discussed in the literature is **Stakeholder-Specific Vulnerability Categorization (SSVC)**. SSVC uses decision trees to support vulnerability-response decisions and explicitly considers the requirements and context of different stakeholders (Spring et al., 2019). I would argue that SSVC should replace CVSS as the primary method for **vulnerability prioritization**, because it focuses on the decision that an organization needs to make rather than reducing vulnerability characteristics to a single numerical score. This does not mean that CVSS should disappear completely; its technical severity information could remain useful as an input to SSVC. Overall, combining technical vulnerability information with organizational context provides a more meaningful basis for deciding which vulnerabilities require immediate action.

**References**

FIRST (2024) *Common Vulnerability Scoring System version 4.0: Specification Document*. Available at: https://www.first.org/cvss/v4.0/specification-document (Accessed: 3 October 2026).

Spring, J., Hatleback, E., Householder, A.D., Manion, A. and Shick, D. (2019) *Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization*. Pittsburgh, PA: Software Engineering Institute, Carnegie Mellon University. Available at: https://www.sei.cmu.edu/library/prioritizing-vulnerability-response-a-stakeholder-specific-vulnerability-categorization/ (Accessed: 3 October 2026).

Wunder, J., Kurtz, A., Eichenmüller, C., Gassmann, F. and Benenson, Z. (2024) ‘Shedding Light on CVSS Scoring Inconsistencies: A User-Centric Study on Evaluating Widespread Security Vulnerabilities’, *2024 IEEE Symposium on Security and Privacy*, pp. 1102–1121.

</div>


## 2. My peer responses (Unit 8)

### Response to Asma Umar

<div class="artefact" markdown="1">
<p class="artefact-meta">Unit 8 peer response, in reply to Asma Umar</p>

I agree with your argument that the subjectivity involved in applying CVSS can undermine the consistency that the framework is intended to provide. The findings from Wunder et al. (2024) are particularly relevant because differences in metrics such as Attack Vector, User Interaction and Scope demonstrate that even standardized criteria can be interpreted differently by different assessors.

I also agree with your distinction between **technical severity and vulnerability prioritization**. A numerical CVSS score is useful for communicating the characteristics of a vulnerability, but it does not necessarily reflect the actual risk to a particular organization. As Spring et al. (2021) argue, vulnerability prioritization needs to consider the context in which the vulnerability exists rather than relying solely on a generic severity score.

Your suggestion of using SSVC for prioritization is therefore convincing. I particularly like the fact that SSVC focuses on the **decision that needs to be made** rather than simply assigning a number to a vulnerability. Factors such as exploitation and organizational impact can provide security teams with a more actionable basis for determining remediation priorities (Spring et al., 2020).

However, I think there is also a practical argument for retaining CVSS. Many vulnerability-management platforms, security advisories and vendors already use CVSS, making it valuable for communication and interoperability. Replacing it completely could therefore create additional challenges for organizations that rely on CVSS-based reporting.

For this reason, I agree with your conclusion that **CVSS and SSVC can serve different purposes**: CVSS can communicate technical severity, while SSVC can provide the contextual decision-making layer for remediation prioritization. This combination could provide a more complete vulnerability-management process than relying on either framework alone.

**References**

Spring, J.M., Hatleback, E., Householder, A.D., Manion, A. and Shick, D. (2020) ‘Prioritizing vulnerability response: A stakeholder-specific vulnerability categorization (Version 1.1)’, *Workshop on the Economics of Information Security*. Available at: https://weis2020.econinfosec.org/wp-content/uploads/sites/8/2020/06/weis20-final6.pdf (Accessed: 3 October 2026).

Spring, J.M., Hatleback, E., Householder, A.D., Manion, A. and Shick, D. (2021) ‘Time to change the CVSS?’, *IEEE Security & Privacy*, 19(2), pp. 74–78. doi: 10.1109/MSEC.2020.3044475.

Wunder, J., Kurtz, A., Eichenmüller, C., Gassmann, F. and Benenson, Z. (2024) ‘Shedding light on CVSS scoring inconsistencies: A user-centric study on evaluating widespread security vulnerabilities’, *2024 IEEE Symposium on Security and Privacy (SP)*, pp. 1102–1121. doi: 10.1109/SP54263.2024.00058.

</div>


### Response to Kaona Hoxha

<div class="artefact" markdown="1">
<p class="artefact-meta">Unit 8 peer response, in reply to Kaona Hoxha</p>

I agree with your argument that the main weakness of CVSS is not necessarily the scoring concept itself, but the inconsistency that can arise when different assessors interpret its metrics. Your point about the 68% of participants changing their scores after nine months is particularly important because it suggests that reproducibility can remain problematic even when the evaluator has previous experience with the framework (Wunder et al., 2024).

I also agree with your distinction between **technical severity and organizational risk**. CVSS is specifically designed to communicate the severity of a vulnerability rather than provide a complete assessment of organizational risk (FIRST, 2020). Therefore, a high CVSS score does not necessarily mean that a vulnerability should receive the highest remediation priority. Organizational factors such as asset criticality, exposure, compensating controls and business impact also need to be considered.

Your choice of SSVC is interesting because it addresses this contextual problem directly. Rather than producing a universal numerical score, SSVC uses decision trees to connect vulnerability characteristics with stakeholder-specific response decisions (Spring et al., 2020). However, I wonder whether SSVC should completely replace CVSS. CVSS remains useful for providing a common technical language between vendors, security teams and organizations, particularly because its standardized metrics support consistent communication of vulnerability characteristics (FIRST, 2020).

Perhaps the strongest approach would therefore be to use **CVSS for technical severity and SSVC for organizational prioritization**. This would preserve the interoperability and technical information provided by CVSS while reducing the risk of treating a numerical severity score as equivalent to organizational risk. In this sense, SSVC could complement CVSS by turning vulnerability information into a contextual remediation decision.

FIRST (2020) *Common Vulnerability Scoring System v3.1: Specification Document*. Available at: https://www.first.org/cvss/v3-1/specification-document (Accessed: 3 October 2026).

Spring, J.M., Hatleback, E., Householder, A.D., Manion, A. and Shick, D. (2020) *Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization (Version 1.1)*. Pittsburgh, PA: Carnegie Mellon University Software Engineering Institute.

Wunder, J., Kurtz, A., Eichenmüller, C., Gassmann, F. and Benenson, Z. (2024) ‘Shedding light on CVSS scoring inconsistencies: a user-centric study on evaluating widespread security vulnerabilities’, in *2024 IEEE Symposium on Security and Privacy*. San Francisco, CA: IEEE, pp. 1102–1121

</div>


## 3. Peer responses I received

<div class="artefact received" markdown="1">
<p class="artefact-meta">From Kaona Hoxha, Sunday 4 October 2026, in reply to my initial post</p>

Your distinction between vulnerability severity and organisational priority is important, particularly because CVSS v4.0 now includes Threat and Environmental metric groups intended to provide greater context (FIRST, 2024). However, these additions do not fully resolve the inconsistency identified by Wunder et al. (2024). If organisations interpret contextual metrics differently or fail to update them when exploit activity changes, the resulting score may still create an unjustified impression of precision.

I agree that SSVC is more suitable as the primary prioritisation method, although its effectiveness also depends on governance. A decision tree cannot produce reliable actions if asset criticality, exploitation status or mission impact are inaccurate. Organisations should therefore maintain an asset inventory linked to business services, record the reasoning behind each SSVC decision and require a second reviewer for vulnerabilities affecting critical systems. Periodic reassessment is also necessary because a vulnerability initially assigned "Track" may require "Act Immediately" once exploitation evidence emerges.

A practical approach would be to use CVSS as a structured description of technical characteristics and SSVC as the decision mechanism. Exploitation intelligence, affected-asset exposure and compensating controls should then be used to validate the selected response. This would preserve CVSS's interoperability while reducing reliance on a single numerical score.

The principal improvement is therefore not simply changing frameworks, but making prioritisation evidence-based, reviewable and responsive to changing threat conditions. Without those controls, SSVC could reproduce the same inconsistency it is intended to address.

**References**

FIRST (2024) *Common Vulnerability Scoring System version 4.0: Specification Document*. Available at: https://www.first.org/cvss/v4.0/specification-document (Accessed: 4 October 2026).

Wunder, J., Kurtz, A., Eichenmüller, C., Gassmann, F. and Benenson, Z. (2024) 'Shedding light on CVSS scoring inconsistencies: a user-centric study on evaluating widespread security vulnerabilities', *2024 IEEE Symposium on Security and Privacy*, pp. 1102–1121.
</div>

<div class="artefact received" markdown="1">
<p class="artefact-meta">From Janet Karani, Wednesday 7 October 2026, in reply to Kaona's response on my thread</p>

I agree with both of you Mohammed and Kaona that CVSS has significant limitations when used as the primary basis for vulnerability prioritisation. Kaona correctly highlights that subjectivity in assessing CVSS metrics can lead to inconsistent scores. As Wunder et al. (2024) demonstrate, different assessors may interpret metrics differently, reducing the reliability of what appears to be an objective numerical score. I also agree that vulnerability severity and organisational priority are distinct concepts. A high CVSS score does not automatically translate into high organisational risk, particularly when compensating controls or limited exposure reduce the likelihood of exploitation.

Kaona's argument provides an important extension to this argument by recognising that SSVC is not immune to inconsistency. While SSVC incorporates organisational context and supports decision-making more effectively than CVSS, its outcomes are only as reliable as the quality of the information used. If asset criticality, threat intelligence, or business impact assessments are inaccurate, prioritisation decisions may still be flawed. I particularly agree with the recommendation for governance measures such as maintaining accurate asset inventories, documenting decisions, and conducting periodic reviews.

Overall, I believe the strongest approach is to use CVSS and SSVC together. CVSS provides a widely recognised method for communicating technical severity, while SSVC enables organisations to prioritise vulnerabilities according to operational risk and business context. This combined approach addresses the weaknesses of relying solely on a numerical score while preserving the benefits of standardisation and interoperability. Consequently, effective vulnerability management depends not only on the framework chosen but also on the quality of organisational processes that support risk-based decision-making.

**References**

FIRST (2024) *Common Vulnerability Scoring System v4.0 Specification Document*. Forum of Incident Response and Security Teams. Available at: https://www.first.org/cvss/specification-document (Accessed: 5 October 2026).

Spring, J.M., Hatleback, E., Householder, A.D. and Manion, A. (2019) *Stakeholder-Specific Vulnerability Categorization (SSVC)*. Carnegie Mellon University, Software Engineering Institute.

Wunder, J., Riek, M., Fuchs, A. and Wirtz, G. (2024) *Evaluating the Reliability of CVSS Assessments*.
</div>

## 4. Summary post (Unit 9)

<div class="artefact" markdown="1">
<p class="artefact-meta">Posted Friday 16 October 2026</p>

In my initial post, I argued that Wunder et al. (2024) expose real weaknesses in CVSS. Its metrics are interpreted inconsistently between assessors, and the resulting numerical score suggests an objectivity that the underlying judgements do not support. I distinguished technical severity from organisational priority and proposed that SSVC (Spring et al., 2019) should replace CVSS as the primary prioritisation method, with CVSS kept as an input.

The peer discussion refined my position rather than overturning it. Kaona noted that the Threat and Environmental metric groups in CVSS v4.0 (FIRST, 2024) add context but still depend on assessor judgement and timely updates, so they do not remove the inconsistency Wunder et al. (2024) identified. More importantly, Kaona challenged an assumption in my argument: SSVC is not inherently more consistent. Its decision trees are reliable only if their inputs are accurate, such as exploitation status, exposure and mission impact. Janet reinforced this and concluded that the two frameworks work best together.

This has shifted my view. I still consider SSVC the better decision mechanism, because it asks what action the organisation should take rather than how severe a flaw is in the abstract. CISA (2022) has adopted this approach operationally. However, changing frameworks does not by itself solve the reliability problem. Without certain controls, SSVC could reproduce the same subjectivity in a different form. These controls include an asset inventory linked to business services, documented decision rationale, second review for critical systems, and reassessment as threat intelligence changes. Exploit-likelihood data such as EPSS (Jacobs et al., 2021) could also strengthen the exploitation input.

My revised conclusion is that SSVC should replace CVSS as the primary basis for prioritisation, while CVSS remains a standardised description of technical characteristics. Both must sit within governance that makes decisions evidence-based, reviewable and responsive to change.

**References**

CISA (2022) *Stakeholder-Specific Vulnerability Categorization Guide*. Washington, DC: Cybersecurity and Infrastructure Security Agency. Available at: <https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc> (Accessed: 16 October 2026).

FIRST (2024) *Common Vulnerability Scoring System version 4.0: Specification Document*. Available at: <https://www.first.org/cvss/v4.0/specification-document> (Accessed: 3 October 2026).

Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I. and Roytman, M. (2021) ‘Exploit Prediction Scoring System (EPSS)’, *Digital Threats: Research and Practice*, 2(3), pp. 1–17.

Spring, J., Hatleback, E., Householder, A.D., Manion, A. and Shick, D. (2019) *Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization*. Pittsburgh, PA: Software Engineering Institute, Carnegie Mellon University.

Wunder, J., Kurtz, A., Eichenmüller, C., Gassmann, F. and Benenson, Z. (2024) ‘Shedding Light on CVSS Scoring Inconsistencies: A User-Centric Study on Evaluating Widespread Security Vulnerabilities’, *2024 IEEE Symposium on Security and Privacy*, pp. 1102–1121.

</div>

