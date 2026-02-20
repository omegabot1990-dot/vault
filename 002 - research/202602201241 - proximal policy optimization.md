---
tags:
  - reinforcement_learning
aliases:
  - Proximal Policy Optimization
  - PPO
title: proximal policy optimization
description: ""
bot: false
parent nodes:
  - "[[202602200129 - policy gradient methods|Policy Gradient Methods]]"
published on:
---

- Proximal Policy Optimization is an on-policy [[202602200129 - policy gradient methods|policy-gradient method]] designed for stable [[202602192245 - policy|policy]] updates
- <mark style="background: #BBFABBA6;">PPO constrains policy change between updates using a clipped objective on probability ratios</mark>
- It balances sample efficiency and stability without the complexity of full trust-region optimization
- PPO typically uses actor-critic architecture with advantage estimates for gradient weighting
- [[202602111625 - batch size|Mini-batch]] [[202602111623 - epochs|epochs]] over collected trajectories improve data utilisation per rollout
- PPO is widely used in robotics, control benchmarks, and [[202602191524 - large language model|Large Language Model (LLM)]] [[202602191644 - post-training|post-training]] pipelines