---
tags:
  - training
aliases:
  - Rejection Sampling
title: rejection sampling
description: ""
bot: false
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- Rejection [[202602080005 - sampling|sampling]] generates samples from a target [[202602072325 - distribution|distribution]] by filtering proposals from an easier proposal distribution
- Given target density $p(x)$ and proposal $q(x)$ with bound $p(x) \le M q(x)$, sample $x\sim q$ and accept with probability $\frac{p(x)}{M q(x)}$
- Accepted samples follow the target distribution exactly when the bound condition holds
- Efficiency depends on how tight the proposal is to the target; loose bounds cause many rejections
- In ML pipelines, rejection sampling is used for data curation, candidate filtering, and [[202602191644 - post-training|post-training]] sample selection
- In [[202602191524 - large language model|LLMs]], rejection sampling operates by curating new candidate completions, filtering them based on a trained [[202602201334 - reward model|reward model]], and then instruction [[202601282201 - supervised fine-tuning|fine-tuning]] the original [[202602010044 - model|model]] only on the top completions (same loss function as when doing a dedicated training stage for learning to follow instructions)
- It trades compute for higher-quality or distribution-matched accepted samples


[^1]: [Accept-Reject Sampling - Explained](https://www.youtube.com/watch?v=tTxfYh5dC6k)
[^2]: https://rlhfbook.com/c/09-rejection-sampling#:~:text=Rejection%20sampling%20operates%20by%20curating%20new%20candidate%20completions%2C%20filtering%20them%20based%20on%20a%20trained%20reward%20model%2C%20and%20then%20instruction%20fine%2Dtuning%20the%20original%20model%20only%20on%20the%20top%20completions%20(same%20loss%20function%20as%20when%20doing%20a%20dedicated%20training%20stage%20for%20learning%20to%20follow%20instructions).