---
tags:
  - math
aliases:
  - Probability Density Function
title: probability density function
description:
parent nodes:
  - "[[202602072325 - distribution|Distribution]]"
child nodes:
annotation-target:
published on:
---

- The Probability Density Function (PDF) is used for <mark style="background: #ADCCFFA6;">continuous data</mark> (like height)
- It gives the "density" or [[202602061241 - likelihood|likelihood]] rather than the exact probability
- For a continuous random variable $X$, the probability of $X$ falling between $a$ and $b$ is the <mark style="background: #FF5582A6;">area under the curve</mark>:

> [!MATH] Probability Density Function
> $$P(a \le X \le b) = \int_{a}^{b} f(x) \, dx$$

- Properties
	- <mark style="background: #FFF3A3A6;">Total Area</mark>
		- The entire area under the curve must be exactly 1
	- <mark style="background: #D2B3FFA6;">Not a Probability</mark>
		- $f(x)$ can be greater than 1 (unlike a PMF), it represents "density", not "chance"
	- <mark style="background: #FFB86CA6;">Points</mark>
		- $P(X = \text{exactly } 1.75) = 0$, since we only measure intervals