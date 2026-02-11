---
tags:
- note
aliases:
- Optimization Algorithms
title: optimization algorithms
description: ''
bot: true
parent nodes:
- '[[optimizer]]'
published on: null
---

- Optimization algorithms are methods that update model parameters to minimize an objective function
- They use gradients and update rules to control step direction, scale, and stability
- Core families are first-order methods such as SGD, momentum SGD, RMSProp, Adam, and AdamW
- Different optimizers trade off convergence speed, memory cost, and generalization behavior
- Hyperparameters like learning rate and weight decay strongly influence optimizer performance
- In deep learning, mini-batch training is typically combined with an optimizer and a learning-rate schedule