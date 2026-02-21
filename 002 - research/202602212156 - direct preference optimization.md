---
tags:
- note
aliases:
- Direct Preference Optimization
- DPO
title: direct preference optimization
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Direct Preference Optimization (DPO) aligns policies to preference data without explicitly training a reward model or running RL rollouts
- It optimizes a classification-style objective over preferred vs. dispreferred responses relative to a reference policy
- DPO can be interpreted as implicitly optimizing a reward-consistent objective under KL regularization
- Compared with RLHF pipelines, DPO is typically simpler to implement and more stable in practice
- The method depends strongly on preference data quality and reference-policy choice
- DPO and related preference-optimization methods are widely used in LLM post-training