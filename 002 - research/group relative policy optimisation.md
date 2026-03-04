---
tags:
- moc
description: ''
parent nodes:
- '[[policy gradient methods]]'
---

## Topics

- [ ] KL-divergence penalty for regularisation and against reward hacking

- [ ] Final reward works as the advantage signal $A_{t}$

## Blogs

- [ ] [GRPO++: Tricks for Making RL Actually Work](https://cameronrwolfe.substack.com/p/grpo-tricks)

## Papers

- [ ] [Self-Hinting Language Models Enhance Reinforcement Learning](https://www.alphaxiv.org/abs/2602.03143)
	- [ ] SAGE (Self-hint Aligned GRPO with Privileged Supervision) is an on-policy reinforcement learning framework that injects self-generated privileged hints during training to increase rollout diversity and prevent advantage collapse under sparse rewards, while deploying as a standard no-hint policy at test time
	- [ ] <mark style="background: #FFB86CA6;">IMPORTANT</mark>

- [ ] [F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare](https://www.alphaxiv.org/abs/2602.06717)
	- [ ] **F-GRPO** scales group-relative advantages by a Focal-loss-inspired difficulty weight $g(x) = (1 - \hat{\mu}_{pos}(x))^{\gamma}$ to down-weight updates on high-success prompts and prevent the policy from concentrating on common solutions while forgetting rare ones
	- [ ] <mark style="background: #FFB86CA6;">IMPORTANT</mark>

- [ ] [GRP-Obliteration: Unaligning LLMs With a Single Unlabeled Prompt](https://www.alphaxiv.org/abs/2602.06258)
	- [ ] GRP-Obliteration (GRP-Oblit) uses Group Relative Policy Optimization (GRPO) with a judge-based reward to invert safety constraints through adversarial fine-tuning, requiring as little as a single unlabeled prompt to achieve broad unalignment



## Videos

- [ ] [YouTube - DeepSeek's GRPO (Group Relative Policy Optimization) | Reinforcement Learning for LLMs](https://www.youtube.com/watch?v=xT4jxQUl0X8&t=1031s)

## Code
