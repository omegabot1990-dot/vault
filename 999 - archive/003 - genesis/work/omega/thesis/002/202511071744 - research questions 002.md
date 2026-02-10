---
tags:
  - work
  - academic
aliases:
  - Research Question - Scratch Pad
title: research questions 002
description:
parent nodes:
  - "[[003 - genesis/work/omega/thesis/thesis]]"
child nodes:
annotation-target:
---
## Keywords

- LLMs
	- Transformers
- Reasoning
- Foundational Models
- Pre-training
- Training
	- Distillation
- Finetuning
- RAG
- Frameworks
- Agents
- Mixture-of-Experts (MoE)
	- Sparse
	- Dense
- Efficiency
	- Quantisation
- Feedback
	- RLHF
	- RL AI F

---
### Abstract

- What problem does the paper tackle?
    
- Why does it matter?
    
- What method did they use?
    
- What gap do they claim to fill?
    
- What results did they get?

I need to find the _problem_ + _gap_ + _method_ + _feasibility_ intersection.

---

## Random

- [Artificial intelligence in psychology: How can we enable psychology students to accept and use artificial intelligence?](https://journals.sagepub.com/doi/full/10.1177/14757257211037149)
- [Cognitive psychology-based artificial intelligence review](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.1024316/full)
- [Uses of Artificial Intelligence in Psychology](https://www.asianinstituteofresearch.org/_files/ugd/ed8b62_55687345a293412680b985cc98d2729f.pdf#page=26)

### LLMs and Psychotherapy

- [Artificial Intelligence Will Change the Future of Psychotherapy: A Proposal for Responsible, Psychologist-Led Development](https://static1.squarespace.com/static/53d29678e4b04e06965e9423/t/645ec4bd577cb4377d52d6a5/1683932350430/clinicalLLMsv14.pdf)
- [A Survey of Large Language Models in Psychotherapy: Current Landscape and Future Directions](https://arxiv.org/abs/2502.11095) - IMPORTANT
- [Large language models could change the future of behavioral healthcare: a proposal for responsible development and evaluation](https://www.nature.com/articles/s44184-024-00056-z)
- [LLM-based Conversational AI Therapist for Daily Functioning Screening and Psychotherapeutic Intervention via Everyday Smart Devices](https://arxiv.org/abs/2403.10779)
- [Therapy as an NLP Task: Psychologists' Comparison of LLMs and Human Peers in CBT](https://arxiv.org/abs/2409.02244)
- [Introducing CounseLLMe: A dataset of simulated mental health dialogues for comparing LLMs like Haiku, LLaMAntino and ChatGPT against humans](https://www.sciencedirect.com/science/article/pii/S2667118225000017)
- [Preference Learning Unlocks LLMs' Psycho-Counseling Skills](https://arxiv.org/abs/2502.19731)
- [Script-Strategy Aligned Generation: Aligning LLMs with Expert-Crafted Dialogue Scripts and Therapeutic Strategies for Psychotherapy](https://dl.acm.org/doi/abs/10.1145/3757655) - IMPORTANT
- [How LLM Counselors Violate Ethical Standards in Mental Health Practice: A Practitioner-Informed Framework](https://ojs.aaai.org/index.php/AIES/article/view/36632)
- [Unlocking LLMs: Addressing Scarce Data and Bias Challenges in Mental Health and Therapeutic Counselling](https://aclanthology.org/2024.nlpaics-1.26.pdf)
- [PsyDT: Using LLMs to Construct the Digital Twin of Psychological Counselor with Personalized Counseling Style for Psychological Counseling](https://aclanthology.org/2025.acl-long.55.pdf) - IMPORTANT
- [Psy-LLM: Scaling up Global Mental Health Psychological Services with AI-based Large Language Models](https://arxiv.org/abs/2307.11991)
- [A Computational Framework for Behavioral Assessment of LLM Therapists](https://arxiv.org/abs/2401.00820)
- [PsycholexTherapy: Simulating Reasoning in Psychotherapy with Small Language Models in Persian](https://arxiv.org/abs/2510.03913) - IMPORTANT
- [AI meets psychology: an exploratory study of large language models’ competence in psychotherapy contexts](https://www.tandfonline.com/doi/full/10.1080/29974100.2025.2545258#abstract)
- [Exploring the potential of lightweight large language models for AI-based mental health counselling task: a novel comparative study](https://www.nature.com/articles/s41598-025-05012-1) - IMPORTANT
- [Trustworthy AI Psychotherapy: Multi-Agent LLM Workflow for Counseling and Explainable Mental Disorder Diagnosis](https://dl.acm.org/doi/abs/10.1145/3746252.3761164)
- [HealMe: Harnessing Cognitive Reframing in Large Language Models for Psychotherapy](https://arxiv.org/abs/2403.05574)
- [DOMAIN-SPECIFIC IMPROVEMENT ON PSYCHOTHERAPY CHATBOT USING ASSISTANT](https://arxiv.org/pdf/2404.16160)
- [Feel the Difference? A Comparative Analysis of Emotional Arcs in Real and LLM-Generated CBT Sessions](https://aclanthology.org/anthology-files/anthology-files/pdf/findings/2025.findings-emnlp.1089.pdf)
	- [CBT Dialogue Data](https://gitlab.com/xiaoyi.wang/realcbt-dataset/-/tree/main?ref_type=heads)
- [Comparing Human Role-Players and LLM-Simulated Clients in Online Counselling Training: An Analysis of Counselling Patterns](https://educationaldatamining.org/EDM2025/proceedings/2025.EDM.short-papers.116/2025.EDM.short-papers.116.pdf)
- [Roleplaying with Structure: Synthetic Therapist-Client Conversation Generation from Questionnaires](https://www.arxiv.org/abs/2510.25384)
- [Guardians of Trust: Risks and Opportunities for LLMs in Mental Health](https://aclanthology.org/2025.nlp4pi-1.2/)
- [Improving Workplace Well-being in Modern Organizations: A Review of Large Language Model-based Mental Health Chatbots](https://www.researchgate.net/publication/385135480_Improving_Workplace_Well-being_in_Modern_Organizations_A_Review_of_Large_Language_Model-based_Mental_Health_Chatbots)
- [Towards the "Digital Me": A vision of authentic Conversational Agents powered by personal Human Digital Twins](https://arxiv.org/abs/2506.23826)
- [Information Extraction in Low-Resource Scenarios: Survey and Perspective](https://arxiv.org/abs/2202.08063)
- [AdaptiCare: A Psychological Counseling Dialogue Enhancement Framework Based on Multi-Agent Collaboration](https://www.researchgate.net/publication/396395482_AdaptiCare_A_Psychological_Counseling_Dialogue_Enhancement_Framework_Based_on_Multi-Agent_Collaboration)

---
## Problems

1. How to acquire the input data?
	1. Can we collaborate with a therapist/s?
	2. Can we use a public internet conversation corpus?
		1. [Council Chat Dataset](https://huggingface.co/datasets/nbertagnolli/counsel-chat)
			1. Sherry Katz, LCSWCouples and Family Therapist, LCSW has 497 responses
		2. [Cactus: Towards Psychological Counseling Conversations using Cognitive Behavioral Theory](https://arxiv.org/abs/2407.03103)
		3. [DiaCBT: A Long-Periodic Dialogue Corpus Guided by Cognitive Conceptualization Diagram for CBT-based Psychological Counseling](https://arxiv.org/abs/2509.02999)
			1. Contact the Authors for the dataset.
		4. [Therapy as an NLP Task: Psychologists' Comparison of LLMs and Human Peers in CBT](https://arxiv.org/abs/2409.02244)
			1. Contact the Authors for the dataset.
		5. [Feel the Difference? A Comparative Analysis of Emotional Arcs in Real and LLM-Generated CBT Sessions](https://arxiv.org/abs/2508.20764)
			1. RealCBT dataset: One of the first publicly available datasets of authentic CBT dialogues.
	3. What do we need?
		1. **Idiosyncratic behaviour** of the target therapist
		2. **Domain framing** (CBT, ACT, psychodynamic, etc.)
		3. **Therapeutic style markers** (Socratic questioning, reflections)

---
%% 
(action-items:: Action Items - 202511111342) 
%%
> [!info] 2025-11-11
> > [!todo] **Action Items:**
> > - [ ] Go through LocalLLama (Reddit)


