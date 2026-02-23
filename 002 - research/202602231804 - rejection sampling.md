---
tags:
- note
aliases:
- Rejection Sampling
title: rejection sampling
description: ''
bot: true
parent nodes:
- '[[neural networks]]'
published on: null
---

- Rejection sampling generates samples from a target distribution by filtering proposals from an easier proposal distribution
- Given target density $p(x)$ and proposal $q(x)$ with bound $p(x) \le M q(x)$, sample $x\sim q$ and accept with probability $\frac{p(x)}{M q(x)}$
- Accepted samples follow the target distribution exactly when the bound condition holds
- Efficiency depends on how tight the proposal is to the target; loose bounds cause many rejections
- In ML pipelines, rejection sampling is used for data curation, candidate filtering, and post-training sample selection
- It trades compute for higher-quality or distribution-matched accepted samples