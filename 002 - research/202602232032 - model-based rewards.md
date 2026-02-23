---
tags:
  - reinforcement_learning
aliases:
  - Model-Based Rewards
title: model-based rewards
description: ""
bot: false
parent nodes:
  - "[[202602192352 - reward|Reward]]"
published on:
---

- Model-based rewards are reward signals produced by a [[202602201334 - reward model|learned model]] rather than fixed hand-written rules
- The reward model predicts preference or task quality from trajectory snippets, actions, or generated outputs
- This enables optimization in tasks where explicit verifiers are unavailable or too expensive
- Reward quality depends on labelling data, model calibration, and robustness to [[202602072325 - distribution|distribution]] shift
- Learned rewards can be exploited by [[202602192245 - policy|policies]], so regular auditing and adversarial evaluation are important
- Practical systems often combine model-based rewards with [[202602232031 - rule-based rewards|rule-based]] checks to improve reliability