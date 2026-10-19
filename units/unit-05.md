---
layout: default
title: "Unit 5: Security and risk standards in industry and the enterprise"
kicker: Unit 5 of 12
permalink: /units/unit-05/
lo: [1, 2, 3, 4]
prev: { title: "Unit 4: Applying threat models", url: "/units/unit-04/" }
next: { title: "Unit 6: Standards in practice", url: "/units/unit-06/" }
---

The unit reviewed how standards and frameworks shape risk assessment, including ISO 31000 (Barafort, Mesquida and Mas, 2019), and asked how to select frameworks for different industries using Kirvan's (2021) overview and an enterprise risk management perspective (Adhillah *et al.*, 2025).

### What the unit set out to teach

On completing the unit I should be able to:

- List common security standards and select the appropriate one(s) for a given situation.
- Describe how to allow for standards in typical threat models.

## Artefact: Module Wiki entry on security frameworks

The wiki activity asked which frameworks suit an international bank, a large hospital and a large food manufacturer, and what tests and recommendations I would give each. My entry is reproduced below.

<div class="artefact" markdown="1">
<p class="artefact-meta">Posted to the Module Wiki, Unit 5</p>


#### Introduction

Cybersecurity frameworks provide structured approaches for identifying, assessing and managing information-security risks. However, different organisations face different threats, regulatory requirements and operational consequences. Kirvan (2021) reviews several established security frameworks and standards, demonstrating that they serve different governance, risk-management, compliance and technical purposes. Adhillah et al. (2025), from an Enterprise Risk Management (ERM) perspective, further demonstrate the importance of considering organisational risks holistically. Therefore, cybersecurity should not be treated solely as an IT issue because cyber incidents can create financial, operational, regulatory, safety and reputational consequences.

#### 1. International Bank

For an international bank, I would recommend ISO/IEC 27001, NIST Cybersecurity Framework (NIST CSF), COBIT and PCI DSS.

ISO/IEC 27001 provides a risk-based Information Security Management System (ISMS), making it appropriate for protecting sensitive financial and personal information. NIST CSF provides a broader structure for governing, identifying, protecting, detecting, responding to and recovering from cybersecurity risks. COBIT can strengthen IT governance and management accountability, while PCI DSS is particularly relevant where payment-card information is processed.

This combination reflects Kirvan's (2021) argument that frameworks have different purposes and can therefore complement each other. From the ERM perspective considered by Adhillah et al. (2025), cyber risk within a bank must also be connected to financial, operational, regulatory and reputational risks.

**Tests and recommendations**

The bank should undertake regular vulnerability assessments and penetration testing of online banking systems, mobile applications, APIs and internal networks. Multi-factor authentication, privileged-access management and encryption should also be tested.

Phishing simulations, social-engineering assessments and red-team exercises should evaluate human and organisational vulnerabilities. Incident-response exercises should simulate ransomware, data breaches and payment-system attacks, while disaster-recovery testing should determine whether essential banking services can be restored effectively.

Third-party suppliers, cloud providers and payment processors should also undergo security assessments. Management should integrate cybersecurity findings into its wider enterprise risk register and governance arrangements.

#### 2. Large Hospital

For a large hospital, I would recommend ISO/IEC 27001 and NIST CSF, supplemented by relevant healthcare-specific security and regulatory requirements.

Hospitals process highly sensitive patient information while operating electronic health records, medical devices, cloud systems and interconnected clinical networks. ISO/IEC 27001 would provide systematic information-security management, while NIST CSF would strengthen prevention, detection, response and recovery capabilities.

The ERM perspective of Adhillah et al. (2025) is particularly important because a hospital cyberattack can develop beyond an information-security incident. For example, ransomware could make patient records unavailable, interrupt treatment and potentially affect patient safety. Cybersecurity should therefore be integrated with clinical, operational and organisational risk management.

**Tests and recommendations**

The hospital should regularly assess servers, electronic patient-record systems, wireless networks, medical devices and external services for vulnerabilities. Penetration testing should examine patient portals, web applications and remote-access infrastructure.

Network-segmentation testing should establish whether compromise of an administrative computer could allow an attacker to access clinical systems. Medical devices should be checked for unsupported software, default credentials and insecure configurations.

Staff should receive regular cybersecurity awareness training supported by phishing simulations. Ransomware exercises, incident-response simulations and backup-restoration testing should also be conducted.

However, testing of live medical equipment should be carefully controlled because intrusive cybersecurity testing could itself create patient-safety risks.

#### 3. Large Food Manufacturing Factory

For a large food manufacturing factory, I would recommend NIST CSF, ISO/IEC 27001 and CIS Critical Security Controls, supplemented by appropriate Industrial Control System (ICS) and Operational Technology (OT) security guidance.

Modern factories increasingly connect conventional IT systems with SCADA systems, programmable logic controllers, sensors and automated production equipment. Kirvan (2021) supports the selection of frameworks according to organisational requirements, making the flexibility of NIST CSF particularly useful within this mixed IT/OT environment.

From the ERM perspective identified by Adhillah et al. (2025), an attack against industrial systems could create consequences beyond cybersecurity, including production downtime, financial losses, supply-chain disruption and potentially food-safety concerns.

**Tests and recommendations**

The organisation should first maintain comprehensive inventories of its IT and OT assets. Vulnerability assessments should identify unsupported systems, unpatched vulnerabilities, default passwords and insecure configurations.

A major priority should be IT/OT network-segmentation testing. The organisation should determine whether compromise of the corporate network could provide attackers with access to production systems.

Remote access provided to engineers, equipment suppliers and maintenance contractors should use multi-factor authentication and least-privilege access. Backup testing should include PLC configurations and other information necessary for restoring production.

Incident-response exercises should simulate ransomware and industrial-system compromise. However, aggressive penetration testing against live industrial systems should be avoided where it could disrupt production. Intrusive testing should instead be conducted within controlled or replicated environments where appropriate.

#### Conclusion

The three organisations demonstrate why cybersecurity frameworks should be selected according to organisational risk rather than simply adopted for compliance purposes. Kirvan (2021) demonstrates that security frameworks and standards have different purposes; consequently, organisations may benefit from combining complementary frameworks.

Adhillah et al. (2025) add an important ERM perspective. Cybersecurity risks are interconnected with wider organisational risks. A cyberattack against a bank can become a financial and regulatory crisis; an attack against a hospital can affect clinical services and patient safety; and an attack against a factory can interrupt production and supply chains.

Therefore, framework compliance should not be confused with cybersecurity effectiveness. Organisations should continuously test their controls through vulnerability assessments, penetration testing, security monitoring, staff awareness exercises, incident-response simulations and recovery testing. Cybersecurity findings should ultimately inform enterprise-level risk-management and strategic decision-making.

#### References

Adhillah, M.N. *et al.* (2025) ‘Systematic Literature Review the Development of Enterprise Risk Management’, *Jurnal Manajemen Bisnis, Akuntansi dan Keuangan*, 4(1), pp. 81–100.

Kirvan, P. (2021) *Top 15 IT security frameworks and standards explained*.

International Organization for Standardization (ISO) (2022) *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. Geneva: ISO.

National Institute of Standards and Technology (NIST) (2024) *The NIST Cybersecurity Framework (CSF) 2.0*. Gaithersburg, MD: NIST.

</div>



## Learning note

The exercise confirmed something I see in compliance work: organisations tend to adopt a framework because a regulator or client expects it, not because it fits their risk. Writing the hospital and factory sections made me add a caution I would not have written a few years ago, that intrusive testing of live medical devices or industrial controllers can itself become a safety risk.
