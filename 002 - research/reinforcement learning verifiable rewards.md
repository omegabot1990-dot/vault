---
tags:
- moc
description: ''
parent nodes:
- '[[proximal policy optimisation]]'
- '[[group relative policy optimisation]]'
- '[[reward model]]'
---

## Topics

## Blogs

- [ ] [Verifiable Rewards (RLVR) Framework](https://www.emergentmind.com/topics/verifiable-rewards-rlvr)
	- [ ] Dec 2025

- [ ] [RISE: Online Self-Verification for RL Models](https://www.emergentmind.com/topics/online-self-verification-rise)
	- [ ] Dec 2025

- [ ] [Reinforcement Learning with Verified Reward (RLVR)](https://www.emergentmind.com/topics/reinforcement-learning-with-verified-reward-rlvr)
	- [ ] Aug 2025

- [ ] [Multi-tasking: Verifiable & Non-verifiable Rewards](https://www.emergentmind.com/topics/multi-tasking-with-verifiable-and-non-verifiable-rewards)
	- [ ] July 2025

- [ ] [Verifiable Rewards in Reinforcement Learning](https://www.emergentmind.com/topics/reinforcement-learning-with-verifiable-rewards-paradigm)
	- [ ] June 2025

- [ ] [Reinforcement Learning with Verifiable Rewards](https://www.emergentmind.com/topics/reinforcement-learning-with-verifiable-rewards-rlvr)
	- [ ] June 2025

## Papers

#### Tool Use + Search

- [x] [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](https://www.alphaxiv.org/abs/2503.19470)

- [ ] [R1-Searcher: Incentivizing the Search Capability in LLMs via Reinforcement Learning](https://www.alphaxiv.org/abs/2503.05592)
	- [ ] R1-Searcher utilises a **two-stage, outcome-based reinforcement learning** approach to autonomously incentivise LLMs to invoke external search systems during reasoning, without requiring supervised fine-tuning or distillation
	- [ ] Stage-1 uses **retrieve-rewards** to teach the model how to invoke the search tool format, while Stage-2 uses **answer-rewards** to train it to integrate retrieved knowledge to solve complex questions correctly
	- [ ] <mark style="background: #FF5582A6;">VERY IMPORTANT</mark>

- [ ] [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://www.alphaxiv.org/abs/2503.09516)
	- [ ] SEARCH-R1 extends reinforcement learning for reasoning by training LLMs to autonomously generate multi-turn search queries and process real-time retrieval results using an outcome-based reward function and retrieved token masking for stable optimization
	- [ ] <mark style="background: #FF5582A6;">VERY IMPORTANT</mark>

#### Data Generation

- [ ] [Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text](https://www.alphaxiv.org/abs/2601.22975)
	- [ ] Golden Goose synthesises unlimited RLVR tasks by transforming unverifiable internet text into multiple-choice "fill-in-the-middle" questions, where an LLM masks key reasoning steps and generates plausible distractors to create automatically verifiable training signals
	- [ ] <mark style="background: #FF5582A6;">IMPORTANT</mark>

- [ ] [SWE-Universe: Scale Real-World Verifiable Environments to Millions](https://www.alphaxiv.org/abs/2602.02361)
	- [ ] SWE-Universe utilises an autonomous building agent powered by an efficient MoE model that employs iterative self-verification and in-loop hacking detection to automatically construct million-scale, multi-lingual, verifiable software engineering environments from GitHub pull requests
	- [ ] <mark style="background: #ADCCFFA6;">LATER</mark>

#### Long Context

- [ ] [InftyThink+: Effective and Efficient Infinite-Horizon Reasoning via Reinforcement Learning](https://www.alphaxiv.org/overview/2602.06960)
	- [ ] **InftyThink+** is an end-to-end reinforcement learning framework that optimizes "infinite-horizon" iterative reasoning by teaching models to autonomously decide when to summarise intermediate thoughts and how to continue reasoning from those compressed states
	- [ ] <mark style="background: #FF5582A6;">IMPORTANT</mark>
#### Misc

- [ ] [Learning to Reason in 13 Parameters](https://www.alphaxiv.org/abs/2602.04118)
	- [ ] <mark style="background: #FF5582A6;">IMPORTANT</mark>
- [ ] [Reinforcement World Model Learning for LLM-based Agents](https://www.alphaxiv.org/abs/2602.05842)
	- [ ] **Reinforcement World Model Learning (RWML)** is a self-supervised method that trains LLM agents to predict action-conditioned next states by minimising the "sim-to-real" gap in a pre-trained embedding space using reinforcement learning
	- [ ] <mark style="background: #BBFABBA6;">LATER</mark>

## Videos

## Code
