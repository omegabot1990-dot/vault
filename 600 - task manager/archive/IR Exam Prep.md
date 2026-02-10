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

## Model Exam 1

- What is Boolean Retrieval?
	- Advantages and Disadvantages
- What is a Power Law?
- What is Zipf's Law?
- Encoding
	- `docid posting list`
	- variable byte encoding of the gaps
- What is Precision@10?
	- Assumptions
- What is AP@10?
	- How does it incorporate Recall?
- What is Recall@10?
- What is nDCG@10?
- What metric is most important for first-stage retrieval?
- What are vector space term weighing schemes?
- What is Jaccard?
	- Weaknesses?
- What is Euclidean distance when it comes to ranking?
	- Explain the disadvantages with an example
- What is parsimony w.r.t model evaluation?
	- Advantages
- What are Embeddings Vector Spaces?
- What are Term Vector Spaces?
- What is MonoBERT?
- What is Pointwise Learning approach?
- What is bi-encoder architecture?
- What is cross-encoder architecture?
- What is nearest neighbour search?
- Explain Fine Tuning and Relevance Relation between words?
- Why do we have to do truncation with BERT?
	- Why does it work for scientific papers and not law texts?
- What are the alternatives in dealing with long texts?
	- Split text into shorter passages?
- What is the concept of "late interaction" in ColBERT?
- Explain the concepts and formulas for simple generative language models for ranking?
	- What part of the formulae is "memory"?
- Constraints made for memory in the ranking formulae for query likelihood?
- Explain the relevance model of Lavrenko and Croft?
- What is position bias and how can it be estimated in live online search engine?
- What is search result diversification?
	- Give an example query where it is needed?
- What is maximal marginal relevance?
	- Why does it provide implicit diversification?
- What is PageRank?
- What is the dependent click model?
	- What are the assumptions?
	- Give the equations that pertain to this?
- What is `Doc2Query`?
	- Who ar Nogueira and Lin?
- What is the T5 model?
	- What kinda data is it trained on for `Doc2Query`?
- Why is `Doc2Query` 50x faster than MonoBERT?

#### Topics

1. Boolean | Indexing | Compression
2. Evaluation
3. Vector Space Modelling and Ranking
4. Transformers for Ranking
5. Simple Generative Language Models for Ranking
6. Web Search
7. User Interaction

---

## Model Exam 1 Concepts
### 1. What is Boolean Retrieval?

Prerequisite: 
Before search engines used machine learning, they employed a much simpler approach — Boolean logic (AND, OR, NOT).

Explanation:
Boolean Retrieval is a classic model for information retrieval. It assumes each document either matches a query or doesn’t. Queries are Boolean expressions, like:
- apple AND banana — finds documents with both words.
- apple OR banana — finds documents with either word.
- apple AND NOT banana — finds documents with “apple” but not “banana”.

Advantages:
- Simple and interpretable.
- Very fast (especially on small datasets).

Disadvantages:
- No ranking: All matching documents are treated equally.
- Rigid: Requires exact matches, no tolerance for synonyms, partial relevance, etc.

---

### 2. What is a Power Law?

Explanation:
A power law describes a relationship where a small number of events are very common, and a large number of events are rare. Mathematically:

$P(x) \propto x^{-\alpha}$

In IR, it appears in document length distributions or the frequency of terms.

---

### 3. What is Zipf’s Law?

Prerequisite: Term frequency distributions in natural language.

Explanation:
Zipf’s Law is a specific power law: the frequency of a word is inversely proportional to its rank in the frequency table. So, the most common word appears twice as much as the second most common, three times as much as the third, and so on.

 $f \propto \frac{1}{r}$

Where:
- f = frequency of the word
- r = rank of the word

---

### 4. Encoding: docid posting list

Explanation:
This is used in inverted indexes. For each term, you store a posting list — a list of docids where the term appears.  

Example:

```
term: "apple"
posting list: [2, 4, 5, 12]
```

---

### 5. Variable Byte Encoding of the Gaps

Prerequisite: 
Posting lists can be compressed by storing the difference between doc IDs.

Explanation:
Instead of storing [2, 4, 5, 12], you store [2, 2, 1, 7] (gaps). These are then encoded using Variable Byte Encoding (VBE), a compression scheme where smaller numbers use fewer bytes.

