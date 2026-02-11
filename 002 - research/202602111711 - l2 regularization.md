---
tags:
  - deep_learning
aliases:
  - L2 regularization
title: l2 regularization
description: ""
bot: true
parent nodes:
  - "[[202602111636 - regularization|Regularization]]"
published on:
---

- L2 regularisation adds a <mark style="background: #FF5582A6;">penalty proportional to squared parameter norms</mark> to the [[202602111335 - training|training]] [[202602010047 - objective function|objective]]
- It discourages large weights and helps reduce [[202602010049 - overfitting|overfitting]]
- In deep learning, L2 regularisation is commonly implemented through [[202602111634 - weight decay|weight decay]]
- The regularisation coefficient controls penalty strength and is tuned as a [[202602111256 - hyperparameters|hyperparameter]]
- Stronger L2 regularisation can improve generalisation, but too much causes [[202602010049 - overfitting|overfitting]]
- It is often combined with other techniques such as [[202602111640 - dropout|dropout]], augmentation, and early stopping