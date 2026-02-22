---
tags:
  - deep_learning
aliases:
  - Hyperparameters
title: hyperparameters
description: ""
bot: false
parent nodes:
  - "[[202602061150 - deep learning|Deep Learning]]"
  - "[[202602111335 - training|Training]]"
published on:
---

- [ ] What are search strategies?
- [ ] What is grid search?
- [ ] What is random search?
- [ ] What is Bayesian optimisation?
- [x] [[202602220121 - cosine decay|Cosine Decay]]

---
- Hyperparameters are <mark style="background: #BBFABBA6;">top-level configuration values</mark> set before [[202602111335 - training|training]] that control model structure or learning behaviour [^1][^2]
- They are <mark style="background: #FF5582A6;">not learned directly from gradient updates</mark>, unlike [[202602111314 - model parameters|model parameters]] [^3]
- Typical examples are: [^4]
	- [[202602111600 - learning rate|learning rate]]
	- [[202602111605 - optimization algorithms|optimization algorithm]]
	- [[202602111400 - activation|activation function]]
	- [[202602010047 - objective function|loss or cost function]]
	- [[202602111625 - batch size|batch size]]
	- [[202602111623 - epochs|epochs]]
	- [[202602111634 - weight decay|weight decay]]
	- [[202602111640 - dropout|dropout rate]]
	- number of layers
	- hidden dimension
- Good hyperparameter choices improve <mark style="background: #ADCCFFA6;">convergence speed, stability, and generalisation</mark>
- Common search strategies are,
	- Grid search
	- Random search
	- Bayesian optimisation
- <mark style="background: #FFF3A3A6;">Validation performance is the main signal used to compare hyperparameter settings</mark>


[^1]: https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac/#:~:text=Hyperparameters%20are%20parameters%20whose%20values%20control%20the%20learning%20process%20and%20determine%20the%20values%20of%20model%20parameters%20that%20a%20learning%20algorithm%20ends%20up%20learning
[^2]: https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac/#:~:text=%E2%80%98top%2Dlevel%E2%80%99%20parameters%20that%20control%20the%20learning%20process%20and%20the%20model%20parameters%20that%20result%20from%20it
[^3]: https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac/#:~:text=In%20this%20light%2C%20hyperparameters%20are%20said%20to%20be%20external%20to%20the%20model%20because%20the%20model%20cannot%20change%20its%20values%20during%20learning/training.
[^4]: https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac/#:~:text=Here%20are%20some%20common%20examples