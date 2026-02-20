---
tags:
- note
aliases:
- Value-Based Methods
title: value-based methods
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Value-based methods learn value functions and derive action choices from those value estimates
- They typically optimize action-value functions such as $Q(s,a)$ using Bellman-style targets
- Policies are often implicit, e.g., greedy or epsilon-greedy with respect to learned values
- Canonical examples include Q-learning, SARSA, and deep Q-network variants
- They can be sample-efficient with replay and bootstrapping but may suffer from overestimation or instability
- Value-based approaches are especially common in discrete-action control settings