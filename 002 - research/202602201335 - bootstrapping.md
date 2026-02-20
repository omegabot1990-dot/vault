---
tags:
- note
aliases:
- Bootstrapping
title: bootstrapping
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- In reinforcement learning, bootstrapping updates an estimate using other current estimates as targets
- Instead of waiting for full-episode returns, methods use one-step or multi-step targets from successor states
- Temporal-difference methods (e.g., TD(0), SARSA, Q-learning) rely on bootstrapping
- Bootstrapping often improves sample efficiency and enables online learning
- It introduces bias because targets depend on imperfect learned estimates
- Practical stability depends on step sizes, target construction, and function approximation choices