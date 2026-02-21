---
tags:
  - reinforcement_learning
aliases:
  - Temporal-Difference Algorithm
  - TD learning
  - TD Error
  - TD Residual
title: temporal-difference algorithm
description: ""
bot: false
parent nodes:
  - "[[202602201335 - bootstrapping|Bootstrapping]]"
published on:
---

- [ ] What is TD(0)?
- [ ] What is SARSA?

---
- Temporal-difference algorithms learn [[202602200020 - value|value]] estimates by [[202602201335 - bootstrapping|bootstrapping]] from other learned estimates
- They update from incomplete [[202602192356 - episode|episodes]] using one-step prediction errors, improving [[202602010053 - on-line learning|online learning]] efficiency
- The TD error or TD residual is commonly written as:

>[!MATH] TD-Error or TD-Residual
>$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$
>
> - $\delta_t$ or **TD Error**: The "Surprise" or prediction error at time $t$
> - $r_{t+1}$ or **Immediate Reward**: The actual reward observed after transitioning from $s_t$ 
> - $\gamma$ or **Discount Factor**: The weight given to future rewards (0 to 1) 
> - $V(s_{t+1})$ or **Next State Value**: The agent's current estimate of how good the *next* state is
> - $V(s_t)$ or **Current State Value**: The agent's current estimate of how good the *current* state is

- TD(0), SARSA, and [[202602201303 - q-learning|Q-learning]] are core temporal-difference methods
- TD methods usually trade lower [[202602062206 - variance|variance]] for some bias compared with pure [[202602201958 - monte carlo|Monte Carlo]] estimation
- They are foundational for modern [[202602201255 - value-based methods|value-based]] and [[202602201254 - actor-critic methods|actor-critic]] reinforcement learning algorithms
