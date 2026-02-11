---
tags:
- note
aliases:
- Data Augmentation
title: data augmentation
description: ''
bot: true
parent nodes:
- '[[training]]'
published on: null
---

- Data augmentation expands effective training data by applying label-preserving transformations to inputs
- It acts as regularization by exposing the model to diverse variations and reducing overfitting
- Common image augmentations are random crop, flip, rotation, color jitter, and scaling
- In text and speech, augmentation can include masking, paraphrasing, noise injection, or speed perturbation
- Good augmentation policies improve robustness and generalization without changing task semantics
- Excessive or invalid augmentations can hurt learning if transformed samples no longer match true labels