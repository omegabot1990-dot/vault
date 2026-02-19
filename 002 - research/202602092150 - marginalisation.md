---
tags:
  - math
aliases:
  - Marginalisation
title: marginalisation
description: ""
parent nodes:
  - "[[202602092343 - law of total probabilities|Law of Total Probabilities]]"
published on:
---

- In probability, marginalising (or "<mark style="background: #FF5582A6;">marginalising out</mark>") a [[202602061340 - random variable|random variable]] means removing it from a [[202602080100 - joint probability|joint probability]] [[202602072325 - distribution|distribution]] to focus on the remaining variables
- To find the [[202602062040 - probability|probability]] of $X$ alone, we sum (or integrate) over all possible values of $Y$

1. Discrete Setting (Summation)

> [!MATH] Marginalising Out $Y$
> 
> $$P(X = x) = \sum_{y} P(X = x, Y = y)$$

2. Continuous Setting (Integration)

> [!MATH] Marginalizing Out $Y$
>  $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy$$
> 

- The Goal
	- <mark style="background: #BBFABBA6;">To eliminate the "nuisance" variable $Y$ from the equation</mark>
