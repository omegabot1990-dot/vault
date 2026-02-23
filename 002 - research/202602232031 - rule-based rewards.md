---
tags:
  - reinforcement_learning
aliases:
  - Rule-Based Rewards
title: rule-based rewards
description: ""
bot: false
parent nodes:
  - "[[202602192352 - reward|Reward]]"
published on:
---

- Rule-based rewards assign scores using <mark style="background: #BBFABBA6;">explicit programmatic rules</mark> instead of learned [[202602201334 - reward model|reward models]]
- They encode domain constraints such as format validity, test pass rate, safety checks, or exact-match correctness
- In [[202602192221 - reinforcement learning|RL]] pipelines, they provide transparent and reproducible reward signals that are easy to audit
- Rule-based rewards work best when the target behaviour can be clearly specified with deterministic checks
- <mark style="background: #FFB86CA6;">Overly narrow rules can be gamed, leading to reward hacking and brittle optimization</mark>
- Practical systems combine rule-based rewards with <mark style="background: #FFF3A3A6;">robustness checks</mark>, <mark style="background: #FF5582A6;">curriculum shaping</mark>, and <mark style="background: #ABF7F7A6;">periodic rule updates</mark>
