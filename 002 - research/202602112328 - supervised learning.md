---
tags:
- note
aliases:
- Supervised Learning
title: supervised learning
description: ''
bot: true
parent nodes:
- '[[training]]'
published on: null
---

- Supervised learning trains a model from labeled pairs $(x,y)$ to predict targets from inputs
- The objective is to minimize a task-specific loss and generalize to unseen examples from the same distribution
- Main task types are classification for discrete labels and regression for continuous values
- Typical workflow includes train/validation/test splits, optimization on training data, and model selection by validation metrics
- Common losses include cross-entropy for classification and mean squared error for regression
- Generalization quality depends on data quality, model capacity, regularization, and optimization setup