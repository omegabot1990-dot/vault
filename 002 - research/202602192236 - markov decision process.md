---
tags:
- note
aliases:
- Markov Decision Process
- MDP
title: markov decision process
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- A Markov decision process formalizes sequential decision making under uncertainty
- An MDP is defined by states $\mathcal{S}$, actions $\mathcal{A}$, transition dynamics $P$, reward function $R$, and discount factor $\gamma$
- The Markov property means next-state dynamics depend only on the current state and action
- A policy $\pi(a\mid s)$ selects actions to maximize expected discounted return
- Value functions estimate long-term utility of states or state-action pairs under a policy
- Many RL algorithms solve MDPs by policy optimization, value estimation, or both