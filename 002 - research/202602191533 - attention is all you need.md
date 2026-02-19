---
tags:
  - paper
aliases:
  - Attention Is All You Need
title: attention is all you need
description: ""
bot: false
parent nodes:
  - "[[202602102143 - transformer|Transformer]]"
published on: 2017-06-12
---

- [ ] What are sequence models?
- [ ] [Attention Is All You Need](https://www.youtube.com/watch?v=iDulhoQ2pro)
- [ ] What are encoder-decoder models?
- [ ] What is label smoothing (generalisation)?

---
> [Attention Is All You Need](https://www.alphaxiv.org/abs/1706.03762)

## Summary

- Introduces the [[202602102143 - transformer|Transformer]], an encoder-decoder [[202602010044 - model|model]] built only with [[202602191531 - attention|attention]] and [[202602191537 - feed-forward network|feed-forward layers]]
- Removes recurrence and convolution to <mark style="background: #BBFABBA6;">improve parallelism and long-range dependency modelling</mark>
- Achieves state-of-the-art translation quality with much lower [[202602111335 - training|training]] cost than prior sequence models

<div align="center">
  <img src="https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-21.png" width="500">
</div>

## Problem

- RNN/CNN sequence models are hard to parallelise across sequence positions
- Long dependency paths in recurrent models make optimization and information flow harder
- Existing attention-augmented RNNs still retain recurrent bottlenecks

## Method

- Uses stacked encoder and decoder blocks with [[202602191621 - residual connection|residual connections]] and [[202602191623 - layer normalization|layer normalization]]
- Core operator is scaled dot-product attention

> [!MATH] Attention
> $$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

<div align="center">
  <img src="https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-19.png" width="300">
</div>

- Uses [[202602191619 - multi-head self attention|multi-head attention]] to capture diverse token relations in parallel subspaces

> [!MATH] MHSA
> $$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O$$
> Where,
>  $$head_{i}​=Attention(QW_{i}^{Q}​,KW_{i}^K​,VW_{i}^V​)$$

<div align="center">
  <img src="https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-20.png" width="400">
</div>

- Adds [[202602192054 - positional encoding|positional encoding]] to inject [[202602192100 - token|token]]-order information without recurrence

> [!MATH] Positional Encoding
> $$PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}})$$
> $$PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}})$$

- Each layer in both encoder and decoder includes position-wise feed-forward networks, which apply two linear transformations with a ReLU activation:

> [!MATH] Feed-Forward Network
>$$  
>\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2  
>$$

- The Transformer employs three different types of attention:

1. <mark style="background: #BBFABBA6;">Encoder self-attention</mark>
	1. Each position attends to all positions in the input sequence
2. <mark style="background: #FF5582A6;">Decoder self-attention (masked)</mark>
	1. Each position attends only to earlier positions in the output sequence
3. <mark style="background: #FFF3A3A6;">Encoder-decoder attention (cross-attention)</mark>
	1. Decoder positions attend to all encoder positions

- The model was trained on standard machine translation datasets
	- WMT 2014 English-German (4.5M sentence pairs) and English-French (36M sentences)
- Training utilised 8 NVIDIA P100 GPUs with a carefully designed [[202602111617 - learning rate schedule|learning rate schedule]] that <mark style="background: #D2B3FFA6;">increased linearly for the first 4,000 steps</mark>, then decreased proportionally to the inverse square root of the step number
- Incorporated [[202602111640 - dropout|dropout]] for [[202602111636 - regularization|regularization]] along with label smoothing to improve generalisation

## Result

- 28.4 BLEU on WMT14 En-De, improving prior best systems
- 41.8 BLEU on WMT14 En-Fr with a single model
- <mark style="background: #ABF7F7A6;">Trains faster and parallelises better</mark> than recurrent baselines
	- The base model trained in just 12 hours, demonstrating the efficiency benefits of the attention-based architecture
- They found that <mark style="background: #FFF3A3A6;">multi-head attention significantly outperformed single-head variants</mark>, with 8 heads providing optimal performance
- The <mark style="background: #ADCCFFA6;">dimension of attention keys proved important for model quality</mark>, and <mark style="background: #FF5582A6;">dropout was essential for preventing overfitting</mark>

## Take Away

- Attention-only architectures are sufficient for high-quality sequence transduction
	- <mark style="background: #BBFABBA6;">Self-attention enables unprecedented parallelisation, drastically reducing training times for sequence models</mark>
- Parallel self-attention became the new default backbone for modern [[202602191524 - large language model|LLMs]]

## Limitations

- Self-attention cost scales quadratically with sequence length
- The original model requires substantial compute for large-scale training
- <mark style="background: #FF5582A6;">Positional encoding design in the paper is fixed and may limit extrapolation</mark>

## Future Work

- Efficient/sparse attention for long-context scaling
- Better positional schemes and length generalisation
- Broader transfer from translation to general language modelling and reasoning