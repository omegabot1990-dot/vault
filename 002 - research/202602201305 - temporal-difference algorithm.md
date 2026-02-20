---
tags:
- note
aliases:
- Temporal-Difference Algorithm
- TD learning
title: temporal-difference algorithm
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Temporal-difference algorithms learn value estimates by bootstrapping from other learned estimates
- They update from incomplete episodes using one-step prediction errors, improving online learning efficiency
- The TD error is commonly written as:
  - $$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$
- TD(0), SARSA, and Q-learning are core temporal-difference methods
- TD methods usually trade lower variance for some bias compared with pure Monte Carlo estimation
- They are foundational for modern value-based and actor-critic reinforcement learning algorithms