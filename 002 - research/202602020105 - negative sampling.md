---
tags:
  - training
aliases:
  - Negative Sampling
title: negative sampling
description: ""
parent nodes:
  - "[[data]]"
  - "[[fine-tuning]]"
published on:
---

- [ ] What is contrastive learning?

---
- Negative Sampling in [[202601282201 - supervised fine-tuning|supervised fine-tuning]] is a [[202602111335 - training|training]] strategy where, in addition to the standard positive target response, the model is presented with <mark style="background: #FF5582A6;">rejected samples</mark> (negatives) and is trained to <mark style="background: #FFF3A3A6;">minimise</mark> their [[202602061424 - log-likelihood|log-likelihood]] (increase their loss) while simultaneously <mark style="background: #FFF3A3A6;">maximising</mark> the [[202602061241 - likelihood|likelihood]] of the <mark style="background: #BBFABBA6;">preferred sample</mark> (positive)
- While traditional SFT focuses on maximising the likelihood of positive expert demonstrations, negative sampling introduces a <mark style="background: #BBFABBA6;">contrastive or negative signal</mark> to help the model "unlearn" bad behaviours