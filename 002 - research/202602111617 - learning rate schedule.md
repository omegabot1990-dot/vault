---
tags:
- note
aliases:
- Learning Rate Schedule
title: learning rate schedule
description: ''
bot: true
parent nodes:
- '[[hyperparameters]]'
published on: null
---

- A learning rate schedule is a rule for changing the learning rate across training steps or epochs
- It balances fast initial progress with stable late-stage convergence
- Schedules usually start larger, then decay to smaller values as training proceeds
- Common schedules are step decay, cosine decay, exponential decay, and one-cycle policy
- Warmup is often used at the start to avoid instability when gradients are noisy
- The schedule interacts with optimizer choice, batch size, and total training budget