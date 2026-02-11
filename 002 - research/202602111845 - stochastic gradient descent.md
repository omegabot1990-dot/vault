---
tags:
  - deep_learning
aliases:
  - Stochastic Gradient Descent
  - SGD
title: stochastic gradient descent
description: ""
bot: true
parent nodes:
  - "[[202602111558 - gradient descent|Gradient Descent]]"
published on:
---

- Stochastic Gradient Descent (SGD) updates [[202602111314 - model parameters|parameters]] using <mark style="background: #BBFABBA6;">gradients estimated from sampled data rather than the full dataset</mark>
- In practice, mini-[[202602111625 - batch size|batch]] SGD is commonly used, where each step uses a small batch
- Compared with full-batch [[202602111558 - gradient descent|gradient descent]], SGD reduces per-step compute and enables scalable [[202602111335 - training|training]]
- Gradient noise from sampling can help escape sharp minima and improve generalisation
- The core update rule is $\theta_{t+1}=\theta_t-\eta g_t$, where $g_t$ is a <mark style="background: #FF5582A6;">stochastic gradient estimate</mark>
- Momentum is often added to accelerate convergence and stabilise updates