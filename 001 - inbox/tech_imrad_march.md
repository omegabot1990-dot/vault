# Domain Adaptation of Large Language Models (LLMs) with Reinforcement Learning and Tool Use

Authors: Gaurisankar Jayadas

Date: 2026-03-11  

## Abstract

Large Language Models (LLMs) have become an everyday object of todays world, whether it be as a simple chat assistant or a autonomous agent, their presence is ubiquitous. Nowadays we see these models exhibit capabilities that are generalist and applicable to a wide array of domains. One of the biggest barriers to entry for self-hosting and training these models is their massive size. The frontier models that the public has access to is over 600B parameters. Beyond compute constraints the other big barrier is data privacy issues. Our objective is to explore specialize these generalist models to our particular domain by breaking these barriers. For this we will use open-source LLMs of smaller sizes (0.5M to 10B) that can be trained in resource constrained setting without concerns regarding issues around data privacy. We will explore reinforcement learning and supervised fine-tuning, separately and in combination, as a means of training our model to exhibit the behavior we expect.

Keywords: large language models, supervised fine-tuning, reinforcement learning

## Introduction

Sequence modelling was a long standing issue that troubled Deep Learning for many years. Over the years, many solutions have been proposed for this including Recurrent Neural Networks (RNN) with sophisticated memory management units such as Long-Short Term Memory (LSTM) or their simpler relatives Gated Recurrent Units (GRUs). But they suffered from two major issues, long-range dependencies and sequential computation. But in 2017, a new sort of architecture was introduced as a solution for a machine translation model, called the Transformer [1]. Transformers, unlike its predecessors, had long context windows and could be processed in parallel. And from then it has become the cutting edge of Deep Learning architectures, from language models to vision models and beyond.

![transformer](https://paper-assets.alphaxiv.org/figures/1706.03762v7/ModalNet-21.png)

The encoder-decoder architecture was introduced for language understanding tasks. The decoder only module was later on adapted to make what we now know as the transformer based Large Language Models (LLMs). The transformer architecture comprises of stacked transformer blocks which are a combination of attention blocks which helps the each entity of the sequence to refine each other and a feed-forward block that refines each entity of a sequence. Fast-forward two years, researchers from OpenAI released GPT2 (Generative Pre-trained Transformer) [2], they exhibited that scaling this architecture and pre-training it in a self-supervised fashion created models that could do multiple tasks that they were not explicitly taught. This was the start of the race for intelligence. Subsequently in 2020, GPT3 [3] was released, they scaled the architecture from 124M parameter to 175B parameters and showed promising results with few-shot prompting. In 2022 InstructGPT [4], was released, post-training with a 3-stage pipeline; which included 1) supervised fine-tuning 2) reward model training on preference data 3) and using the reward model to train the model with reinforcement learning with an updated Proximal Policy Optimization algorithm; could align models to behave according to human preferences and instructions. 
2023 was the year the public got to know about LLMs, GPT3.5 was released and took the world by storm. The race towards intelligence had become ever more involved. From 2023 to 2025 we saw the field become saturated by numerous players. January 2025, DeepSeek came out with an open-source rival to OpenAI proprietary O1 model, DeepSeek-R1 [5]. Chain-of-Thought had already been established as a novel prompting mechanism to improve LLM accuracy, DeepSeek showcased that "reasoning" could be elicited only by large scale reinforcement learning.

This is where we start our journey. We will explore means to use a combination of SFT and RL to elicit domain specific reasoning in LLMs of smaller size that can be trained in a constrained compute environment. We choose Group Relative Policy Optimization (GRPO) for RL because of its need for less compute compared to PPO which is an Actor-Critic method. Furthermore, we will explore the use of tools to enable sophisticated reasoning over specific domains.


## Methods

We choose to employ supervised fine-tuning and reinforcement learning for training our model. Both paradigms use Back Propagation to update the weight using gradient based methods. 
As for the objective function for SFT, we use causal language modelling with or without masks and the loss function is calculated via cross-entropy loss between the logits and the gold-label targets, the optimization algorithm is gradient descent (Adam, AdamW, Muon). 

