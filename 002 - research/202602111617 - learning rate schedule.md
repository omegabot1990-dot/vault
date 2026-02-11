---
tags:
  - deep_learning
aliases:
  - Learning Rate Schedule
title: learning rate schedule
description: ""
bot: true
parent nodes:
  - "[[202602111600 - learning rate|Learning Rate]]"
published on:
---

- [ ] What is step decay?
- [ ] What is cosine decay?
- [ ] What is exponential decay?
- [ ] One-cycle policies?

---
- A learning rate schedule is a rule for changing the learning rate across training steps or epochs
- It balances fast initial progress with stable late-stage convergence
- Schedules usually start larger, then decay to smaller values as training proceeds
- Common schedules include:
	- Step decay
	- Cosine decay
	- Exponential decay
	- [[202602011426 - warmup|Warmup]]
	- One-cycle policies
- The schedule interacts with [[202602111605 - optimization algorithms|optimizer]] choice, batch size, and total training budget