---

### 6. What is Precision@10?

Explanation:
Precision@10 = Number of relevant documents in top 10 results ÷ 10.

Assumptions:
- You know which documents are relevant (ground truth).
- Relevance is binary (relevant or not).

---

### 7. What is AP@10 (Average Precision)?

Explanation:
AP@10 is the average of precision scores at ranks where relevant items appear, considering the top 10.

- $R$ = set of ranks where relevant items occur
- $P(k)$ = precision at rank $k$
- $\text{rel}(k)$ = 1 if item at rank $k$ is relevant, 0 otherwise

$\text{AP} = \frac{1}{\text{Total Relevant Items}} \sum_{k=1}^{N} P(k) \cdot \text{rel}(k)$

|Rank|Relevant?|Precision at k|
|---|---|---|
|1|✅|1/1 = 1.00|
|2|❌|—|
|3|✅|2/3 = 0.67|
|4|✅|3/4 = 0.75|
|5|❌|—|

$\text{AP} = \frac{1}{3} (1.0 + 0.67 + 0.75) = \frac{2.42}{3} \approx 0.807$

It incorporates recall by rewarding systems that retrieve relevant items earlier.

---

### 8. What is Recall@10?

Explanation:
Recall@10 = Number of relevant documents retrieved in the top 10 ÷ Total number of relevant documents.

It answers: “Did I find most of the relevant stuff?”

---

### 9. What is nDCG@10?

Explanation:
nDCG (Normalised Discounted Cumulative Gain) gives higher importance to relevant documents that appear earlier in the ranked list. It also supports graded relevance (not just binary).

$\text{DCG@k} = \sum_{i=1}^{k} \frac{2^{\text{rel}_i} - 1}{\log_2(i + 1)}$
- $\text{rel}_i$​: relevance score of the item at position $i$
- $\log_2(i+1)$: discounts the score as the rank increases

$\text{DCG}@10 = \sum_{i=1}^{10} \frac{rel_i}{\log_2(i+1)}, \quad \text{nDCG}@10 = \frac{DCG@10}{\text{Ideal DCG@10}}$

---

### 10. What metric is most important for first-stage retrieval?

Answer:
Recall@k (often Recall@1000).

You want to catch all possibly relevant documents — reranking will handle the rest.

---

### 11. What are vector space term weighting schemes?

Prerequisite: Term frequency and inverse document frequency.

Explanation:
These are ways to assign importance to terms when representing documents as vectors.

Common:
- TF-IDF: Term frequency * Inverse Document Frequency

$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)$

Where:
- $\text{TF}(t, d)$ = number of times term $t$ appears in document $d$
- $\text{IDF}(t) = \log\left(\frac{N}{\text{df}_t}\right)$
    - $N$: total number of documents
    - $\text{df}_t$​: number of documents containing term $t$

- BM25: A more advanced probabilistic variant

$\text{BM25}(t, d) = \text{IDF}(t) \cdot \frac{f(t, d) \cdot (k_1 + 1)}{f(t, d) + k_1 \cdot (1 - b + b \cdot \frac{|d|}{\text{avgdl}})}$

Where:
- $f(t, d)$: term frequency of term $t$ in document $d$
- $|d|$: length of document $d$
- $\text{avgdl}$: average document length in the corpus
- $k_1$​, $b$: tuning parameters (commonly $k_1 = 1.2$, $b = 0.75$)
- $\text{IDF}(t) = \log \left( \frac{N - \text{df}_t + 0.5}{\text{df}_t + 0.5} + 1 \right)$

---

### 12. What is Jaccard?

Explanation:
Jaccard similarity = Intersection ÷ Union of two sets (e.g., document word sets)

$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$

Weaknesses:
- Doesn’t handle term frequency
- Ignores order and importance of terms

---

### 13. What is Euclidean distance for ranking?

Explanation:
Euclidean distance measures geometric distance between vectors. In IR, documents/users as vectors.

Disadvantage Example:
A short and a long document on the same topic may be far apart in Euclidean space, but actually similar.

---

### 14. What is parsimony in model evaluation?

Explanation:
Parsimony = Simplicity. A model should explain data with minimal complexity.

