---
tags:
- note
aliases:
- Generalized Advantage Estimation
- GAE
title: generalized advantage estimation
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Generalized Advantage Estimation (GAE) computes low-variance policy-gradient advantages by exponentially weighting multi-step TD residuals
- It introduces a bias-variance tradeoff controlled by $\lambda$ between Monte Carlo-like and TD-like estimates
- With value baseline $V$, TD residuals are $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$
- GAE aggregates these residuals as:
  - $$\hat A_t^{\text{GAE}(\gamma,\lambda)} = \sum_{l=0}^{\infty} (\gamma\lambda)^l \delta_{t+l}$$
- It is widely used in actor-critic methods, especially PPO/TRPO-style optimization
- Typical practice tunes $\lambda$ close to 1 for lower bias while retaining variance reduction