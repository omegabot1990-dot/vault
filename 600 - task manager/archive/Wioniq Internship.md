---
tags:
  - work
description: wioniq internship
due date:
start date:
end date:
status: Archive
importance level:
urgency level:
task type:
story points:
parent nodes:
child nodes:
recurrent:
---

#### Misc

Hugging Face Inference End Point Pricing - https://huggingface.co/pricing#endpoints


---

## **Internship Plan: Evaluating and Fine-Tuning Open-Source LLMs**

### **Objective**

To explore and benchmark open-source Large Language Models (LLMs) for replacing OpenAI APIs in our application and to design a reliable evaluation pipeline to ensure performance, relevance, and robustness.

---

### **Week 1-2: Familiarisation and Scoping**

#### Deliverables:

- Understand existing app architecture, backend integration with OpenAI APIs.
    
- Define core use cases: What types of questions does the user ask?
    
- Define success criteria: response accuracy, latency, cost, model footprint.

#### Actions:

- Conduct team interviews to gather functional requirements.
    
- Set up a sandbox testbed (e.g., small web interface + backend test runner).
    
- List datasets: Build or reuse a Q&A-style dataset that reflects real-world usage (e.g., AlpacaEval, TruthfulQA, custom app logs).

---

### **Week 3-4: Open-Source LLM Research and Testing**

#### Deliverables:

- Shortlist 3–5 top open-source models from HuggingFace based on benchmarks (e.g., Mistral, LLaMA 3, Phi-3, Gemma, Mixtral).
    
- Run zero-shot tests on real prompts to evaluate response quality.

#### Actions:

- Research model specs: performance, licensing, hardware requirements.
    
- Load models using `transformers`, `vLLM`, or `text-generation-webui`.
    
- Compare with OpenAI responses on the same prompt set.

---

### **Week 5-6: Fine-Tuning Pipeline Exploration**

#### Deliverables:

- Prototype a fine-tuning pipeline (e.g., using LoRA, PEFT, QLoRA).
    
- Identify/curate domain-specific data to improve model relevance.
    
- Fine-tune at least one smaller model on a limited dataset.

#### Actions:

- Use HuggingFace’s `Trainer`, PEFT library, or Axolotl.
    
- Experiment with quantised models (e.g., 4-bit with GGUF or GPTQ).
    
- Evaluate cost/performance trade-offs of fine-tuning vs prompt tuning.

---

### **Week 7-8: Evaluation Strategy and Metrics Design**

#### Deliverables:

- Design an evaluation framework (automated + human-in-the-loop).
    
- Implement scripts for:
    
    - BLEU / ROUGE / BERTScore
        
    - TruthfulQA / Hallucination rate
        
    - Custom relevance scoring using embedding similarity
        
- Set up basic A/B testing infrastructure (LLM A vs B vs OpenAI).

#### Actions:

- Use `lm-eval-harness`, `TruLens`, or `Ragas` to build eval suite.
    
- Build dashboard or output CSV for easy comparison.

---

### **Week 9-10: Deployment Strategy + Final Report**

#### Deliverables:

- Recommendation document: which model(s) to choose, when to fine-tune, expected costs, performance.
    
- Codebase with reproducible setup scripts, README, and sample configs.
    
- Presentation to the team.

#### Actions:

- Explore Dockerization or serverless options for model deployment.
    
- Run integration test simulations with existing backend.
    
- Document learnings and limitations.

---

## **Optional Extensions (Time-Permitting)**

- Explore retrieval-augmented generation (RAG) for factual grounding.
    
- Try RLHF or DPO-style preference fine-tuning using user feedback.
    
- Create CI pipeline to monitor hallucination drift or broken outputs.

---

## **Tools & Libraries**

| Task          | Tools                                                     |
| ------------- | --------------------------------------------------------- |
| Model Hosting | HuggingFace, vLLM, ollama, LM Studio                      |
| Fine-Tuning   | PEFT, LoRA, QLoRA, Axolotl                                |
| Evaluation    | RAGAS, lm-eval-harness, TruLens, BERTScore                |
| Deployment    | Docker, FastAPI, Streamlit, ONNX, Triton Inference Server |
| Hardware      | Colab Pro, AWS EC2 (GPU), local GPU if available          |

---

## **Success Criteria**

- At least one fine-tuned open-source LLM matches or exceeds OpenAI’s performance on internal benchmarks.
    
- Evaluation framework in place and reusable.
    
- Clear cost/performance deployment recommendation.

---
