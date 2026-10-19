---
layout: default
title: "Unit 10: Practical applications and issues in DR implementations"
kicker: Unit 10 of 12
permalink: /units/unit-10/
lo: [3, 4]
prev: { title: "Unit 9: BC and DR", url: "/units/unit-09/" }
next: { title: "Unit 11: Future trends", url: "/units/unit-11/" }
---

The unit examined how RPO and RTO values drive DR architecture, the trade-offs of disaster recovery as a service, and vendor lock-in, resilience and network security (Alhazmi and Malaiya, 2013; Kumar, 2024). The seminar asked students to design a solution for given recovery objectives.

### What the unit set out to teach

On completing the unit I should be able to:

- Design a solution that will meet a set of RPO and RTO requirements.
- Describe the advantages and disadvantages of DRaaS.
- Discuss the challenges with vendor lock-in, resilience and (network) security.

## Artefact: two-region DR design for one-minute RTO and RPO

I applied this unit's material in the disaster recovery section of my individual project. The design runs the online shop active-active across two cloud regions behind a global load balancer, keeps a single-writer database that is promoted automatically on failure, and adds immutable cross-account backups because replication copies ransomware damage instantly. Because a four-person business cannot operate this, I recommended a managed service provider bound contractually to both 60-second targets, a quarterly end-to-end failover test against ISO 22301 and NIST SP 800-34, and lock-in controls through containers, infrastructure as code, open-format exports and a tested exit plan.

<figure><img src="{{ '/assets/img/exec-summary-fig2-dr-architecture.png' | relative_url }}" alt="Two-region cloud architecture with an active-active application tier and a single-writer database replicated to a secondary region."><figcaption>Proposed two-region architecture, from Section 5 of the individual project.</figcaption></figure>

[Read the full DR section in the individual project]({{ '/projects/individual-project/' | relative_url }})


## Seminar: DR solutions design and review

*2 October 2026.* The seminar explained how recovery time and recovery point objectives drive DR design, set out a tier matrix running from mission-critical active-active systems with automated failover to non-critical systems rebuilt from scratch, and compared cold, warm, hot and active-active standby (Mazumdar, 2026f).

**How I used it.** Pampered Pets' one-minute objectives placed its online shop in the mission-critical tier, which is why my design uses an active-active application tier and automated database promotion, and why I flagged that a four-person firm needs a managed provider to run it.

## Learning note

The key insight was that a vendor's recovery figure covers one component, not the service. Aurora's sub-minute promotion says nothing about detection, traffic shift or application reconnection, so I defined a pass condition for the whole chain. This is a point I now raise when reviewing vendors' resilience claims at work.
