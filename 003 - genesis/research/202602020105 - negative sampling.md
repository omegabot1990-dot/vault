---
tags:
  - note
aliases:
  - Negative sampling
title: negative sampling
description:
parent nodes:
  - "[[data]]"
  - "[[fine-tuning]]"
child nodes:
annotation-target:
published on:
---

- [ ] What is contrastive learning?

---
- **Negative Sampling in [[202601282201 - supervised fine-tuning|Supervised Fine-Tuning]]** is a training strategy where, in addition to the standard positive target response, the model is presented with <mark style="background: #FF5582A6;">rejected samples</mark> (negatives) and is trained to **minimise their log-likelihood** (increase their loss) while simultaneously maximising the likelihood of the <mark style="background: #BBFABBA6;">preferred sample</mark> (positive)
- While traditional SFT focuses on **maximising the likelihood of positive expert demonstrations**, negative sampling introduces a <mark style="background: #BBFABBA6;">contrastive or negative signal</mark> to help the model "unlearn" bad behaviours