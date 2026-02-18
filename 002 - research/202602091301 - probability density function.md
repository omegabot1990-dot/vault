---
tags:
  - math
aliases:
  - Probability Density Function
  - PDF
title: probability density function
description: ""
parent nodes:
  - "[[202602072325 - distribution|Distribution]]"
published on:
---

- The Probability Density Function (PDF) is used for <mark style="background: #ADCCFFA6;">continuous data</mark> (like height)
- It gives the "density" or [[202602061241 - likelihood|likelihood]] rather than the exact [[202602062040 - probability|probability]]
- For a continuous random variable $X$, the probability of $X$ falling between $a$ and $b$ is the <mark style="background: #FF5582A6;">area under the curve</mark>:

> [!MATH] Probability Density Function
> $$P(a \le X \le b) = \int_{a}^{b} f(x) \, dx$$

- Properties
	- <mark style="background: #FFF3A3A6;">Total Area</mark>
		- The entire area under the curve must be exactly 1 [^1]
	- <mark style="background: #D2B3FFA6;">Not a Probability</mark>
		- $f(x)$ can be greater than 1 (unlike a PMF), it represents "density", not "chance"
	- <mark style="background: #FFB86CA6;">Points</mark>
		- $P(X = \text{exactly } 1.75) = 0$, since we only measure intervals


[^1]: https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/random-variables.html#:~:text=It%20turns%20out,(22.6.10)
[^2]: [Probability density and mass functions](https://www.youtube.com/watch?v=hDjcxi9p0ak)