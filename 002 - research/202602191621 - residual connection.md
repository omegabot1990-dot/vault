---
tags:
- note
aliases:
- Residual Connection
- Skip connection
title: residual connection
description: ''
bot: true
parent nodes:
- '[[transformers]]'
published on: null
---

- A residual connection adds a block input directly to its transformed output
- It creates a shortcut path that improves gradient flow in deep networks
- A common form is $y = x + F(x)$ where $F$ is a nonlinear sublayer
- Residual paths help optimization by making identity mapping easy to represent
- In transformers, residual connections wrap attention and feedforward sublayers
- Residual design improves training stability and depth scaling