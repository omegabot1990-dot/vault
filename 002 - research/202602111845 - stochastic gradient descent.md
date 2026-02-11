---
tags:
- note
aliases:
- Stochastic Gradient Descent
- SGD
- Stochatic Gradient Descent
title: stochastic gradient descent
description: ''
bot: true
parent nodes:
- '[[optimizer]]'
published on: null
---

- Stochastic gradient descent updates parameters using gradients estimated from sampled data rather than the full dataset
- In practice, mini-batch SGD is commonly used, where each step uses a small batch
- Compared with full-batch gradient descent, SGD reduces per-step compute and enables scalable training
- Gradient noise from sampling can help escape sharp minima and improve generalization
- Core update rule is $\theta_{t+1}=\theta_t-\eta g_t$, where $g_t$ is a stochastic gradient estimate
- Momentum is often added to accelerate convergence and stabilize updates