Advantage:
Avoids overfitting; generalises better.

---

### 15. What are Embedding Vector Spaces?

Explanation:
These are dense, low-dimensional representations of words or documents that capture meaning (e.g., word2vec, BERT embeddings).

---

### 16. What are Term Vector Spaces?

Explanation:
Sparse, high-dimensional vectors representing documents by word occurrences (like TF-IDF vectors).

---

### 17. What is MonoBERT?

Explanation:
A re-ranking model where BERT takes `[CLS] query [SEP] document` and outputs a relevance score. It’s accurate but slow.

---

### 18. What is Pointwise Learning?

Explanation:
You train the model to assign a relevance score to individual query-document pairs (e.g., regression or classification).

---

### 19. What is Bi-encoder Architecture?

Explanation:
Query and document are encoded independently, allowing fast retrieval (via similarity search). But they lose the interaction between the query and the document.

---

### 20. What is Cross-encoder Architecture?

Explanation:
Query and document are fed together into the model (similar to MonoBERT), allowing for full interaction but at a high computational cost.

---

### 21. What is Nearest Neighbour Search?

Explanation:
Given a query vector, find the closest document vectors. Used with bi-encoders and embeddings.

---

### 22. Explain Fine-Tuning and the Relevance Relation between Words

Explanation:
Fine-tuning adjusts pre-trained models, such as BERT, on a smaller, task-specific dataset (e.g., ranking relevance). It helps the model better understand relationships like “laptop” ≈ “notebook.”

---

### 23. Why do we do truncation with BERT?

Explanation:
BERT has a 512-token limit. You truncate to fit this constraint.

Why it works for scientific papers but not law texts:
- Scientific papers are more structured and concise
- Law texts are long and full of cross-references

---

### 24. Alternatives to Truncation for Long Texts

- Chunk into smaller passages
- Use Longformer or BigBird (models built for long inputs)
- Hierarchical models (e.g., sentence-level → document-level)

---

### 25. What is Late Interaction in ColBERT?

Explanation:
ColBERT encodes each query and document token separately. Interaction happens late (during scoring), making it faster than cross-encoders but more accurate than bi-encoders.

---

### 26. Generative Language Models for Ranking (Query Likelihood Model)

Formula:
$P(Q|D) = \prod_{i=1}^{|Q|} P(q_i|D)$

This estimates how likely the query is generated from the document.  

Memory = Document language model, which “remembers” which words are likely in a document.

---

### 27. Constraints in Memory (Query Likelihood Models)

- Add smoothing (e.g., Jelinek-Mercer) so that unseen words get non-zero probability.
- Trade-off between specificity (document-level) and generality (collection-level).

---

### 28. Relevance Model (Lavrenko & Croft)

Explanation:
Estimates a relevance model from the top documents for a query. Generates expanded queries. Very effective for query expansion.

---

### 29. What is Position Bias?

Explanation:
Users are more likely to click top results, regardless of their actual relevance.

How to estimate:
- Randomize ranking
- Use eye-tracking/click models

---

### 30. What is Search Result Diversification?

Explanation:
Showing results that cover different interpretations of a query.

Example Query:
“Python” → Could mean a language or a snake

---

### 31. What is Maximal Marginal Relevance (MMR)?

Explanation:
Select results that are relevant and diverse:

$\text{MMR} = \arg\max_{D_i} \left[\lambda \cdot \text{Rel}(D_i) - (1 - \lambda) \cdot \max_{D_j \in S} \text{Sim}(D_i, D_j)\right]$

Implicitly diversifies by penalizing redundancy.

---

### 32. What is Dependent Click Model?

Explanation:
A model of user clicks where each click depends on whether the previous document was clicked and satisfied.

Assumptions:
- Users click top-down
- Satisfaction stops search

Equations:
Often use Markov chains; exact form depends on model variant (DBN, DCM).

---

### 33. What is Doc2query?

Explanation:
A method that generates synthetic queries for documents using a generative model. Boosts retrieval by enriching documents.

Nogueira and Lin proposed it.

---

### 34. What is the T5 Model?

Explanation:
A text-to-text transformer trained on multiple tasks (translation, summarization, QA). Doc2query uses T5 to generate queries from documents.

