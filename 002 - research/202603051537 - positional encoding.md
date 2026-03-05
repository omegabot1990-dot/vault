---
tags:
  - transformers
aliases:
  - Positional Encoding
title: positional encoding
description: ""
bot: false
parent nodes:
  - "[[202602191531 - attention|Attention]]"
published on:
---

- Positional encoding injects token-order information into sequence representations used by [[202602191531 - attention|attention]] models
- <mark style="background: #FF5582A6;">Since self-attention is permutation-invariant, positional signals are needed to distinguish different token orders</mark>
- Encodings can be fixed sinusoidal vectors, learned embeddings, or relative/rotary position schemes
- They let models represent locality, distance, and order-dependent patterns in text
- Choice of positional method affects long-context generalisation and extrapolation behaviour
- Modern [[202602191524 - large language model|LLMs]] often use rotary-style encodings for efficient relative position handling