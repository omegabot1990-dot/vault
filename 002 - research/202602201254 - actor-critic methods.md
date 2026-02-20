---
tags:
  - reinforcement_learning
aliases:
  - Actor-Critic Methods
title: actor-critic methods
description: ""
bot: false
parent nodes:
  - "[[202602200129 - policy gradient methods|Policy Gradient Methods]]"
  - "[[202602201255 - value-based methods|Value-Based Methods]]"
published on:
---

- [ ] What is A2C?
- [ ] What is A3C?
- [ ] What is SAC?

---
- Actor-critic methods combine a parameterised [[202602192245 - policy|policy]] (actor) with a [[202602192359 - value estimation|value estimator]] (critic)
- The actor updates policy [[202602111314 - model parameters|parameters]] to improve [[202602061333 - expectation|expected]] [[202602192355 - return|return]] using gradients weighted by critic signals
- The critic learns value targets from transitions to provide lower-[[202602062206 - variance|variance]] learning signals than pure Monte Carlo updates
- This framework bridges [[202602200129 - policy gradient methods|policy-gradient]] and [[202602201255 - value-based methods|value-based]] ideas in a single optimization loop
- Many practical algorithms (A2C, A3C, [[202602201241 - proximal policy optimization|PPO]], SAC variants) are actor-critic or closely related
- Stability depends on [[202602201850 - bias-variance tradeoff|bias-variance trade-offs]] in critic learning and update step sizes