Dataset:
$$
\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{N}, \quad y_i = (y_{i,1},\ldots,y_{i,T_i})
$$

Supervised fine-tuning loss:
$$
\mathcal{L}_{\mathrm{SFT}}(\theta)
= - \frac{1}{\sum_{i=1}^{N} T_i}
\sum_{i=1}^{N} \sum_{t=1}^{T_i}
\log p_{\theta}\!\left(y_{i,t} \mid x_i,\, y_{i,<t}\right)
$$

Masked variant (e.g., only score target tokens of interest):
$$
\mathcal{L}_{\mathrm{SFT}}^{\text{mask}}(\theta)
= - \frac{1}{\sum_{i=1}^{N}\sum_{t=1}^{T_i} m_{i,t}}
\sum_{i=1}^{N} \sum_{t=1}^{T_i}
m_{i,t}\, \log p_{\theta}\!\left(y_{i,t} \mid x_i,\, y_{i,<t}\right),
\qquad m_{i,t}\in\{0,1\}.
$$

For reinforcement learning, we choose to use Group Relative Policy Optimization (GRPO), which is a variant of Policy Gradient Methods. It builds on top of Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO) but removes the Value model and replacing it with a group based advantage calculation that stops it from being an actor-critic method to a pure policy gradient one. This algorithm has shown promise from its introduction by DeepSeek Math [6]. It is more light-weight since we avoid the critic essentially bringing down the compute to half. Furthermore, it uses a KL term in order to mitigate variance along with the clipped objective borrowed from PPO. The reward function will be designed in due time and this will be the direct scientific contribution we choose to deliver.

GRPO loss (cross-entropy to match $p_j(\theta)$ to \$q_j$, with optional KL regularization to the reference policy):
$$
\mathcal{L}_{\text{GRPO}}(\theta)
\;=\;
\mathbb{E}_{x,\mathcal{G}(x)}\!\left[
-\sum_{j=1}^{K} q_j \,\log p_j(\theta)
\right]
\;+\;
\lambda \,\mathbb{E}_{x}\!\left[
\mathrm{KL}\!\big(\pi_\theta(\cdot\mid x)\,\|\,\pi_{\text{ref}}(\cdot\mid x)\big)
\right].
$$

$$
A_j \;=\; r_j \;-\; b,
\qquad
b \;=\; \frac{1}{K}\sum_{k=1}^{K} r_k
\quad\text{(group mean as baseline)}.
$$

Gradient (using $\partial \mathcal{L}/\partial \ell_j = p_j - q_j$:
$$
\nabla_\theta \mathcal{L}_{\text{GRPO}}(\theta)
\;=\;
\mathbb{E}_{x,\mathcal{G}(x)}\!\left[
\sum_{j=1}^{K} \big(p_j(\theta) - q_j\big)\, \nabla_\theta \ell_j(\theta)
\right]
\;+\;
\lambda \,\nabla_\theta \,\mathbb{E}_{x}\!\left[
\mathrm{KL}\!\big(\pi_\theta(\cdot\mid x)\,\|\,\pi_{\text{ref}}(\cdot\mid x)\big)
\right].
$$

Parameter update (e.g., SGD; in practice use Adam/AdamW):
$$
\theta \leftarrow \theta \;-\; \eta \,\nabla_\theta \mathcal{L}_{\text{GRPO}}(\theta).
$$

## Data
- TBD

## Results
- TBD

## Discussion
- TBD

## References
1. [Attention Is All You Need](https://www.alphaxiv.org/overview/1706.03762)
2. [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
3. [Language Models are Few-Shot Learners](https://www.alphaxiv.org/overview/2005.14165)
4. [Training language models to follow instructions with human feedback](https://www.alphaxiv.org/overview/2203.02155)
5. [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://www.alphaxiv.org/overview/2501.12948v1)
6. [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://www.alphaxiv.org/overview/2402.03300v3)