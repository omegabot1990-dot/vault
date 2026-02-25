---
tags:
  - reinforcement_learning
aliases:
  - Reinforcement Learning Verifiable Rewards
  - RLVR
title: reinforcement learning verifiable rewards
description: ""
bot: false
parent nodes:
  - "[[reinforcement learning]]"
published on:
---

- Reinforcement Learning with Verifiable Rewards (RLVR) [[202602111335 - training|trains]] [[202602192245 - policy|policies]] using [[202602192352 - reward|rewards]] computed by objective checks rather than human preference models
- Rewards are derived from automatic validators such as:
	- Unit tests
	- Symbolic solvers
	- Exact match
	- Formal verification signals
- This reduces reward-model misspecification and improves training signal reliability in domains with clear correctness criteria ([[202602020018 - verifiable domains|verifiable domains]])
- RLVR is especially effective for:
	- Math
	- Coding
	- Tool-using tasks where outputs can be programmatically verified
- Main limitations are <mark style="background: #FF5582A6;">sparse rewards</mark> and <mark style="background: #BBFABBA6;">limited applicability to open-ended subjective tasks</mark>
- Practical RLVR setups often combine verifiable rewards with <mark style="background: #FFF3A3A6;">curriculum design</mark>, <mark style="background: #ABF7F7A6;">shaping</mark>, and <mark style="background: #FFB86CA6;">controlled exploration</mark>
