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
	- States $\mathcal{S}$
	- Actions $\mathcal{A}$
	- Transition dynamics $P$
	- Reward function $R$
	- Discount factor $\gamma$
- <mark style="background: #BBFABBA6;">The Markov property means next-state dynamics depend only on the current state and action</mark>
- A policy $\pi(a\mid s)$ selects actions to maximise expected discounted return
- Value functions estimate the long-term utility of states or state-action pairs under a policy
- Many [[202602192221 - reinforcement learning|RL]] algorithms solve MDPs by policy optimization, value estimation, or both