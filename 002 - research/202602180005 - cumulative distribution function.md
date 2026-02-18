---
tags:
  - math
aliases:
  - Cumulative Distribution Function
  - CDF
title: cumulative distribution function
description: ""
bot: false
parent nodes:
  - "[[202602072325 - distribution|Distribution]]"
published on:
---

- The Cumulative Distribution Function (CDF) gives the [[202602062040 - probability|probability]] that a [[202602061340 - random variable|random variable]] is less than or equal to a value
- It is defined for both discrete and continuous random variables
- A CDF is monotone non-decreasing, right-continuous, and ranges from 0 to 1 [^1]
- For a random variable $X$:

> [!MATH] Cumulative Distribution Function (CDF)
> $$F_X(x)=\Pr(X\le x)$$

- Boundary behaviour [^1]
    - $\lim_{x\to-\infty}F_X(x)=0$
    - $\lim_{x\to\infty}F_X(x)=1$
- If $X$ has density $f_X$, then: (continuous case) [^2]

> [!MATH] Relationship to [[202602091301 - probability density function|PDF]]
> $$F_X(x)=\int_{-\infty}^{x} f_X(t)\,dt, \qquad f_X(x)=\frac{d}{dx}F_X(x)$$

- Probabilities on intervals can be computed by CDF differences

> [!MATH] CDF Intervals
> $$\Pr(a<X\le b)=F_X(b)-F_X(a)$$


[^1]: https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/random-variables.html#:~:text=Let%E2%80%99s%20observe%20a,continuous%20random%20variable.
[^2]: https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/random-variables.html#:~:text=In%20particular%2C%20by,(22.6.12)