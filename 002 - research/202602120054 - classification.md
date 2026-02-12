---
tags:
  - deep_learning
  - training
aliases:
  - Classification
title: classification
description: ""
bot: true
parent nodes:
  - "[[202602112328 - supervised learning|Supervised Learning]]"
published on:
---

- [ ] What is ROC-AUC?

---
- Classification is a [[202602112328 - supervised learning|supervised learning]] task where inputs are mapped to discrete class labels
- The model outputs class scores or [[202602062040 - probability|probabilities]], and the prediction selects the most likely class
- Common settings are
	- Binary classification
	- Multi-class classification
	- Multi-label classification
- Typical training uses cross-entropy-based losses with [[202602111510 - sigmoid|sigmoid]] or [[202602111530 - softmax|softmax]] output layers
- Performance is evaluated with metrics such as the below depending on class balance and task goals
	- [[202602011507 - accuracy|Accuracy]]
	- [[202602011511 - precision|Precision]]
	- [[202602011513 - recall|Recall]]
	- [[202602011551 - f1|F1 score]]
	- ROC-AUC
- Good classification performance depends on data quality, calibration, [[202602111636 - regularization|regularization]], and decision-threshold selection