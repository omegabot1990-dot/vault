---
tags:
  - training
aliases:
  - Supervised Fine-Tuning
title: supervised fine-tuning
description: ""
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- [ ] What is AdamW?

---
- <mark style="background: #BBFABBA6;">Behavioural cloning</mark>
- Input is a structured template consisting of a Prompt (user) and a Response (LLM)
	- Instruction-Response pairs
	- (Batch, Time)
- Output is logits
	- (Batch, Time, Channel)
- Learning objective is [[202602050155 - causal language modelling|next-token prediction]]
	- Same as [[202602030230 - pre-training|pre-training]]
- [[202602010047 - objective function|Loss function]] is Masked [[202602030238 - cross-entropy loss|Cross-entropy Loss]]
	- <mark style="background: #FF5582A6;">Only tokens in the response are trained</mark>

> [!MATH] Supervised Fine-Tuning
> $$\mathcal{L}_{SFT}(\theta) = -\frac{1}{N_{res}} \sum_{t=1}^{T} m_t \log P_{\theta}(x_t \mid x_{<t})$$
> - $m_t$ is a binary mask 
> 	- $m_t = 1$ if part of **Response**
> 	- $m_t = 0$ if part of **Prompt**

- [[202602111605 - optimization algorithms|Optimizer]] used is usually AdamW in [[large language models|Large Language Models (LLMs)]]