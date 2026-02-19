---
tags:
  - training
aliases:
  - Causal Language Modelling
  - Next Token Prediction
title: causal language modelling
description: ""
parent nodes:
  - "[[202602050153 - self-supervised learning|Self-supervised learning]]"
published on:
---

- [ ] Update GPT link

---
- Often called [[202602050141 - autoregressive|autoregressive]] modelling, causal language modelling predicts the next token in a sequence based only on the tokens that came before it
- Strictly <mark style="background: #BBFABBA6;">unidirectional (left-to-right)</mark>, the model is "causally masked", so it cannot "cheat" by looking at future words
- Next-token prediction
- Self-supervised learning paradigm
- Examples: Text Generation ([[generative pre-trained transformer|GPT]])