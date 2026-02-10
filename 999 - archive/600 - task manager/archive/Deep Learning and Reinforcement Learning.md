---
tags:
  - inbox
  - work
  - academic
description:
due date:
start date: 2025-11-15
end date:
status: Archive
importance level: important
urgency level: urgent
task type: capture
story points: 8
parent nodes:
child nodes:
recurrent:
---

> Use as a method to learn Python, Tensorflow, and the Math behind the working.

# Resources

### Deep Learning

- [[d2l_en.pdf|D2L]]
- [Understanding Deep Learning - Website](https://udlbook.github.io/udlbook/)
	- Has some excellent content.
	- Theory and notebooks.
	- [Interactive Content](https://udlbook.github.io/udlfigures/)
- [[understanding_deep_learning_2025.pdf|Understanding Deep Learning]]
- [Deep Learning with Python](https://deeplearningwithpython.io/chapters/)
	- Very cool resource.

### Reinforcement Learning

- [[reinforcement_learning_an_introduction.pdf|Reinforcement Learning - An Introduction]]
- [[deep_reinforcement_learning.pdf|Deep Reinforcement Learning]]
- [OpenAI RL](https://spinningup.openai.com/en/latest/)
- [[reinforcement_learning_introduction.pdf|Reinforcement Learning Introduction]] - VERY IMPORTANT
	- http://incompleteideas.net/book/the-book-2nd.html
- [YouTube DeepMind x UCL - 2015](https://youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ&si=Z_ehZvM8ZBHQsMJf)
- [YouTube DeepMind x UCL - 2021](https://www.youtube.com/playlist?list=PLqYmG7hTraZDVH599EItlEWsUOsJbAodm)
- Blogs
	- [RLHF Book](https://rlhfbook.com/)

## Math Intuition

- [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [Essence of Calculus](https://youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr&si=bZEfsQrzly6-EWX4)
- [Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

## Hugging Face

- [LLM Course](https://huggingface.co/learn/llm-course/chapter7/1)

## Notes

### Introduction

- For a **Data Point** (Example or Sample), there is a set of attributes we call **Features** (Covariates), and our objective is to predict another feature, called the Label (Target), that is not part of the input space.
- A model is a statistical model that can estimate or predict based on Data.
	- Takes Data as input and predicts Labels as output.
- **Objective Functions** define a formal measure of how good or bad the predicted Label is.
	- Generally framed as lower-the-better, hence called **Loss Functions**.
	- When it's harder to optimise because of non-differentiability or other complications, we might use a **Surrogate Objective**.
- **Overfitting** is when a model performs well on training data but does not generalise to unseen data (test data).
- Supervised Learning
	- We estimate the conditional probability of a label given input features.
- Unsupervised Learning
	- Clustering
	- Subspace Estimation
		- Principal Component Analysis (PCA) (Linear)?
	- Causality
	- Probabilistic Graphical Models
	- Variational Autoencoders?
	- Generative Adversarial Networks?
	- Normalising Flows?
	- Diffusion Models?
- **Offline Learning** is when learning takes place with the algorithm disconnected from the environment.
- Reinforcement Learning
	- Markov Decision Process
		- The environment is fully observable
	- Contextual Bandit Problem
		- The state does not depend on previous actions
	- Multi-armed Bandit Problem
		- There is no state, only a set of available actions with initially unknown rewards
- Check out papers from:
	- https://d2l.ai/chapter_introduction/index.html#the-road-to-deep-learning

### Preliminaries

- **Imputation** replaces missing values with estimates, whereas **deletion** discards either the rows or the columns containing missing values.
