---
tags:
- note
aliases:
- Importance Sampling
title: importance sampling
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Importance sampling reweights trajectory terms to estimate expectations under a target policy using data from a different behavior policy
- In off-policy RL, it corrects distribution mismatch via probability ratios between target and behavior policies
- A common per-step ratio is $\rho_t = \frac{\pi(a_t\mid s_t)}{\mu(a_t\mid s_t)}$, with cumulative products used over horizons
- The estimator is unbiased under support overlap but can have very high variance
- Weighted or truncated variants trade some bias for lower variance and better practical stability
- Importance sampling is central in off-policy evaluation, policy-gradient correction, and logged-bandit learning