---
tags:
  - reinforcement_learning
aliases:
  - Bootstrapping
title: bootstrapping
description: ""
bot: false
parent nodes:
  - "[[202602201305 - temporal-difference algorithm|Temporal-Difference Algorithm]]"
published on:
---

- [ ] What is TD(0)?
- [ ] What is SARSA?

---
- Bootstrapping updates an estimate using other current estimates as targets
- Instead of waiting for full-episode returns, methods use one-step or multi-step targets from successor states
- [[202602201305 - temporal-difference algorithm|Temporal-difference]] methods (e.g., TD(0), SARSA, [[202602201303 - q-learning|Q-learning]]) rely on bootstrapping
- Bootstrapping often improves sample efficiency and enables [[202602010053 - on-line learning|online learning]]
- It <mark style="background: #BBFABBA6;">introduces bias because targets depend on imperfect learned estimates</mark>
- Practical stability depends on step sizes, target construction, and function approximation choices