---

### 35. Why is Doc2query 50x faster than MonoBERT?

Answer:
Because Doc2query is used during indexing time. During retrieval, you still use BM25 (no transformer scoring), unlike MonoBERT which scores each doc at query time.

---

## Model Exam 2

- What is disjunctive normal form? (Boolean expressions)
- What is binary search?
- What are merging algorithms?
	- Compare with binary search for posting lists.
- What is the complexity of merge algorithms with respect to posting lengths?
- What is a frequency table?
- What is the Huffman coding scheme?
- What is Recall@10?
	- Assumptions made?
- What is MAP?
- What is MRR?
- What is AP@10?
- What is the term statistics table?
- How to compute the IDF?
- How to compute the log TF weights for query and document?
- How to compute the TF.IDF vectors for query and document?
- How to compute the length-normalised versions of both vectors?
- How to compute the cosine similarity between the two?
- How to compute pointwise loss or average squared regression loss?
- How to compute pairwise loss or summed hinge loss?
- What is the prior probability of being relevant?
- What is the binary independent model?
- What is the retrieval score on the ordinal scale?
- What is Dirichlet smoothing for a generative language model?
- What is the BM25 model?
	- Does it use log scaling for term frequency?
- Explain the binary independence model.
	- What are the probabilities used in this model?
- What is a 2-Poisson distribution?
- What is BIM?
	- How is it different from BM25?
- What is the long tail problem in IR?
	- Why is it a challenge in supervised learning?
- What is implicit feedback for relevance assumptions?
	- Assumptions made?
- What are the metrics to evaluate generative conversational agents?
- What is ROUGE?
- What is BERTscore?
- What is MAP?
- What are the advantages of RAG?

## Model Exam 2 Concepts


### 1. What is Disjunctive Normal Form (DNF)?

Prerequisite: Boolean logic
Answer: DNF is a way to write Boolean expressions using only ORs of AND clauses.

Example:
(A AND B) OR (C AND NOT D)

This form is useful for evaluation and logic simplification.

---

### 2. What is Binary Search?

Prerequisite: Sorted list
Answer: A search algorithm that splits the search space in half at every step.

Time complexity: O(log n)

---

### 3. What are Merging Algorithms?

Answer:
They combine two sorted lists by iterating through them together — useful in intersecting posting lists (e.g., AND queries).

#### Compare with Binary Search for Posting Lists:
- Merging: O(m+n), better when lists are of similar size.
- Binary Search: O(n log m), better if one list is much smaller.

---

### 4. What is the complexity of merge algorithms with respect to posting lengths?

Answer:
If the posting lists are of length m and n, merging takes O(m + n) time.

---

### 5. What is a frequency table?

Answer:
A table showing how often each term appears in a document or collection.

---

### 6. What is the Huffman coding scheme?

Answer:
A compression method that uses variable-length codes. Frequent terms get shorter codes using a binary tree.

---

### 7. What is Recall@10?

Answer:
Fraction of relevant items retrieved in the top 10 results.

