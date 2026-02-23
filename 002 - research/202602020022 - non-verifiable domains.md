---
tags:
  - note
aliases:
  - Non-verifiable Domains
title: non-verifiable domains
description: ""
parent nodes:
  - "[[definitions]]"
published on:
---

- Non-deterministic domains
- These are subjective areas where "correctness" is a matter of preference, style, or human values rather than universal rules
- Examples,
	- Creative writing
	- Helpfulness
	- Honesty
- [[reinforcement learning human feedback|RLHF]] can be used for training
- [[rubrics as reward|RoR]] can be used for training

| Feature              | Verifiable Domains                                                | Non-Verifiable Domains                                             |
| :------------------- | :---------------------------------------------------------------- | :----------------------------------------------------------------- |
| **Correctness**      | Objective / Deterministic                                         | Subjective / Nuanced                                               |
| **Checker**          | Rule-based / Algorithmic                                          | Human judge / LLM judge                                            |
| **Primary Examples** | Math, Coding, Logic                                               | Writing, Ethics, Dialogue                                          |
| **Training Method**  | [[reinforcement learning verifiable rewards\|RLVR]] (exact match) | [[reinforcement learning human feedback\|RLHF]] (preference match) |
| **Risk**             | False negatives (strictness)                                      | Reward hacking (subjectivity)                                      |
