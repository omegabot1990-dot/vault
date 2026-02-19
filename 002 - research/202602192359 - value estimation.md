---
tags:
  - reinforcement_learning
aliases:
  - Value Estimation
title: value estimation
description: ""
bot: false
parent nodes:
  - "[[202602192221 - reinforcement learning|RL]]"
published on:
---

- Value estimation learns expected return quantities used to evaluate decisions in reinforcement learning
- Common targets are the state-value $V^\pi(s)$ and action-value $Q^\pi(s,a)$ functions
- Estimates can be obtained by Monte Carlo returns, temporal-difference bootstrapping, or dynamic programming
- Value estimation reduces long-horizon planning to local updates based on Bellman relations
- Accurate value estimates improve policy improvement and action selection
- Approximation error, variance, and distribution shift can destabilise value learning