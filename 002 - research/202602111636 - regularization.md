---
tags:
  - deep_learning
aliases:
  - Regularization
title: regularization
description: ""
bot: false
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- Regularization is a set of methods used to reduce [[202602010049 - overfitting|overfitting]] and improve generalisation
- It constrains [[202602010044 - model|model]] complexity or injects noise so the model learns robust patterns
- Common methods include:
	- [[202602111634 - weight decay|Weight decay]]
	- [[202602111640 - dropout|Dropout]]
	- [[202602111733 - early stopping|Early stopping]]
	- [[202602111731 - data augmentation|Data augmentation]]
- Regularization strength is controlled by [[202602111256 - hyperparameters|hyperparameters]] and must be tuned with validation data
- Too much regularization causes [[202602111639 - underfitting|underfitting]], while too little can cause [[202602010049 - overfitting|overfitting]]
- Effective regularisation depends on [[202602111314 - model parameters|model size]], dataset scale, and [[202602111605 - optimization algorithms|optimization]] setup