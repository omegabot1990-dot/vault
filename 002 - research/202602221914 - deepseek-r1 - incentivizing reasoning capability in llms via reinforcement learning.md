---
tags:
  - paper
aliases:
  - DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
title: deepseek-r1 - incentivizing reasoning capability in llms via reinforcement learning
description: ""
bot: false
parent nodes:
  - "[[deepseek]]"
published on: 2025-01-22
---

- [ ] majority voting

> [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://www.alphaxiv.org/abs/2501.12948)

## Summary

- The paper introduces DeepSeek-R1-Zero and DeepSeek-R1 as [[202602231757 - reasoning|reasoning]]-focused [[202602191524 - large language model|LLMs]] [[202602111335 - training|trained]] primarily through [[202602192221 - reinforcement learning|RL]]
- <mark style="background: #BBFABBA6;">It shows pure RL can induce strong reasoning behaviours</mark>, then improves readability and stability with a multi-stage pipeline
- DeepSeek-R1 reaches near-o1-level reasoning results on math and coding benchmarks and enables strong distilled, smaller models

## Problem

- Existing LLM reasoning methods heavily rely on labour-intensive human-annotated data, leading to scalability issues and the introduction of human cognitive biases
- Training models to imitate human reasoning pathways caps their performance and prevents exploration of potentially superior, non-human strategies
- Prior open methods had not matched o1-class reasoning while staying reproducible and scalable
- Pure RL for reasoning without a supervised chain-of-thought warm start was not clearly validated at scale
- Strong reasoning often conflicted with readability, language consistency, and broad assistant alignment

## Method

- DeepSeek-R1-Zero
	- Trained from a base model with large-scale [[202602201939 - group relative policy optimization|GRPO]]-style RL and outcome-based [[202602192352 - reward|rewards]] ([[202602232025 - reinforcement learning verifiable rewards|RLVR]])
		- GRPO eliminates the need for a separate value model and estimates the [[202602200148 - advantage|advantages]] from grouped rewards
		- <mark style="background: #FF5582A6;">Reducing computational overhead</mark>
	- [[202602232031 - rule-based rewards|Rule-based rewards]]
		- <mark style="background: #BBFABBA6;">Binary accuracy rewards</mark> (correct/incorrect final answers) and <mark style="background: #FFF3A3A6;">format rewards </mark>(proper reasoning structure using `<think>...</think><answer>...</answer>` tags)
	- <mark style="background: #ABF7F7A6;">Extensive exploration</mark>
		- High sampling temperature (1.0) and very long response lengths (up to 65,536 tokens)
	- <mark style="background: #FFB86CA6;">Objective feedback</mark>
		- Compiler-based evaluation for coding problems and answer format verification for mathematics
- DeepSeek-R1
	- Build via a staged pipeline: [[202602232008 - cold-start sft|cold-start SFT]], reasoning RL, [[202602231804 - rejection sampling|rejection-sampled]] [[202601282201 - supervised fine-tuning|SFT]] refresh, then broader RL alignment

> [!MATH] R1-Pipeline
> $$\text{Cold Start SFT} \rightarrow \text{First RL Stage} \rightarrow \text{Rejection Sampling + Secondary SFT} \rightarrow \text{Second RL Stage}$$

- This framework addresses practical limitations of R1-Zero (poor readability, language mixing) while preserving reasoning capabilities
- The process incorporates both <mark style="background: #BBFABBA6;">rule-based</mark> and [[202602232032 - model-based rewards|model-based rewards]], including helpful and safety [[202602201334 - reward model|reward models]] trained on human preference data

- [[202602231948 - distillation|Distil]] reasoning traces and behaviours into smaller, dense [[qwen|Qwen]]/[[llama|Llama]]-family models

![Pipeline|700](https://paper-assets.alphaxiv.org/figures/2501.12948v2/img-2.jpeg)

## Result

- R1-Zero improves sharply on reasoning metrics from base performance through RL alone
- DeepSeek-R1-Zero demonstrates remarkable emergent behaviours during training
	- The model naturally develops sophisticated reasoning strategies including:
		- <mark style="background: #BBFABBA6;">Self-reflection</mark>
			- Dramatic increases in reflective language use, with words like "wait," "evaluate," and "retry" appearing 5-7 times more frequently
		- <mark style="background: #FF5582A6;">Verification</mark>
			- Active attempts to check and validate reasoning steps
		- <mark style="background: #FFF3A3A6;">Dynamic strategy adaptation</mark>
			- Evidence of "aha moments" where the model suddenly shifts its approach to problem-solving
- DeepSeek-R1 reports strong pass@1 and benchmark results competitive with frontier closed models on reasoning-heavy tasks
- Distilled small/medium models show strong gains, with several checkpoints surpassing earlier open baselines
- [[202602201241 - proximal policy optimization|PPO]] vs GRPO

![PPOvsGRPO|700](https://paper-assets.alphaxiv.org/figures/2501.12948v2/img-4.jpeg)

## Take Away

- RL can be a primary driver of reasoning emergence in LLMs, not just a final alignment step
- Multi-stage pipelines combining RL and targeted SFT can preserve reasoning gains while improving usability
- Reinforcement learning incentivises emergent behaviours such as <mark style="background: #FF5582A6;">self-reflection</mark>, <mark style="background: #BBFABBA6;">verification</mark>, and <mark style="background: #FFF3A3A6;">dynamic strategy adaptation</mark>, with models generating longer 'thinking chains' for harder problems
- <mark style="background: #ABF7F7A6;">Bypassing conventional supervised fine-tuning for reasoning tasks can allow LLMs to discover novel and potentially superior problem-solving strategies beyond human cognitive biases</mark>
- Distillation transfers reasoning patterns effectively, making strong reasoning more accessible at smaller scales

## Limitations

- Pure RL variants can produce poor readability and language-mixing artefacts
- Outcome-centric rewards risk reward-hacking, and weak process faithfulness
- Benchmark-heavy evaluation may not fully capture real-world reliability and safety failure modes

## Future Work

- Improve process-level supervision and reward robustness for faithful long-chain reasoning
- Increase stability and multilingual quality without losing reasoning depth
- Study data-efficient distillation and stronger small-model reasoning transfer
