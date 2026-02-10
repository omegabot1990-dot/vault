---
tags:
- math
aliases:
- Expected Log-Likelihood
title: expected log-likelihood
description: ''
parent nodes:
- '[[202602061424 - log-likelihood]]'
published on: null
---

- If we have a true distribution $p(x)$ and a model distribution $q(x|\theta)$, the expected log-likelihood is written as,

> [!MATH] [[202602061333 - expectation|Expected]] Log-Likelihood
> $$E_{x \sim p} [\log q(x|\theta)] = \int p(x) \log q(x|\theta) \, dx$$

- You are looking at how well your <mark style="background: #FF5582A6;">model parameters</mark> $\theta$, <mark style="background: #BBFABBA6;">fit that data</mark>
- This is the core of [[202602030238 - cross-entropy loss|Cross-Entropy]]
	- $H(p, q) = -E_{p}[\log q]$
- Maximising this expectation is the goal of most probabilistic models 
