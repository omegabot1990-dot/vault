---
tags:
  - math
aliases:
  - Mutually Exclusive
title: mutually exclusive
description:
parent nodes:
  - "[[202602092352 - event|Event]]"
child nodes:
annotation-target:
published on:
---

- Mutually Exclusive events (also called <mark style="background: #FF5582A6;">disjoint events</mark>) are events that cannot happen at the same time [^1]
- If one event occurs, the other is physically or logically impossible
- Two events $A$ and $B$ are mutually exclusive if their intersection is the empty set ($\emptyset$):

> [!MATH] Disjoint Sets
> $$A \cap B = \emptyset$$

- The Rules of Mutually Exclusive Events
	1. <mark style="background: #BBFABBA6;">Joint Probability</mark>
		1. $P(A \cap B) = 0$ (They never happen together)
	2. <mark style="background: #FFF3A3A6;">The Addition Rule</mark>
		1. $P(A \cup B) = P(A) + P(B)$
	3. <mark style="background: #ADCCFFA6;">Conditional Probability</mark>
		1. $P(A | B) = 0$ (If $B$ happened, the chance of $A$ is zero)


[^1]:  [Mutually Exclusive vs. Independent Events EXPLAINED in 4 minutes](https://www.youtube.com/watch?v=aVqmWW3xmdU)