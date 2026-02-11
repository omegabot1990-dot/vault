---
tags:
- note
aliases:
- Unsupervised Learning
title: unsupervised learning
description: ''
bot: true
parent nodes:
- '[[training]]'
published on: null
---

- Unsupervised learning [[202602111335 - training|trains]] [[202602010044 - model|models]] on unlabelled data to discover <mark style="background: #FF5582A6;">latent structure</mark> or <mark style="background: #BBFABBA6;">useful representations</mark>
- The objective is not direct label prediction but
	- Pattern discovery
	- Compression
	- Density estimation
	- Generation
- Common task families include clustering, dimensionality reduction, representation learning, and generative modeling
- Typical methods include k-means, PCA, autoencoders, contrastive/self-supervised objectives, and diffusion-based models
- Evaluation is often indirect, using reconstruction quality, likelihood proxies, clustering metrics, or downstream transfer performance
- Unsupervised learning is important when labeled data is scarce but raw data is abundant