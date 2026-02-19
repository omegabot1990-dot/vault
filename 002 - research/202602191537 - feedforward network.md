---
tags:
- note
aliases:
- Feedforward Network
- Feed-forward network
title: feedforward network
description: ''
bot: true
parent nodes:
- '[[neural networks]]'
published on: null
---

- A feedforward network maps inputs to outputs through stacked layers with one-way information flow
- It has no recurrent state or cyclic connections, so activations move only from earlier to later layers
- A standard feedforward block applies an affine transform followed by a nonlinearity
- Multilayer perceptrons are canonical feedforward neural networks
- Parameters are trained with backpropagation and gradient-based optimization
- Feedforward networks are widely used for classification, regression, and as submodules inside larger architectures