---
tags:
  - deep_learning
aliases:
  - Stochastic Gradient Descent
  - SGD
title: stochastic gradient descent
description: ""
bot: false
parent nodes:
  - "[[202602111558 - gradient descent|Gradient Descent]]"
published on:
---

- Stochastic Gradient Descent (SGD) updates [[202602111314 - model parameters|parameters]] using <mark style="background: #BBFABBA6;">gradients estimated from sampled data rather than the full dataset</mark>
	- Unlike Batch [[202602111558 - gradient descent|Gradient Descent]], which computes the gradient using the entire dataset, SGD updates parameters for each training example $x^{(i)}$ and label $y^{(i)}$
- In practice, mini-[[202602111625 - batch size|batch]] SGD is commonly used, where each step uses a small batch
- Compared with full-batch [[202602111558 - gradient descent|gradient descent]], SGD reduces per-step compute and enables scalable [[202602111335 - training|training]]
- Gradient noise from sampling can help escape sharp minima and improve generalisation
- The core update rule is $\theta_{t+1}=\theta_t-\eta g_t$, where $g_t$ is a <mark style="background: #FF5582A6;">stochastic gradient estimate</mark>
- For a single training example $i$, the update rule is:

> [!MATH] Gradient Step
> $$\theta = \theta - \eta \cdot \nabla_{\theta} J(\theta; x^{(i)}, y^{(i)})$$
> 
Where:
> - $\theta$: The model parameters ([[202602111358 - weights and biases|weights and biases]])
> - $\eta$: The [[202602111600 - learning rate|learning rate]] (step size)
> - $\nabla_{\theta} J$: The gradient of the loss function with respect to the parameters

- In practice, we use a "Mini-[[202602111625 - batch size|Batch]]" of size $n$ to balance efficiency and stability:

> [!MATH] Mini-Batch SGD
> $$\theta = \theta - \eta \cdot \frac{1}{n} \sum_{i=1}^{n} \nabla_{\theta} J(\theta; x^{(i)}, y^{(i)})$$

- [[202602111851 - momentum|Momentum]] is often added to accelerate convergence and stabilise updates
