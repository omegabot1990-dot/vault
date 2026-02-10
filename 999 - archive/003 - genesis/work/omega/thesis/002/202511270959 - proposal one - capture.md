---
tags:
  - academic
  - work
aliases:
  - Capture
title: proposal one - capture
description:
parent nodes:
  - "[[003 - genesis/work/omega/thesis/thesis]]"
child nodes:
annotation-target:
---
# Efficient Small-Model Framework for Building Personalised Therapist Digital Twins

The importance of mental health in the healthcare system is increasingly recognised, leading to a higher demand for accessible and effective psychotherapy[^1]. LLMs are seen as a promising solution because of their capacity to understand rich contextual semantics, which can facilitate a shift from discrete NLP-based reasoning methods to a continuous, multi-turn reasoning paradigm[^1]. One way to utilise an LLM is as a **Virtual Therapist**[^1]. A key limitation of current mental health LLMs is that they blend multi-turn dialogues with various counselling styles during fine-tuning, while neglecting that real-world psychological counsellors have diverse personal styles, including language use and therapy approaches[^2]. PsyDT introduces a new framework that includes 1) **Dynamic One-Shot Learning from Counselling Cases** (Real-World Analysis), 2) **Client Personality Simulation**, 3) **Multi-Turn Dialogue Synthesis**, and 4) **Model Construction** to develop an LLM reflecting a particular counsellor's personalised style[^2].

Here, we dive deeper into capturing the core aspects of a therapist, including their *linguistic style*, *reasoning patterns*, *relational qualities*, *safety rules*, *values*, and *knowledge base*. Our goal is to develop a more comprehensive corpus of synthetic, multi-turn, annotated dialogue for use in downstream tasks. 

The first phase, similar to the PsyDT framework, would be to collect a limited set of authentic counselling dialogues that reflect the personalised style of the professional being modelled. PsyDT recruited a professional psychological counsellor who meets national standards; our initial step would be to try this approach and, if successful, potentially recruit professionals. In case this step is not feasible, we propose three approaches as follows,
1. Use single-turn dialogues from scraped CouncilChat data[^3].
	CouncilChat is a website where therapists respond to clients' questions, and users can like responses they find most helpful.
2. Use RealCBT data[^4].
    One of the first publicly available datasets of authentic CBT dialogues.
3. Contact authors of DiaCBT[^5] for access to their dataset.
    The curated dataset includes multiple sessions for each counselling session.

The second phase includes 1) **extracting** and **representing** features such as *linguistic style*, *reasoning patterns*, and *relational qualities*, and 2) developing a corpus of *safety rules*, *values*, and a *knowledge base* for psychotherapy practices. For the first step, we will review the field of Open Information Extraction[^6], aiming to find a more efficient alternative to GPT-4. In the second step, we will first gather data for the corpus under domain expert supervision, then explore a RAG system for factual grounding[^7].

The third phase involves simulating the client; we will investigate alternatives to GPT-4, starting with the CARE-Bench survey[^8]. The aim here is to determine if a smaller model can replicate a client. 

The final step is to simulate the therapist based on phase one and the client based on phase three, then generate a synthetic data set using LLM-LLM role-playing[^9]. 

We then evaluate the dataset using the PsyDT methodology[^2].

The main goal of this research is to develop a more efficient method for building a robust dataset for downstream tasks. We aim to replace GPT-4 with models ranging from 1B to 7B in size. This approach allows an individual therapist to run the system locally on their edge device. 

For this purpose, we will also be exploring the articles below.
1. [Large Language Model based Multi-Agents: A Survey of Progress and Challenges](https://arxiv.org/abs/2402.01680)
2. [Retrieval Augmented Generation (RAG) and Beyond: A Comprehensive Survey on How to Make your LLMs use External Data More Wisely](https://arxiv.org/abs/2409.14924)
3. [PsycholexTherapy: Simulating Reasoning in Psychotherapy with Small Language Models in Persian](https://arxiv.org/abs/2510.03913)
4. [Trustworthy AI Psychotherapy: Multi-Agent LLM Workflow for Counseling and Explainable Mental Disorder Diagnosis](https://arxiv.org/abs/2508.11398)
5. [Towards the "Digital Me": A vision of authentic Conversational Agents powered by personal Human Digital Twins](https://arxiv.org/abs/2506.23826)
6. [PATIENT-Ψ: Using Large Language Models to Simulate Patients for Training Mental Health Professionals](https://arxiv.org/abs/2405.19660)
7. [AdaptiCare: A Psychological Counseling Dialogue Enhancement Framework Based on Multi-Agent Collaboration](https://www.computer.org/csdl/proceedings-article/caibda/2025/11183315/2aFKba2oKqs)

---
## References

[^1]: [A Survey of Large Language Models in Psychotherapy: Current Landscape and Future Directions](https://arxiv.org/pdf/2502.11095)
[^2]: [PsyDT: Using LLMs to Construct the Digital Twin of Psychological Counselor with Personalized Counseling Style for Psychological Counseling](https://arxiv.org/abs/2412.13660v1)
[^3]: [Council Chat Dataset](https://huggingface.co/datasets/nbertagnolli/counsel-chat)
[^4]: [Feel the Difference? A Comparative Analysis of Emotional Arcs in Real and LLM-Generated CBT Sessions](https://arxiv.org/abs/2508.20764)
[^5]: [DiaCBT: A Long-Periodic Dialogue Corpus Guided by Cognitive Conceptualization Diagram for CBT-based Psychological Counseling](https://arxiv.org/abs/2509.02999)
[^6]: [A Survey on Open Information Extraction from Rule-based Model to Large Language Model](https://arxiv.org/abs/2208.08690)
[^7]: [Towards Agentic RAG with Deep Reasoning: A Survey of RAG-Reasoning Systems in LLMs](https://arxiv.org/abs/2507.09477)
[^8]: [CARE-Bench: A Benchmark of Diverse Client Simulations Guided by Expert Principles for Evaluating LLMs in Psychological Counseling](https://arxiv.org/abs/2511.09407)
[^9]: [Interactive Agents: Simulating Counselor-Client Psychological Counseling via Role-Playing LLM-to-LLM Interactions](https://arxiv.org/abs/2511.09407)