---
tags:
  - academic
  - work
aliases:
  - Expert Digital Twin
title: proposal four - expert digital twin
description:
parent nodes:
  - "[[003 - genesis/work/omega/thesis/thesis]]"
child nodes:
annotation-target:
---

# Towards an Expert Digital Twin

Traditionally, Human Digital Twins (HDTs) have been data-driven models designed to support decision-making[^1]. Recent advancements in conversational LLMs shed light on the potential to create an *authentic, interactive digital counterpart* of an individual[^1]. Lluís C. Coll et al. address the question "How can the integration of advanced conversational AI with dynamic, multimodal personal data enhance the authenticity and effectiveness of virtual representations in mimicking human personalities in interactions?"[^1]. We choose to follow their approach but focus solely on textual data and restrict the scope to a particular domain. Our goal is to capture the essence of an expert in conversational fields such as sales, education, and psychotherapy (goal-oriented conversations).
What is the essence of a person? We first examine how someone behaves in a particular setting, the persona. Jungian theory states that a persona is an adaptive mask used in society[^2]. The persona is merely the surface level of the essence. In Bandura's **social cognitive theory**, he introduces reciprocal determinism: behaviour, personal characteristics, and the environment mutually influence one another in a continuous cycle[^3]. Here we see that personality, why someone behaves the way they do in a particular setting, can be modelled as a *policy-like* behaviour.
Furthermore, from a philosophical standpoint, we encounter the **narrative identity theory**[^4]. So your essence becomes the story you tell about yourself. We see here that the essence of a person has many definitions. In this project, we choose to focus on 1) *Linguistic Style*, 2) *Cognitive Style* (reasoning patterns), 3) *Relational Styles* (emotional style), and 4) *Knowledge Base*. 
First, we select a domain with abundant publicly available resources and conversational data to validate our proof of concept[^5]. We will follow Bandura's theory and assume that personality is a combination of learned patterns of behaviour and cognition[^3]. This can be seen as an application of a Partially Observable Markov Decision Process[^6]. For example, the expert can be a salesperson, and the client can be a potential buyer with a hidden state. 
Once we obtain a corpus of conversational data and a knowledge base, we apply text-style transfer via fine-tuning or prompting to capture the conversational data's linguistic style[^7]. Ideally, we will use LoRA for fine-tuning rather than prompting[^8]. This results in an LLM with a persona. 
The next step is to model the conversation as a POMDP[^9]. We now create a gym[^10] for the model to train on, and we build virtual clients with hidden states using dynamic prompting[^11] and OCEAN personality trait combinations. We then create a reward model[^12]. 
Now that our environment is prepared, we design a multi-agent architecture consisting of a client simulator model, a reward model, and a guardrail model[^13]. We then start the reinforcement learning process[^14][^15]. 
Formally, we first decide what to reward, create a generic latent space schema, obtain supervision signals from text, train a virtual client model, and then define the reward function. 
Once we have our aligned model, we will evaluate alignment[^15] along with coherence,  semantic similarity and style matching with stylometric embeddings[^17].
The objective of this research is to develop a domain-agnostic, modular framework that can align a large language model to demonstrate the knowledge and personality of an expert individual through reinforcement learning. 

## TODO

- [In-Context Learning User Simulators for Task-Oriented Dialog Systems](https://github.com/telepathylabsai/prompt-based-user-simulator?utm_source=chatgpt.com)
- [Shop-R1: Rewarding LLMs to Simulate Human Behavior in Online Shopping via Reinforcement Learning](https://arxiv.org/abs/2507.17842v1)
- [Reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback?utm_source=chatgpt.com) - Wikipedia
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
- [ConvLab-3](https://github.com/ConvLab/ConvLab-3?utm_source=chatgpt.com)
- [ConvLab-2: An Open-Source Toolkit for Building, Evaluating, and Diagnosing Dialogue Systems](https://truthless11.github.io/pdf/ConvLab2.pdf?utm_source=chatgpt.com)
- [TRL - Transformer Reinforcement Learning](https://huggingface.co/docs/trl/en/index?utm_source=chatgpt.com)
- [Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges](https://arxiv.org/abs/2503.02167v1)
- [A survey of cognitive digital twin and the potential use of LLMs](https://www.sciencedirect.com/science/article/pii/S2213846325001762)
- [A Human Digital Twin Architecture for Knowledge-based Interactions and Context-Aware Conversations](https://arxiv.org/abs/2504.03147)
- [A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More](https://arxiv.org/abs/2407.16216)
- [Human Digital Twins: A systematic literature review and concept disambiguation for industry 5.0](https://www.sciencedirect.com/science/article/pii/S0166361524001581)
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) - IMPORTANT

# REFERENCES

[^1]: [Towards the "Digital Me": A vision of authentic Conversational Agents powered by personal Human Digital Twins](https://arxiv.org/abs/2506.23826)
[^2]: [A TYPOLOGY OF PERSONA AS SUGGESTED BY JUNGIAN THEORY AND THE EVOLVING PERSONA STUDIES LITERATURE](https://search.informit.org/doi/epdf/10.3316/informit.609093216085752)
[^3]: [SOCIAL COGNITIVE THEORY: An Agentic Perspective](https://scispace.com/pdf/social-cognitive-theory-an-agentic-perspective-3a2jt1u3lk.pdf)
[^4]: [Narrative Identity](https://link.springer.com/chapter/10.1007/978-1-4419-7988-9_5)
[^5]: [doc2dial: A Goal-Oriented Document-Grounded Dialogue Dataset](https://aclanthology.org/2020.emnlp-main.652/)
[^6]: [A Survey of POMDP Applications](https://www.cassandra.org/arc/papers/applications.pdf)
[^7]: [LLM-Based Text Style Transfer: Have We Taken a Step Forward?](https://ieeexplore.ieee.org/abstract/document/10915631)
[^8]: [A survey on LoRA of large language models](https://link.springer.com/article/10.1007/s11704-024-40663-9)
[^9]: [The Hidden Information State model: A practical framework for POMDP-based spoken dialogue management](https://www.sciencedirect.com/science/article/pii/S0885230809000230)
[^10]: [Gymnasium: A Standard Interface for Reinforcement Learning Environments](https://arxiv.org/abs/2407.17032)
[^11]: [Chain-of-thought driven dynamic prompting and computation method](https://www.sciencedirect.com/science/article/pii/S1568494625015170)
[^12]: [A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future](https://arxiv.org/abs/2504.12328)
[^13]: [Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents](https://arxiv.org/abs/2306.03314)
[^14]: [LLM-based Multi-Agent Reinforcement Learning: Current and Future Directions](https://arxiv.org/abs/2405.11106)
[^15]: [Reinforcement Learning Enhanced LLMs: A Survey](https://arxiv.org/abs/2412.10400)
[^16]: [Trustworthy LLMs: a Survey and Guideline for Evaluating Large Language Models' Alignment](https://arxiv.org/abs/2308.05374)
[^17]: [Stylometric Embeddings](https://books.google.nl/books?hl=en&lr=&id=WG5xEQAAQBAJ&oi=fnd&pg=PA446&dq=stylometric+embeddings&ots=qcLuKFWJ18&sig=z0VI-npPKhm1y0hnMxa7kLcHasE&redir_esc=y#v=onepage&q=stylometric%20embeddings&f=false)



