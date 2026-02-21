---
tags:
- note
aliases:
- The Bellman Equation
- Bellman equation
title: the bellman equation
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- The Bellman equation expresses recursive consistency of value functions under a policy or optimal control
- For policy evaluation, state values satisfy:
  - $$V^\pi(s)=\mathbb{E}_{a\sim\pi,\,s'\sim P}\left[r(s,a,s') + \gamma V^\pi(s')\right]$$
- For optimal control, the Bellman optimality equation is:
  - $$V^*(s)=\max_a\mathbb{E}_{s'\sim P}\left[r(s,a,s') + \gamma V^*(s')\right]$$
- Equivalent action-value forms define targets used by Q-learning and other value-based methods
- Dynamic programming and temporal-difference algorithms rely directly on Bellman updates
- The equation is foundational because it turns long-horizon return optimization into local recursive updates