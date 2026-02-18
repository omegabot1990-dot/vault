---
tags:
  - math
aliases:
  - Conditional Entropy
title: conditional entropy
description: ""
bot: false
parent nodes:
  - "[[202602181530 - joint entropy|Joint Entropy]]"
published on:
---

- Conditional [[202602061804 - entropy|entropy]] measures the remaining uncertainty in one variable after observing another
- It quantifies the average uncertainty of $X$ given $Y$
- Lower conditional entropy means $Y$ is more informative about $X$
- For discrete variables:

> [!MATH] Conditional Entropy 
> $$H(X\mid Y)= -\sum_{x,y} p(x,y)\log p(x\mid y)$$

> [!MATH] Equivalent Forms
> $$H(X\mid Y)=H(X,Y)-H(Y)$$
> $$I(X;Y)=H(X)-H(X\mid Y)$$

- Bounds
	- $0\le H(X\mid Y)\le H(X)$
- $H(X\mid Y)=0$ when $X$ is a deterministic function of $Y$