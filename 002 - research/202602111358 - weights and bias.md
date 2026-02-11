---
tags:
- note
aliases:
- Weights and Bias
title: weights and bias
description: ''
bot: true
parent nodes:
- '[[neural networks]]'
published on: null
---

- Weights and bias are trainable model parameters in a neural layer
- The weights scale and mix input features, while the bias shifts the activation
- A layer computes an affine map $z = Wx + b$ before applying a nonlinearity
- During training, gradients update both weights and bias to reduce loss
- Weight values largely control feature interactions and model capacity
- Bias helps move decision boundaries and represent functions that do not pass through the origin