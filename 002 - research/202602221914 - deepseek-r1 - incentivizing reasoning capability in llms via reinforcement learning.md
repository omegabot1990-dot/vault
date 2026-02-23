---
tags:
- paper
aliases:
- DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
title: deepseek-r1 - incentivizing reasoning capability in llms via reinforcement learning
description: ''
bot: true
parent nodes:
- '[[deepseek]]'
published on: 2025-01-22
---

## Topics (not in KG yet)

- [ ] DeepSeek-R1-Zero
- [ ] cold-start data
- [ ] rejection sampling
- [ ] majority voting
- [ ] reasoning-oriented reinforcement learning
- [ ] distillation

## Summary

- The paper introduces DeepSeek-R1-Zero and DeepSeek-R1 as reasoning-focused LLMs trained primarily through [[202602192221 - reinforcement learning|RL]]
- It shows pure RL can induce strong reasoning behaviours, then improves readability and stability with a multi-stage pipeline
- DeepSeek-R1 reaches near-o1-level reasoning results on math and coding benchmarks and enables strong distilled smaller models

## Problem

- Prior open methods had not matched o1-class reasoning while staying reproducible and scalable
- Pure RL for reasoning without supervised chain-of-thought warm start was not clearly validated at scale
- Strong reasoning often conflicted with readability, language consistency, and broad assistant alignment

## Method

- Train DeepSeek-R1-Zero from a base model with large-scale GRPO-style RL and outcome-based rewards
- Build DeepSeek-R1 via a staged pipeline: cold-start SFT, reasoning RL, rejection-sampled SFT refresh, then broader RL alignment
- Distill reasoning traces and behaviors into smaller dense Qwen/Llama-family models

## Result

- R1-Zero improves sharply on reasoning metrics from base performance through RL alone
- DeepSeek-R1 reports strong pass@1 and benchmark results competitive with frontier closed models on reasoning-heavy tasks
- Distilled small/medium models show strong gains, with several checkpoints surpassing earlier open baselines

## Take Away

- RL can be a primary driver of reasoning emergence in LLMs, not just a final alignment step
- Multi-stage pipelines combining RL and targeted SFT can preserve reasoning gains while improving usability
- Distillation transfers reasoning patterns effectively, making strong reasoning more accessible at smaller scales

## Limitations

- Pure RL variants can produce poor readability and language-mixing artifacts
- Outcome-centric rewards risk reward hacking and weak process faithfulness
- Benchmark-heavy evaluation may not fully capture real-world reliability and safety failure modes

## Future Work

- Improve process-level supervision and reward robustness for faithful long-chain reasoning
- Increase stability and multilingual quality without losing reasoning depth
- Study data-efficient distillation and stronger small-model reasoning transfer
