---
tags:
  - training
aliases:
  - Direct Preference Optimization
  - DPO
title: direct preference optimization
description: ""
bot: false
parent nodes:
  - "[[202602191644 - post-training|Post-Training]]"
published on:
---

- Direct Preference Optimization (DPO) aligns [[202602192245 - policy|policies]] to preference data without explicitly [[202602111335 - training|training]] a [[202602201334 - reward model|reward model]] or running [[202602192221 - reinforcement learning|RL]] rollouts
- It optimizes a [[202602120054 - classification|classification]]-style objective over preferred vs. dispreferred responses relative to a reference policy
- DPO optimizes the [[202602010044 - model|model]] to increase the relative log-probability of preferred completions ($y_w$) over rejected completions ($y_l$) directly

> [!MATH] Direct Preference Optimization
> $$\mathcal{L}_{DPO}(\pi_\theta; \pi_{ref}) = -E_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)} \right) \right]$$
> 
> - $\pi_\theta$ or **Policy (Model)**: The LLM we are currently training
> - $\pi_{ref}$ or **Reference Model**: The frozen base model (to prevent the model from "forgetting")
> - $y_w, y_l$ or **Win / Loss Pair**: The "preferred" ($y_w$) and "rejected" ($y_l$) responses from the dataset $\mathcal{D}$
> - $\beta$ or **KL Constraint**: Controls how strictly the model stays near the reference (usually $0.1$ to $0.5$)
> - $\sigma$ or **Sigmoid Function**: Maps the log-ratio difference to a probability between 0 and 1

- DPO can be interpreted as implicitly optimizing a reward-consistent objective under [[202602181827 - kl divergence|KL]] regularization
- Compared with [[202602192217 - reinforcement learning human feedback|RLHF]] pipelines, DPO is typically simpler to implement and more stable in practice
- The method depends strongly on preference data quality and reference-policy choice
- DPO and related preference-optimization methods are widely used in [[202602191524 - large language model|LLM]] [[202602191644 - post-training|post-training]]
- Stability
	- Unlike [[202602201241 - proximal policy optimization|PPO]], DPO is not sensitive to [[202602111256 - hyperparameters|hyperparameters]] like [[202602111600 - learning rate|learning rate]] or clipping
- Data Requirement
	- Needs a dataset of pairs (Prompt $\to$ Better Answer, Worse Answer)


[^1]: [Tülu 3 from AI2: Full open-source fine-tuning recipe for LLMs](https://www.youtube.com/watch?v=P26xOoUuef4)
