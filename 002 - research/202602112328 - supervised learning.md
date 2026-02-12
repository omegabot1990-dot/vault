---
tags:
  - training
aliases:
  - Supervised Learning
title: supervised learning
description: ""
bot: false
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- [ ] What is MSE?

---
- We estimate the [[202602080132 - conditional probability|conditional probability]] of a label given input features
- For a <mark style="background: #BBFABBA6;">Data Point</mark> (Example or Sample), there is a set of attributes we call <mark style="background: #FF5582A6;">Features</mark> (Covariates), and our objective is to predict another feature, called the <mark style="background: #FFF3A3A6;">Label</mark> (Target), that is not part of the input space
- Supervised learning [[202602111335 - training|trains]] a [[202602010044 - model|model]] from labelled pairs $(x,y)$ to predict targets from inputs
- The objective is to minimise a task-specific [[202602010047 - objective function|loss]] and generalise to unseen examples from the same [[202602072325 - distribution|distribution]]
- Main task types are [[202602120054 - classification|classification]] for discrete labels and [[202602120056 - regression|regression]] for continuous values
- Typical workflow includes train/validation/test splits, [[202602111605 - optimization algorithms|optimization]] on training data, and model selection by validation metrics
- Common losses include [[202602120102 - cross-entropy|cross-entropy]] for classification and mean-squared error for regression
- Generalisation quality depends on data quality, [[202602111314 - model parameters|model capacity]], [[202602111636 - regularization|regularization]], and optimization setup
