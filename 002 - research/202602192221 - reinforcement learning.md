---
tags:
  - reinforcement_learning
aliases:
  - Reinforcement Learning
title: reinforcement learning
description: ""
bot: true
parent nodes:
  - "[[reinforcement learning]]"
published on:
---

- [ ] What is value-based?
- [ ] What is actor-critic?
- [ ] [YouTube - The FASTEST introduction to Reinforcement Learning on the internet](https://www.youtube.com/watch?v=VnpRp7ZglfA&t=1755s)

---
- Reinforcement learning studies how an <mark style="background: #FF5582A6;">agent</mark> learns <mark style="background: #BBFABBA6;">actions</mark> through interaction with the <mark style="background: #ABF7F7A6;">environment</mark> to maximise cumulative <mark style="background: #FFF3A3A6;">reward</mark>
- The setting is usually modelled as a Markov Decision Process (MDP) with:
	- <mark style="background: #FF5582A6;">States</mark>
	- <mark style="background: #BBFABBA6;">Actions</mark>
	- <mark style="background: #FFF3A3A6;">Rewards</mark>
	- <mark style="background: #D2B3FFA6;">Transitions</mark>
- <mark style="background: #ADCCFFA6;">A policy maps states to actions, and learning improves this policy from experience</mark>
- Core method families are:
	- Value-based
	- Policy-gradient
	- Actor-critic
- <mark style="background: #FF5582A6;">Exploration-exploitation</mark> trade-offs are central because rewards are observed only for chosen actions
- RL is used in:
	- Control
	- Games
	- Robotics
	- Recommendation
	- [[202602191644 - post-training|Post-training]] of [[202602191524 - large language model|Large Language Model]]