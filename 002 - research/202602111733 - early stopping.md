---
tags:
- note
aliases:
- Early Stopping
title: early stopping
description: ''
bot: true
parent nodes:
- '[[training]]'
published on: null
---

- Early stopping is a regularization strategy that stops training when validation performance stops improving
- It prevents overfitting by avoiding unnecessary optimization after generalization peaks
- A common rule monitors validation loss with a patience window and minimum improvement threshold
- The best checkpoint is typically the model state with the best validation metric, not the last step
- Early stopping reduces compute usage while often improving test performance
- It is frequently combined with weight decay, dropout, and learning-rate schedules