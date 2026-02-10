---
tags:
  - work
aliases:
  - research questions 001
title: research questions 001
description:
parent nodes:
  - "[[202510300118 - proposal 001]]"
child nodes:
annotation-target:
---

1. How can a **small-scale LLM** (≤1B parameters) be trained or adapted to maintain conversational quality in emotional support contexts?
	
	1. Exhibit robust _stepwise reasoning_ in supportive conversations when equipped with a **planner–solver–checker** stack?
	    
2. How effective is a **RAG (Retrieval-Augmented Generation)** pipeline in enhancing a compact model’s psychological reasoning ability?
	
	1. How much does **RAG** (psychoeducational sources) improve reasoning, faithfulness, and _factuality_ for a compact model?
	    
3. Can **reasoning traces** be **distilled** into a small model (e.g., “R1-style” or CoT distillation) without sacrificing latency and privacy?
	
4. Can **federated learning** enable collective improvement of emotional classification while preserving user privacy?
	
	1. Can **federated learning** safely improve **non-diagnostic classification of symptoms/states** and **strategy recommendation** patterns?
	    
5. How feasible is deploying this LLM on **edge devices** (Raspberry Pi, Jetson, smartphones) while minimising carbon footprint?
	
	1. What is the energy/latency trade-off of **edge inference** with quantisation + LoRA adapters?
	    
6. How can we **evaluate** such a model ethically — measuring empathy, coherence, and user trust instead of diagnostic accuracy?
	
	1. What evaluation rubric best captures **empathy + reasoning quality + safety** in this domain?
		
7. How can multimodal fusion of text, voice, and bio-signals enhance emotion classification accuracy while maintaining interpretability and user trust in human-centric AI systems?
	

---

> How can a **small reasoning model** or an **agentic swarm of small reasoning models**, running on an **edge device**, show *structured* and *auditable* thinking for ==**emotion exploration**==? 