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
- In self-attention, queries, keys, and values are all derived from the same token sequence
- <mark style="background: #BBFABBA6;">Each head captures different relation patterns</mark>, and then the <mark style="background: #FF5582A6;">head outputs are concatenated and projected</mark>
- This improves representation capacity versus a single-head attention block at a similar model width
- Scaled dot-product attention is used inside each head with [[202602111530 - softmax|softmax]]-normalised similarity scores
- MHSA is a core component of [[202602102143 - transformer|transformer]] encoder and decoder blocks


![](https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-20.png)

> [!MATH] MHSA
> $$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O$$
> Where,
>  $$head_{i}​=Attention(QW_{i}^{Q}​,KW_{i}^K​,VW_{i}^V​)$$