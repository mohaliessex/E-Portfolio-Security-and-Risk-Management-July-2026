---
layout: default
title: "Unit 4: Application of threat modelling and management techniques"
kicker: Unit 4 of 12
permalink: /units/unit-04/
lo: [1, 3]
prev: { title: "Unit 3: Threat modelling", url: "/units/unit-03/" }
next: { title: "Unit 5: Security standards", url: "/units/unit-05/" }
---

The unit applied threat modelling using the Threat Model Cookbook, OWASP guidance and MITRE ATT&CK, and asked how to choose the right method for a situation (Shevchenko *et al.*, 2018; Salter *et al.*, 1998). The seminar focused on risk identification and modelling.

### What the unit set out to teach

On completing the unit I should be able to:

- Describe where to find the key tools and resources used for threat modelling.
- Explain how to select the most appropriate tool for various situations.
- Critically evaluate the use of such tools.

## Artefact: a scoped STRIDE threat model for Pampered Pets

The main application of this unit's learning was the threat modelling approach I contributed to the team project, which was being drafted at the time. I argued that STRIDE should be applied only to identities, systems and data flows, because it cannot evaluate food safety, staff capacity or supplier economics, which need qualitative scenarios instead. Kaona then applied this scoping in Section 3 of the report. The resulting threats for the digitalised future state were:

| STRIDE category | Threat to Pampered Pets | Key mitigations |
|---|---|---|
| Tampering | Accidental or unauthorised alteration of stock, product and recall data | Role-based access, dual approval, immutable audit history, supplier reconciliation |
| Spoofing and elevation of privilege | Stolen staff or administrator credentials permit safety-critical changes | MFA, unique accounts, least privilege, privileged-action alerts |
| Denial of service | Ransomware, provider failure or corrupt synchronisation disables ordering and traceability | Independent backups, tested restoration, contractual recovery terms, paper-based degraded mode |
| Information disclosure and repudiation | Customer data exposure and disputes over who did what | Data minimisation, restricted access, deletion periods, auditable transaction records |

The full analysis is in Section 3 of the [team report]({{ '/projects/team-project/' | relative_url }}).


## Seminar: Risk identification and modelling

*21 August 2026.* The seminar presented threat modelling as a design-phase exercise that maps assets, entry points and trust boundaries before applying STRIDE, using a connected office coffee machine as the example. It compared tools (Microsoft Threat Modeling Tool, OWASP Threat Dragon, IriusRisk), pointed to MITRE ATT&CK and D3FEND as resources, and discussed threat modelling for cyber-physical systems, where physical consequences must be modelled alongside data flows (Mazumdar, 2026c).

**How I used it.** Three days later Group 3 agreed its methodology. The cyber-physical discussion reinforced my argument that STRIDE should cover only Pampered Pets' identities, systems and data flows, with food safety and supply risks handled by separate scenarios.

## Learning note

The most useful idea this week was negative: knowing when a method does not fit. Applying STRIDE to every risk in a pet food business would have looked thorough but produced weak analysis. Scoping it honestly, and saying what other method covers the rest, is a judgement I now try to make explicit in professional threat models as well.
