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
## Summary

- The paper introduces DeepSeek-R1-Zero and DeepSeek-R1 as [[202602231757 - reasoning|reasoning]]-focused [[202602191524 - large language model|LLMs]] [[202602111335 - training|trained]] primarily through [[202602192221 - reinforcement learning|RL]]
- It shows pure RL can induce strong reasoning behaviours, then improves readability and stability with a multi-stage pipeline
- DeepSeek-R1 reaches near-o1-level reasoning results on math and coding benchmarks and enables strong distilled, smaller models

## Problem

- Prior open methods had not matched o1-class reasoning while staying reproducible and scalable
- Pure RL for reasoning without a supervised chain-of-thought warm start was not clearly validated at scale
- Strong reasoning often conflicted with readability, language consistency, and broad assistant alignment

## Method

- Train DeepSeek-R1-Zero from a base model with large-scale [[202602201939 - group relative policy optimization|GRPO]]-style RL and outcome-based [[202602192352 - reward|rewards]]
- Build DeepSeek-R1 via a staged pipeline: cold-start SFT, reasoning RL, [[202602231804 - rejection sampling|rejection-sampled]] [[202601282201 - supervised fine-tuning|SFT]] refresh, then broader RL alignment
- [[202602231948 - distillation|Distil]] reasoning traces and behaviours into smaller, dense [[qwen|Qwen]]/[[llama|Llama]]-family models

## Result

- R1-Zero improves sharply on reasoning metrics from base performance through RL alone
- DeepSeek-R1 reports strong pass@1 and benchmark results competitive with frontier closed models on reasoning-heavy tasks
- Distilled small/medium models show strong gains, with several checkpoints surpassing earlier open baselines

## Take Away

- RL can be a primary driver of reasoning emergence in LLMs, not just a final alignment step
- Multi-stage pipelines combining RL and targeted SFT can preserve reasoning gains while improving usability
- Distillation transfers reasoning patterns effectively, making strong reasoning more accessible at smaller scales

## Limitations

- Pure RL variants can produce poor readability and language-mixing artefacts
- Outcome-centric rewards risk reward-hacking, and weak process faithfulness
- Benchmark-heavy evaluation may not fully capture real-world reliability and safety failure modes

## Future Work

- Improve process-level supervision and reward robustness for faithful long-chain reasoning
- Increase stability and multilingual quality without losing reasoning depth
- Study data-efficient distillation and stronger small-model reasoning transfer
