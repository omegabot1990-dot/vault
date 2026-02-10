---
tags:
  - work
aliases:
  - ethics, evaluation and safety 001
title: ethics, evaluation and safety 001
description:
parent nodes:
  - "[[202510300118 - proposal 001]]"
child nodes:
annotation-target:
---

### **Ethics, Evaluation & Safety Framework**

- Adhere to **GDPR** and **EU AI Act** compliance guidelines (AI for wellbeing).
    
- Obtain **Ethics Committee approval** for any user data collection or pilot studies.
    
- Ensure **data anonymisation** and **federated learning setups** to prevent any central storage of sensitive data.
    
- Maintain full **transparency of scope**:  
    _Not a diagnostic or therapeutic tool_, but a **reflective, supportive assistant** aimed at emotional awareness and journaling guidance.
    

---

### **Reasoning & Grounding**

- Measure **Groundedness@turn** (checker pass rate).
    
- Track **citation accuracy** and **contradiction rate** across turns.
    
- Evaluate **plan completeness** using expert rubrics for journaling and cognitive reframing coverage.
    

---

### **Conversation Quality**

- Evaluate **empathy** and **helpfulness** using Likert-scale expert ratings.
    
- Measure **task success** (e.g., whether the user identified emotions or completed a reflective entry).
    
- Compute **coherence proxies** via BERTScore / COMETkiwi-style entailment checks.
    

---

### **Safety**

- Track **diagnostic claim rate** (target ≈ 0).
    
- Record **unsafe suggestion rate**, **correct refusal rate**, and **escalation precision/recall**.
    
- Enforce **strict language templates** to prevent leakage of diagnostic or clinical terms.
    

---

### **Efficiency & Sustainability**

- Log **latency (P50/P95)**, **tokens/sec**, and **energy per 10 turns** (edge vs. server).
    
- Monitor **memory footprint** and **carbon cost per interaction**.
    

---

### **Multilingual Evaluation**

- Compare all the above metrics across **English (EN)**, **Dutch (NL)**, and optionally **Malayalam**.
    
- Measure **drop in coherence, empathy, and safety** metrics across languages.
    

---

### **Learning & Federated Evaluation**

- Compare **Federated vs Centralized** training performance:
    
    - Classifier: F1-score differences.
        
    - Recommender: CTR-proxy differences.
        
- Add **differential privacy (DP)** noise to updates; publish only aggregated weights.
    
- Include explicit **consent UX** for any federated participation.
    

---

### **Failure Modes & Mitigation**

- **Leakage of Diagnostic Language** → strict output templates, safety classifier, and red-teamed data.
    
- **Hallucination or Ungrounded Claims** → enforce RAG citation verification; checker blocks responses without valid sources.
    
- **Edge Performance Degradation** → automatic fallback to server inference _only with user consent_; maintain the smallest viable on-device model.
    
- **Federated Privacy Risks** → apply DP noise, secure aggregation, and local model transparency logs.
    
- **Evaluation Bias** → blind expert review, balanced participant sampling, and reporting of confidence intervals.
    

---