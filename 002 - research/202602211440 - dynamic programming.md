---
tags:
- note
aliases:
- Dynamic Programming
title: dynamic programming
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Dynamic programming solves sequential decision problems by combining Bellman policy evaluation and policy improvement
- In reinforcement learning, classic dynamic programming assumes a known model of transitions and rewards
- Policy evaluation computes values for a fixed policy, and policy improvement updates the policy greedily w.r.t. those values
- Value iteration merges these steps into repeated Bellman optimality updates
- Dynamic programming is foundational but limited in large or unknown environments where exact models are unavailable
- Many model-free and approximate RL methods can be viewed as sampled or function-approximate variants of dynamic programming