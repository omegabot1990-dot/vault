---
tags:
  - inbox
description:
due date: 2026-01-30
start date: 2026-01-29
end date:
status: Done
importance level: important
urgency level: urgent
task type: plan
story points: 3
parent nodes:
child nodes:
recurrent:
---

1. Attention Is All You Need - 2017
	1. Talk about attention
	2. End with causal attention
2. Language Models Are Unsupervised Multi-task Learners (GPT2) - 2019
	1. Talk about pre-training
	2. Self-supervised
	3. Next-token prediction with cross-entropy loss
3. Scaling Laws for Neural Language Models - 2020
	1. Compute + Data + Parameters
4. Language Models Are Few-Shot Learners (GPT3) - 2020
	1. In-context learning 
5. Training Language Models to Follow Instructions with Human Feedback (InstructGPT) - 2022
	1. SFT - behavioural cloning
		1. Annotated data is expensive
		2. Still more accessible than pre-training
	2. RL for preference tuning
		1. PPO from 2017, removed the entropy term to reward exploration
		2. Employs a reward model
		3. Policy gradient method
		4. Gradient ascent, used a value policy/function
		5. Similar to REINFORCE from 1992
		6. Actor-Critic method, expensive and complicated
		7. Variant of TRPO without second-order derivatives
			1. Uses clipping instead
	3. 1.3B param InstructGPT preferred more than much larger models (175B) by human evaluators
6. GPT3.5 released in November 2022
7. 2023 starts the era of public awareness of LLMs
	1. Prompt-engineering
	2. Fine-tuning paradigms
		1. Neural adapters
		2. LoRA adapters
	3. Inference paradigms
	4. DPO
	5. Distillation
	6. Open-source models
		1. Llama
		2. Gemma
		3. DeepSeek
		4. Qwen
		5. Kimi
8. Fast forward to December 2024, GPT-o1 is released, the first public-facing reasoning/thinking model, but they chose to omit the reasoning traces
9. DeepSeek-R1 and R1-Zero
	1. Talk about RLVR
	2. A sparse reward model elicited self-reflection, and we have the Aha moment
	3. Paradigm shift from costly SFT to RL
	4. Reasoning improves accuracy to a certain degree
	5. GRPO algorithm
		1. Simplifies the learning objective, advantage uses the final reward instead of the return and uses the rollouts' mean and std to calculate
		2. Loss function is the same as PPOs, but with a KL term to combat variance
	6. Makes RL more accessible for practitioners
	7. Distilled to smaller models (hard distillation)
	8. Uses format reward and final answer reward
10. How to extend to non-deterministic or non-verifiable domains?
	1. Reward modelling?
		1. MCQ-based, again, answer-based
			1. MedRLVR
		2. Soft rewards based on gold labels, answer-based
		3. Based on token distribution
			1. Mean token probabilities 
			2. Self-certainty, KL-divergence between uniform distribution and token distribution
		4. Rubric-based, could be static, like a constitution or dynamic 
		5. Format
		6. F1-based
	2. Meta tags?
		1. Meta-reasoning rewards
		2. ReSearch
	3. Curriculum learning and transfer learning (pedagogical approach)
		1. Adaptive guidance
		2. Difficulty-aware staged RL
		3. Reasoning gym
11. Tool use is the use case I would like to use
12. Domain adaptation is not behavioural cloning with SFT, but is reasoning about how to interact with the domain
	1. Knowledge cut-off problem
	2. Data privacy issues
	3. Replacing RAG, which is more static, dynamic and brittle
	4. Small models, efficient RL

