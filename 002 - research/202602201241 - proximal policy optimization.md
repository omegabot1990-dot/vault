---
tags:
- note
aliases:
- Proximal Policy Optimization
- PPO
title: proximal policy optimization
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Proximal Policy Optimization is an on-policy policy-gradient method designed for stable policy updates
- PPO constrains policy change between updates using a clipped objective on probability ratios
- It balances sample efficiency and stability without the complexity of full trust-region optimization
- PPO typically uses actor-critic architecture with advantage estimates for gradient weighting
- Mini-batch epochs over collected trajectories improve data utilization per rollout
- PPO is widely used in robotics, control benchmarks, and LLM post-training pipelines