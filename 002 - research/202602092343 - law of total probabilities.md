---
tags:
- math
aliases:
- Law of Total Probabilities
title: law of total probabilities
description: 'Math note: - The Law of Total Probability is the mathematical "bridge"
  that allows you'
parent nodes:
- '[[202602092150 - marginalisation|Marginalisation]]'
published on: null
---

- The <mark style="background: #BBFABBA6;">Law of Total Probability</mark> is the mathematical "bridge" that allows you to calculate the total [[202602062040 - probability|probability]] of an [[202602092352 - event|event]] by breaking it down into several distinct, easier-to-calculate scenarios [^1]

> [!MATH] Law of Total Probability
> If $A_1, A_2, \dots, A_n$ are distinct scenarios that cover all possibilities, the total probability of event $B$ is:
> $$P(B) = \sum_{i=1}^{n} P(B | A_i)P(A_i)$$

-  Key Requirements
	1. <mark style="background: #FF5582A6;">Mutually Exclusive</mark> [^1]
		1. The scenarios ($A_i$) cannot overlap
	2. <mark style="background: #FFF3A3A6;">Collectively Exhaustive</mark> [^1]
		1. The scenarios must cover 100% of the possibilities


[^1]:  [Law of Total Probability: P(A) = ΣP(A|Bi)P(Bi) Explained Simply](https://www.youtube.com/watch?v=ChSamffiS64)