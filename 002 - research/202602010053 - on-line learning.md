---
tags:
  - training
aliases:
  - On-line learning
title: on-line learning
description: ""
parent nodes:
  - "[[202602111335 - training|Training]]"
published on:
---

- Online Learning (also called incremental learning) is a paradigm where a [[202602010044 - model|model]] learns continuously from a stream of data as it arrives, rather than being [[202602111335 - training|Training]] once on a static dataset

| Feature        | Online Learning                                 | Offline (Batch) Learning                         |
| :------------- | :---------------------------------------------- | :----------------------------------------------- |
| **Data Usage** | Sequential stream, processes data as it arrives | Static dataset, trained on all data at once      |
| **Updating**   | Continuous, real-time updates                   | Requires full retraining to incorporate new data |
| **Storage**    | Low, data can often be discarded after use      | High, must store the entire training dataset     |
| **Best For**   | Dynamic trends (e.g., social media, finance)    | Stable patterns (e.g., image classification)     |
