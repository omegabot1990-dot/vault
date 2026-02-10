---
tags:
- math
aliases:
- Conditional Probability
title: conditional probability
description: ''
parent nodes:
- '[[202602062040 - probability|Probability]]'
published on: null
---

- <mark style="background: #BBFABBA6;">Conditional Probability</mark> is the probability of an event occurring given that another event has already happened [^1]
- It is the act of updating your beliefs in light of new information
- The probability of $A$ occurring given that $B$ has occurred:

> [!MATH] Conditional Probability $P(A|B)$
> $$P(A | B) = \frac{P(A \cap B)}{P(B)}$$
> 
> **Where:**
> - **$P(A \cap B)$**: The [[202602080100 - joint probability|Joint Probability]] (Both happening)
> - **$P(B)$**: The probability of the condition (The "New World")
> - **Constraint**: $P(B) > 0$ (You can't condition on something impossible)

- Why does the formula work?
	- When we say "Given $B$" we are making $B$ our new [[202602061346 - sample space|sample space]]
	- We look only at the outcomes where $B$ is true
	- Inside that "B-world," we look for how often $A$ happens $A\cap B$
	- We divide by the size of $B$ to turn it back into a percentage


[^1]:  [Conditional Probabilities, Clearly Explained!!!](https://www.youtube.com/watch?v=_IgyaD7vOOA)