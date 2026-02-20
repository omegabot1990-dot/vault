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

- Policy gradient methods optimize [[202602192245 - policy|policy]] [[202602111314 - model parameters|parameters]] directly by <mark style="background: #BBFABBA6;">ascending an estimate</mark> of [[202602061333 - expectation|expected]] [[202602192355 - return|return]]
- They use the policy gradient theorem to avoid differentiating [[202602192345 - environment|environment]] dynamics
- REINFORCE provides an unbiased but high-[[202602062206 - variance|variance]] gradient estimate from sampled trajectories
- Baselines (e.g., [[202602200020 - value|value]] functions) reduce variance without changing expected gradient
- Actor-critic methods combine policy gradients with learned critics for better sample efficiency
- PPO and related methods add trust-region style constraints for stable policy updates