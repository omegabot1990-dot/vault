---
tags:
  - reinforcement_learning
aliases:
  - Value-Based Methods
title: value-based methods
description: ""
bot: false
parent nodes:
  - "[[202602192359 - value estimation|Value Estimation]]"
published on:
---

- [ ] What are Bellman-style targets?
- [ ] What is greedy?
- [ ] What is epsilon-greedy?
- [ ] What is SARSA?
- [ ] What is deep-Q?
- [ ] What is a replay buffer?
- [ ] What is bootstrapping?

---
- Value-based methods learn [[202602200020 - value|value]] functions and derive [[202602192350 - action|action]] choices from those value estimates
- <mark style="background: #BBFABBA6;">They typically optimize action-value functions</mark> such as $Q(s,a)$ using Bellman-style targets
- [[202602192245 - policy|Policies]] are often implicit, e.g., greedy or epsilon-greedy with respect to learned values
- Canonical examples include [[202602201303 - q-learning|Q-learning]], SARSA, and deep Q-network variants
- They can be sample-efficient with replay and bootstrapping, but may suffer from overestimation or instability
- Value-based approaches are especially <mark style="background: #FF5582A6;">common in discrete-action control</mark> settings