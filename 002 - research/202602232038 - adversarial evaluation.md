---
tags:
- note
aliases:
- Adversarial Evaluation
title: adversarial evaluation
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Adversarial evaluation stress-tests a model with targeted hard cases designed to expose failure modes
- In RL systems, it probes robustness to reward hacking, distribution shift, and unsafe policy behaviors
- Evaluations can use red-team prompts, adversarial perturbations, counterexamples, and worst-case scenario suites
- The goal is to measure reliability under pressure, not just average benchmark performance
- Results guide reward redesign, policy constraints, and safer training objectives
- Continuous adversarial evaluation is important because models adapt and new exploit strategies emerge over time