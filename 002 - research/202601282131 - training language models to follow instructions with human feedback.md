---
tags:
  - paper
aliases:
  - Training language models to follow instructions with human feedback
title: training language models to follow instructions with human feedback
description: ""
parent nodes:
  - "[[post-training]]"
published on: 2022-03-04
---

- [ ] Read overview
- [ ] Read paper
- [ ] What is a reward model?
- [ ] What is reinforcement learning?
- [ ] What is PPO?
- [ ] What is RLHF?
- [ ] What is TruthfulQA?
- [ ] What is SQuAD v2?
- [ ] What is DROP?

---
> [Training language models to follow instructions with human feedback](https://www.alphaxiv.org/abs/2203.02155)

## Summary

- InstructGPT was developed by [[openai|OpenAI]]
	- Aligned with human instructions with [[202602192217 - reinforcement learning human feedback|Reinforcement Learning Human Feedback (RLHF)]]
- Smaller aligned models were preferred by human evaluators over larger models
	- <mark style="background: #BBFABBA6;">1.3B aligned model > 175B unaligned model</mark>
- Aligned models demonstrated improvements in truthfulness and reduced toxicity
- Instruct GPT of 3 sizes
	- 1.3B, 6B and 175B

## Problem

- [[202602191524 - large language model|Large Language Models (LLMs)]] outputs can be,
	- Unhelpful
	- Factually incorrect
	- Fail to follow instructions
	- Toxic
	- Biased
	- Harmful
- The [[202602050155 - causal language modelling|next token prediction]] objective does not inherently align with human preferences
	- Challenges identified with the next token prediction objective
		- Plausible-sounding but factually incorrect information
		- Toxic or harmful content
		- Don't reliably follow the specific instructions given by users
		- Models may optimise for metrics that don't align with actual user preferences

### Method

- A 3-stage pipeline was introduced,
	- Starting with [[202601282201 - supervised fine-tuning|supervised fine-tuning]]
	- Training a [[reward model|reward model]] on human-labelled preference data
	- Optimising a policy against the reward model using [[reinforcement learning]]
		- The RL algorithm used was [[proximal policy optimisation|Proximal Policy Optimisation]]

![3-step Process|700](https://paper-assets.alphaxiv.org/figures/2203.02155/img-1.jpeg)

- The alignment approach here is termed [[reinforcement learning human feedback|reinforcement learning with human feedback (RLHF)]]
	- A reward model is trained on human-labelled preference data
	- The policy is updated against the reward model using [[reinforcement learning|reinforcement learning]]
	- The reinforcement learning algorithm is called [[proximal policy optimisation|Proximal Policy Optimisation]]
- The resultant aligned model was <mark style="background: #BBFABBA6;">InstructGPT</mark>

### Result

- <mark style="background: #FF5582A6;">Human evaluators preferred outputs from the 1.3B parameter InstructGPT model over the 175B parameter GPT-3 model</mark> 71% of the time, and the 175B InstructGPT model over the 175B GPT-3 model 85% of the time
- InstructGPT models showed improvements in truthfulness on the TruthfulQA benchmark and modest reductions in toxicity when specifically prompted for respectful behaviour
- Performance on standard [[202602061133 - natural language processing|Natural Language Processing]] benchmarks varied
	- InstructGPT models maintained or improved performance on some tasks (e.g., SQuAD v2) and showed some regression on others (e.g., DROP), but the PPO-ptx variant helped mitigate these drops

### Take Away

- <mark style="background: #FF5582A6;">Alignment can be more impactful than increasing model size alone</mark>
- Reinforcement Learning Human Feedback (RLHF) can help with alignment without significantly degrading general capabilities
- <mark style="background: #BBFABBA6;">InstructGPT generalised beyond its training distribution</mark>
	- Aligned models showcase increased generalisation capabilities beyond their specific training data, extending to:
		- Held-out human evaluators
		- Non-English instructions
		- Different task domains like code 

### Limitations

- Evaluation is subjective and difficult
- Relies on human feedback
	- It is costly, time-consuming and potentially biased
- The model could game the reward system
