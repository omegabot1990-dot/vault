---
tags:
- note
aliases:
- L2 Early Stopping
title: l2 early stopping
description: ''
bot: true
parent nodes:
- '[[training]]'
published on: null
---

- L2 regularization and early stopping are complementary methods to reduce overfitting
- L2 regularization penalizes large weights during optimization, while early stopping limits over-training time
- In practice, both are tuned together using validation metrics
- Too strong L2 can underfit even with long training, while weak L2 may rely heavily on early stopping
- A common setup is moderate L2 plus patience-based early stopping on validation loss
- This combination often improves stability and generalization compared with using only one of them