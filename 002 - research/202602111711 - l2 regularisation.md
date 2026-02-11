---
tags:
- note
aliases:
- L2 regularisation
- L2 regularization
title: l2 regularisation
description: ''
bot: true
parent nodes:
- '[[hyperparameters]]'
published on: null
---

- L2 regularisation adds a penalty proportional to squared parameter norms to the training objective
- It discourages large weights and helps reduce overfitting
- In deep learning, L2 regularisation is commonly implemented through weight decay
- The regularisation coefficient controls penalty strength and is tuned as a hyperparameter
- Stronger L2 regularisation can improve generalization but too much causes underfitting
- It is often combined with other techniques such as dropout, augmentation, and early stopping