---
tags:
  - reinforcement_learning
aliases:
  - Dynamic Programming
title: dynamic programming
description: ""
bot: false
parent nodes:
  - "[[202602192359 - value estimation|Value Estimation]]"
published on:
---

- Dynamic programming solves sequential decision problems by combining [[202602211420 - bellman equation|Bellman]] policy evaluation and policy improvement
- In [[202602192221 - reinforcement learning|reinforcement learning]], classic dynamic programming assumes a known model of [[202602200013 - transition|transitions]] and [[202602192352 - reward|transitions]]
- Policy evaluation computes [[202602200020 - value|values]] for a fixed policy, and policy improvement updates the policy greedily w.r.t. those values
- Value iteration merges these steps into repeated Bellman optimality updates
- Dynamic programming is foundational but limited in large or unknown environments where exact models are unavailable
- Many [[202602201253 - model-free|model-free]] and approximate RL methods can be viewed as sampled or function-approximate variants of dynamic programming