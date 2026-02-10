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
published on: null
---

## Topics (not in KG yet)

- [ ] agents
- [ ] chain-of-thought
- [ ] Computer Science
- [ ] cs.AI
- [ ] cs.CL
- [ ] instruction-tuning
- [ ] reasoning
- [ ] reinforcement-learning
- [ ] tool-use
- [ ] transformers

## Summary

- Trains an LLM to interleave thinking with search using reinforcement learning
- Does not use supervised data for intermediate reasoning or search steps
- Improves multi-hop QA results and shows self-correction during training

## Problem

- Multi-step RAG often relies on hand-designed prompts or fixed heuristics for search
- Supervised tool-use datasets with step-by-step traces are expensive to collect
- LLMs hallucinate on knowledge-heavy multi-hop questions without strong retrieval

## Method

- Treats search as part of the reasoning chain using explicit tags
	- `<think> ... </think>`
	- `<search> ... </search>`
	- `<result> ... </result>`
- Uses GRPO to optimize the policy with an outcome reward and a KL penalty
- Masks retrieved result tokens in the loss so learning targets the model decisions

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-1.jpeg)

## Result

- Improves Exact Match and LLM-as-a-Judge scores over strong multi-hop QA baselines
- Trained on one dataset and still generalizes across multiple benchmarks
- Learns to use more search steps and longer reasoning as training progresses

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-0.jpeg)

![](https://paper-assets.alphaxiv.org/figures/2503.19470v3/img-2.jpeg)

## Take Away

- Reinforcement learning with a simple outcome reward can teach search behavior
- Explicitly structuring search inside the reasoning chain makes tool use more stable
- Reflection and self-correction can emerge without being directly supervised

## Limitations

- Reward based on answer overlap may not fit tasks with subjective or long-form targets
- Depends on the quality and coverage of the external knowledge source
- Reinforcement learning adds compute and engineering cost

## Future Work

- Improve reward design beyond simple overlap metrics
- Extend to broader tools and more diverse knowledge sources
- Reduce training cost and test smaller models
