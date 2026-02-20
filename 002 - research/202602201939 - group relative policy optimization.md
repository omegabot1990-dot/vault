---
tags:
- note
aliases:
- Group Relative Policy Optimization
- GRPO
title: group relative policy optimization
description: ''
bot: true
parent nodes:
- '[[reinforcement learning]]'
published on: null
---

- Group Relative Policy Optimization (GRPO) is a policy optimization method that normalizes rewards within sampled output groups
- Instead of relying on a separate value critic, it computes relative advantages from group-level statistics
- This reduces dependence on explicit value-function fitting while preserving policy-gradient style updates
- GRPO is commonly discussed in LLM post-training where multiple candidate responses are scored per prompt
- Relative normalization can improve stability when absolute reward scales vary across prompts
- As with PPO-like methods, clipping or trust-style constraints are often used to limit destructive policy updates