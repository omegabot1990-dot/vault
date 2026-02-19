---
tags:
- note
aliases:
- Multi-Head Self Attention
- MHSA
title: multi-head self attention
description: ''
bot: true
parent nodes:
- '[[transformers]]'
published on: null
---

- Multi-head self attention applies attention in parallel across multiple learned projection subspaces
- In self-attention, queries, keys, and values are all derived from the same token sequence
- Each head captures different relation patterns, then head outputs are concatenated and projected
- This improves representation capacity versus a single-head attention block at similar model width
- Scaled dot-product attention is used inside each head with softmax-normalized similarity scores
- MHSA is a core component of transformer encoder and decoder blocks