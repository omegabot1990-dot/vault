---
tags:
  - deep_learning
aliases:
  - Backpropagation
  - Back propagation
title: backpropagation
description: ""
bot: true
parent nodes:
  - "[[202602061153 - neural network|Neural Network]]"
published on:
---

- [ ] What is Adam?

---
- Backpropagation computes gradients of a [[202602010047 - objective function|loss]] with respect to [[202602111314 - model parameters|Model Parameters]] by <mark style="background: #BBFABBA6;">applying the chain rule from the output layer to the input layer</mark>
- It reuses intermediate forward-pass values to efficiently compute all partial derivatives
- For a composition $L(f(g(x)))$:

> [!MATH] Chain Rule Form
> $$\frac{\partial L}{\partial x}=\frac{\partial L}{\partial f}\cdot\frac{\partial f}{\partial g}\cdot\frac{\partial g}{\partial x}$$

- In layered networks, gradients are propagated backward one layer at a time
- For $z=Wx+b$ and upstream gradient $\delta=\frac{\partial L}{\partial z}$:

> [!MATH] Affine Layer Gradients
> $$\frac{\partial L}{\partial W}=\delta x^\top,\qquad \frac{\partial L}{\partial b}=\delta,\qquad \frac{\partial L}{\partial x}=W^\top\delta$$

- Backpropagation enables [[202602111558 - gradient descent|gradient-based]] optimisation methods like,
	- [[202602111845 - stochastic gradient descent|Stochastic Gradient Descent (SGD)]]
	- Adam
- Automatic differentiation systems implement backpropagation on computational graphs


[^1]: [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=3&t=1s)