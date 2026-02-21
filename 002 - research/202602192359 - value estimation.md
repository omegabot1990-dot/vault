---
tags:
  - reinforcement_learning
aliases:
  - Value Estimation
title: value estimation
description: ""
bot: false
parent nodes:
  - "[[202602200020 - value|Value]]"
published on:
---

- Value estimation learns [[202602061333 - expectation|expected]] [[202602192355 - return|return]] quantities used to evaluate decisions
- Common targets are the [[202602192351 - state|state]]-[[202602200020 - value|value]] $V^\pi(s)$ and [[202602192350 - action|action]]-value $Q^\pi(s,a)$ functions
- The value of a state $s$ under a policy $\pi$ is the [[202602061333 - expectation|expected]] [[202602192355 - return|return]] when starting in $s$ and following $\pi$ thereafter:
	- We can decompose the value into the immediate [[202602192352 - reward|reward]] plus the discounted value of the next state:

> [!MATH] The [[202602211420 - bellman equation|Bellman Equation]] for $V(s)$
> $$V^\pi(s) = \sum_{a} \pi(a|s) \sum_{s', r} p(s', r | s, a) \left[ r + \gamma V^\pi(s') \right]$$
> 
> - $V(s)$ or **State-Value**: The "score" or desirability of being in state $s$
> - $G_t$ or **Return**: The sum of all future discounted rewards
> - $\gamma$ or **Discount Factor**: Determines how much we care about future vs. immediate rewards
> - $\pi(a|s)$ or **Policy**: The probability of taking action $a$ in state $s$

- The value of taking action $a$ in state $s$ under policy $\pi$ is the expected return starting from that state-action pair:
	- We can decompose the action-value into the immediate reward plus the discounted value of the next state's actions:

> [!MATH] The Bellman Equation for $Q(s, a)$
> 
> $$Q^\pi(s, a) = \sum_{s', r} p(s', r | s, a) \left[ r + \gamma \sum_{a'} \pi(a'|s') Q^\pi(s', a') \right]$$
> 
> - $Q(s, a)$ or **Quality (Q)**: The "desirability" of taking action $a$ in state $s$
> - $s, a, r$ or **State, Action, Reward**: The current state, the chosen move, and the resulting payoff
> - $\gamma$ or **Discount Factor**: Weights the importance of future rewards
> - $\pi(a'|s')$ or **Next Action Prob.**: The probability of taking action $a'$ in the next state $s'$

- Estimates can be obtained by [[202602201958 - monte carlo|Monte Carlo]] returns, [[202602201305 - temporal-difference algorithm|temporal-difference]] [[202602201335 - bootstrapping|bootstrapping]], or [[202602211440 - dynamic programming|dynamic programming]]
- Value estimation reduces long-horizon planning to local updates based on Bellman relations
- Accurate value estimates improve [[202602192245 - policy|policy]] improvement and action selection
- Approximation error, [[202602062206 - variance|variance]], and [[202602072325 - distribution|distribution]] shift can destabilise value learning


[^1]: [Bellman Equations, Dynamic Programming, Generalized Policy Iteration | Reinforcement Learning Part 2](https://www.youtube.com/watch?v=_j6pvGEchWU&list=PLzvYlJMoZ02Dxtwe-MmH4nOB5jYlMGBjr&index=2)