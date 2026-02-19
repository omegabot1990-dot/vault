---
tags:
- note
aliases:
- Layer Normalization
- LayerNorm
title: layer normalization
description: ''
bot: true
parent nodes:
- '[[transformers]]'
published on: null
---

- Layer normalization normalizes activations within each token across feature dimensions
- It stabilizes hidden-state scale and improves optimization in deep sequence models
- Unlike batch normalization, it does not depend on batch statistics and works well for variable-length sequences
- A normalized activation is followed by learned scale and shift parameters
- Transformers apply layer normalization around attention and feedforward sublayers
- Layer normalization helps training stability, especially at depth and with long contexts