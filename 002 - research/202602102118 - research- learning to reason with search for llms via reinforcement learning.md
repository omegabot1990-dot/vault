---
tags:
- paper
aliases:
- "ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning"
title: research- learning to reason with search for llms via reinforcement learning
description: ''
bot: true
parent nodes:
- '[[reinforcement learning verifiable rewards]]'
published on: 2025-03-25
---

## Topics (not in KG yet)

- [ ] agents
- [ ] reasoning
- [ ] reinforcement-learning
- [ ] transformers
- [ ] retrieval augmented generation
- [ ] retrieval
- [ ] dense retriever
- [ ] multi-hop question answering
- [ ] external search
- [ ] FlashRAG
- [ ] E5-base-v2
- [ ] Wikipedia
- [ ] Qwen2.5
- [ ] group relative policy optimisation
- [ ] tool use

## Summary

- Trains an LLM to interleave reasoning with external search using reinforcement learning
- Optimizes tool-use decisions without supervised intermediate reasoning traces
- Targets multi-hop question answering with an outcome reward

## Problem

- Multi-step RAG often relies on hand-designed prompts or fixed heuristics for search
- Supervised tool-use datasets with step-by-step traces are expensive to collect
- LLMs hallucinate on knowledge-heavy multi-hop questions without strong retrieval

## Method

- Treats search operations as part of the reasoning chain using explicit tags
	- `<think> ... </think>`
	- `<search> ... </search>`
	- `<result> ... </result>`
- Uses GRPO to optimize behavior with an outcome reward plus a KL penalty
- Masks retrieved result tokens in the loss so learning pressure focuses on decisions rather than copying evidence

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-1.jpeg)

## Result

- Reports higher multi-hop QA performance than baselines across multiple benchmarks
- Trained on a single dataset and evaluated on several multi-hop QA datasets
- Search usage increases during training, suggesting learned reliance on retrieval

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-0.jpeg)

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-2.jpeg)

## Take Away

- Outcome-reward RL can be enough to induce useful search behavior
- Explicit structure for tool calls may reduce prompt brittleness
- Self-correction behaviors can emerge under RL fine-tuning

## Limitations

- Reward based on answer overlap may not fit tasks with subjective or long-form targets
- Depends on the quality and coverage of the external knowledge source
- Reinforcement learning adds compute and engineering cost

## Future Work

- Improve reward design beyond simple overlap metrics
- Extend to broader tools and more diverse knowledge sources
- Reduce training cost and test smaller models
