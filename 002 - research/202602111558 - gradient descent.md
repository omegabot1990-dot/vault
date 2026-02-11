---
tags:
  - math
aliases:
  - Gradient Descent
title: gradient descent
description: ""
bot: false
parent nodes:
  - "[[202602111605 - optimization algorithms|Optimization Algorithms]]"
published on:
---

- Gradient descent is an iterative [[202602111605 - optimization algorithms|optimization]] method for minimising a differentiable [[202602010047 - objective function|objective]]
- It updates [[202602111314 - model parameters|parameters]] by moving in the negative gradient direction
- For objective $f(\theta)$ and [[202602111600 - learning rate|learning rate]] $\eta>0$:

> [!MATH] Gradient descent update
> $$\theta_{t+1}=\theta_t-\eta\nabla f(\theta_t)$$

- The gradient gives the <mark style="background: #BBFABBA6;">local steepest ascent direction</mark>, so its negative points toward local decrease
- Learning rate controls step size,
    - Too large can cause divergence or oscillation
    - Too small can make convergence very slow
- In high dimensions, curvature differences across directions affect convergence speed
- Stochastic gradient descent and mini-[[202602111625 - batch size|batch]] variants approximate this update with sampled data


[^1]: 