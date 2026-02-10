---
tags:
  - math
aliases:
  - Independent and Identically Distributed
title: independent and identically distributed
description:
parent nodes:
  - "[[202602072325 - distribution|Distribution]]"
annotation-target:
published on:
---

- If your data is [[202602100004 - independence|Independent]] and Identically Distributed, it means every observation comes from the exact same source and doesn't influence the others
- A collection of random variables $X_1, X_2, \dots, X_n$ is <mark style="background: #BBFABBA6;">IID</mark> if:

> [!MATH] Independent and Identically Distributed Random Variables
> - <mark style="background: #FF5582A6;">Independent</mark>
> 	- The [[202602080100 - joint probability|joint probability]] is the product of individual probabilities:
>    $$P(X_1, X_2, \dots, X_n) = \prod_{i=1}^{n} P(X_i)$$
> 
> - <mark style="background: #D2B3FFA6;">Identically Distributed</mark>
> 	- Every $X_i$ has the exact same [[202602072325 - distribution|probability distribution]] ($F$):
>    $$X_i \sim F \quad \text{for all } i$$
