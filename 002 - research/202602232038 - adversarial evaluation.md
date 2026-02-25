---
tags:
  - evaluation
aliases:
  - Adversarial Evaluation
title: adversarial evaluation
description: ""
bot: false
parent nodes:
  - "[[202602120132 - evaluation|Evaluation]]"
published on:
---

- [ ] What are red-team prompts?
- [ ] What are adversarial perturbations?
- [ ] What are counterexamples?
- [ ] What are worst-case scenario suites?

---
- Adversarial evaluation stress-tests a [[202602010044 - model|model]] with targeted hard cases designed to expose failure modes
- In [[202602192221 - reinforcement learning|RL]] systems, it probes robustness to reward hacking, [[202602072325 - distribution|distribution]] shift, and unsafe [[202602192245 - policy|policy]] behaviours
- Evaluations can use,
	- Red-team prompts
	- Adversarial perturbations
	- Counterexamples
	- Worst-case scenario suites
- <mark style="background: #BBFABBA6;">The goal is to measure reliability under pressure, not just average benchmark performance</mark>
- Results guide reward redesign, policy constraints, and safer [[202602111335 - training|training]] objectives
- Continuous adversarial evaluation is important because models adapt, and new exploit strategies emerge over time