---
tags:
  - academic
  - rl
description: assignment one for RL
due date: 2025-03-14
start date:
end date: 2025-03-17
status: Archive
importance level: important
urgency level: urgent
task type: execute
story points:
parent nodes:
child nodes:
recurrent:
---

## **📌 Preliminary Plan for Tackling the Assignment (Q-Learning - Tabular & Deep)**

This assignment consists of two major **components**:

1. **Theoretical Component:** Understanding Q-learning, loss functions, and deep function approximation.
2. **Experimental Component:** Implementing Q-learning (tabular & deep), running experiments, analyzing results.

The **final deliverables** include:

- **Source code**
- **Requirements file**
- **Scientific report (LaTeX format, 4-6 pages)**

---

# **✅ Phase 1: Understanding the Assignment & Setting Up the Environment**

### **📌 Tasks**

1. **Read & Understand Q-learning**
    
    - Understand **Tabular Q-learning** and why it's limited for large/continuous state spaces.
    - Understand how **Deep Q-Networks (DQN)** overcomes tabular Q-learning's limitations.
2. **Set up a development environment**
    
    - Create a virtual environment:
        
        ```bash
        python -m venv qlearning_env
        source qlearning_env/bin/activate  # Linux/Mac
        qlearning_env\Scripts\activate     # Windows
        ```
        
    - Install required packages:
        
        ```bash
        pip install numpy gymnasium torch matplotlib
        ```
        

---

# **✅ Phase 2: Theoretical Questions**

### **📌 Tasks**

1. **Explain how the DQN loss function is derived**
    
    - Show how we move from **Bellman equations** to a differentiable loss function.
2. **Why can't we use tabular RL update rules in Deep RL?**
    
    - Discuss issues with large/continuous state spaces.
    - Explain why function approximation (neural networks) is required.
3. **Write Pseudo Code for DQN with Experience Replay (ER) & Target Networks (TN)**
    
    - Provide a 10-step summary of how DQN works with **ER & TN**.

---

# **✅ Phase 3: Implement Q-Learning in CartPole**

### **📌 Tasks**

1. **Implement Tabular Q-learning**
    
    - Train an agent using **Q-tables**.
    - Plot **learning curves (return vs environment steps)**.
    - Analyze **whether the agent reaches optimal performance**.
2. **Implement Deep Q-Learning (DQN)**
    
    - Use a **neural network to approximate Q-values** instead of a table.
    - Define **network architecture** (input → fully connected layers → output).
    - Implement **DQN training loop** (similar to tabular Q-learning).
3. **Ablation Study: Hyperparameter Analysis**
    
    - Tune:
        - **Learning rate**
        - **Update-to-data ratio**
        - **Network size**
        - **Exploration factor (ε-greedy)**
    - **Test 3 values** for each (small, medium, large).
    - Plot the impact on learning.

---

# **✅ Phase 4: Implement Target Networks & Experience Replay**

### **📌 Tasks**

1. **Add Target Networks (TN)**
    
    - Create a **separate Q-network** for target values.
    - Periodically copy weights from the main network.
2. **Implement Experience Replay (ER)**
    
    - Store past experiences in a **replay buffer**.
    - Train the network by sampling **mini-batches**.
3. **Compare all four configurations:**
    
    - **Naïve DQN**
    - **DQN + TN**
    - **DQN + ER**
    - **DQN + TN & ER**
4. **Plot results & compare performance.**
    
    - Single graph comparing all four configurations.

---

# **✅ Phase 5: Write the Scientific Report**

### **📌 Required Sections**

1. **Abstract (¼ page)**
    
    - Summarize the problem, approach, and key findings.
2. **Introduction (½ page)**
    
    - Explain RL, Q-learning, and the motivation for Deep RL.
3. **Theory (1 page)**
    
    - Derivation of the **DQN loss function**.
    - Why **tabular updates fail for Deep RL**.
4. **Experiments (1-2 pages)**
    
    - Describe the **CartPole environment**.
    - Explain the **training setup & hyperparameters**.
5. **Results (1-2 pages)**
    
    - Present **learning curves**.
    - Show results from the **ablation study**.
    - Compare **Naïve vs TN vs ER vs TN+ER**.
6. **Discussion (½ page)**
    
    - **Analyze weaknesses & performance bottlenecks**.
7. **Conclusion (½ page)**
    
    - Reflect on **what was learned & future improvements**.

---

# **✅ Phase 6: Finalizing the Submission**

### **📌 Tasks**

1. **Document the code**
    
    - Create a `README.md` with instructions for running experiments.
    - Provide a `requirements.txt` file:
        
        ```bash
        pip freeze > requirements.txt
        ```
        
2. **Format the report using the ICML LaTeX template**
    
    - **Overleaf Link:** [ICML Template](https://www.overleaf.com/latex/templates/icml2021-template/dsftnbmjgyhv)
    - Compile a **PDF report** (4-6 pages).
3. **Test on a University Lab Machine**
    
    - Ensure code runs on **Linux** in the university environment.
4. **Submit before the deadline (March 14, 23:59:59)**
    

---

# **🎯 Summary: High-Level Plan**

|**Phase**|**Tasks**|
|---|---|
|**Phase 1**|Understand Q-learning & set up environment|
|**Phase 2**|Answer theoretical questions & write pseudo-code|
|**Phase 3**|Implement Q-learning (tabular & deep) in CartPole|
|**Phase 4**|Implement Target Networks & Experience Replay|
|**Phase 5**|Run experiments & analyze results|
|**Phase 6**|Write the scientific report & finalize submission|

---

# **🚀 Next Steps**

- **Start implementing Tabular Q-learning today**.
- **Write theoretical answers while running experiments**.
- **Implement DQN & ablation study over the next few days**.
- **Finalize the report by March 13**.

