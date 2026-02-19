---
tags:
- note
aliases:
- Reinforcement Learning Human Feedback
- Reinforcement Learning from Human Feedback
- RLHF
title: reinforcement learning human feedback
description: ''
bot: true
parent nodes:
- '[[large language models]]'
published on: null
---

- Reinforcement learning from human feedback (RLHF) aligns model behavior to human preferences after pre-training
- A typical RLHF pipeline has supervised fine-tuning, reward-model training from preference rankings, then policy optimization
- The reward model approximates human preference signals and guides optimization of the language model policy
- PPO-style updates are commonly used to improve helpfulness while constraining drift from a reference model
- RLHF improves instruction following and subjective quality but can introduce reward hacking and preference bias
- Evaluation combines automatic metrics with human preference judgments and safety checks