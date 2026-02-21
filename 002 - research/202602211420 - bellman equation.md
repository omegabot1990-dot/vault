---
tags:
  - reinforcement_learning
aliases:
  - The Bellman Equation
  - Bellman Equation
title: bellman equation
description: ""
bot: false
parent nodes:
  - "[[202602192359 - value estimation|Value Estimation]]"
published on:
---

- The Bellman equation expresses <mark style="background: #FF5582A6;">recursive consistency</mark> of [[202602200020 - value|value]] functions under a [[202602192245 - policy|policy]] or optimal control
- For policy evaluation, state values satisfy:

> [!MATH] Bellman Equation for Policy Evaluation
  > $$V^\pi(s)=\mathbb{E}_{a\sim\pi,\,s'\sim P}\left[r(s,a,s') + \gamma V^\pi(s')\right]$$

- For optimal control, the Bellman optimality equation is:

> [!MATH] Bellman Equation for Optimal Control
>$$V^*(s)=\max_a\mathbb{E}_{s'\sim P}\left[r(s,a,s') + \gamma V^*(s')\right]$$

- Equivalent [[202602192350 - action|action]]-value forms define targets used by [[202602201303 - q-learning|Q-learning]] and other [[202602201255 - value-based methods|value-based methods]]
- Dynamic programming and [[202602201305 - temporal-difference algorithm|temporal-difference algorithms]] rely directly on Bellman updates
- The equation is foundational because it turns long-horizon [[202602192355 - return|return]] optimization into local recursive updates