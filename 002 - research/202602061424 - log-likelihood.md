---
tags:
- math
aliases:
- Log-Likelihood
title: log-likelihood
description: ''
parent nodes:
- '[[202602061241 - likelihood]]'
published on: null
---

- Log-likelihood converts the calculation from <mark style="background: #FF5582A6;">Product to Sum</mark>

> [!MATH] Log-Likelihood
> If Likelihood $L(\theta)$ is the product of probabilities:
> $$L(\theta) = \prod_{i=1}^{n} P(x_i | \theta)$$
> 
> Then Log-Likelihood $\ell(\theta)$ is the sum of their logs:
> $$\ell(\theta) = \sum_{i=1}^{n} \log P(x_i | \theta)$$

- No More Underflow
	- Multiplying 1,000 tiny probabilities results in a number so small a computer thinks it is zero
	- Adding the logs of those numbers avoids this entirely
- Gradient Friendly
	- When training a model via [[202602061429 - stochastic gradient descent|Stochastic Gradient Descent]], taking the derivative of a sum is much simpler than the derivative of a complex product (thanks to the Sum Rule in calculus)
- Maximum stays the same
	- Because $log(x)$ always goes up as $x$ goes up, the peak of the mountain is in the same place
	- Finding the best "Log-Likelihood" gives you the exact same result as finding the best "Likelihood.