---
tags:
- note
aliases:
- Positional Encoding
title: positional encoding
description: ''
bot: true
parent nodes:
- '[[transformers]]'
published on: null
---

- Positional encoding injects token-order information into transformer inputs
- It is needed because self-attention alone is permutation-invariant over token positions
- The original transformer uses fixed sinusoidal encodings added to token embeddings
- Learned positional embeddings are also common and can improve task adaptation
- Positional schemes affect length extrapolation, locality bias, and long-context behavior
- Modern variants include relative positions, rotary embeddings, and ALiBi-style biases