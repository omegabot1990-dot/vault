---
tags:
  - note
aliases:
  - Verifiable domains
title: verifiable domains
description:
parent nodes:
  - "[[reward model]]"
published on:
---

- Deterministic domains
- These are fields where a "ground truth" exists, and the correctness of an answer can be automatically and definitively determined
- Examples,
	- Mathematics
	- Programming
	- Logic
- The reward signal can be binary
- [[reinforcement learning verifiable rewards|RLVR]] can be used for training

| Feature              | Verifiable Domains                                                | Non-Verifiable Domains                                             |
| :------------------- | :---------------------------------------------------------------- | :----------------------------------------------------------------- |
| **Correctness**      | Objective / Deterministic                                         | Subjective / Nuanced                                               |
| **Checker**          | Rule-based / Algorithmic                                          | Human judge / LLM judge                                            |
| **Primary Examples** | Math, Coding, Logic                                               | Writing, Ethics, Dialogue                                          |
| **Training Method**  | [[reinforcement learning verifiable rewards\|RLVR]] (exact match) | [[reinforcement learning human feedback\|RLHF]] (preference match) |
| **Risk**             | False negatives (strictness)                                      | Reward hacking (subjectivity)                                      |
