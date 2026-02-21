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

- Importance Sampling allows us to calculate the expectation of a function $f(x)$ under distribution $p$ by using samples from distribution $q$

> [!MATH] Importance Sampling
> $$E_{x \sim p}[f(x)] = E_{x \sim q}\left[ f(x) \frac{p(x)}{q(x)} \right]$$
> 
> - $p(x)$ or **Target Distribution**: The distribution we want to learn about (e.g., the optimal policy $\pi$)
> - $q(x)$ or **Proposal Distribution**: The distribution we are actually sampling from (e.g., the behaviour policy $\mu$)
> - $\frac{p(x)}{q(x)}$ or **Importance Weight**: Also called the "Likelihood Ratio", it corrects the bias of sampling from the wrong source
> - $w(x)$ or **Weight**: If $w > 1$, the sample is more likely in the target; if $w < 1$, it is less likely

- Off-Policy Learning
	- Algorithms like [[202602201241 - proximal policy optimization|PPO]] and [[202602201917 - trust region policy optimization|TRPO]] use the ratio $\frac{\pi_{\theta}(a|s)}{\pi_{\theta_{old}}(a|s)}$ to reuse old experience data.
- Variance
	- The estimator is unbiased under support overlap but can have very high [[202602062206 - variance|variance]]
	- If $p(x)$ and $q(x)$ are very different, the weights can become massive, leading to <mark style="background: #FF5582A6;">high variance</mark>
	- This is why PPO "clips" the ratio
- Requirement
	- $q(x)$ must be greater than zero whenever $p(x) > 0$
	- You can't learn about something that your behaviour policy never tries!
- Weighted or truncated variants trade some bias for lower variance and better practical stability
- Importance sampling is central in off-policy evaluation, [[202602200129 - policy gradient methods|policy-gradient]] correction, and logged-bandit learning


[^1]: [Importance Sampling](https://www.youtube.com/watch?v=C3p2wI4RAi8)