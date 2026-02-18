---
tags:
- math
aliases:
- Mutual information
- MI
title: mutual information
description: ''
bot: true
parent nodes:
- '[[math]]'
published on: null
---

- Mutual information measures how much knowing one random variable reduces uncertainty about another
- It is zero iff the variables are independent
- It is always nonnegative and symmetric

> [!MATH] Discrete mutual information
> For joint $p(x,y)$ with marginals $p(x),p(y)$:
> $$I(X;Y)=\sum_{x,y} p(x,y)\log\frac{p(x,y)}{p(x)p(y)}$$

> [!MATH] Entropy form
> $$I(X;Y)=H(X)-H(X\mid Y)=H(Y)-H(Y\mid X)=H(X)+H(Y)-H(X,Y)$$

- Mutual information quantifies statistical dependence, not causality
- Larger mutual information implies stronger dependence between variables