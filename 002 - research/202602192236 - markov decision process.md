---
tags:
  - reinforcement_learning
aliases:
  - Markov Decision Process
  - MDP
title: markov decision process
description: ""
bot: false
parent nodes:
  - "[[202602192221 - reinforcement learning|Reinforcement Learning]]"
published on:
---

- A <mark style="background: #FF5582A6;">Markov Decision Process formalises sequential decision-making under uncertainty</mark>
- In MDPs, the environment is fully observable
- An MDP is defined by:
	- [[202602192351 - state|States]] $\mathcal{S}$
	- [[202602192350 - action|Actions]] $\mathcal{A}$
	- [[202602200013 - transition|Transition]] dynamics $P$
	- [[202602192352 - reward|Reward]] function $R$
	- Discount factor $\gamma$
- <mark style="background: #BBFABBA6;">The Markov property means next-state dynamics depend only on the current state and action</mark>
- A [[202602192245 - policy|policy]] $\pi(a\mid s)$ selects actions to maximise [[202602061333 - expectation|expected]] discounted [[202602192355 - return|return]]
- Value functions estimate the long-term utility of states or state-action pairs under a policy
- Many [[202602192221 - reinforcement learning|RL]] algorithms solve MDPs by [[202602200001 - policy optimization|policy optimization]], [[202602192359 - value estimation|value estimation]], or both


[^1]: [Reinforcement Learning, by the Book](https://www.youtube.com/watch?v=NFo9v_yKQXA&list=PLzvYlJMoZ02Dxtwe-MmH4nOB5jYlMGBjr)