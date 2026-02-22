---
tags:
  - training
aliases:
  - Reinforcement Learning Human Feedback
  - Reinforcement Learning from Human Feedback
  - RLHF
title: reinforcement learning human feedback
description: ""
bot: true
parent nodes:
  - "[[202602191644 - post-training|Post-Training]]"
published on:
---

- Reinforcement learning from human feedback (RLHF) aligns [[202602010044 - model|model]] behaviour to human preferences after [[202602030230 - pre-training|pre-training]]
- A typical RLHF pipeline has [[202601282201 - supervised fine-tuning|supervised fine-tuning]], [[202602201334 - reward model|reward-model]] training from preference rankings, and then [[202602200001 - policy optimization|policy optimization]]
- The reward model approximates human preference signals and guides optimization of the language model policy
- PPO-style updates are commonly used to improve helpfulness while constraining drift from a reference model
- <mark style="background: #BBFABBA6;">RLHF improves instruction following and subjective quality</mark>, but <mark style="background: #FF5582A6;">can introduce reward hacking and preference bias</mark>
- Evaluation combines automatic metrics with human preference judgments and safety checks


[^1]: [Reinforcement Learning with Human Feedback (RLHF), Clearly Explained!!!](https://www.youtube.com/watch?v=qPN_XZcJf_s&list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1&index=25)