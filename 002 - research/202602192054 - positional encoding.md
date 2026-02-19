---
tags:
  - transformers
aliases:
  - Positional Encoding
title: positional encoding
description: ""
bot: false
parent nodes:
  - "[[202602102143 - transformer|Transformer]]"
published on:
---

- Positional encoding injects token-order information into [[202602102143 - transformer|transformer]] inputs
- It is needed because [[202602191531 - attention|self-attention]] alone is permutation-invariant over token positions
- The original transformer uses fixed sinusoidal encodings added to token embeddings

> [!MATH] Positional Encoding
> $$PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}})$$
> $$PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}})$$

- Learned positional embeddings are also common and can improve task adaptation
- Positional schemes affect length extrapolation, locality bias, and long-context behaviour
- Modern variants include:
	- Relative positions
	- Rotary embeddings
	- ALiBi-style biases