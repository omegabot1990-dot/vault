---
tags:
- note
aliases:
- Positional Encoding
title: positional encoding
description: ''
bot: true
parent nodes:
- '[[large language models]]'
published on: null
---

- Positional encoding injects token-order information into sequence representations used by attention models
- Since self-attention is permutation-invariant, positional signals are needed to distinguish different token orders
- Encodings can be fixed sinusoidal vectors, learned embeddings, or relative/rotary position schemes
- They let models represent locality, distance, and order-dependent patterns in text
- Choice of positional method affects long-context generalization and extrapolation behavior
- Modern LLMs often use rotary-style encodings for efficient relative position handling