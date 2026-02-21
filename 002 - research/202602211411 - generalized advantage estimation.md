---
tags:
  - reinforcement_learning
aliases:
  - Generalized Advantage Estimation
  - GAE
title: generalized advantage estimation
description: ""
bot: false
parent nodes:
  - "[[202602200148 - advantage|Advantage]]"
published on:
---

- Generalised Advantage Estimation (GAE) computes low-[[202602062206 - variance|variance]] [[202602200129 - policy gradient methods|policy-gradient]] [[202602200148 - advantage|advantages]] by exponentially weighting multi-step [[202602201305 - temporal-difference algorithm|TD residuals]]
- It introduces a [[202602201850 - bias-variance tradeoff|bias-variance tradeoff]] controlled by $\lambda$ between [[202602201958 - monte carlo|Monte Carlo]]-like and TD-like estimates
- With a [[202602200020 - value|value]] baseline $V$, TD residuals are:

 > [!MATH] TD-Residuals
> $$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

- GAE aggregates these residuals as:

  > [!MATH] GAE
  > $$\hat A_t^{\text{GAE}(\gamma,\lambda)} = \sum_{l=0}^{\infty} (\gamma\lambda)^l \delta_{t+l}$$

- It is widely used in [[202602201254 - actor-critic methods|actor-critic methods]], especially [[202602201241 - proximal policy optimization|PPO]]/[[202602201917 - trust region policy optimization|TRPO]]-style optimization
- Typical practice tunes $\lambda$ <mark style="background: #FF5582A6;">close to 1 for lower bias while retaining variance reduction</mark>
