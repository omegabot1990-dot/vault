---
tags:
  - deep_learning
aliases:
  - Weights and Biases
title: weights and biases
description: ""
bot: true
parent nodes:
  - "[[202602061153 - neural network]]"
published on:
---

- Weights and bias are trainable [[202602111314 - model parameters|model parameters]] in a neural layer
- The weights <mark style="background: #FF5582A6;">scale and mix input features</mark>, while the bias shifts the [[202602111400 - activation|activation]] [^1]
- The weights act like dials that control how strongly each input feature influences the decision [^1]
- A layer computes an [[202602111417 - affine map|affine map]] before applying a nonlinearity

> [!MATH] Weights and Biases
> $$z = Wx + b$$

- During [[202602111335 - training|training]], gradients update both weights and bias to reduce [[202602010047 - objective function|loss]]
- Weight values largely control feature interactions and model capacity
- Bias helps <mark style="background: #BBFABBA6;">move decision boundaries</mark> and represent functions that do not pass through the origin [^2]


[^1]: https://www.ibm.com/think/topics/neural-networks#:~:text=Weights%20act%20like%20dials%20that%20control%20how%20strongly%20each%20input%20feature%20influences%20the%20decision
[^2]: https://www.ibm.com/think/topics/neural-networks#:~:text=Biases%20are%20built%2Din%20values%20that%20shift%20the%20decision%20threshold%2C%20allowing%20a%20neuron%20to%20activate%20even%20if%20the%20inputs%20themselves%20are%20weak