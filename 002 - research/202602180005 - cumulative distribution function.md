---
tags:
- math
aliases:
- Cumulative Distribution Function
- CDF
title: cumulative distribution function
description: ''
bot: true
parent nodes:
- '[[math]]'
published on: null
---

- The cumulative distribution function (CDF) gives the probability that a random variable is less than or equal to a value
- It is defined for both discrete and continuous random variables
- A CDF is monotone non-decreasing, right-continuous, and ranges from 0 to 1

> [!MATH] CDF definition
> For random variable $X$:
> $$F_X(x)=\Pr(X\le x)$$

- Boundary behavior
  - $\lim_{x\to-\infty}F_X(x)=0$
  - $\lim_{x\to\infty}F_X(x)=1$

> [!MATH] Relationship to PDF (continuous case)
> If $X$ has density $f_X$, then
> $$F_X(x)=\int_{-\infty}^{x} f_X(t)\,dt, \qquad f_X(x)=\frac{d}{dx}F_X(x)$$

- Probabilities on intervals can be computed by CDF differences
  - $$\Pr(a<X\le b)=F_X(b)-F_X(a)$$