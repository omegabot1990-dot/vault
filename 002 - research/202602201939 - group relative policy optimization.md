---
tags:
  - reinforcement_learning
aliases:
  - Group Relative Policy Optimization
  - GRPO
title: group relative policy optimization
description: ""
bot: false
parent nodes:
  - "[[202602201241 - proximal policy optimization|PPO]]"
published on:
---

- Group Relative Policy Optimization (GRPO) is a [[202602200001 - policy optimization|policy optimization]] method that normalizes [[202602192352 - reward|rewards]] within sampled output groups
- Instead of relying on a separate [[202602200020 - value|value]] critic, it <mark style="background: #BBFABBA6;">computes relative</mark> [[202602200148 - advantage|advantages]] <mark style="background: #BBFABBA6;">from group-level statistics</mark>
- This reduces dependence on explicit value-function fitting while preserving [[202602200129 - policy gradient methods|policy-gradient]] style updates
- GRPO optimizes the policy by comparing each output's reward against the average reward of a group of outputs generated from the same prompt:

> [!MATH] Group Relative Policy Optimization
> $$L_{GRPO}(\theta) = \hat{E}_{q \sim P, \{a_i\}_{i=1}^G \sim \pi_{\theta_{old}}} \left[ \frac{1}{G} \sum_{i=1}^G \left( \min(r_i(\theta)\hat{A}_i, \text{clip}(r_i(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_i) - \beta D_{KL}(\pi_\theta \| \pi_{ref}) \right) \right]$$
> 
> 1. $\{a_i\}_{i=1}^G$ or **Group Samples**: $G$ different responses generated for the same prompt
> 2.  $\hat{A}_i$ or **Relative Advantage**: Calculated as $\frac{r_i - \text{mean}(R)}{\text{std}(R)}$ so no Critic needed!
> 3. $r_i(\theta)$ or **Probability Ratio**: The ratio $\frac{\pi_{\theta}(a_i|q)}{\pi_{\theta_{old}}(a_i|q)}$ (same as PPO)
> 4. $D_{KL}(\cdot \| \cdot)$ or **KL Penalty**: Keeps the model from drifting too far from the base model ($\pi_{ref}$)
> 5. $\beta$ or **KL Coefficient**: Controls how strictly the model stays near the reference

- GRPO is commonly discussed in [[202602191524 - large language model|Large Language Model (LLM)]] [[202602191644 - post-training|post-training]], where multiple candidate responses are scored per prompt
- <mark style="background: #FF5582A6;">Relative normalization can improve stability when absolute reward scales vary across prompts</mark>
- As with [[202602201241 - proximal policy optimization|PPO]]-like methods, clipping or trust-style constraints are often used to limit destructive policy updates
- Key Properties
	- <mark style="background: #BBFABBA6;">Memory Efficient</mark>
		- Specifically designed for scaling Large Language Models
	- <mark style="background: #FFF3A3A6;">Reasoning Focused</mark>
		- The core algorithm behind DeepSeek-R1's ability to self-correct and "think" longer
