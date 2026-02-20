---
tags:
- note
aliases:
- Actor-Critic Methods
title: actor-critic methods
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Actor-critic methods combine a parameterized policy (actor) with a value estimator (critic)
- The actor updates policy parameters to improve expected return using gradients weighted by critic signals
- The critic learns value targets from transitions to provide lower-variance learning signals than pure Monte Carlo updates
- This framework bridges policy-gradient and value-based ideas in a single optimization loop
- Many practical algorithms (A2C, A3C, PPO, SAC variants) are actor-critic or closely related
- Stability depends on bias-variance trade-offs in critic learning and update step sizes