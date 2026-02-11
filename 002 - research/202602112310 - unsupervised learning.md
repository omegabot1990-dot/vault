---
tags:
  - deep_learning
  - training
aliases:
  - Unsupervised Learning
title: unsupervised learning
description: ""
bot: false
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- [ ] What is clustering?
- [ ] What is dimensionality reduction?
- [ ] What is representation learning?
- [ ] What is generative modelling?
- [ ] What is k-means?
- [ ] What is PCA?
- [ ] What are autoencoders?
- [ ] What is contrastive learning?
- [ ] What are diffusion-based models?

---
- Unsupervised learning [[202602111335 - training|trains]] [[202602010044 - model|models]] on unlabelled data to discover <mark style="background: #FF5582A6;">latent structure</mark> or <mark style="background: #BBFABBA6;">useful representations</mark>
- The objective is not direct label prediction, but:
	- Pattern discovery
	- Compression
	- Density estimation
	- Generation
- Common task families include, 
	- Clustering
	- Dimensionality reduction
	- Representation learning
	- Generative modelling
- Typical methods include
	- k-means
	- PCA
	- Autoencoders
	- Contrastive/[[202602050153 - self-supervised learning|self-supervised]] objectives
	- Diffusion-based models
- Evaluation is often indirect, using reconstruction quality, [[202602061241 - likelihood|likelihood]] proxies, clustering metrics, or downstream transfer performance
- Unsupervised learning is important when labelled data is scarce, but raw data is abundant