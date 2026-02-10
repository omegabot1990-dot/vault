---
tags:
  - academic
  - work
aliases:
  - Distil
title: proposal two - distil
description:
parent nodes:
  - "[[003 - genesis/work/omega/thesis/thesis]]"
child nodes:
annotation-target:
---
# A Multi-Agent RAG Framework for Personalised Digital Therapist Construction

The importance of mental health in the healthcare system is increasingly recognised, leading to a higher demand for accessible and effective psychotherapy [^1]. LLMs are seen as a promising solution because of their capacity to understand rich contextual semantics, which can facilitate a shift from discrete NLP-based reasoning methods to a continuous, multi-turn reasoning paradigm [^1]. One way to utilise an LLM is as a **Virtual Therapist** [^1]. A key limitation of current mental health LLMs is that they blend multi-turn dialogues with various counselling styles during fine-tuning, while neglecting that real-world psychological counsellors have diverse personal styles, including language use and therapy approaches [^2]. PsyDT introduces a new framework that includes 1) **Dynamic One-Shot Learning from Counselling Cases** (Real-World Analysis), 2) **Client Personality Simulation**, 3) **Multi-Turn Dialogue Synthesis**, and 4) **Model Construction** to develop an LLM reflecting a particular counsellor's personalised style [^2].

Here, we dive deeper into how we can enhance the LLM's ability to embody the therapist's specific style, focusing on the model construction phase.

The first phase involves finding the right base model. We first dig deeper into small LLMs from 100M to 5B in size[^3]. This knowledge will be leveraged to select a base model.

The second phase involves fine-tuning the base model based on the multi-turn data corpus. PsyDT[^2] uses MIFT; we first explore the fine-tuning landscape[^5]. Then we use this knowledge to fine-tune the base model.

The third phase, in addition to the work carried out by PsyDT, involves using a RAG-enabled[^6] LLM to generate the output first. Then, our fine-tuned LLM from phase two transforms the text, followed by a RAG-enabled verifier model to consolidate the output[^7]. Here we have two RAG systems: one for the therapy style, curated by a domain expert, and the other for safety, values, and ethics, also created by a domain expert.

Finally, the Agentic RAG is benchmarked using the same methodology described in PsyDT[^2].

The main aim of this research is to create a robust multi-agent LLM system framework that a specific therapist can run on their edge device to create a robust human digital twin.

For this purpose, we will also be exploring the articles below.
1. [Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges](https://arxiv.org/abs/2503.02167v1)
2. [A survey of cognitive digital twin and the potential use of LLMs](https://www.sciencedirect.com/science/article/pii/S2213846325001762)
3. [A Human Digital Twin Architecture for Knowledge-based Interactions and Context-Aware Conversations](https://arxiv.org/abs/2504.03147)
4. [Trustworthy AI Psychotherapy: Multi-Agent LLM Workflow for Counseling and Explainable Mental Disorder Diagnosis](https://arxiv.org/abs/2508.11398)

---
## References

[^1]: [A Survey of Large Language Models in Psychotherapy: Current Landscape and Future Directions](https://arxiv.org/pdf/2502.11095)
[^2]: [PsyDT: Using LLMs to Construct the Digital Twin of Psychological Counselor with Personalized Counseling Style for Psychological Counseling](https://arxiv.org/abs/2412.13660v1)
[^3]: [Small Language Models: Survey, Measurements, and Insights](https://arxiv.org/abs/2409.15790)
[^4]: [A Comprehensive Overview of Large Language Models](https://arxiv.org/abs/2307.06435)
[^5]: [The Ultimate Guide to Fine-Tuning LLMs from Basics to Breakthroughs: An Exhaustive Review of Technologies, Research, Best Practices, Applied Research Challenges and Opportunities](https://arxiv.org/abs/2408.13296)
[^6]: [Retrieval Augmented Generation (RAG) and Beyond: A Comprehensive Survey on How to Make your LLMs use External Data More Wisely](https://arxiv.org/abs/2409.14924)
[^7]: [Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents](https://arxiv.org/abs/2306.03314)

