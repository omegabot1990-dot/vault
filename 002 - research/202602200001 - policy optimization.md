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

- Policy optimization updates [[202602192245 - policy|policy]] [[202602111314 - model parameters|parameters]] directly to maximise expected [[202602192355 - return|return]]
- It frames [[202602192221 - reinforcement learning|reinforcement learning]] as optimizing: 

> [!MATH] Optimization Objective
>$$J(\theta)=\mathbb{E}_{\pi_\theta}[G_t]$$

- Policy-gradient methods estimate gradients of expected return and apply stochastic optimization
- Trust-region or clipping constraints (e.g., TRPO/PPO-style) improve training stability
- Actor-critic methods combine policy optimization with value estimation for lower-variance updates
- Policy optimization is widely used in robotics, control, and LLM post-training pipelines