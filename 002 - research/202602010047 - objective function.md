---
tags:
  - training
aliases:
  - Objective Function
  - Cost Function
  - Loss Function
title: objective function
description: ""
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- Objective Functions define a <mark style="background: #BBFABBA6;">formal measure of how good or bad the predicted Label is</mark>
	- Generally framed as lower-the-better, hence called <mark style="background: #BBFABBA6;">Loss Functions</mark>
	- When it's harder to optimise because of non-differentiability or other complications, we might use a <mark style="background: #FF5582A6;">Surrogate Objective</mark>
- Loss Function $L$
	- Computed on a <mark style="background: #FFF3A3A6;">single training example</mark>
	- It measures how "wrong" the prediction was for one specific row of data
- Cost Function $J$ 
	- The <mark style="background: #ABF7F7A6;">average of all loss functions across the entire training set</mark> (often with a [[202602111636 - regularization|regularization]] term added)