---
tags:
- math
aliases:
- Joint Probability
title: joint probability
description: ''
parent nodes:
- '[[202602062040 - probability|Probability]]'
published on: null
---

- <mark style="background: #FF5582A6;">Joint Probability</mark> is the probability of two or more independent events happening at the same time 
	- Returns the probability assigned to the intersection of the corresponding subsets of the [[202602061346 - sample space|sample space]] [^1]
- For two events $A$ and $B$, the joint probability is written as $P(A \cap B)$ or $P(A, B)$
- The probability that both events $A$ <mark style="background: #FF5582A6;">AND</mark> $B$ occur is:

> [!MATH] Joint Probability $P(A \cap B)$
> 
> **1. General Case (The Chain Rule):**
> $$P(A \cap B) = P(A) \cdot P(B | A)$$
> $$P(A \cap B) = P(B) \cdot P(A | B)$$
> 
> **2. For Independent Events:**
> 
> If $A$ and $B$ do not affect each other:
> $$P(A \cap B) = P(A, B) = P(A) \cdot P(B)$$
> 
> **3. The Monotonicity Property:**
> 
> Because $P(B | A) \leq 1$, the joint probability can never exceed the individual probability, the intersection (overlap) of two circles can never be larger than the circles themselves:
> $$P(A \cap B) \leq P(A)$$
> $$P(A \cap B) \leq P(B)$$


[^1]: https://d2l.ai/chapter_preliminaries/probability.html#a-more-formal-treatment:~:text=The%20probability%20function,the%20sample%20space