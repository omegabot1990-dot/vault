---
tags:
  - inbox
description: Internship Plan
bot: false
status: In Progress
task type: recurrent
urgency level: urgent
importance level: important
due date:
start date:
end date:
story points: 5
recurrent: true
parent nodes:
---
# **6‑Month Internship Plan: Domain‑Specialized LLM / SLM Adaptation (DAPT, SFT, RL)**

### *For Railway Root Cause Analysis & Maintenance Expertise Transfer into LLMs*

***

# **0) Program Overview**

### **Purpose**

Enable a small/medium LLM (1B–7B) to understand and reason over:

*   train component failures
*   field service reports
*   root-cause analysis chains
*   diagnostic sequences
*   repair procedures
*   domain‑specific jargon used in railway operations, FRB reports, and maintenance logs

### **Outcomes**

By the end of 6 months, the intern produces:

**Technical Outcomes**

*   A domain-specialized LLM (1–7B) adapted using:
    *   **RL (RLVR + GRPO)**
    *   **SFT**
        * **Final-layers**
        *  **LoRA**
    * **DAPT** - Only if needed?
*   A reproducible **training + inference pipeline**, with an evaluation suite and benchmarks.
*   ==A library of **Tool‑Verified reasoning tasks** tailored to railway diagnostics.== - What is this?

**Business Outcomes**

*   A prototype model capable of:
    *   Suggesting root causes from textual descriptions
    *   Summarising FRB discussions
    *   Extracting failure patterns from service notes
    *   Proposing repair actions with traceable reasoning

**Artifacts**

*   Code: notebooks + training pipelines + evaluation suite
*   Reports: IMRaD `.md` documents (monthly), technical + business
*   Release: v1.0 domain-adapted LLM
*   Handover & roadmap for productionization

***

# **1) Meeting Cadence & Governance**

**Daily**

*   15‑min stand‑up (yesterday/today/blockers)

**Monthly Technical Review**

*   Alireza, Thijs, FSCO domain expert
*   Evaluate: data prep, SFT progress, RL stability, evaluation metrics, ==DAPT quality?==

**Monthly Business Review**

*   Alireza + Erik
*   Evaluate business value, reasoning accuracy, domain adoption, and user fit

**Open Door Policy**

*   Intern can ask Alireza at any time

**Decision Gates** ==TODO: UPDATE==

*   **Gate A (Week 4):** Base Model + Training Pipelines
*   ==**Gate A (Week 4):** Data readiness + corpus design validated== TODO: REMOVE
## Task

- 

*   **Gate B (Week 8):** DAPT + LoRA → coherent domain outputs
*   **Gate C (Week 16):** SFT + baseline RL working
*   **Gate D (Week 22):** Prototype reasoning model validated
*   **Gate E (Week 24):** Final handover & roadmap accepted

***

# **2) Deliverables** ==TODO: UPDATE==

### **Code (Notebooks & Scripts)**

*   Data preprocessing + corpus builder
*   Tokenizer extension (if needed)
*   DAPT training pipeline (LoRA-adapted)
*   SFT pipeline
*   RL training pipeline (RLVR + GRPO)
*   Evaluation suite (perplexity; domain QA; reasoning tree validation; tool-use verification)
*   Model packaging (weights + adapter + configs)
*   Inference server (if relevant)

### **Reports (IMRaD, Markdown in Git repo)**

*   **Tech IMRaD** (monthly updates)
*   **Business IMRaD-lite** (monthly)
*   **Final RL report**
*   **Handover & roadmap**

***

# **3) Repository Structure** ==TODO: UPDATE==

    repo/
      README.md
      reports/
        tech_imrad.md
        business_imrad.md
        rl_research_report.md
        handover.md
      data/
        raw_corpus/
        cleaned_corpus/
        tokenizer/
        metadata.json
      notebooks/
        01_corpus_builder.ipynb
        02_tokenizer.ipynb
        03_dapt.ipynb
        04_sft.ipynb
        05_rl_training.ipynb
        06_eval.ipynb
      src/
        data/
        training/
          dapt/
          sft/
          rl/
        evaluation/
        inference/
      configs/
        dapt.yaml
        sft.yaml
        rl.yaml
        eval.yaml
      scripts/
        run_dapt.py
        run_sft.py
        run_rl.py
        eval.py
      models/
        base_model/
        adapters/
      ci/
        workflow.yaml
      requirements.txt
      Dockerfile

