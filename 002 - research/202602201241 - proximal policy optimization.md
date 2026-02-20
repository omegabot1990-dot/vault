---
tags:
  - reinforcement_learning
aliases:
  - Proximal Policy Optimization
  - PPO
title: proximal policy optimization
description: ""
bot: false
parent nodes:
  - "[[202602201254 - actor-critic methods|Actor-Critic Methods]]"
published on:
---

- Proximal Policy Optimization is an on-policy [[202602200129 - policy gradient methods|policy-gradient method]] designed for stable [[202602192245 - policy|policy]] updates
- <mark style="background: #BBFABBA6;">PPO constrains policy change between updates using a clipped objective on probability ratios</mark>
- PPO is an [[202602201254 - actor-critic methods|Actor-Critic]] algorithm that uses a "Clipped Surrogate Objective" to prevent the updated policy from deviating too far from the old policy:

> [!MATH] Proximal Policy Optimization
> $$L^{CLIP}(\theta) = \hat{E}_t \left[ \min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t) \right]$$
> 
> 1. $r_t(\theta)$ or **Probability Ratio**: The ratio $\frac{\pi_{\theta}(a|s)}{\pi_{\theta_{old}}(a|s)}$, how much more/less likely the action is now vs. before
> 2. $\hat{A}_t$ or **Advantage Estimate**: How much better the action was than the average: $G_t - V(s_t)$ 
> 3.  $\epsilon$ or **Clipping Parameter**: Usually set to $0.1$ or $0.2$, limits how much the policy can change in one step
> 4. $\text{clip}(\cdot)$ or **Clipped Ratio**: Forces the ratio to stay between $[1-\epsilon, 1+\epsilon]$

- It balances sample efficiency and stability without the complexity of full trust-region optimization
- PPO typically uses actor-critic architecture with advantage estimates for gradient weighting
- [[202602111625 - batch size|Mini-batch]] [[202602111623 - epochs|epochs]] over collected trajectories improve data utilisation per rollout
- PPO is widely used in robotics, control benchmarks, and [[202602191524 - large language model|Large Language Model (LLM)]] [[202602191644 - post-training|post-training]] pipelines
- Key Properties
	- <mark style="background: #BBFABBA6;">On-Policy</mark>
		- PPO learns from data collected by its current version, but the "Ratio" allows it to safely reuse that data for a few mini-batch updates
	- <mark style="background: #FF5582A6;">Actor-Critic</mark>
		- The **Actor** updates the policy ($\pi$), while the **Critic** updates the [[202602200020 - value|Value]] Function ($V$) to calculate the [[202602200148 - advantage|Advantage]] ($\hat{A}_t$)


[^1]: [Proximal Policy Optimization (PPO) for LLMs Explained Intuitively](https://www.youtube.com/watch?v=8jtAzxUwDj0)