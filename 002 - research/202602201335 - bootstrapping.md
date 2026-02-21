---
tags:
  - reinforcement_learning
aliases:
  - Bootstrapping
title: bootstrapping
description: ""
bot: false
parent nodes:
  - "[[202602192221 - reinforcement learning|Reinforcement Learning]]"
published on:
---

- [ ] What is TD(0)?
- [ ] What is SARSA?

---
- <mark style="background: #FF5582A6;">Bootstrapping updates an estimate using other current estimates as targets</mark>
- Instead of waiting for full-[[202602192356 - episode|episode]] [[202602192355 - return|returns]], methods use one-step or multi-step targets from successor states
- [[202602201305 - temporal-difference algorithm|Temporal-difference]] methods (e.g., TD(0), SARSA, [[202602201303 - q-learning|Q-learning]]) rely on bootstrapping
- Bootstrapping often improves sample efficiency and enables [[202602010053 - on-line learning|online learning]]
- It <mark style="background: #BBFABBA6;">introduces bias because targets depend on imperfect learned estimates</mark>
- Practical stability depends on step sizes, target construction, and function approximation choices


[^1]: [Temporal Difference Learning (including Q-Learning) | Reinforcement Learning Part 4](https://www.youtube.com/watch?v=AJiG3ykOxmY&list=PLzvYlJMoZ02Dxtwe-MmH4nOB5jYlMGBjr&index=4)