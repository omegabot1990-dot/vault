---
tags:
  - deep_learning
aliases:
  - Neural Network
title: neural network
description: ""
parent nodes:
  - "[[neural networks]]"
published on:
---

- A neural network is a machine learning [[202602010044 - model|model]] that stacks simple "neurons" in layers and learns pattern-recognising weights and biases from data to map inputs to outputs [^1]
- Neural networks are <mark style="background: #FF5582A6;">function approximators</mark> built from layers of interconnected units (neurons)
- Each layer applies an affine transformation followed by a nonlinear activation
- Depth enables hierarchical feature learning from simple to complex patterns

![Deep Neural Networks](https://assets.ibm.com/is/image/ibm/ICLH_Diagram_Batch_01_03-DeepNeuralNetwork:16x9?fmt=png-alpha&dpr=on%2C2&wid=1536&hei=864)

- Parameters are learned from data using backpropagation and gradient-based optimization
- Common architectures include multilayer perceptrons, convolutional networks, and transformers
- Model quality depends on architecture, data quality, optimization, and regularization choices


[^1]: https://www.ibm.com/think/topics/neural-networks#:~:text=A%20neural%20network%20is%20a%20machine%20learning%20model%20that%20stacks%20simple%20%22neurons%22%20in%20layers%20and%20learns%20pattern%2Drecognizing%20weights%20and%20biases%20from%20data%20to%20map%20inputs%20to%20outputs.