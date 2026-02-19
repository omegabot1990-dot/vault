---
tags:
  - reinforcement_learning
aliases:
  - Policy Optimization
title: policy optimization
description: ""
bot: false
parent nodes:
  - "[[202602192245 - policy|Policy]]"
published on:
---

- Policy optimization updates [[202602192245 - policy|policy]] [[202602111314 - model parameters|parameters]] directly to maximise expected [[202602192355 - return|return]]
- It frames [[202602192221 - reinforcement learning|reinforcement learning]] as optimizing: 

> [!MATH] Optimization Objective
>$$J(\theta)=\mathbb{E}_{\pi_\theta}[G_t]$$

- Policy-gradient methods estimate gradients of expected return and apply [[202512271205 - stochastic|stochastic]] optimization
- Trust-region or clipping constraints (e.g., TRPO/PPO-style) improve training stability
- Actor-critic methods combine policy optimization with value estimation for lower-variance updates
- Policy optimization is widely used in robotics, control, and [[202602191524 - large language model|Large Language Model (LLM)]] [[202602191644 - post-training|post-training]] pipelines