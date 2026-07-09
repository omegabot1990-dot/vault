---
tags:
  - information_retrieval
aliases:
  - Inverted Index
title: inverted index
description: ""
bot: false
parent nodes:
  - "[[202605011609 - information retrieval|information retrieval]]"
published on:
---

- An inverted index is a data structure that maps each term in a vocabulary to the list of documents containing that term [^1]
	- "Inverted" because it is the <mark style="background: #BBFABBA6;">opposite of a forward index</mark> (which maps doc → terms it contains)
	- It is the <mark style="background: #FF5582A6;">core data structure of every classical </mark> [[202605011609 - information retrieval|IR]] system — Lucene, Elasticsearch, OpenSearch, every [[202605011627 - bm25|BM25]] implementation
- Two parts
	- Dictionary (vocabulary)
		- The set of all unique terms in the corpus
		- Often stored as a hash map or B-tree, with each entry pointing at the term's postings list
	- Postings list
		- For each term, the list of `(docID, ...)` entries for every document containing it
		- Sorted by `docID` so that set operations (AND/OR) can be done by linear merge
- Postings entry variants
	- Term-only: just `docID` — enough for boolean queries
	- Frequency: `(docID, tf)` — needed for [[202605011625 - tf-idf|TF-IDF]] / [[202605011627 - bm25|BM25]] scoring
	- Positional: `(docID, [pos1, pos2, ...])` — needed for phrase queries and proximity search
- Construction (offline)
	1. For each document, tokenize and normalize (lowercase, stem, drop stopwords)
	2. Emit `(term, docID, [tf | positions])` tuples
	3. Sort by `(term, docID)` — usually external merge sort for large corpora
	4. Group consecutive tuples by term → each group is one postings list

> [!example] Tiny example
>
> Docs: `d1: "the cat sat"`, `d2: "the dog sat"`, `d3: "cat and dog"`
>
> Inverted index:
> - `cat → [d1, d3]`
> - `dog → [d2, d3]`
> - `sat → [d1, d2]`
> - `the → [d1, d2]`
> - `and → [d3]`

- Query processing
	- Boolean `A AND B` → intersect postings(A) and postings(B) by linear merge
	- Boolean `A OR B` → union postings(A) and postings(B)
	- Phrase `"A B"` → positional intersect: keep only docs where A's position + 1 = B's position
- Compression
	- Postings lists are long and sorted — compress aggressively
	- <mark style="background: #BBFABBA6;">Delta (gap) encoding</mark>: store differences between consecutive `docID`s instead of the raw IDs
	- Variable-byte / gamma / Elias coding to pack small gaps into a few bytes
	- Block-based compression (PForDelta, Roaring bitmaps) for very large indexes
- Optimizations
	- Skip pointers — let intersection skip ahead in long postings lists, $O(\sqrt{n})$ per skip
	- Champion lists / tiered indexes — keep only the highest-scoring docs per term for fast top-k
	- Impact-ordered postings — sort postings by score, not docID, for early termination during ranked retrieval
- Modern context
	- Inverted indexes power <mark style="background: #FF5582A6;">all sparse retrievers</mark> ([[202605011627 - bm25|BM25]], SPLADE) and the <mark style="background: #FFB86CA6;">sparse half of hybrid retrieval</mark>
	- Even neural retrievers often keep an inverted index alongside dense embeddings — sparse and dense scores are then fused at query time
	- TODO: cite — survey of learned sparse retrievers (e.g. SPLADE)
- See also
	- [[202605011609 - information retrieval|information retrieval]]
	- [[embeddings|embeddings]] — for the dense counterpart


[^1]: https://nlp.stanford.edu/IR-book/html/htmledition/a-first-take-at-building-an-inverted-index-1.html
