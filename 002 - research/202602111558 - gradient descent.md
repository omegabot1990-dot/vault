---
tags:
- math
aliases:
- Gradient Descent
title: gradient descent
description: ''
bot: true
parent nodes:
- '[[math]]'
published on: null
---

- Gradient descent is an iterative optimization method for minimizing a differentiable objective
- It updates parameters by moving in the negative gradient direction

> [!MATH] Gradient descent update
> For objective $f(\theta)$ and learning rate $\eta>0$:
> $$\theta_{t+1}=\theta_t-\eta\nabla f(\theta_t)$$

- The gradient gives the local steepest ascent direction, so its negative points toward local decrease
- Learning rate controls step size
  - Too large can cause divergence or oscillation
  - Too small can make convergence very slow
- In high dimensions, curvature differences across directions affect convergence speed
- Stochastic gradient descent and mini-batch variants approximate this update with sampled data