---
tags:
  - note
aliases:
  - Weights and Bias
title: weights and bias
description: ""
bot: true
parent nodes:
  - "[[202602061153 - neural network]]"
published on:
---

- Weights and bias are trainable [[202602111314 - model parameters|model parameters]] in a neural layer
- The weights scale and mix input features, while the bias shifts the activation
- A layer computes an affine map $z = Wx + b$ before applying a nonlinearity
- During [[202602111335 - training|training]], gradients update both weights and bias to reduce [[202602010047 - objective function|loss]]
- Weight values largely control feature interactions and model capacity
- Bias helps move decision boundaries and represent functions that do not pass through the origin