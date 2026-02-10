---
tags:
  - academic
description:
due date:
start date:
end date:
status: Archive
importance level:
urgency level:
task type:
story points:
parent nodes:
child nodes:
recurrent:
---

- Apply and integrate key recommendation algorithms, including collaborative filtering, sequential models, graph-based approaches, neural networks, and hybrid methods.
- Practice end-to-end model development: preprocessing, modelling, training, inference, and evaluation.
- Analyse trade-offs, identify model weaknesses, and communicate results.

## Notes

- Data has implicit feedback, which means we only have positive interactions, so we will use negative sampling.
	- Randomly choosing items the user didn’t interact with to act as "negative" examples.
- We have timestamp data, which we can use for sequential models, such as BERT4Rec.
	- Split data chronologically into train/val/test.
	- Sort the user history to model recent interests. 

|Use Case|Field(s) Used|Purpose|
|---|---|---|
|Text-based hybrid models|`title`, `description`|Embed textual info using TF-IDF or transformers|
|Content-based recommenders|`main_category`, `features`|Build item profiles and recommend similar items|
|Popularity signals|`rating_number`, `price`|Add bias toward high-quality/popular items|
|Graph-based recommenders|`bought_together`|Build co-purchase graphs (LightGCN, Node2Vec, etc.)|
