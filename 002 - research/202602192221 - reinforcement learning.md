---
tags:
  - reinforcement_learning
aliases:
  - Reinforcement Learning
  - RL
title: reinforcement learning
description: ""
bot: false
parent nodes:
  - "[[202602061145 - machine learning|Machine Learning]]"
published on:
---

- [ ] [YouTube - The FASTEST introduction to Reinforcement Learning on the internet](https://www.youtube.com/watch?v=VnpRp7ZglfA&t=1755s)

---
- Reinforcement learning studies how an <mark style="background: #FF5582A6;">agent</mark> learns <mark style="background: #BBFABBA6;">actions</mark> through interaction with the <mark style="background: #ABF7F7A6;">environment</mark> to maximise cumulative <mark style="background: #FFF3A3A6;">reward/feedback</mark>

![RL-Loop](https://www.reinforcementlearningpath.com/wp-content/uploads/2025/12/RL-is-a-loop-not-a-formula.png)



- The setting is usually modelled as a [[202602192236 - markov decision process|Markov Decision Process (MDP)]] with:
	- <mark style="background: #FF5582A6;">States</mark>
	- <mark style="background: #BBFABBA6;">Actions</mark>
	- <mark style="background: #FFF3A3A6;">Rewards</mark>
	- <mark style="background: #D2B3FFA6;">Transitions</mark>
- <mark style="background: #ADCCFFA6;">A policy maps states to actions, and learning improves this policy from experience</mark>
- Core method families are:
	- [[202602201255 - value-based methods|Value-based]]
	- [[202602200129 - policy gradient methods|Policy-gradient]]
	- [[202602201254 - actor-critic methods|Actor-critic]]
- <mark style="background: #FF5582A6;">Exploration-exploitation</mark> trade-offs are central because rewards are observed only for chosen actions
- RL is used in:
	- Control
	- Games
	- Robotics
	- Recommendation
	- [[202602191644 - post-training|Post-training]] of [[202602191524 - large language model|Large Language Model]]


[^1]: [Reinforcement Learning with Neural Networks: Essential Concepts](https://www.youtube.com/watch?v=9hbQieQh7-o&list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1&index=23)
[^2]: [Reinforcement Learning with Neural Networks: Mathematical Details](https://www.youtube.com/watch?v=DVGmsnxB2UQ&list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1&index=24)
[^3]: [Reinforcement Learning, by the Book](https://www.youtube.com/watch?v=NFo9v_yKQXA&list=PLzvYlJMoZ02Dxtwe-MmH4nOB5jYlMGBjr)