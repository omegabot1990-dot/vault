---
tags:
  - training
  - evaluation
aliases:
  - Pair-Wise Ranking Loss
  - Pairwise Ranking Loss
title: pair-wise ranking loss
description: ""
bot: false
parent nodes:
  - "[[202602120145 - loss|Loss]]"
published on:
---

- Pair-wise ranking loss [[202602111335 - training|trains]] a [[202602010044 - model|model]] to score preferred items higher than non-preferred items
- It is defined on pairs $(x^+, x^-)$ instead of single-labelled targets
- A common form is margin ranking loss:

> [!MATH] Marginal Ranking Loss
> $$\mathcal{L}=\max(0, m - s(x^+) + s(x^-))$$

- Another common form is logistic pairwise loss:

> [!MATH] Logistic Pairwise Loss
> $$\mathcal{L}=\log\left(1+\exp(-(s(x^+) - s(x^-)))\right)$$

- The Bradley-Terry Model
	- We assume the probability that a human prefers completion $y_w$ over $y_l$ follows a [[202602111510 - sigmoid|sigmoid]] distribution of the difference in their rewards:

> [!MATH] Bradley-Terry Model
> $$P(y_w \succ y_l) = \sigma(r_\phi(x, y_w) - r_\phi(x, y_l))$$
>
> * $y_w$: The "winning" or preferred completion
> * $y_l$: The "losing" or rejected completion
> * $x$: The input prompt/state
> * $r_\phi$: The Reward Model being trained (parameterized by $\phi$)
> * $\sigma$: The sigmoid function, $\sigma(z) = \frac{1}{1 + e^{-z}}$

- The Negative Log-Likelihood Loss
	- To train the model, we want to maximise the probability of the preferred choice. In optimization, we minimise the negative log-likelihood (NLL):

> [!MATH] Negative Log-Likelihood Loss
> $$L(\phi) = -\mathbb{E}_{(x, y_w, y_l) \sim D} [\log(\sigma(r_\phi(x, y_w) - r_\phi(x, y_l)))]$$
> 
> - $L(\phi)$: The pairwise ranking loss
> - $D$: The dataset of human-labeled comparisons
> - $\mathbb{E}$: The expectation over the sampled triples (prompt, winner, loser)

- Sometimes a margin $m$ or a bias term is added to ensure the model doesn't just barely separate the scores, but creates a meaningful gap:

> [!MATH] Adding a Regularizer 
> $$L(\phi) = -\mathbb{E} [\log(\sigma(r_\phi(x, y_w) - r_\phi(x, y_l) - m))]$$
> $m$: A margin hyperparameter to enforce a minimum distance between scores

- It is widely used in preference learning, recommendation, information retrieval, and [[202602192217 - reinforcement learning human feedback|RLHF]]-style ranking data
- Performance depends on pair quality, score calibration, and [[202602020105 - negative sampling|negative-sampling]] strategy
