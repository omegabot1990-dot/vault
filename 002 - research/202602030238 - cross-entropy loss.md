---
tags:
- note
aliases:
- Cross-Entropy Loss
title: cross-entropy loss
description: Concise concept note on cross-entropy loss.
parent nodes:
- '[[loss]]'
published on: null
---

- Minimise the divergence between the true distribution $p$ and predicted distribution $q$
- Measures the difference between two probability distributions [^1]
- <mark style="background: #BBFABBA6;">Binary cross-entropy</mark> is used for two classes (binary)

> [!MATH] Binary Cross-Entropy Loss
> $$L = -\frac{1}{N} \sum_{i=1}^{N} [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)]$$

- <mark style="background: #BBFABBA6;">Categorical cross-entropy</mark> is used for more than two <mark style="background: #ADCCFFA6;">mutually exclusive classes</mark> (multi-class)
	- Usually paired with the `softmax` activation function
- <mark style="background: #FF5582A6;">Minimising Cross-Entropy Loss</mark> is mathematically equivalent to <mark style="background: #FF5582A6;">maximising</mark> [[202602061241 - likelihood|Log-Likelihood]] or <mark style="background: #FF5582A6;">minimising Negative</mark> [[202602061241 - likelihood|Log-Likelihood]] 

> [!MATH] Categorical Cross-Entropy Loss or Negative Log-Likelihood
> $$L(\theta) = -\sum_{i=1}^{n} y_i \log(\hat{y}_i)$$

- Also called <mark style="background: #FF5582A6;">log loss</mark>
- Negative average log probability of the target token [^2]
- Primary objective function used to train <mark style="background: #BBFABBA6;">classification models</mark>


