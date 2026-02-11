---
tags:
  - deep_learning
aliases:
  - Data Augmentation
title: data augmentation
description: ""
bot: false
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- Data augmentation expands effective [[202602111335 - training|training]] data by <mark style="background: #BBFABBA6;">applying label-preserving transformations to inputs</mark>
- It acts as [[202602111636 - regularization|regularization]] by exposing the model to diverse variations and reducing [[202602111639 - underfitting|overfitting]]
- Common image augmentations are random:
	- Crop
	- Flip
	- Rotation
	- Color jitter
	- Scaling
- In text and speech, augmentation can include:
	- Masking
	- Paraphrasing
	- Noise injection
	- Speed perturbation
- Good augmentation policies improve robustness and generalisation without changing task semantics
- Excessive or invalid augmentations can hurt learning if transformed samples no longer match true labels