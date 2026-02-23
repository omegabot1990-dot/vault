---
tags:
- note
aliases:
- Model-Based Rewards
title: model-based rewards
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Model-based rewards are reward signals produced by a learned model rather than fixed hand-written rules
- The reward model predicts preference or task quality from trajectory snippets, actions, or generated outputs
- This enables optimization in tasks where explicit verifiers are unavailable or too expensive
- Reward quality depends on labeling data, model calibration, and robustness to distribution shift
- Learned rewards can be exploited by policies, so regular auditing and adversarial evaluation are important
- Practical systems often combine model-based rewards with rule-based checks to improve reliability