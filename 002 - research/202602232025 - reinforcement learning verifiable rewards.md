---
tags:
- note
aliases:
- Reinforcement Learning Verifiable Rewards
- RLVR
title: reinforcement learning verifiable rewards
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Reinforcement Learning with Verifiable Rewards (RLVR) trains policies using rewards computed by objective checks rather than human preference models
- Rewards are derived from automatic validators such as unit tests, symbolic solvers, exact match, or formal verification signals
- This reduces reward-model misspecification and improves training signal reliability in domains with clear correctness criteria
- RLVR is especially effective for math, coding, and tool-using tasks where outputs can be programmatically verified
- Main limitations are sparse rewards and limited applicability to open-ended subjective tasks
- Practical RLVR setups often combine verifiable rewards with curriculum design, shaping, and controlled exploration