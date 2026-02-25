---
tags:
  - inference
aliases:
  - Self-Consistency Decoding
title: self-consistency decoding
description: ""
bot: false
parent nodes:
  - "[[202602111350 - inference|Inference]]"
published on:
---

- [ ] What is CoT?
- [ ] What is temperature?

---
- Self-consistency decoding samples multiple reasoning paths for the same prompt and aggregates their final answers
- Instead of relying on a single greedy chain-of-thought, it uses diversity to reduce reasoning variance
- <mark style="background: #BBFABBA6;">A common aggregation rule is the majority vote over final answers from independently sampled traces</mark>
- This often improves math and logic accuracy when correct reasoning paths are present among samples
- It trades extra inference compute for better reliability and robustness
- Performance depends on sample count, decoding temperature, and answer normalization strategy