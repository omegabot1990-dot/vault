---
tags:
- note
aliases:
- Trust Region Policy Optimization
- TRPO
title: trust region policy optimization
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Trust Region Policy Optimization (TRPO) is a policy-gradient method designed to make stable monotonic policy improvements
- It constrains each policy update to stay within a trust region measured by KL divergence from the previous policy
- The optimization is commonly formulated as a constrained objective with a surrogate advantage-based gain
- This reduces destructive large policy steps that can collapse performance
- TRPO is often more stable than unconstrained policy gradients but computationally heavier than PPO
- It is foundational for later clipped-objective methods such as PPO