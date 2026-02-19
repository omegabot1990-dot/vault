---
tags:
  - deep_learning
aliases:
  - Residual Connection
  - Skip Connection
title: residual connection
description: ""
bot: false
parent nodes:
  - "[[residual connections]]"
published on:
---

- A residual connection adds a block input directly to its transformed output
- It creates a shortcut path that improves gradient flow in [[202602061153 - neural network|deep networks]]
- A common form is as below where $F$ is a nonlinear sublayer

> [!MATH] Residual Connection
> $$y = x + F(x)$$

- Residual paths help optimization by making identity mapping easy to represent
- In [[202602102143 - transformer|transformers]], residual connections wrap [[202602191531 - attention|attention]] and [[202602191537 - feedforward network|feedforward]] sublayers
- Residual design improves [[202602111335 - training|training]] stability and depth scaling