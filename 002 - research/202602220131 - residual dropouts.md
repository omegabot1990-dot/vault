---
tags:
- note
aliases:
- Residual Dropouts
title: residual dropouts
description: ''
bot: true
parent nodes:
- '[[202602111640 - dropout|Dropout]]'
published on: null
---

- Residual dropout applies dropout to the output of a sublayer before adding it through a residual connection
- In Transformers, it is commonly used around attention and feedforward sublayers to regularize deep stacks
- The residual branch is stochastically thinned during training while the skip path preserves gradient flow
- This reduces co-adaptation and overfitting without removing the stabilizing effect of residual shortcuts
- At inference, dropout is disabled and full residual computations are used deterministically
- Proper dropout rates are task- and scale-dependent; too much residual dropout can hurt optimization and underfit