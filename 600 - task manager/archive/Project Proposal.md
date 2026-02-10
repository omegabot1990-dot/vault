---
tags:
  - inbox
  - academic
  - work
description: project proposal for thesis
due date: 2025-10-10
start date: 2025-10-05
end date: 2025-11-04
status: Archive
importance level: important
urgency level: urgent
task type: distil
story points: 5
parent nodes:
child nodes:
recurrent:
---

%% 
(resources:: Resources - 202510292134)
%%
> [!info] 2025-10-29
> > [!example] **Resources:**
> > - [LIACS Research](https://www.universiteitleiden.nl/en/science/computer-science/research)
> > - [Social Intelligence Modelling Lab](https://sim-lab.nl/)
> > - [Text Mining and Retrieval](https://tmr.liacs.nl/projects.php)
> > - [Low-Resource Chat-based Conversational Intelligence (LESSEN)](https://www.universiteitleiden.nl/en/research/research-projects/science/liacs-low-resource-chat-based-conversational-intelligence-lessen)
> > - [Domain Specific Systems for Information Extraction and Retrieval (DoSSIER)](https://dossier-project.eu/)

## Possible Supervisors

#### Health Data Science

Wessel Kraaij (Prof Health Data) 
Anton Schreuder (Postdoc) 
Richard Bortsov (Postdoc)

##### Relevant Research

> 10-04-2025: seminar with Prof. Jildau Bouwman (TNO and LACDR)

Title: Personalized Digital Health

Abstract: The future of healthcare is digital, patient-centric and also focused on prevention. Digital solutions can ensure better patient outcomes, empower individuals to take control of their own health, and unburden the healthcare system. For this, it is key to be able to reuse data. Doing so, we can learn from data and thereby, improve public and personal health. Within C4yourself, we have shown that this individual data can be unlocked via the Personal Health environment, but to understand health in all its complexity, data from the whole system is needed and needs to be combined with multiple sources. Within Heracles, we combined data from several medical resources to create a system to learn from the journeys of other patients. From this project, we learned that the medical data currently stored in the Netherlands is not of the quality needed for a learning healthcare system. Collecting data and making it reusable costs time and needs standardization. The next step for fitting advice is bringing together knowledge and data using models towards fitting and explainable advice. For instance, data of other patients can help in predicting what can benefit you, but then the data should be representable for you. We have developed a tool to visualize the effect of the representation on the fit of the model. The last step of giving personal advice is making it easy to adhere to, also here AI can be helpful by giving the advice in a way that fits to the preferences of the individual. For personal advice, LLMs can help in the fitting communication. We have developed a RAG based system for dietary advice.

> 15-06-2023, 13.15 : seminar with Samar Samir Khalil (PhD candidate at LIACS)

Title: Multilingual Federated Learning for Mental Health Disorder Detection

Abstract:   Mental illnesses are now more prevalent in a way that threatens society's productivity. Depression, suicide, and similar mental health issues are often reflected in the language used by patients who suffer from such conditions. Early detection of mental health disorders saves lives and enhances the well-being of affected people. An increasing number of studies in Natural Language Processing (NLP) have been devoted to the recognition and detection of early symptoms of related disorders. Meanwhile, the non-availability of data due to patients' data privacy hinders this research direction. Federated learning (FL) is a new paradigm that provides a collaborative machine learning environment where it trains and updates a centralized model on decentralized data so the data never leaves the client side. Mental health can benefit from the privacy-preserving trait offered by FL to reconcile the need for big deep-learning datasets and the high sensitivity of data ownership. While FL has been employed in the medical domain by promoting the adoption of machine learning models in clinical settings, however, little research has investigated how multilingual text impacts FL algorithms. In this research, we investigate the potential of Federated Learning combined with Natural Language Processing, applied in the psychology field by simulating a multi-lingual data setting. We train and compare results from a collaborative learning model versus a data-centralized model.

#### Software and AI in Business

Joost Visser (Prof Software Engineering) 
Guus Ramackers (UD) 
Christoph Stettina (UD) 
Miros Zohrehvand (UD) 
Bas Kruiswijk (docent) 
Niels van Weeren (docent) 
Paul van Leeuwen (docent) 
Werner Heijstek (docent) 
Natalia Amat-Lefort (docent/postdoc)

#### Human AI

Max van Duijn (UD Theory of Mind)

---

### 🧭 **Primary Matches (Directly Aligned)**

#### **1. [Joost Broekens](d.j.broekens@liacs.leidenuniv.nl)** – _Affective Computing & Human–AI Interaction_

- **Why:**
    
    - Head of the _Affective Computing and Human–Robot Interaction Lab_.
        
    - Focuses on **computational modelling of emotions**, **emotion psychology**, **human–agent interaction**, and **explainable emotional AI**.
        
    - Your goal of a psychologically aware assistant (non-clinical emotional support, journaling, empathy modelling) fits _perfectly_ within his domain.
        
    - Has organized interdisciplinary workshops bridging **emotion psychology** and **computational models**—exactly your intersection.
        
- **Keywords:** Affective computing, emotion modeling, empathy in AI, human–agent interaction.
    
- **Best fit for:** The psychological reasoning, emotion classification, and validation parts of your LLM.
    

---

#### **2. [Suzan Verberne](s.verberne@liacs.leidenuniv.nl)** – _Natural Language Processing & Information Retrieval_

- **Why:**
    
    - Works on **LLMs, NLP efficiency, bias, hallucination mitigation, and factual grounding**.
        
    - Focus on **building smaller, more efficient, source-aware models**—aligned with your **RAG + small LLM + edge deployment** vision.
        
    - Her emphasis on **factual correctness, ethical AI, and efficient LLMs** matches your idea of minimizing carbon footprint and hallucinations.
        
- **Keywords:** Small and efficient LLMs, RAG, factual grounding, bias mitigation, language modeling efficiency.
    
- **Best fit for:** Model design, RAG integration, multilingual NLP, and evaluation methodology.
    

---

#### **3. Wessel Kraaij** – _AI for Healthy Living & Data Science for Health_

- **Why:**
    
    - Focuses on **AI for health and wellbeing**, **E/M-health systems**, and **privacy-sensitive citizen data**.
        
    - Works with **P4 Health** (Preventive, Personalized, Predictive, Participatory) — conceptually parallel to your reflective, awareness-based assistant.
        
    - Interested in **secure, privacy-sensitive software stacks**—relevant to your **federated learning and data privacy** goals.
        
- **Keywords:** AI for wellbeing, data privacy, participatory health, personalized AI.
    
- **Best fit for:** Federated learning, ethical validation, and health-oriented impact framing.
    

---

#### **4. Peter van der Putten** – _Artificial Emotions, Creativity & Responsible AI_

- **Why:**
    
    - Researches “Artificial X” — creativity, emotions, bonding, morality — i.e., _AI that feels human_.
        
    - Interested in **AI ethics, generative AI, and emotional interaction**.
        
    - Bridges **trustworthy AI and creative emotional interfaces**, which aligns with your assistant’s empathetic personality goal.
        
- **Keywords:** Artificial emotions, bonding, trustworthy AI, generative assistants.
    
- **Best fit for:** Human-centric framing, ethical and creative aspects of conversational agents.
    

---

### ⚙️ **Secondary Matches (Technical Complementary)**

#### **5. Todor Stefanov** – _Embedded Systems & AI at the Edge_

- **Why:**
    
    - Works on **distributed deep learning at the Edge** and **embedded AI systems**.
        
    - Could co-supervise the **edge deployment and energy efficiency** part of your work.
        
- **Keywords:** Edge AI, embedded systems, distributed learning.
    
- **Best fit for:** Deployment optimization and sustainability.
    

---

#### **6. Niki van Stein** – _Explainable AI & Optimization_

- **Why:**
    
    - Focus on **Explainable AI (XAI)** and **trustworthy AI** for human collaboration.
        
    - Could contribute to the **explainability and transparency** aspects of your reasoning model.
        
- **Best fit for:** Explainability and human interpretability of your reasoning traces.
    

---

### 🧩 **Optimal Collaboration Setup**

To make your thesis truly interdisciplinary and balanced:

|Aspect|Ideal Supervisor|
|---|---|
|**Emotional reasoning, affective modeling**|Joost **Broekens**|
|**Small/RAG LLM design & multilingual NLP**|Suzan **Verberne**|
|**Health, privacy, validation**|Wessel **Kraaij**|
|**Edge AI & sustainability** _(optional co-supervisor)_|Todor **Stefanov**|
|**Ethical framing & creativity** _(advisory)_|Peter **van der Putten**|

---

### 💡 Suggested Pitch Approach

When reaching out:

- Pitch your project as **Human-Centric AI for Emotional Wellbeing**, combining  
    **Affective Computing (Broekens)** + **Efficient LLMs (Verberne)** + **Privacy-Preserving Health AI (Kraaij)**.
    
- Mention that you aim to contribute to Leiden’s focus on _trustworthy, explainable, and sustainable AI_.
    
- You can propose **Broekens as main supervisor** with **Verberne or Kraaij** as co-supervisor — that’s a strong, realistic combination.
    

---

I want to blend **AI architecture design, psychology-oriented NLP, sustainability (edge computing), federated learning, and human-centric validation** — all within the boundaries of ethical and socially beneficial AI.

---

# 🧠 Thesis Proposal Outline (INSTANT)

### Title (Working)

**“Designing a Sustainable, Privacy-Preserving Conversational Assistant for Emotional Well-Being using Small-Scale LLMs and Federated Learning”**

---

## 1. **Motivation & Background**

- Mental health awareness is growing, yet access to therapy is limited by stigma, cost, and availability.
    
- Current large language models (LLMs), such as GPT-4 and Gemini, show promise as companions but are too large, opaque, and data-hungry to be deployed ethically in sensitive domains like mental health.
    
- A **smaller, edge-deployable, privacy-preserving LLM**, fine-tuned to support journaling, self-reflection, and early emotional awareness, could bridge this gap.
    
- **Goal:** Build a compact, interpretable, and ethically aligned LLM that acts as a psychological assistant — not a therapist — to help users reflect, identify emotions, and explore coping mechanisms.
    

---

## 2. **Research Questions**

1. How can a **small-scale LLM** (≤1B parameters) be trained or adapted to maintain conversational quality in emotional support contexts?
    
2. How effective is a **RAG (Retrieval-Augmented Generation)** pipeline in enhancing a compact model’s psychological reasoning ability?
    
3. Can **federated learning** enable collective improvement of emotional classification while preserving user privacy?
    
4. How feasible is deploying this LLM on **edge devices** (Raspberry Pi, Jetson, smartphones) while minimising carbon footprint?
    
5. How can we **evaluate** such a model ethically — measuring empathy, coherence, and user trust instead of diagnostic accuracy?
    

---

## 3. **Objectives**

- ✅ Train or fine-tune a **compact LLM** architecture (e.g., Phi-2, Mistral-7B-instruct, TinyLlama, Qwen-1.5B) using emotion-focused dialogues and psychological literature.
    
- ✅ Implement a **RAG pipeline** using curated resources (psychoeducational materials, CBT/DBT worksheets, journaling prompts).
    
- ✅ Integrate **multilingual support** (English + Dutch or Malayalam) using transfer learning or mT5/mBERT embeddings.
    
- ✅ Explore **edge deployment**: quantisation, distillation, and LoRA adapters for efficient inference.
    
- ✅ Integrate **Federated Learning** to allow decentralised learning of emotion classification patterns.
    
- ✅ Validate via small-scale user studies measuring **helpfulness, empathy, emotional alignment**, and **energy efficiency**.
    

---

## 4. **Methodology (Step-by-Step Plan)**

### **Phase 1 – Literature & Feasibility Study (Weeks 1–4)**

- Review existing work:
    
    - LLMs in mental health (e.g., Wysa, Replika, Woebot).
        
    - Emotion classification & sentiment models.
        
    - Federated learning for sensitive data.
        
    - Edge deployment & quantisation techniques.
        
- Define an ethical framework & risk boundaries (not for diagnosis, but as a reflection aid).
    

### **Phase 2 – Model Selection & Training Setup (Weeks 5–8)**

- Select candidate small LLM architectures:
    
    - **Phi-2**, **TinyLlama**, **Mistral-7B**, or **DistilGPT-2**.
        
- Choose fine-tuning method:
    
    - **Instruction tuning** on emotion-support dialogue datasets (EmpatheticDialogues, DailyDialog++, RECCON).
        
    - Use **LoRA** or **PEFT** for lightweight adaptation.
        
- Develop a **RAG pipeline** with curated psychoeducational documents for contextual grounding.
    

### **Phase 3 – Emotional Understanding Layer (Weeks 9–12)**

- Train a **lightweight emotion classifier** (transformer-based) to detect emotional tone and context.
    
- Integrate this layer with the conversational model to guide responses.
    
- Use **federated learning simulation** (e.g., Flower or FedML) for distributed training of emotion detection models.
    

### **Phase 4 – Edge Deployment & Optimization (Weeks 13–16)**

- Experiment with **quantization** (4-bit, 8-bit) and **distillation** to deploy the model on low-resource devices (Jetson Nano, Raspberry Pi, smartphone).
    
- Measure latency, throughput, and energy usage.
    
- Compare performance vs. cloud inference.
    

### **Phase 5 – Validation & Evaluation (Weeks 17–20)**

- **User Study / Expert Review:**
    
    - Simulate interactions with psychology students or therapists.
        
    - Evaluate empathy, coherence, helpfulness.
        
- **Quantitative Metrics:**
    
    - BLEU / ROUGE / BERTScore (for coherence).
        
    - Emotion alignment (F1 for emotion classification).
        
    - Carbon footprint estimation (energy used per interaction).
        
- **Qualitative Metrics:**
    
    - User satisfaction, perceived empathy, ethical compliance.
        

### **Phase 6 – Reporting & Ethics Review (Weeks 21–24)**

- Document architecture, training pipeline, and evaluation.
    
- Discuss ethical implications, limitations, and potential for real-world deployment.
    
- Submit for review with supervisors.
    

---

## 5. **Expected Outcomes**

- A **compact, privacy-preserving conversational assistant** capable of emotion-aware dialogue.
    
- Demonstration of **RAG-enhanced reasoning** for psychoeducational support.
    
- Prototype deployed on **edge hardware** (Jetson Nano or mobile).
    
- Federated learning proof-of-concept for privacy-preserving emotion learning.
    
- Validation framework for **ethical and empathetic LLM evaluation**.
    

---

## 6. **Potential Supervisors / Research Groups**

- Leiden Institute of Advanced Computer Science (LIACS):
    
    - **Human-Centric AI Lab**
        
    - **Leiden AI in Health and Psychology Group**
        
- Possible co-supervision:
    
    - Faculty of Psychology and Education (for ethical validation)
        
    - e.g., Dr. Anna van Duuren, Dr. Willem Zuidema, or AI & Mental Health researchers in Leiden or Utrecht
        

---

## 7. **Validation & Ethical Considerations**

- Adhere to **GDPR** and **EU AI Act** guidelines (AI for wellbeing).
    
- Perform **Ethics Committee approval** for any user data collection.
    
- Data anonymisation and federated setups to ensure no central storage of user data.
    
- Transparency in scope: _not a diagnostic or therapeutic tool_, but a _reflective assistant_.
    

---

## 8. **Extensions (Optional but Ambitious)**

- Add **speech-to-text / text-to-speech** modules for voice interaction.
    
- Add **multilingual embeddings** for cross-cultural emotion modelling.
    
- Integrate **NCF (Neural Collaborative Filtering)** to suggest personalised coping strategies based on collective anonymised data.
    

---

## 9. **Deliverables**

- ✅ Thesis report (~60 pages)
    
- ✅ Open-source prototype (Python + HuggingFace + RAG)
    
- ✅ Technical documentation + ethical assessment
    
- ✅ Presentation + live demo of the assistant
    

---

# Working Title (THINKING)

**“Small, Private, and Thoughtful: A Planner–Solver–Checker Reasoning LLM for Emotional Well-Being with RAG, Edge Deployment, and Federated Learning.”**

---

## 1) Motivation & Problem

Most mental-health chat agents rely on large black-box LLMs that are hard to deploy privately and often “sound empathetic” without **verifiable reasoning**. Your thesis targets a **small reasoning model** that (a) shows structured, auditable thinking via an internal scratchpad and verifier, (b) runs on edge devices, and (c) remains firmly _non-diagnostic_, focused on **psychoeducation, journaling, and emotion exploration**.

---

## 2) Research Questions

1. Can a **small LLM (≤1–3B params)** exhibit robust _stepwise reasoning_ in supportive conversations when equipped with a **planner–solver–checker** stack?
    
2. How much does **RAG** (psychoeducational sources) improve reasoning _faithfulness_ and _factuality_ for a compact model?
    
3. Can **reasoning traces** be **distilled** into a small model (e.g., “R1-style” or CoT distillation) without sacrificing latency and privacy?
    
4. What is the energy/latency trade-off of **edge inference** with quantization + LoRA adapters?
    
5. Can **federated learning** safely improve **non-diagnostic classification of symptoms/states** and **strategy recommendation** patterns?
    
6. What evaluation rubric best captures **empathy + reasoning quality + safety** in this domain?
    

---

## 3) Objectives

- Build a **reasoning-centric pipeline**: **Planner (task decomposition)** → **Solver (response generation)** → **Checker (factuality/safety/consistency)**.
    
- Keep the base model small (Phi-2/TinyLlama/1–3B class) with **PEFT/LoRA** and **int8/4-bit** inference.
    
- Add **RAG** over curated psychoeducation content (CBT/DBT skills, burnout/perfectionism literature, journaling prompts).
    
- Add **state/symptom classification** (not conditions) + **recommendation layer** (optionally NCF) for coping strategies.
    
- **Multilingual** capability (EN + NL to start; optional Malayalam).
    
- **Edge** deployment (Jetson/RPi/Android) + **Federated** updates for classifiers and recommender signals.
    
- A clear **human-subjects validation** and **ethics** protocol.
    

---

## 4) System Design (Thinking Model)

**A. Reasoning Core (Small LLM + Scratchpad)**

- **Internal scratchpad** (hidden from users): chain-of-thought style reasoning for planning and self-checks.
    
- **Program-Aided** hints when useful (e.g., emotion labeller outputs fed as structured hints to the solver).
    
- **Self-consistency** (sample multiple short internal plans, pick or merge via checker for final answer).
    
- **Toolformer/ReAct-lite**: controlled tool calls to (i) RAG retriever, (ii) emotion classifier, (iii) safety policy checker.
    

**B. Planner–Solver–Checker**

- **Planner**: decomposes user goal (e.g., “reflect on burnout patterns”) into micro-steps (clarify context → probe emotions → suggest journaling frame → offer coping options).
    
- **Solver**: drafts the user-visible reply using retrieved snippets + style policy (supportive, non-diagnostic).
    
- **Checker**:
    
    - **Factuality**: Does the reply align with the retrieved sources?
        
    - **Scope/Safety**: flags diagnostic/medical claims; nudges to disclaimers; provides resources if risk cues appear.
        
    - **Reasoning quality**: rule-based or small verifier model to catch contradictions.
        

**C. RAG (Domain Grounding)**

- Curated, non-clinical, evidence-based resources (psychoeducation, worksheets, journaling prompts).
    
- Chunked, citation-ready passages; **semantic + keyword** hybrid retrieval; de-duplication and recency tagging.
    
- Multilingual indexing (EN/NL), with locale-aware retrieval.
    

**D. Symptom/State & Strategy Layer**

- **Lightweight classifier** (emotion, stressors, cognitive distortions, coping intentions).
    
- **NCF or bandit-style recommender** for **methods that helped similar users** (purely non-diagnostic; opt-in; anonymised).
    
- Explanations like: “People who reported X often found Y helpful.”
    

**E. Privacy & Learning**

- **On-device inference** is used where possible; **telemetry is disabled by default**.
    
- **Federated learning** (Flower/FedML) for classifier/recommender updates; DP-noise optional; no raw logs leave the device.
    
- Server index for RAG can be public/hosted; user texts are never stored without consent.
    

---

## 5) Methodology & Timeline (24 weeks)

**Phase 1 — Scoping & Ethics (Weeks 1–3)**

- Define _non-diagnostic_ boundaries, escalation and crisis disclaimers, consent UX.
    
- Curate safe, evidence-based RAG corpus (burnout, perfectionism, journaling).
    
- IRB/ethics pre-screen; DPIA for GDPR; data handling SOP.
    

**Phase 2 — Base Model & Reasoning Adaptation (Weeks 4–8)**

- Pick base (e.g., **Phi-2 / TinyLlama / Qwen-1.5B**).
    
- **Instruction-tune** on supportive conversation tasks.
    
- Add **CoT/R1-style distillation** from a stronger teacher for _reasoning traces_ on synthetic tasks (planning, reframing, journaling scaffolds).
    
- Implement **Planner–Solver–Checker** controller; unit tests with synthetic dialogs.
    

**Phase 3 — RAG & Tools (Weeks 9–12)**

- Build retriever (bi-encoder + BM25 hybrid), reranker, and citation insertion.
    
- Train **emotion/state classifier** (EN first; NL via translate-train or multilingual backbone).
    
- Implement **safety checker** (rule-based + small classifier for red flags).
    
- Start **NCF prototype** (implicit feedback from opt-in pilot/simulations).
    

**Phase 4 — Edge & Federated (Weeks 13–16)**

- **Quantize** (int8/4-bit), **LoRA** heads for domain, measure latency/energy on Jetson/RPi/Android.
    
- **Federated simulation**: multiple clients with local logs → aggregate classifier/recommender weights (no raw text).
    
- Carbon/energy logging (per request Joules/Wh).
    

**Phase 5 — Evaluation & User Study (Weeks 17–21)**

- **Reasoning Quality**:
    
    - _Faithfulness_: groundedness rate (checker pass), citation correctness.
        
    - _Consistency_: contradiction rate across multi-turns.
        
    - _Planning quality_: expert rubric (coverage of journaling steps, CBT-style reframing correctness).
        
- **Conversation Quality**: Empathy/Helpfulness (Likert), coherence (BERTScore/MAUVE as proxies).
    
- **Safety/Scope**: % diagnostic claims (target ≈ 0), refusal correctness, escalation correctness.
    
- **Efficiency**: latency, tokens/sec, energy per conversation; edge vs server.
    
- **Multilingual**: parallel prompts in EN/NL—measure deltas.
    
- Small N **expert panel** (psych grad students) + **pilot users** (non-clinical).
    
- Optional A/B: with vs without Planner–Checker; with vs without RAG.
    

**Phase 6 — Write-up & Packaging (Weeks 22–24)**

- Full thesis, ablations, limitations, ethics appendix, and reproducible code.
    
- Demo: phone/Jetson app with on-device inference + opt-in federated toggle.
    

---

## 6) Datasets & Training Material (carefully curated)

- **Dialogue**: EmpatheticDialogues, DailyDialog++ (filtered for non-clinical use), synthetic journaling turns.
    
- **Reasoning Supervision**: synthetic _plans/checklists_ (e.g., “journal scaffold → identify thought → reframe → action”).
    
- **Emotion/State**: GoEmotions (mapped to your taxonomy), custom annotations from psychology students (small but high-quality).
    
- **RAG**: Licensed/allowlisted psychoeducational content, CBT/DBT worksheets, burnout/perfectionism articles; multilingual where possible.
    

_(Avoid medical/diagnostic datasets; keep the scope educational/supportive.)_

---

## 7) Validation Metrics (concise checklist)

**Reasoning & Grounding**

- Groundedness@turn (checker pass %), citation accuracy, contradiction rate.
    
- Plan completeness score (expert rubric).  
    **Conversation Quality**
    
- Empathy/helpfulness Likert; task success (did user produce a journal entry? identify emotions?).
    
- Coherence proxies (BERTScore / COMETkiwi-style entailment checks).  
    **Safety**
    
- Diagnostic claim rate, unsafe suggestion rate, correct refusal rate, escalation precision/recall.  
    **Efficiency & Sustainability**
    
- Latency P50/P95; energy per 10 turns (edge vs server); memory footprint.  
    **Multilingual**
    
- Drop in above metrics from EN→NL (and optionally Malayalam).  
    **Learning**
    
- Federated vs central baseline on classifier F1 and recommender CTR-proxy.
    

---

## 8) Risks & Mitigations

- **Leakage of diagnostic language** → strict templates + safety checker + training red-team data.
    
- **Hallucination** → enforce RAG citations; checker blocks ungrounded claims.
    
- **Edge performance** → back off to the server only with consent; keep the smallest viable model.
    
- **Federated privacy** → DP noise on updates; publish aggregation only; explicit consent UX.
    
- **Evaluation bias** → blind expert review, mixed user cohort, report confidence intervals.
    

---

## 9) Deliverables

- Code: controller (Planner–Solver–Checker), RAG, classifiers, recommender, edge builds, FL scripts.
    
- Datasets: curation scripts + documentation.
    
- Evaluation suite + red-teaming checklists.
    
- Demo app (text + optional voice).
    
- Thesis and ethics/DPIA appendix.
    

---

## 10) Nice-to-Have Extensions

- **Verifier LLM** distilled to **tiny “reasoning checker”** head.
    
- **Self-reflection loop** (Reflexion-style): store private “lessons” as rules, not user data.
    
- **Program-of-Thought** tools: simple calculators/trackers for mood journaling.
    

---

## Methodology & Timeline (24 weeks) [UPDATED]

### **Phase 1 – Literature & Feasibility Study**

- Review existing work:
    
    - ==LLMs in mental health (e.g., Wysa, Replika, Woebot).==
        
    - Emotion classification & sentiment models.
        
    - Federated learning for sensitive data.
        
    - Edge deployment & quantisation techniques.
        
- Define an ethical framework & risk boundaries (not for diagnosis, but as a reflection aid).
	
- Scoping & Ethics
	
	- Define _non-diagnostic_ boundaries, escalation and crisis disclaimers, and consent UX.
	    
	- Curate a safe, evidence-based RAG corpus (burnout, perfectionism, journaling).
	    
	- IRB/ethics pre-screen; DPIA for GDPR; data handling SOP.
	    

### **Phase 2 – Model Selection & Training Setup (Reasoning Adaptation)** 

- Select candidate small LLM architectures:
    
    - **Phi-2**, **TinyLlama**, **Mistral-7B**, or **DistilGPT-2**.
        
- Choose fine-tuning method:
    
    - **Instruction tuning** on emotion-support dialogue datasets (EmpatheticDialogues, DailyDialog++, RECCON).
        
    - Use **LoRA** or **PEFT** for lightweight adaptation.
        
- Add **CoT/R1-style distillation** from a stronger teacher for _reasoning traces_ on synthetic tasks (planning, reframing, journaling scaffolds).
	
- Implement a **Planner–Solver–Checker** controller and unit tests with synthetic dialogues.
	

### **Phase 3 - RAG & Tools**

- Develop a **RAG pipeline** with curated psychoeducational documents for contextual grounding.
	
- Build a retriever (bi-encoder + BM25 hybrid), a reranker, and citation insertion.
    
- Train **emotion/state classifier** (EN first; NL via translate-train or multilingual backbone).
    
- Implement **safety checker** (rule-based + small classifier for red flags).
    
- Start **NCF prototype** (implicit feedback from opt-in pilot/simulations).
    

### **Phase 4 – Emotional Understanding Layer**

- Train a **lightweight emotion classifier** (transformer-based) to detect emotional tone and context.
    
- Integrate this layer with the conversational model to guide responses.
    
- Utilise federated learning simulation tools (e.g., Flower or FedML) for the distributed training of emotion detection models.
    

### **Phase 5 – Edge Deployment & Optimisation & Federated**

- Experiment with **quantisation** (4-bit, 8-bit) and **distillation** to deploy the model on low-resource devices (Jetson Nano, Raspberry Pi, smartphone).
	
	- **Quantise** (int8/4-bit), **LoRA** heads for domain, measure latency/energy on Jetson/RPi/Android.
	    
- Measure latency, throughput, and energy usage.
    
- Compare performance vs. cloud inference.
    
- Carbon/energy logging (per request Joules/Wh).
	
- **Federated simulation**: multiple clients with local logs → aggregate classifier/recommender weights (no raw text).
    

### **Phase 6 – Validation & Evaluation & User Study**

- **User Study / Expert Review:**
    
    - Simulate interactions with psychology students or therapists.
        
    - Evaluate empathy, coherence, and helpfulness.
        
- **Quantitative Metrics:**
    
    - BLEU / ROUGE / BERTScore (for coherence).
        
    - Emotion alignment (F1 for emotion classification).
        
    - Carbon footprint estimation (energy used per interaction).
        
- **Qualitative Metrics:**
    
    - User satisfaction, perceived empathy, and ethical compliance.
        
- **Reasoning Quality**:
    
    - _Faithfulness_: groundedness rate (checker pass), citation correctness.
        
    - _Consistency_: contradiction rate across multi-turns.
        
    - _Planning quality_: expert rubric (coverage of journaling steps, CBT-style reframing correctness).
        
- **Conversation Quality**: Empathy/Helpfulness (Likert), coherence (BERTScore/MAUVE as proxies).
    
- **Safety/Scope**: % diagnostic claims (target ≈ 0), refusal correctness, escalation correctness.
    
- **Efficiency**: latency, tokens/sec, energy per conversation; edge vs server.
    
- **Multilingual**: parallel prompts in EN/NL—measure deltas.
    
- Small N **expert panel** (psych grad students) + **pilot users** (non-clinical).
    
- Optional A/B: with vs without Planner–Checker; with vs without RAG.
	

### **Phase 6 – Reporting & Ethics Review**

- Document architecture, training pipeline, and evaluation.
    
- Discuss ethical implications, limitations, and potential for real-world deployment.
    
- Submit for review with supervisors.
    
- Complete thesis, ablations, limitations, ethics appendix, and reproducible code.
    
- Demo: phone/Jetson app with on-device inference + opt-in federated toggle.

---