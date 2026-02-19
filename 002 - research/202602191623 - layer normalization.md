---
tags:
  - deep_learning
aliases:
  - Layer Normalization
  - LayerNorm
title: layer normalization
description: ""
bot: false
parent nodes:
  - "[[normalization]]"
published on:
---

- [ ] What is BatchNorm?

---
- Layer normalization normalizes activations within each token across feature dimensions
- It stabilises hidden-state scale and improves optimization in deep sequence models
- Unlike batch normalization, it does not depend on batch statistics and works well for variable-length sequences
- A normalized activation is followed by learned scale and shift parameters
- [[202602102143 - transformer|Transformers]] apply layer normalization around [[202602191531 - attention|attention]] and [[202602191537 - feed-forward network|feedforward]] sublayers
- Layer normalization helps [[202602111335 - training|training]] stability, especially at depth and with long contexts