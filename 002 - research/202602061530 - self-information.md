---
tags:
  - math
aliases:
  - Self-Information
title: self-information
description:
parent nodes:
  - "[[202602061605 - information theory|Information Theory]]"
annotation-target:
published on:
---

- <mark style="background: #BBFABBA6;">Information is a measure of surprise</mark> [^1]
	- Information represents the degree of surprise or the abstract possibility of the event [^2]
- For a discrete [[202602061340 - random variable|random variable]] $X$ with probability $P(X=x)$, the information $I(X=x)$ is:

> [!MATH] Self-Information (Surprise)
> $$I(X=x) = \log_{2} \frac{1}{P(X=x)} = -\log_2 P(X=x)$$

- Units
	- Measured in <mark style="background: #FF5582A6;">bits</mark> (when using $\log_2$), for discrete random variables  [^3]
	- Measured in <mark style="background: #FF5582A6;">nats</mark> (when using $\log_e$ or $\ln$), for continuous random variables 
- <mark style="background: #BBFABBA6;">Deterministic outcomes contain no information</mark> [^1]
- Inverse Relationship
	- As probability $P(x)$ goes up, information $I(x)$ goes down [^1]
- Additive
	- The information from two independent events is the sum of their individual information [^1]
	- $I(x, y) = I(x) + I(y)$.


[^1]: [Information Theory Basics](https://www.youtube.com/watch?v=bkLHszLlH34)
[^2]: https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/information-theory.html#:~:text=information%20represents%20the%20degree%20of%20surprise%20or%20the%20abstract%20possibility%20of%20the%20event
[^3]: https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/information-theory.html#:~:text=bit%20as%20the%20unit%20of%20information
