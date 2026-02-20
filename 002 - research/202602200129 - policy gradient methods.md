---
tags:
- note
aliases:
- Policy Gradient Methods
title: policy gradient methods
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Policy gradient methods optimize policy parameters directly by ascending an estimate of expected return
- They use the policy gradient theorem to avoid differentiating environment dynamics
- REINFORCE provides an unbiased but high-variance gradient estimate from sampled trajectories
- Baselines (e.g., value functions) reduce variance without changing expected gradient
- Actor-critic methods combine policy gradients with learned critics for better sample efficiency
- PPO and related methods add trust-region style constraints for stable policy updates