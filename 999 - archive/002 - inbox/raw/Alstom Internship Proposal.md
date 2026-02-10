---
tags:
  - inbox
  - work
description: alstom proposal
due date: 2026-01-12
start date:
end date:
status: Done
importance level: important
urgency level: urgent
task type: capture
story points: 3
parent nodes:
child nodes:
recurrent:
---

## Domain Adaptation of Large Language Models focusing on Tool Use

Large Language Models have become ubiquitous in today's world. Gemini, ChatGPT, Claude, etc., spend millions on data and compute to pre-train their flagship models, which is often not affordable for most industries. Data privacy concerns, along with pre-training costs, have slowed the adoption of LLMs in many industries[^1]. In this study, we aim to explore the potential of post-training open-source foundational models for domain-specialised use cases. We will focus on models in the 1B to 7B range due to computational constraints. We will perform Domain Adaptive Pre-Training (DAPT)[^2] with Low Rank Adaptation (LoRA)[^3] as a preliminary stage to teach the LLM domain-based jargon. Our main objective is to explore Reinforcement Learning (RL) as a means of enabling reasoning in a small model[^4]. We will explore Supervised Fine Tuning (SFT), SFT + RL and pure RL and compare the results. Here, we will use Reinforcement Learning Verifiable Rewards (RLVR)[^4] with Group Relative Proximal Policy (GRPO)[^4], in which tool use will be a special case of a verifiable domain.


[^1]: [Domain Specialization as the Key to Make Large Language Models Disruptive: A Comprehensive Survey](https://arxiv.org/abs/2305.18703)
[^2]: [Continual Pre-training of Language Models](https://arxiv.org/abs/2302.03241)
[^3]: [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
[^4]: [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)