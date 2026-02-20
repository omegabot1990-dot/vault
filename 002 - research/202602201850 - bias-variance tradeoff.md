---
tags:
- note
aliases:
- Bias-Variance Tradeoff
title: bias-variance tradeoff
description: ''
bot: true
parent nodes:
- '[[neural networks]]'
published on: null
---

- The bias-variance tradeoff describes how model error decomposes into underfitting bias and overfitting variance
- High-bias models are too rigid and miss underlying structure, while high-variance models overreact to sample noise
- Increasing model capacity often lowers bias but can raise variance unless regularized
- Good generalization balances representational power with inductive constraints and sufficient data
- Regularization, data augmentation, early stopping, and ensembling help reduce variance
- In practice, validation performance guides the operating point on the bias-variance spectrum