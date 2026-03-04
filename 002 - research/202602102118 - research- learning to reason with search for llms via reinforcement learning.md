---
tags:
  - paper
aliases:
  - "ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning"
title: research- learning to reason with search for llms via reinforcement learning
description: ""
bot: false
parent nodes:
  - "[[202602232025 - reinforcement learning verifiable rewards|RLVR]]"
published on: 2025-03-25
---

- [ ] [[reinforcement learning verifiable rewards|Similar Papers]]

---
> [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](https://www.alphaxiv.org/abs/2503.19470)
> [GitHub](https://github.com/Agent-RL/ReCall)

## Summary

- Trains an LLM to interleave reasoning with external search using [[202602192221 - reinforcement learning|reinforcement learning]]
- <mark style="background: #BBFABBA6;">Optimises tool-use decisions without supervised intermediate reasoning traces</mark>
- Targets <mark style="background: #FF5582A6;">multi-hop</mark> question answering with an outcome reward

## Problem

- Multi-step RAG often relies on hand-designed prompts or fixed heuristics for search
- Supervised tool-use datasets with step-by-step traces are expensive to collect
- [[202602191524 - large language model|LLMs]] hallucinate on knowledge-heavy multi-hop questions without strong retrieval

## Method

- Trains LLMs to dynamically incorporate internal thought processes, search query formulation, and integration of retrieved information into a structured reasoning chain using specific tags
- Treats search operations as part of the reasoning chain using explicit tags
	- `<think> ... </think>`
	- `<search> ... </search>`
		- The framework uses Wikipedia as the knowledge base, accessed through the FlashRAG toolkit with an E5-base-v2 retriever
	- `<result> ... </result>`
- Uses [[202602201939 - group relative policy optimization|GRPO]] to optimise behaviour with an outcome reward plus a [[202602181827 - kl divergence|KL]] penalty
	- <mark style="background: #BBFABBA6;">Answer Reward</mark>
		- [[202602011551 - f1|F1 score]] between the final answer and ground truth
	- <mark style="background: #FFF3A3A6;">Format Reward</mark>
		- Small bonus (0.1) for correct formatting when the answer is incorrect

> [!MATH] Loss
> $$\mathcal{L}(\theta) = \mathbb{E}_{y \sim \pi_\theta} \left[ A(y) \log \pi_\theta(y|x) \right] - \beta \cdot \text{KL}(\pi_\theta || \pi_{\text{ref}})$$

- Masks retrieved result tokens in the [[202602120145 - loss|loss]], so learning pressure focuses on decisions rather than copying evidence
- Trained on a single dataset
	- Trained exclusively on the MuSiQue training set
- Evaluation
	- HotpotQA
	- 2WikiMultiHopQA
	- Bamboogle

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-1.jpeg)

## Result

- Reports higher multi-hop QA performance than baselines across multiple benchmarks
	- Average improvements ranging from 14.82% to 15.81% in Exact Match (EM) and 15.46% to 17.56% in LLM-as-a-Judge (LJ)
- Evaluated on several multi-hop QA datasets
- Search usage increases during [[202602111335 - training|training]], suggesting learned reliance on retrieval
- Analysis of training progression showed [[202602010044 - model|models]] increasing their response length and the average number of search operations per rollout, indicating a learned ability to engage in more extensive and iterative reasoning
- Shows remarkable generalisation ability

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-0.jpeg)

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-2.jpeg)

## Take Away

- Outcome-reward RL can be enough to induce useful search behaviour
- <mark style="background: #FF5582A6;">Learns fundamental reasoning with search capabilities rather than dataset-specific patterns</mark>
- Explicit structure for tool calls may reduce prompt brittleness
- Advanced reasoning capabilities, such as self-elicited reflection and self-correction behaviours, can emerge under RL fine-tuning

## Limitations

- [[202602192352 - reward|Reward]] based on answer overlap may not fit tasks with subjective or long-form targets
- Depends on the quality and coverage of the external knowledge source
	- Reliance on Wikipedia as the primary knowledge source, while standard for evaluation, limits immediate applicability to specialised domains
- Reinforcement learning adds compute and engineering costs

## Future Work

- <mark style="background: #FF5582A6;">Improve reward design</mark> beyond simple overlap metrics
- <mark style="background: #FFF3A3A6;">Extend to broader tools and more diverse knowledge sources</mark>
- Reduce training cost and <mark style="background: #ABF7F7A6;">test smaller models</mark>
