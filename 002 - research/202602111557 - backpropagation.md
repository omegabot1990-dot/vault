---
tags:
- math
aliases:
- Backpropagation
- Back propagation
title: backpropagation
description: ''
bot: true
parent nodes:
- '[[math]]'
published on: null
---

- Backpropagation computes gradients of a loss with respect to model parameters by applying the chain rule from output layer to input layer
- It reuses intermediate forward-pass values to efficiently compute all partial derivatives

> [!MATH] Chain rule form
> For a composition $L(f(g(x)))$:
> $$\frac{\partial L}{\partial x}=\frac{\partial L}{\partial f}\cdot\frac{\partial f}{\partial g}\cdot\frac{\partial g}{\partial x}$$

- In layered networks, gradients are propagated backward one layer at a time

> [!MATH] Affine layer gradients
> For $z=Wx+b$ and upstream gradient $\delta=\frac{\partial L}{\partial z}$:
> $$\frac{\partial L}{\partial W}=\delta x^\top,\qquad \frac{\partial L}{\partial b}=\delta,\qquad \frac{\partial L}{\partial x}=W^\top\delta$$

- Backpropagation enables gradient-based optimization methods like SGD and Adam
- Automatic differentiation systems implement backpropagation on computational graphs