***

# **4) Evaluation Metrics** ==TODO: UPDATE==

### **DAPT**

*   Perplexity on the domain corpus
*   Vocabulary coverage score
*   Jargon comprehension tests

### **SFT**

*   Exact Match / F1 on domain QA pairs
*   Task accuracy (diagnosis classification, reasoning steps)
*   Instruction adherence score

### **RL (RLVR + GRPO)**

*   Reward: verifiable correctness (tool‑based)
*   Refusal rate (must avoid hallucinating repairs)
*   Chain‑of‑thought validity (structured, testable)
*   Stability: variance of reward across training windows
*   Safety score for repair suggestions

### **Business**

*   Model usefulness to FSCOs
*   Accuracy on root cause reasoning tasks
*   Reduction in time required to analyse FRB entries
*   Internal adoption potential

***

# **5) Month‑by‑Month Plan**

***

## **Month 1 — Base Model Creation, Supervised Fine-tuning (Full vs Layer-wise vs LoRA) Pipeline, Reinforcement Learning Pipeline, Generic Evaluation Benchmarks**

### *(Weeks 1–4)*

**Objectives**

* Build Qwen3 0.6B (base model) in Pytorch.
* Build SFT training pipeline.
	* Extend with LoRA training pipeline.
*  Build an RL training pipeline.
	* Implement Group Relative Policy Optimization.
	* Build a reward model.
* Build a suite that can run the Evaluation Benchmarks.

**Tasks**

* Build the Qwen3 architecture in Python using PyTorch.
	* Create a modular code base for Qwen3.
	* Create a notebook to load model weights.
	* Build an inference pipeline.
		* Temperature
		* Top-k
		* To be updated....
* Build a training pipeline for fine-tuning an LLM.
	* Layer selection.
	* LoRA capability.
* Build a training pipeline for reinforcement learning with GRPO.
* Build a test suite.
	* Multi-hop reasoning benchmarks:
		* MuSiQue
		- HotpotQA
		- 2WikiMultiHopQA
		- Bamboogle

**Deliverables**

*   `notebooks/qwen_model_loader.ipynb`
*   `qwen3`
*   `reports/tech_imrad.md` v1
*   **Gate A**: Base Model + Training Pipelines


---
## **Month 1 — Corpus Creation, Tokenizer, and DAPT Planning**

### *(Weeks 1–4)*

**Objectives**

*   Build the domain-specific corpus (FRB documents, repair logs, service notes, field maintenance bulletins, component manuals).
*   Preprocess and clean text
*   Prepare tokenizer adaptation plan
*   Align computational constraints (GPU budget, sequence lengths)

**Tasks**

*   Data discovery + privacy filtering
*   Build a corpus builder notebook
*   Cleaning (de-duplication, section extraction, formatting)
*   Domain vocabulary extraction (technical jargon, component names)
*   Extend tokenizer (if needed)
*   Draft training config for DAPT with LoRA

**Deliverables**

*   `notebooks/01_corpus_builder.ipynb`
*   `notebooks/02_tokenizer.ipynb`
*   `reports/tech_imrad.md` v1
*   **Gate A**: corpus approved + training plan ready

***

## **Month 2 — DAPT + LoRA Training (Domain Adaptation)**

### *(Weeks 5–8)*

**Objectives**

*   Train LoRA-based DAPT to teach the model the domain language
*   Evaluate improvements in jargon comprehension

**Tasks**

*   Configure LoRA ranks, dropout, adapters
*   Run DAPT training (long‑context sequences)
*   Evaluate perplexity before/after DAPT
*   Check outputs on diagnostic prompts (“Explain bearing degradation…”)
*   Optimize tokenization coverage

**Deliverables**

*   `scripts/run_dapt.py`
*   `notebooks/03_dapt.ipynb`
*   Updated tokenizer (if used)
*   `reports/tech_imrad.md` v2
*   **Gate B**: model generates domain‑valid text consistently

