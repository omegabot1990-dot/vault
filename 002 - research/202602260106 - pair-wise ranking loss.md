---
tags:
- note
aliases:
- Pair-Wise Ranking Loss
- Pairwise ranking loss
title: pair-wise ranking loss
description: ''
bot: true
parent nodes:
- '[[202602120145 - loss|Loss]]'
published on: null
---

- Pair-wise ranking loss trains a model to score preferred items higher than non-preferred items
- It is defined on pairs $(x^+, x^-)$ instead of single labeled targets
- A common form is margin ranking loss:
  - $$\mathcal{L}=\max(0, m - s(x^+) + s(x^-))$$
- Another common form is logistic pairwise loss:
  - $$\mathcal{L}=\log\left(1+\exp(-(s(x^+) - s(x^-)))\right)$$
- It is widely used in preference learning, recommendation, information retrieval, and RLHF-style ranking data
- Performance depends on pair quality, score calibration, and negative-sampling strategy