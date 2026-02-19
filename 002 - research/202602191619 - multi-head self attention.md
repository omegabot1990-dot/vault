---
tags:
  - transformers
aliases:
  - Multi-Head Self Attention
  - MHSA
title: multi-head self attention
description: ""
bot: false
parent nodes:
  - "[[202602191531 - attention|Attention]]"
published on:
---

- Multi-head self-attention applies [[202602191531 - attention|attention]] in parallel across multiple learned projection subspaces
- In self-attention, <mark style="background: #FF5582A6;">queries, keys, and values</mark> are all derived from the same token sequence
- Each head captures different relation patterns, and then the head outputs are concatenated and projected
- This improves representation capacity versus a single-head attention block at a similar model width
- Scaled dot-product attention is used inside each head with [[202602111530 - softmax|softmax]]-normalized similarity scores
- MHSA is a core component of [[202602102143 - transformer|transformer]] encoder and decoder blocks