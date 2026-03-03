---
tags:
  - inbox
description: ""
bot: false
status: In Progress
task type:
urgency level:
importance level:
due date:
start date:
end date:
story points:
recurrent:
parent nodes:
---

- What has been done so far?
	- Knowledge Graph
		- Focussed on 4 core papers
			- Attention Is All You Need
				- Understand the architecture and the math behind it
				- Build GPT-2
				- Build a pipeline for pre-training
			- Training language models to follow instructions with human feedback
				- Understand the standard training pipeline
					- Supervised fine-tuning followed by Reinforcement Learning
					- Build a pipeline for fine-tuning (classification)
				- PPO algorithm
			- DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
				- Training setup/formulae
				- Reward setup
				- GRPO
			- <mark style="background: #FF5582A6;">ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning</mark>
				- Training setup/formulae
				- Reward setup
				- Training
					- MuSiQue 
				- Evaluation
					- HotpotQA
					- 2WikiMultiHopQA
					- Bamboogle
				- Future direction:
					- Improve reward design
					- Smaller model
					- Extend knowledge sources
		- Created notes for:
			- Math
				- Information Theory
				- Probability 
				- Statistics
			- Training
			- Evaluation
			- Deep Learning
			- Reinforcement Learning
				- Policy Gradient Methods
					- REINFORCE
					- TRPO
					- PPO
					- GRPO
	- <mark style="background: #BBFABBA6;">Foundational work has been completed for the Knowledge Graph</mark>
- What is pending?
	- Code for RL pipeline (but have found the resource for implementation)
- Question?
- ReSearch
	- Models
		- base model
		- instruction-tuned model
		- Test
			- math model
			- code model
	- Rewards
		- Answer based
			- F1
			- Test
				- Semantic reward
		- Format based
- Plan
	- Build Qwen3 0.6B and load the model
	- Implement a GRPO training pipeline
	- Build a query system with FlashRag (for a search tool)
	- Train on MuSiQue 
	- Evaluate the below for baseline:
		- HotpotQA
		- Bamboogle
		- 2WikiMultiHopQA
