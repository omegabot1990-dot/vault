---
tags:
- note
aliases:
- Rule-Based Rewards
title: rule-based rewards
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Rule-based rewards assign scores using explicit programmatic rules instead of learned reward models
- They encode domain constraints such as format validity, test pass rate, safety checks, or exact-match correctness
- In RL pipelines, they provide transparent and reproducible reward signals that are easy to audit
- Rule-based rewards work best when target behavior can be clearly specified with deterministic checks
- Overly narrow rules can be gamed, leading to reward hacking and brittle optimization
- Practical systems combine rule-based rewards with robustness checks, curriculum shaping, and periodic rule updates