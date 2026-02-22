---
tags:
  - training
aliases:
  - Residual Dropouts
title: residual dropouts
description: ""
bot: false
parent nodes:
  - "[[202602111640 - dropout|Dropout]]"
published on:
---

- Residual dropout applies [[202602111640 - dropout|dropout]] to the output of a sublayer before adding it through a [[202602191621 - residual connection|residual connection]]
- In [[202602102143 - transformer|Transformers]], it is commonly used around [[202602191531 - attention|attention]] and [[202602191537 - feed-forward network|feedforward]] sublayers to regularize deep stacks

> [!MATH] Residual Dropout
> $$\text{Output} = \text{LayerNorm}(x + \text{Dropout}(\text{SubLayer}(x)))$$

- The residual branch is [[202512271205 - stochastic|stochastically]] thinned during [[202602111335 - training|training]], while the skip path preserves gradient flow
- This reduces co-adaptation and [[202602010049 - overfitting|overfitting]] without removing the stabilising effect of residual shortcuts
- In [[202602111350 - inference|inference]], dropout is disabled, and full residual computations are used [[202512271203 - deterministic|deterministically]]
- Proper dropout rates are task- and scale-dependent; too much residual dropout can hurt optimization and [[202602111639 - underfitting|underfit]]


