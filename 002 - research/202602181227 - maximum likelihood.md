---
tags:
  - math
aliases:
  - Maximum Likelihood
  - MLE
title: maximum likelihood
description: ""
bot: false
parent nodes:
  - "[[202602061241 - likelihood]]"
published on:
---

- Maximum [[202602061241 - likelihood|likelihood]] estimates [[202602111314 - model parameters|model parameters]] by maximising the [[202602062040 - probability|probability]] of observed data under the model
- For [[202602092108 - independent and identically distributed|Independent and Identically Distributed]] data, the likelihood is the product of per-sample probabilities or densities
- In practice, optimisation is usually done on the [[202602061424 - log-likelihood|log-likelihood]] for numerical stability and simpler gradients
- For data $x_{1:n}$ and parameter $\theta$:

> [!MATH] Likelihood and MLE
> $$L(\theta\mid x_{1:n})=\prod_{i=1}^{n} p(x_i\mid\theta),\qquad \hat\theta_{\mathrm{MLE}}=\arg\max_{\theta} L(\theta\mid x_{1:n})$$

> [!MATH] Log-likelihood 
> $$\ell(\theta)=\log L(\theta\mid x_{1:n})=\sum_{i=1}^{n}\log p(x_i\mid\theta),\qquad \hat\theta_{\mathrm{MLE}}=\arg\max_{\theta}\ell(\theta)$$

- Many common training objectives are negative log-likelihood minimisation


[^1]: [Maximum Likelihood, clearly explained!!!](https://www.youtube.com/watch?v=XepXtl9YKwc)
[^2]: [Maximum Likelihood For the Normal Distribution, step-by-step!!!](https://www.youtube.com/watch?v=Dn6b9fCIUpM)
[^3]: https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/maximum-likelihood.html#the-maximum-likelihood-principle:~:text=Thus%20we%20see,(22.7.3)