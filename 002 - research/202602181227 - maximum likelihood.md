---
tags:
- math
aliases:
- Maximum Likelihood
- MLE
title: maximum likelihood
description: ''
bot: true
parent nodes:
- '[[math]]'
published on: null
---

- Maximum likelihood estimates model parameters by maximizing the probability of observed data under the model
- For i.i.d. data, likelihood is the product of per-sample probabilities or densities
- In practice, optimization is usually done on log-likelihood for numerical stability and simpler gradients

> [!MATH] Likelihood and MLE
> For data $x_{1:n}$ and parameter $\theta$:
> $$L(\theta\mid x_{1:n})=\prod_{i=1}^{n} p(x_i\mid\theta),\qquad \hat\theta_{\mathrm{MLE}}=\arg\max_{\theta} L(\theta\mid x_{1:n})$$

> [!MATH] Log-likelihood form
> $$\ell(\theta)=\log L(\theta\mid x_{1:n})=\sum_{i=1}^{n}\log p(x_i\mid\theta),\qquad \hat\theta_{\mathrm{MLE}}=\arg\max_{\theta}\ell(\theta)$$

- Many common training objectives are negative log-likelihood minimization