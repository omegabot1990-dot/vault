---
tags:
  - paper
aliases:
  - Attention Is All You Need
title: attention is all you need
description: ""
bot: true
parent nodes:
  - "[[202602102143 - transformer|Transformer]]"
published on: 2017-06-12
---

- [ ] What are sequence models?
- [ ] [Attention Is All You Need](https://www.youtube.com/watch?v=iDulhoQ2pro)
- [ ] What are encoder-decoder models?
- [ ] What is positional encoding?

## Summary

- Introduces the [[202602102143 - transformer|Transformer]], an encoder-decoder [[202602010044 - model|model]] built only with [[202602191531 - attention|attention]] and [[202602191537 - feedforward network|feed-forward layers]]
- Removes recurrence and convolution to <mark style="background: #BBFABBA6;">improve parallelism and long-range dependency modelling</mark>
- Achieves state-of-the-art translation quality with much lower [[202602111335 - training|training]] cost than prior sequence models

![](https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-21.png)

## Problem

- RNN/CNN sequence models are hard to parallelise across sequence positions
- Long dependency paths in recurrent models make optimization and information flow harder
- Existing attention-augmented RNNs still retain recurrent bottlenecks

## Method

- Uses stacked encoder and decoder blocks with [[202602191621 - residual connection|residual connections]] and [[202602191623 - layer normalization|layer normalization]]
- Core operator is scaled dot-product attention
- Uses [[202602191619 - multi-head self attention|multi-head attention]] to capture diverse token relations in parallel subspaces
- Adds positional encoding to inject order information without recurrence

![](https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-19.png)

## Result

- 28.4 BLEU on WMT14 En-De, improving prior best systems
- 41.8 BLEU on WMT14 En-Fr with a single model
- Trains faster and parallelises better than recurrent baselines

## Take Away

- Attention-only architectures are sufficient for high-quality sequence transduction
- Parallel self-attention became the new default backbone for modern [[202602191524 - large language model|LLMs]]

## Limitations

- Self-attention cost scales quadratically with sequence length
- The original model requires substantial compute for large-scale training
- <mark style="background: #FF5582A6;">Positional encoding design in the paper is fixed and may limit extrapolation</mark>

## Future Work

- Efficient/sparse attention for long-context scaling
- Better positional schemes and length generalisation
- Broader transfer from translation to general language modelling and reasoning