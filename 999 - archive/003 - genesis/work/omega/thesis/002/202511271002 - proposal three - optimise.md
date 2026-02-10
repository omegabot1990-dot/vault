---
tags:
  - zettel
  - academic
  - work
aliases:
  - Optimise
title: proposal three - optimise
description:
parent nodes:
  - "[[003 - genesis/work/omega/thesis/thesis]]"
child nodes:
annotation-target:
---
# Reinforcement Learning and Compression for Therapist-Style LLMs: Extending the PsyDT Framework

The importance of mental health in the healthcare system is increasingly recognised, leading to a higher demand for accessible and effective psychotherapy [^1]. LLMs are seen as a promising solution because of their capacity to understand rich contextual semantics, which can facilitate a shift from discrete NLP-based reasoning methods to a continuous, multi-turn reasoning paradigm [^1]. One way to utilise an LLM is as a **Virtual Therapist** [^1]. A key limitation of current mental health LLMs is that they blend multi-turn dialogues with various counselling styles during fine-tuning, while neglecting that real-world psychological counsellors have diverse personal styles, including language use and therapy approaches [^2]. PsyDT introduces a new framework that includes 1) **Dynamic One-Shot Learning from Counselling Cases** (Real-World Analysis), 2) **Client Personality Simulation**, 3) **Multi-Turn Dialogue Synthesis**, and 4) **Model Construction** to develop an LLM reflecting a particular counsellor's personalised style [^2].

Here, we explore the next steps PsyDT's LLM can take.

We first explore how reinforcement learning can enhance the LLM[^3]. We will examine alignment techniques[^4]. With this knowledge, we aim to implement a framework to improve the LLMs' capabilities and reevaluate it.

Second, we aim to make the LLM more efficient. We first explore compression methodologies for LLMs[^5]. We use this knowledge to implement the compression system and reevaluate it against baseline benchmarks.

The main aim of this research is to make the LLM more robust with RL and then more efficient with compression. This will enable a specific therapist to privately host this service, allowing them to maintain privacy-enabled access to their services.

---
## References

[^1]: [A Survey of Large Language Models in Psychotherapy: Current Landscape and Future Directions](https://arxiv.org/pdf/2502.11095)
[^2]: [PsyDT: Using LLMs to Construct the Digital Twin of Psychological Counselor with Personalized Counseling Style for Psychological Counseling](https://arxiv.org/abs/2412.13660v1)
[^3]: [Reinforcement Learning Enhanced LLMs: A Survey](https://arxiv.org/abs/2412.10400)
[^4]: [A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More](https://arxiv.org/abs/2407.16216)
[^5]: [Model Compression and Efficient Inference for Large Language Models: A Survey](https://arxiv.org/abs/2402.09748)