***

## **Month 3 — Supervised Fine Tuning (SFT) for Structured Tasks**

### *(Weeks 9–12)*

**Objectives**

*   Teach the model *structured reasoning tasks* using SFT
*   Build datasets for:
    *   Failure classification
    *   Root cause hypotheses
    *   Repair recommendations
    *   FRB Q\&A

**Tasks**

*   Label construction:
    *   Convert FRB reports into instruction–response pairs
    *   Develop structured reasoning templates (chain-of-thought → justified answers)
*   SFT training using LoRA or QLoRA
*   Compare SFT with and without reasoning scaffolds
*   Create evaluation suite

**Deliverables**

*   `scripts/run_sft.py`
*   `notebooks/04_sft.ipynb`
*   Task dataset (instruction tuning)
*   Metrics: EM, F1, accuracy
*   `reports/tech_imrad.md` v3
*   **Monthly Business Review**

***

## **Month 4 — Reinforcement Learning: RLVR + GRPO**

### *(Weeks 13–16)*

**Objectives**

*   Enable *reasoning* and *verifiable correctness* through RL
*   Implement RLVR (reward based on verifiable facts)
*   Use GRPO to stabilize policy updates

**Tasks**

*   Build verifiable tasks:
    *   “Is the suggested root cause consistent with evidence?”
    *   “Is the repair action valid for this component?”
    *   “Does the reasoning chain follow structural rules?”
*   Implement RLVR reward functions
*   Implement GRPO update loop
*   Run initial RL experiments

**Deliverables**

*   `scripts/run_rl.py`
*   `notebooks/05_rl_training.ipynb`
*   Reward definitions + evaluation
*   `reports/rl_research_report.md` (initial draft)
*   **Gate C**: RL training produces stable improvements

***

## **Month 5 — RL Iteration, Tool‑Use Integration & Evaluation**

### *(Weeks 17–20)*

**Objectives**

*   Refine RL training
*   Add tool-assisted verification (e.g., a failure-mode lookup table)
*   Evaluate models across multiple tasks

**Tasks**

*   Implement tool-use API (special case under RLVR)
*   Integrate domain knowledge base (failure components, symptoms → causes)
*   Evaluate reasoning accuracy and safety
*   Side-by-side comparisons:
    *   SFT
    *   SFT + RL
    *   RL‑only

**Deliverables**

*   `notebooks/06_eval.ipynb`
*   Evaluation benchmarks & dashboards
*   Business IMRaD update
*   **Monthly Business Review**
*   **Gate D**: final prototype model demonstrates domain reasoning capacity

***

## **Month 6 — Consolidation, Packaging, Handover & Roadmap**

### *(Weeks 21–24)*

**Objectives**

*   Freeze the best model
*   Package inference pipeline
*   Deliver documentation, IMRaDs, and long-term roadmap

**Tasks**

*   Consolidate SFT + RL best checkpoints
*   Package inference server
*   Create an internal demo of “Ask the FRB Model”
*   Final reports
*   Handover to engineering + FSCO stakeholders
*   Future roadmap (bigger models, improved RL, safety gating)

**Deliverables**

*   Final `reports/handover.md`
*   Final IMRaD technical + business
*   v1.0 model release
*   Architecture diagram
*   **Gate E**: approval from Erik & FSCO groups

***

# **6) Risk Register (LLM‑specific)**

*   **Catastrophic forgetting during DAPT** → use LoRA adapters; monitor general capabilities
*   **Hallucinations in repair actions** → integrate rule-based verifiers; RLVR rewards
*   **Data leakage** from internal documents → strict preprocessing
*   **Training instability in RL** → use GRPO for clipping + controlled step sizes
*   **GPU constraints** → prioritise 1B–7B, use QLoRA + gradient accumulation
*   **Safety concerns** → implement refusal rules for unsafe instructions

***

# **7) Stretch Goals (If Time Permits)**

*   Multi-turn FRB entries summarizer
*   Causal reasoning traces
*   Mixture‑of‑Experts on top of a domain specialist
*   Synthetic data generation for rare failure modes
*   Multi-modal integration (pictures of components → text reasoning)
