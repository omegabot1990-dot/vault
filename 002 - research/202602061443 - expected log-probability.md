---
tags:
  - math
aliases:
  - Expected Log-Probability
title: expected log-probability
description:
parent nodes:
  - "[[probability and statistics]]"
annotation-target:
published on:
---

- If we have a distribution $p(x)$, the expected log-probability represents the average "log-confidence" the distribution assigns to its own samples

> [!MATH] [[202602061333 - expectation|Expected]] Log-Probability
> $$E_{x \sim p} [\log p(x)] = \int p(x) \log p(x) \, dx$$

- You are looking at the <mark style="background: #BBFABBA6;">information content</mark> or <mark style="background: #FF5582A6;">uncertainty inherent in the distribution</mark> $p(x)$ itself
- This is the core of [[202602030238 - cross-entropy loss|Cross-Entropy]]
	- $H(p) = -E_{p}[\log p]$
- Maximising this value (making it less negative) is the goal of reducing <mark style="background: #BBFABBA6;">Uncertainty</mark> or <mark style="background: #BBFABBA6;">Surprise</mark> in a system