$Recall@10 = \frac{\#\ relevant\ items\ in\ top\ 10}{\#\ total\ relevant\ items}$

Assumptions: Relevance is binary and known.

---

### 8. What is MAP (Mean Average Precision)?

Answer:
The mean of average precision values for multiple queries. It rewards relevant results appearing earlier in the list.

---

### 9. What is MRR (Mean Reciprocal Rank)?

Answer:
Average of the reciprocal ranks of the first relevant document.

$MRR = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{rank_i}$

---

### 10. What is AP@10?

Answer:
Average precision calculated over only the top 10 ranked results. It includes positions where relevant items appear.

---

### 11. What is the term statistics table?

Answer:
A table that contains term frequency, document frequency, and postings for each term.

---

### 12. How to compute the IDF?

Answer:

$IDF(t) = \log\left(\frac{N}{df_t}\right)$

Where:
- $N$ = total documents
- $df_t$ = number of documents with term $t$

---

### 13. How to compute the log TF weights for query and document?

Answer:

$TF(t, d) = 1 + \log(freq(t, d))$

Used to reduce the effect of very frequent terms.

---

### 14. How to compute the TF.IDF vectors for query and document?

Answer:

$TFIDF(t, d) = TF(t, d) \times IDF(t)$

Do this for each term and build a vector.

---

### 15. How to compute the length-normalised versions of both vectors?

Answer:
Normalize using the L2 norm (Euclidean length):

$\vec{v}_{norm} = \frac{\vec{v}}{||\vec{v}||}$

---

### 16. How to compute the cosine similarity between the two?

Answer:
$\text{CosineSimilarity}(q, d) = \frac{q \cdot d}{||q|| \times ||d||}$

Measures the angle between the vectors (similarity in direction).

---

### 17. How to compute pointwise loss or average squared regression loss?

Answer:
Used in learning to rank.

$\text{Loss} = (y_{\text{true}} - y_{\text{pred}})^2$

---

### 18. How to compute pairwise loss or summed hinge loss?

Answer:

$\text{Loss} = \sum \max(0, 1 - (s_{pos} - s_{neg}))$

Encourages relevant items to be scored higher than non-relevant ones.

---

### 19. What is the prior probability of being relevant?

Answer:

$P(\text{Rel}) = \frac{\text{\# relevant documents}}{\text{Total documents}}$

Used in probabilistic models like BIM.

---

### 20. What is the binary independent model (BIM)?

Answer:
A probabilistic model that assumes terms occur independently and have binary presence.

---

### 21. What is the retrieval score on the ordinal scale?

Answer:
Rank-based score — uses position (like 1st, 2nd) rather than absolute values.

---

### 22. What is Dirichlet smoothing for a generative language model?

Answer:
Adds pseudo-counts to avoid zero probabilities in language models:

$P(w|d) = \frac{tf + \mu P(w|C)}{|d| + \mu}$

---

### 23. What is the BM25 model?

Answer:
A state-of-the-art ranking function:

$BM25 = \sum \text{IDF}(t) \cdot \frac{tf \cdot (k+1)}{tf + k(1 - b + b \cdot \frac{dl}{avgdl})}$

Yes, it uses log scaling for term frequency via IDF.

---

### 24. Explain the binary independence model (again):

Answer:
Same as BIM — uses $P(t | relevant)$ and $P(t | not relevant)$, assuming terms are independent and binary.

---

### 25. What is a 2-Poisson distribution?

Answer:
A probabilistic model assuming two types of documents:
- “elite” → high term frequency
- “non-elite” → low frequency
    Each modeled by a Poisson distribution.

---

### 26. What is BIM and how is it different from BM25?

Answer:
- BIM: binary term presence, uses probabilities.
- BM25: term frequency, length normalization, more practical.

---

### 27. What is the long tail problem in IR?

Answer:
Most queries or items are rare (the “tail”).
Challenge in supervised learning: Not enough data to learn good models for them.

---

### 28. What is implicit feedback for relevance assumptions?

Answer:
- Uses clicks, time-on-page, etc. instead of explicit ratings.
- Assumptions:
    - Click = relevance
    - No click = not relevant (but this may be incorrect!)

---

### 29. What are the metrics to evaluate generative conversational agents?

Answer:
- ROUGE
- BLEU
- METEOR
- BERTScore

---

### 30. What is ROUGE?

Answer:
Measures overlap between generated and reference texts using:
- n-grams
- longest common subsequence
- word sequences

---

### 31. What is BERTScore?

Answer:
Compares tokens using BERT embeddings. Matches similar words even if they’re not exact.

---

### 32. What are the advantages of RAG (Retrieval-Augmented Generation)?

Answer:
- Combines retrieval (for knowledge) and generation (for fluency).
- Improves the accuracy of answers.
- Scalable and dynamic (can update facts by changing the retriever).

---

## Notes

- What is SERP?
	- Search Engine Results Page
- What is Stemming?
	- Stemming is the process of reducing words to their root form by chopping off suffixes.
	- "running" → "run"
	- "flies" → "fli"
	- "studies" → "studi"
- What is Lemmatisation?
	- Lemmatisation is the process of reducing a word to its lemma (dictionary form), using vocabulary and grammar.
	- "running" → "run"
	- "better" → "good"
	- "was" → "be"
- Term-based models are sometimes referred to as lexical models or sparse retrieval models.
	- BM25
	- TF-IDF
