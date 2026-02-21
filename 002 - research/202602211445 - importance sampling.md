---
tags:
  - reinforcement_learning
aliases:
  - Importance Sampling
title: importance sampling
description: ""
bot: false
parent nodes:
  - "[[202602200129 - policy gradient methods|Policy Gradient Methods]]"
published on:
---

- [ ] What is logged-bandit learning?

---
- Importance sampling re-weights trajectory terms to estimate [[202602061333 - expectation|expectations]] under a target [[202602192245 - policy|policy]] using data from a different behaviour policy
- In [[202602201246 - off-policy|off-policy]] [[202602192221 - reinforcement learning|RL]], it corrects the [[202602072325 - distribution|distribution]] mismatch via [[202602062040 - probability|probability]] ratios between the target and behaviour policies
- A common per-step ratio is as follows, with cumulative products used over horizons

> [!MATH] Ratio
> $$\rho_t = \frac{\pi(a_t\mid s_t)}{\mu(a_t\mid s_t)}$$

- The estimator is unbiased under support overlap but can have very high [[202602062206 - variance|variance]]
- Weighted or truncated variants trade some bias for lower variance and better practical stability
- Importance sampling is central in off-policy evaluation, [[202602200129 - policy gradient methods|policy-gradient]] correction, and logged-bandit learning