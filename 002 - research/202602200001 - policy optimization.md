---
tags:
- note
aliases:
- Policy Optimization
title: policy optimization
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Policy optimization updates policy parameters directly to maximize expected return
- It frames reinforcement learning as optimizing $J(\theta)=\mathbb{E}_{\pi_\theta}[G_t]$
- Policy-gradient methods estimate gradients of expected return and apply stochastic optimization
- Trust-region or clipping constraints (e.g., TRPO/PPO-style) improve training stability
- Actor-critic methods combine policy optimization with value estimation for lower-variance updates
- Policy optimization is widely used in robotics, control, and LLM post-training pipelines