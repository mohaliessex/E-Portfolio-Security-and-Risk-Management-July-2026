---
layout: default
title: "Unit 12: The great debate: the most influential trend in SRM"
kicker: Unit 12 of 12
permalink: /units/unit-12/
lo: [1, 2, 4]
prev: { title: "Unit 11: Future trends", url: "/units/unit-11/" }
next: { title: "Collaborative Discussion 1", url: "/discussions/discussion-1/" }
---

The final unit was a debate on which trend will most influence security and risk management over the next five years, drawing on the Unit 11 readings, the Module Wiki, Marks (2019) and Nicol *et al.* (2012).

### What the unit set out to teach

On completing the unit I should be able to:

- Describe the main emerging trends in the field.
- Argue for which you believe to be the most influential.
- Cast your vote for the trend you support.

## Artefact: my position in the debate

**The motion.** Which trend will be the most influential in security and risk management over the next five years?

**My position: securing and governing AI.** I argue that the security and governance of machine learning, covering adversarial ML and trustworthy AI, will influence the field more than any other trend.

1. **AI adds an attack surface that existing methods do not cover.** Organisations are adopting AI faster than they can assess it, and each model brings risks such as poisoning, evasion and data extraction (Vassilev *et al.*, 2024). Adversarial ML applies vulnerability assessment at the level of the algorithm, which the scanners and threat models most teams use today were not built for.
2. **AI changes who makes risk decisions.** Autonomous defence agents that isolate or patch systems (Ridley, McCloskey and Mountain, 2018) move decisions from analysts to software. Deciding who is accountable when an agent takes a production system offline is an enterprise governance question, not only a technical one.
3. **AI amplifies the failure modes this module kept exposing.** Discussion 1 showed an algorithm's silence being mistaken for the absence of harm; Discussion 2 showed scores trusted beyond the evidence behind them. Trustworthy AI is, at its core, the discipline of asking how strong the knowledge behind an output is, which is Aven and Thekdi's (2025) central point about risk.

**The strongest counter-argument.** ERM supporters argue that AI risk is simply another enterprise risk, and that treating it as a separate trend recreates the silos ERM was designed to remove (Fraser and Simkins, 2016). I accept the premise: ERM is the vehicle through which AI risk should be governed. But a vehicle is not a trend. Over the next five years, the content of risk registers will change more because of AI than because of any change in how registers are run. A second counter-argument, from the NSA hard problems, is that human behaviour remains the decisive factor (Nicol *et al.*, 2012). That is true, but AI is now one of the main ways human behaviour is both exploited, through convincing phishing, and supported, through recommender systems.

**My vote.** Securing and governing AI.

**Why this matters to me professionally.** Reviewing AI tools and new AI use cases has become a growing part of my security role, and the questions in this debate (what the model can be made to do, what data it sees, who is accountable for its actions) are the questions those reviews now ask.

## Seminar: The great debate

The final seminar split the cohort into opposing teams to argue for different trends, drawing on the Unit 11 readings and the Module Wiki, before a vote on the most influential trend.

## Learning note

Preparing for the debate forced me to separate what I find interesting from what I can defend with evidence. My first instinct was to argue for autonomous cyber defence, but the stronger case was the one underneath it: none of these applications is safe to deploy unless the models themselves can be trusted, assessed and governed.
