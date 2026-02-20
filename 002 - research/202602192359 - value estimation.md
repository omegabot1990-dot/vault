---
tags:
  - reinforcement_learning
aliases:
  - Value Estimation
title: value estimation
description: ""
bot: false
parent nodes:
  - "[[202602200020 - value|Value]]"
published on:
---

- [ ] What are Monte Carlo returns?
- [ ] What is dynamic programming?
- [ ] What is bootstrapping?
- [ ] What are Bellman equations?

---
- Value estimation learns [[202602061333 - expectation|expected]] [[202602192355 - return|return]] quantities used to evaluate decisions in [[202602192221 - reinforcement learning|reinforcement learning]]
- Common targets are the [[202602192351 - state|state]]-[[202602200020 - value|value]] $V^\pi(s)$ and [[202602192350 - action|action]]-value $Q^\pi(s,a)$ functions
- Estimates can be obtained by Monte Carlo returns, [[202602201305 - temporal-difference algorithm|temporal-difference]] [[202602201335 - bootstrapping|bootstrapping]], or dynamic programming
- Value estimation reduces long-horizon planning to local updates based on Bellman relations
- Accurate value estimates improve [[202602192245 - policy|policy]] improvement and action selection
- Approximation error, [[202602062206 - variance|variance]], and [[202602072325 - distribution|distribution]] shift can destabilise value learning