---
tags:
  - deep_learning
aliases:
  - Feedforward Network
  - Feed-forward network
title: feedforward network
description: ""
bot: false
parent nodes:
  - "[[202602061153 - neural network|Neural Network]]"
published on:
---

- [ ] What is an MLP?

---
- A feedforward network maps inputs to outputs through stacked layers with one-way information flow
- It has <mark style="background: #BBFABBA6;">no recurrent state or cyclic connections</mark>, so activations move only from earlier to later layers
- A standard feedforward block applies an [[202602111417 - affine map|affine transform]] followed by a nonlinearity
- Multilayer perceptrons are canonical feedforward [[202602061153 - neural network|neural networks]]
- [[202602111314 - model parameters|Parameters]] are trained with [[202602111557 - backpropagation|backpropagation]] and [[202602111605 - optimization algorithms|gradient-based optimization]]
- Feedforward networks are widely used for [[202602120054 - classification|classification]], [[202602120056 - regression|regression]], and as submodules inside larger architectures