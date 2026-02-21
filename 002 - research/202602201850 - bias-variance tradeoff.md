---
tags:
  - deep_learning
aliases:
  - Bias-Variance Tradeoff
title: bias-variance tradeoff
description: ""
bot: false
parent nodes:
  - "[[202602061153 - neural network|Neural Network]]"
published on:
---

- [ ] What is ensembling?

---
- <mark style="background: #BBFABBA6;">Bias measures how far off, on average, a model’s predictions are from the ground truth values</mark> [^3]
- <mark style="background: #FF5582A6;">Variance measures how much a model’s predictions change with different training datasets</mark> [^4]
- The bias-[[202602062206 - variance|variance]] tradeoff describes how [[202602010044 - model|model]] error decomposes into [[202602111639 - underfitting|underfitting]] bias and [[202602010049 - overfitting|overfitting]] variance
- High-bias models are too rigid and miss the underlying structure, while high-variance models overreact to sample noise

![|700](https://assets.ibm.com/is/image/ibm/bias-variance-diagram:1x1?fmt=png-alpha&dpr=on%2C2&wid=1536&hei=1536)

- The total [[202602061333 - expectation|expected]] error of a [[202602112328 - supervised learning|supervised learning]] algorithm can be broken down as:

> [!MATH] Bias-Variance Tradeoff
> $$\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}$$
> 
> | Component | Name | Description |
> | :--- | :--- | :--- |
> | **Bias** | **Underfitting** | Error from erroneous assumptions, the model is too simple to "see" the patterns (e.g., using a straight line for a curve) |
> | **Variance** | **Overfitting** | Error from sensitivity to small fluctuations, the model "memorises" the noise in the training data |
> | **Irreducible Error** | **Noise** | The "noise" ($\epsilon$) inherent in the data itself that no model can ever remove |

- Increasing [[202602111314 - model parameters|model capacity]] often lowers bias but can raise variance unless [[202602111636 - regularization|regularized]]
- Good generalisation balances representational power with inductive constraints and sufficient data
- [[202602111636 - regularization|Regularization]], [[202602111731 - data augmentation|data augmentation]], [[202602111733 - early stopping|early stopping]], and ensembling help reduce variance
- In practice, validation performance guides the operating point on the bias-variance spectrum


[^1]: https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/statistics.html#the-bias-variance-trade-off:~:text=The%20mean%20squared%20error%20can%20be%20divided%20into%20three%20sources%20of%20error%3A%20the%20error%20from%20high%20bias%2C%20the%20error%20from%20high%20variance%20and%20the%20irreducible%20error.
[^2]: [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA)
[^3]: https://www.ibm.com/think/topics/bias-variance-tradeoff#:~:text=Bias%20measures%20how%20far%20off%2C%20on%20average%2C%20a%20model%E2%80%99s%20predictions%20are%20from%20the%20ground%20truth%20values.
[^4]: https://www.ibm.com/think/topics/bias-variance-tradeoff#:~:text=Variance%20measures%20how%20much%20a%20model%E2%80%99s%20predictions%20change%20with%20different%20training%20datasets.