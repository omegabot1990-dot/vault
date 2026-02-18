---
tags:
  - math
aliases:
  - Mutual Information
  - MI
title: mutual information
description: ""
bot: false
parent nodes:
  - "[[202602061530 - self-information|Self-Information]]"
published on:
---

- Mutual information measures how much knowing one [[202602061340 - random variable|random variable]] reduces uncertainty about another
- It is zero if and only if the variables are [[202602100004 - independence|independent]]
- It is <mark style="background: #FFF3A3A6;">always nonnegative and symmetric</mark>
- For joint $p(x,y)$ with marginals $p(x),p(y)$:

> [!MATH] Discrete Mutual Information
> $$I(X;Y)=\sum_{x}\sum_{y} p(x,y)\log\frac{p(x,y)}{p(x)p(y)}$$

> [!MATH] Entropy Form
> $$I(X;Y)=H(X)-H(X\mid Y)=H(Y)-H(Y\mid X)=H(X)+H(Y)-H(X,Y)$$

- Mutual information <mark style="background: #BBFABBA6;">quantifies statistical dependence</mark>, <mark style="background: #FF5582A6;">not causality</mark>
- Larger mutual information implies stronger dependence between variables

- Properties of $I(X; Y)$
1. Non-negativity
	1. Mutual information is always zero or positive

> [!MATH] Non-negativity
> 
> 
> $$I(X; Y) \ge 0$$
> - $I(X; Y) = 0$ if and only if $X$ and $Y$ are **[[202602100004 - independence|independent]]**
> 

2. Symmetry
	1. The information $X$ tells you about $Y$ is the same as $Y$ tells you about $X$

> [!MATH] Symmetry
> $$I(X; Y) = I(Y; X)$$

3. Relation to Entropy
	1. MI is the difference between the total entropy and the conditional entropy

> [!MATH] Relation to Entropy
> $$I(X; Y) = H(X) - H(X|Y)$$
> $$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

4. Self-Information
	1. The mutual information of a variable with itself is its own entropy

> [!MATH] Self-Information
> $$I(X; X) = H(X)$$

5. Data Processing Inequality
	1. If $X \to Y \to Z$ forms a Markov chain, you cannot gain information by processing data

> [!MATH] Data Processing Inequality
> $$I(X; Y) \ge I(X; Z)$$

![MI|700](https://d2l.ai/_images/mutual-information.svg)


[^1]: [Mutual Information, Clearly Explained!!!](https://www.youtube.com/watch?v=eJIp_mgVLwE)