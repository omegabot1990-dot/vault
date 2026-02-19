---
tags:
- paper
aliases:
- Attention Is All You Need
title: attention is all you need
description: ''
bot: true
parent nodes:
- '[[transformers]]'
published on: 2017-06-12
---

## Topics (not in KG yet)

- [ ] self-attention
- [ ] multi-head attention
- [ ] scaled dot-product attention
- [ ] positional encoding
- [ ] encoder-decoder architecture
- [ ] layer normalization

## Summary

- Introduces the Transformer, an encoder-decoder model built only with attention and feed-forward layers
- Removes recurrence and convolution to improve parallelism and long-range dependency modeling
- Achieves state-of-the-art translation quality with much lower training cost than prior sequence models

![](https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-21.png)

## Problem

- RNN/CNN sequence models are hard to parallelize across sequence positions
- Long dependency paths in recurrent models make optimization and information flow harder
- Existing attention-augmented RNNs still retain recurrent bottlenecks

## Method

- Uses stacked encoder and decoder blocks with residual connections and layer normalization
- Core operator is scaled dot-product attention
- Uses multi-head attention to capture diverse token relations in parallel subspaces
- Adds positional encoding to inject order information without recurrence

![](https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-19.png)

## Result

- 28.4 BLEU on WMT14 En-De, improving prior best systems
- 41.8 BLEU on WMT14 En-Fr with a single model
- Trains faster and parallelizes better than recurrent baselines

## Take Away

- Attention-only architectures are sufficient for high-quality sequence transduction
- Parallel self-attention became the new default backbone for modern LLMs

## Limitations

- Self-attention cost scales quadratically with sequence length
- Original model requires substantial compute for large-scale training
- Positional encoding design in the paper is fixed and may limit extrapolation

## Future Work

- Efficient/sparse attention for long-context scaling
- Better positional schemes and length generalization
- Broader transfer from translation to general language modeling and reasoning