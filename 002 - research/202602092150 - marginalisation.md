---
tags:
- math
aliases:
- Marginalisation
title: marginalisation
description: 'Math note: - In probability, marginalising (or "marginalising out")
  a random variable means removing it'
parent nodes:
- '[[202602072325 - distribution|Distribution]]'
published on: null
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
	- To eliminate the "nuisance" variable $Y$ from the equation
