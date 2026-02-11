---
tags:
  - deep_learning
aliases:
  - Optimization Algorithms
title: optimization algorithms
description: ""
bot: true
parent nodes:
  - "[[optimizer]]"
published on:
---

- [ ] What is SGD?
- [ ] What is Momentum SGD?
- [ ] What is RMSProp?
- [ ] What is Adam?
- [ ] What is AdamW?

---
- Optimization algorithms are methods that update [[202602111314 - model parameters|model parameters]] to minimise an [[202602010047 - objective function|objective function]]
- They use [[202602111558 - gradient descent|gradients]] and update rules to control step direction, scale, and stability
- Core families are first-order methods, such as:
	- Stochastic Gradient Descent (SGD)
	- Momentum SGD
	- RMSProp
	- Adam
	- AdamW
- Different optimizers trade off <mark style="background: #BBFABBA6;">convergence speed</mark>, <mark style="background: #FF5582A6;">memory cost</mark>, and <mark style="background: #FFF3A3A6;">generalisation</mark> behaviour
- Hyperparameters like learning rate and weight decay strongly influence optimizer performance
- In deep learning, mini-batch training is typically combined with an optimizer and a learning-rate schedule