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

`cross-encoder-cross-encoder-ms-marco-MiniLM-L-2-v2-2025-05-21_18-04-42`

```
STEPS: 54999/156250

Queries: 43 
NDCG@10: 66.01 
Recall@100: 49.13 
MAP@1000: 42.51

156493 Q0 1960260 0 4.175086498260498 STANDARD 
156493 Q0 1960255 1 3.920583486557007 STANDARD 
156493 Q0 1960257 2 3.7190210819244385 STANDARD
```

`cross-encoder-cross-encoder-ms-marco-TinyBERT-L-2-v2-2025-05-22_01-13-29`

```
STEPS: 76627/156250

Queries: 43 
NDCG@10: 69.58 
Recall@100: 50.74 
MAP@1000: 45.63

156493 Q0 8182159 0 6.3131422996521 STANDARD 
156493 Q0 3288597 1 5.847297668457031 STANDARD 
156493 Q0 1960255 2 5.44837760925293 STANDARD
```

`cross-encoder-distilroberta-base-2025-05-22_19-52-49`

```
STEPS: 10999/156250

Queries: 43 
NDCG@10: 62.94 
Recall@100: 47.20 
MAP@1000: 39.56

156493 Q0 3288600 0 0.9552138447761536 STANDARD 
156493 Q0 3288601 1 0.9547345638275146 STANDARD 
156493 Q0 8182162 2 0.9545813798904419 STANDARD
```

## Fusion Algorithms

```
=== Results for MAX ===
ndcg@10: 0.6516
recall@100: 0.5020
map@1000: 0.4288

=== Results for MIN ===
ndcg@10: 0.6854
recall@100: 0.4740
map@1000: 0.4130

=== Results for ISR ===
ndcg@10: 0.6740
recall@100: 0.5050
map@1000: 0.4392

=== Results for LOG_ISR ===
ndcg@10: 0.6740
recall@100: 0.5050
map@1000: 0.4392

=== Results for MED ===
ndcg@10: 0.6922
recall@100: 0.5036
map@1000: 0.4515
```

## Combination

```
=== MED Fusion: MINILM + TINYBERT ===
ndcg@10: 0.6993
recall@100: 0.5058
map@1000: 0.4548

=== MED Fusion: MINILM + DISTILROBERTA ===
ndcg@10: 0.6749
recall@100: 0.4986
map@1000: 0.4320

=== MED Fusion: TINYBERT + DISTILROBERTA ===
ndcg@10: 0.6782
recall@100: 0.5046
map@1000: 0.4426
```

