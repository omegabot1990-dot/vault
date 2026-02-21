---
tags:
  - reinforcement_learning
aliases:
  - Trust Region Policy Optimization
  - TRPO
title: trust region policy optimization
description: ""
bot: false
parent nodes:
  - "[[202602200129 - policy gradient methods|Policy Gradient Methods]]"
published on:
---

- Trust Region Policy Optimization (TRPO) is a [[202602200129 - policy gradient methods|policy-gradient method]] designed to make stable monotonic [[202602192245 - policy|policy]] improvements
- It constrains each policy update to stay within a trust region measured by the [[202602181827 - kl divergence|KL divergence]] from the previous policy
- The optimization is commonly formulated as a constrained objective with a surrogate [[202602200148 - advantage|advantage]]-based gain
- TRPO maximises the policy objective subject to a constraint on how much the policy can change, ensuring monotonic improvement

> [!MATH] Trust Region Policy Optimisation
> $$\max_{\theta} E_t \left[ \frac{\pi_{\theta}(a_t|s_t)}{\pi_{\theta_{old}}(a_t|s_t)} \hat{A}_t \right]$$
>$$\text{subject to } E_t [KL(\pi_{\theta_{old}}(\cdot|s_t) || \pi_{\theta}(\cdot|s_t))] \le \delta$$
>
>1.  $\frac{\pi_{\theta}}{\pi_{\theta_{old}}}$ or **Importance Sampling Ratio**: How much more/less likely an action is under the new policy vs the old
> 2. $\hat{A}_t$ or **Advantage Function**: Measures if an action was better than the average ($Q(s,a) - V(s)$)
> 3. $KL(\cdot \| \cdot)$ or **KL Divergence**: Measures the "distance" between the old and new probability distributions
> 4. $\delta$ or **Step Size (Trust Region)**: A small constant (hyperparameter) that limits the maximum allowed change

- <mark style="background: #FFF3A3A6;">This reduces destructive large policy steps that can collapse performance</mark>
- TRPO is often more stable than unconstrained policy gradients but computationally heavier than [[202602201241 - proximal policy optimization|PPO]]
- It is foundational for later clipped-objective methods such as PPO
- Key Properties
	- <mark style="background: #FF5582A6;">Monotonic Improvement</mark>
		- Mathematically guarantees that the policy will get better (or stay the same) at every step
	- <mark style="background: #BBFABBA6;">Second-Order</mark>
		- Uses second-order information (Hessian/Fisher Matrix), making it more accurate but computationally heavy compared to PPO
