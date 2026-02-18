---
tags:
- math
aliases:
- Conditional entropy
title: conditional entropy
description: ''
bot: true
parent nodes:
- '[[math]]'
published on: null
---

- Conditional entropy measures the remaining uncertainty in one variable after observing another
- It quantifies average uncertainty of $X$ given $Y$
- Lower conditional entropy means $Y$ is more informative about $X$

> [!MATH] Conditional entropy definition
> For discrete variables:
> $$H(X\mid Y)= -\sum_{x,y} p(x,y)\log p(x\mid y)$$

> [!MATH] Equivalent forms
> $$H(X\mid Y)=H(X,Y)-H(Y)$$
> $$I(X;Y)=H(X)-H(X\mid Y)$$

- Bounds
  - $0\le H(X\mid Y)\le H(X)$
- $H(X\mid Y)=0$ when $X$ is a deterministic function of $Y$