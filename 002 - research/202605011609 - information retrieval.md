---
tags:
  - root
  - information_retrieval
aliases:
  - IR
title: information retrieval
description: ""
bot: false
parent nodes:
  - "[[research.base]]"
published on:
---

- Information retrieval (IR) is the discipline of finding material — usually documents of an unstructured nature — that satisfies an information need from within large collections [^1]
	- The collection is typically <mark style="background: #BBFABBA6;">heterogeneous, large, and growing</mark> (the web, a paper corpus, a personal vault)
	- The query is short, ambiguous, and the user wants the *most relevant* items, not all matching items
- Core problem
	- <mark style="background: #FF5582A6;">Ranking by relevance</mark> — not "match yes/no" but "order all candidates by how well each satisfies the query"
- Pipeline (classical view)
	1. Indexing
		- Tokenize → normalize (lowercase, stem/lemmatize) → build an [[202605011617 - inverted index|inverted index]]
		- Inverted index = for each term, the postings list of documents containing it
	2. Query processing
		- Parse, normalize, and optionally expand (synonyms, stemming) the query
	3. Scoring & ranking
		- Compute a score per candidate doc, sort, and return top-k
	4. Evaluation
		- Compare ranked results against ground-truth relevance judgements
- Classical scoring methods
	- Boolean retrieval — exact AND/OR/NOT match, no ranking
	- [[202605011625 - tf-idf|TF-IDF]] — weight each (term, doc) pair by term frequency × inverse document frequency, rank by cosine similarity to the query vector
	- [[202605011627 - bm25|BM25]] — a probabilistic refinement of [[202605011625 - tf-idf|TF-IDF]] with term-frequency saturation and length normalization; the <mark style="background: #FF5582A6;">strong classical baseline</mark> that's still widely used in modern systems
- Neural / dense retrieval
	- Encode queries and documents into the same [[embeddings|embedding]] space; retrieve by nearest-neighbour search
	- Bi-encoder
		- Query and doc encoded independently
		- Fast at retrieval time, scales to millions of docs
	- Cross-encoder
		- Query and doc encoded jointly — more accurate, but $O(N)$ per query
		- Used as a *re-ranker* on the top-k from a bi-encoder
	- Approximate nearest-neighbour libraries (FAISS, HNSW, ScaNN) make dense retrieval tractable at scale
- Hybrid retrieval
	- Combine sparse ([[202605011627 - bm25|BM25]]) and dense scores; typically <mark style="background: #BBFABBA6;">stronger than either alone</mark>
	- TODO: cite — recent hybrid retrieval comparison paper
- Evaluation metrics
	- Precision@k — fraction of top-k that are relevant
	- Recall@k — fraction of all relevant docs that appear in top-k
	- MRR (Mean Reciprocal Rank) — mean of $1/\text{rank}$ of the first relevant result
	- nDCG — discounts gains by rank position; the standard metric when relevance is graded (not just binary)
- Connection to LLMs
	- [[retrieval augmented generation|RAG]] uses an IR system as the "retriever" stage to ground generation in fetched context
	- Generation quality is upper-bounded by retrieval quality — hence the <mark style="background: #FFB86CA6;">recent push toward learned dense retrievers and hybrid pipelines</mark>
- Open questions / for later
	- <mark style="background: #FFB86CA6;">How to measure retrieval quality for LLM grounding specifically</mark> — classical IR metrics are query↔document, not query↔answer
	- <mark style="background: #FFB86CA6;">Long-context LLMs vs. RAG</mark> — when does retrieval still pay off vs. just stuffing the prompt?


[^1]: https://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html
