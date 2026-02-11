---
tags:
  - deep_learning
aliases:
  - Early Stopping
title: early stopping
description: ""
bot: false
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- Early stopping is a [[202602111636 - regularization|regularization]] strategy that stops [[202602111335 - training|training]] when validation performance stops improving
- It prevents [[202602010049 - overfitting|overfitting]] by avoiding unnecessary [[202602111605 - optimization algorithms|optimization]] after generalisation peaks
- A common rule monitors validation loss with a patience window and a minimum improvement threshold
- The <mark style="background: #FF5582A6;">best checkpoint is typically the model state with the best validation metric, not the last step</mark>
- Early stopping reduces compute usage while often improving test performance
- It is frequently combined with [[202602111634 - weight decay|weight decay]], [[202602111640 - dropout|dropout]], and [[202602111617 - learning rate schedule|learning-rate schedules]]