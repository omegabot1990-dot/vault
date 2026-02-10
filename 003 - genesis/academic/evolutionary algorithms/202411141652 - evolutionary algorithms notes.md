---
tags:
  - academic
  - ea
aliases:
  - evolutionary algorithms
title: evolutionary algorithms notes
description: notes for evolutionary algorithms
parent nodes:
  - "[[evolutionary algorithms]]"
child nodes: 
annotation-target:
---

## Cues

1. What is Low Auto-correlation Binary Sequence (LABS)?
2. What is Monte-Carlo Search?
   Monte Carlo Search is a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results.
3. What is the Bernoulli process?
   A Bernoulli process is a sequence of random experiments where each experiment (or trial) results in a binary outcome — typically classified as a "success" or "failure". Each trial in a Bernoulli process:
   1. Is binary in nature.
   2. Has only two possible outcomes (success or failure).
   3. The probability of success $p$ remains constant from trial to trial.
   4. Trials are independent of each other.
4. What is the geometric distribution with respect to Bernoulli trials?
   The geometric distribution is a discrete probability distribution that models the number of trials needed to achieve the first success in a sequence of independent and identically distributed Bernoulli trials.
   *Probability Mass Function (PMF)*: The probability that the first success occurs on the $k$-th trial is given by the PMF: $P(X=k)=(1−p)^{k−1}p$.
5. What is the cumulative distribution function? 
   The Cumulative Distribution Function (CDF) of a geometrically distributed random variable $X$ gives the probability that $X$ is less than or equal to a certain value $k$. This is effectively the probability of achieving the first success within $k$ trials: $P(X≤k)=1−(1−p)^k$.
6. What is the hamming distance?
   The Hamming distance is a metric used to measure the difference between two strings of equal length. It calculates the number of positions at which the corresponding symbols are different. In other words, it tells you how many substitutions are needed to change one string into the other or, equivalently, the number of errors that transformed one string into the other.
7. What is the No Free Lunch theorem (NFLT)?
   The No-Free-Lunch Theorem (NFLT) for optimisation is a formal statement in mathematical optimisation and computer science that asserts that all optimisation algorithms perform equally well when averaged across all possible problems.
8. What are the features that make GA good?
   Implicit Parallelism
   Building Block Hypothesis
   

## Notes

1. Terminology
	1. Direct Optimisation
		1. GA
	2. First Order Optimisation
		1. Gradient Descent
	3. Second Order Optimisation
		1. Newton Method
2. Evolutionary Strategies (ES)
	1. **Mixed-integer capabilities**: Can handle optimisation problems involving integer and real numbers.
	2. **Emphasis on mutation**: Mutation is the primary mechanism for generating new solutions.
	3. **Self-adaptation**: Parameters of the algorithm, like mutation rate, can adapt based on the evolutionary progress.
	4. **Small population sizes**: Typically operates with smaller candidate solutions.
	5. **Deterministic selection**: Uses deterministic rules, rather than probabilistic methods, to select individuals for the next generation.
	6. **Developed in Europe**: Originated and evolved primarily in the European research community.
	7. **Theory focused on convergence speed**: The theoretical analysis often focuses on how quickly the algorithm converges to a solution.
3. Genetic Algorithms (GA)
	1. **Discrete representations**: Primarily handles problems where discrete variables represent solutions.
	2. **Emphasis on crossover**: Crossover between pairs of solutions is the main operator used to generate new solutions.
	3. **No self-adaptation**: Typically does not include mechanisms for the algorithm's parameters to adapt independently.
	4. **Larger population sizes**: Uses larger sets of candidate solutions compared to ES.
	5. **Probabilistic selection**: Select individuals based on a probability model, often related to their fitness.
	6. **Developed in the US**: Originated and developed largely within the American research community.
	7. **Theory focused on schema processing**: Theoretical work often involves studying how building blocks of solutions (schemas) combine and evolve.

## Summary

### Binomial Coefficient

The binomial coefficient represents the number of ways to choose $k$ elements from a set of $n$ elements without regard to the order of the elements. It is commonly denoted as $\binom{n}{k}$ and read as "n choose k." 

**Formula:**
$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$
where $n!$ (n factorial) is the product of all positive integers up to $n$, and $k$ must satisfy $0 \leq k \leq n$.

**Example:**
To calculate how many different ways you can choose 3 students from a group of 10:
$$
\binom{10}{3} = \frac{10!}{3!(10-3)!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120
$$

### Permutation

A permutation refers to an arrangement of elements where order is important. The number of ways to arrange $r$ elements out of a total of $n$ elements is given by the formula for permutations.

**Formula:**
$$
P(n, r) = \frac{n!}{(n-r)!}
$$

This formula determines how many different ways $r$ elements can be ordered or arranged from a total of $n$ elements.

**Example:**
To find how many different ways 3 students can be seated in a row from a group of 10:
$$
P(10, 3) = \frac{10!}{(10-3)!} = \frac{10 \times 9 \times 8}{1} = 720
$$

### Combination

A combination is a selection of items where order does not matter, unlike permutation. The number of ways to choose $r$ elements from a set of $n$ elements irrespective of the order is given by the formula for combinations, which is essentially the binomial coefficient.

**Formula:**
$$
C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

This formula is used when the order of elements in the selection does not matter.

**Example:**
To find how many ways you can select 3 students from a group of 10 regardless of the order:
$$
C(10, 3) = \binom{10}{3} = \frac{10!}{3!(10-3)!} = 120
$$

### Summary

- **Binomial Coefficient**: Counts the number of ways to choose $k$ items from $n$ items without regard to order.
- **Permutation**: Counts the number of ways to arrange $r$ items from $n$ items where the order matters.
- **Combination**: Counts the number of ways to choose $r$ items from $n$ items where the order does not matter.


## Assignment

##### Technical Parameters

1. mutation rate
2. population size
3. crossover rates

##### Parameter Tuning

- Representation
- Mutation
- Crossover
- Selection

#####  Individuals
$$
a =\{0,1\}^l
$$
##### Genotype Space
$$
\{0,1\}^l
$$

- Phenotype space is mapped to genotype space.
- Variation Operators act on genotype.
- Genotypes are decoded into phenotypes.
- Phenotypes are evaluated.
- Selection acts on phenotype evaluations.

##### Crossover

- 1-point crossover
- n-point crossover
- Uniform crossover

$$
p_{c} \in [0,1]
$$
Typically,
$$
\begin{align}
p_{c} = 0.6  \\
p_{c} = 0.95 \\
p_{c} = [0.75,0.95] 
\end{align}
$$

##### Mutation

$$
\begin{align}
p_{m} = \frac{1}{l} \\
\frac{1}{l} \leq p_{m} \leq \frac{1}{2}
\end{align}
$$
##### Selection

Roulette Wheel Technique
$$
p_{i} = \frac{f_{i}}{\sum_{j=1}^{\mu}f_{j}}
$$
