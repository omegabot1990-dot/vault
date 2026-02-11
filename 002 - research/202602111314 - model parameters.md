---
tags:
  - deep_learning
aliases:
  - Model Parameters
title: model parameters
description: ""
bot: false
parent nodes:
  - "[[202602010044 - model|Model]]"
published on:
---

- [[202602010044 - model|Model]] parameters are <mark style="background: #BBFABBA6;">values learned from data</mark> during [[202602111335 - training|training]] [^1]
- They are updated by optimisation steps to reduce the [[202602010047 - objective function|loss]]
- In [[202602061153 - neural network|neural networks]], [[202602111358 - weights and biases|weights and biases]] are model parameters [^2]
- Model parameters differ from [[202602111256 - hyperparameters|hyperparameters]], which are set before training
- Parameter count <mark style="background: #FFF3A3A6;">controls model capacity and memory/computation cost</mark>
- Learned parameter values determine the final function used at [[202602111350 - inference|inference]]

[^1]: https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac/#:~:text=they%20are%20learned%20or%20estimated%20purely%20from%20the%20data%20during%20training%20as%20the%20algorithm%20used%20tries%20to%20learn%20the%20mapping%20between%20the%20input%20features%20and%20the%20labels%20or%20targets
[^2]: https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac/#:~:text=Weights%20and%20biases%20of%20a%20nn