---
tags:
  - academic
  - ea
aliases:
  - evolutionary algorithms - quick notes
title: evolutionary algorithms - quick notes
description: exam notes for EA
parent nodes:
  - "[[evolutionary algorithms]]"
child nodes: 
annotation-target:
---

## Notes

### 1: Introduction

#### Probability and Calculus

> [[probability_and_calculus.pdf|A Review of Probability and Calculus]]
- What is a set?
- What is a subset? 
- What is a proper subset? 
	- $A\subseteq B, A\neq B$
	- $A\subset B$
- What is a singleton set?
- What is an empty set?
	- $\emptyset$
- What is a power set?
	- All possible subsets
	- For $A$, $2^A$ power sets exist
	- Contains $\emptyset$ and $A$
- What is a union of sets?
- What is an intersection of sets?
- What is a set complement?
	- $A\subset B$
	- $A^c$ w.r.t $B$
	- $A^c=\{b\in B:b\notin A\}$
- What is sample space?
	- The set of all the outcomes of a random experiment.
	- One flip of a coin
		- $\Omega =\{H,T\}$
- What is event space?
	- The collection of all possible events that can be formed from the outcomes of a random experiment.
	- One flip of a coin
		- $\mathcal{F}=\{\emptyset, \{H\}, \{T\}, \Omega\}$
	- $\Omega \in \mathcal{F}$
- What are disjoint events?
	- $P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i)$
- What is probability space?
	- $(\Omega, \mathcal{F}, \mathbb{P})$
	- Its a tuple
- What is discrete random variable?
	- It is a function $X$ such that,
	- $X : \Omega \to \{0, 1, \dots, k\}$
- What is probability mass function (p.m.f)?
	- $P(X = k) = P(\{\omega \in \Omega \mid X(\omega) = k\})$
- What is an identity function?
- What is independence of events?
- What is Bernoulli distribution?
	- Tossing a coin, the head (1) is observed with probability $p$ and the tail (0) with $1 − p$
	- $P(X) = \begin{cases} p, & \text{if } X(\omega) = 1 \\ 1 - p, & \text{if } X(\omega) = 0 \end{cases}$
- What is Binomial distribution?
	- The number of heads in $n$ independent flips of a coin with heads probability $p$
	- $P(X = i) = \binom{n}{i} p^i (1 - p)^{n-i}$
- What is derivative?
- What is Riemann Integral?
	- $\delta = \max(x_{i+1} - x_i), \quad i = 0, 1, \dots, n$
	- $\int_a^b f(x) \, dx := \lim_{\delta \to 0} \sum_{i=0}^{n-1} f(t_i)(x_{i+1} - x_i)$
	- $\int_a^b f(x) \, dx = F(b) - F(a), \quad \frac{dF}{dx} = f(x)$
- What is a continuous random variable
	- It is a function $X$ such that,
	- $X : \Omega \to \mathbb{R}, \, \omega \mapsto X(\omega)$
	- $P(a \leq X \leq b) = P(\{\omega : a \leq X(\omega) \leq b\})$
- What is cumulative distribution function (c.d.f)?
	- $F_X(x) := P(X \leq x)$
	- $P(X > x) = 1 - P(X \leq x) = 1 - F_X(x)$
	- $P(a \leq X \leq b) = F_X(b) - P(X \leq a) = F_X(b) - F_X(a)$
- What is probability density function?
	- The density function can be thought as the “changing rate” of CDF.
	- If the cumulative distribution function FX is differentiable everywhere, we define the Probability Density Function as the derivative of the CDF,
	- $f_X(x) := \frac{dF_X(x)}{dx}$
	- For very small $\Delta x$
	- $P(x \leq X \leq x + \Delta x) \approx f_X(x) \Delta x$ 
	- $f_X(x) > 0$
	- $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$ 
	- $\int_a^b f_X(x) \, dx = P(a \leq X \leq b)$
- What is expectation?
	- $E[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx$ (continuous)
	- $E(X) = \sum_{i=0}^l i \cdot P(X = i)$ (discreet)
	- The expectation of $X$ can be thought of as a “weighted average” of the values where the weights are given $f_{X} (x)$.
- What is variance?
	- It measures the variability of $X$, which is defined as the expected “deviation” of $X$ from its expectation
	- $\text{Var}[X] = E[(X - E[X])^2]$
- What are common continuous distributions?
	- Uniform
		- $\mathcal{U}(a,b):$ Equal probability density everywhere in the interval $[a, b]$
		- $f_X(x) = \frac{1}{b - a} \quad \text{if } a \leq x \leq b$
	- Normal
		- $\mathcal{N}(\mu,\sigma^2)$: Also known as the Gaussian distribution
		- $f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$

---

#### Asymptotic Analysis

- What is Big-O?
	- Describes the worst case of the running time of an algorithm 
	- $T (n)$ is bounded above
	- $T(n) \in O(g(n)) \iff \limsup_{n \to \infty} \frac{T(n)}{g(n)} < \infty$
- What is Big-Omega?
	- Describes the best case of the running time of an algorithm
	- $T (n)$ is bounded below; Knuth’s definition)
	- $T(n) \in \Omega(g(n)) \iff \liminf_{n \to \infty} \frac{T(n)}{g(n)} > 0$
- What is Big-Theta?
	- $T (n)$ is bounded above and below
	- $T(n) \in O(g(n)) \quad \text{and} \quad T(n) \in \Omega(g(n))$
- What is Small-O?
	- $T (n)$ is dominated asymptotically
	- $T (n)$ grows way slower than $g(n)$
	- $T(n) \in o(g(n)) \iff \lim_{n \to \infty} \frac{T(n)}{g(n)} = 0$
- What is Small-Omega?
	- $T (n)$ is dominating asymptotically
	- $T (n)$ grows way faster than $g(n)$
	- $T(n) \in \omega(g(n)) \iff \lim_{n \to \infty} \frac{T(n)}{g(n)} = \infty$
- What is the same order?
	- Asymptotically equal
	- $T(n) \sim g(n) \iff \lim_{n \to \infty} \frac{T(n)}{g(n)} = 1$

---

- What is OneMax?
- What is LABS?
- What is Monte-Carlo search?
- What is evolutionary search algorithm?
	- Evolution-like algorithms are logarithmic, not exponential, concerning their running time

$$
\begin{aligned}
& \text{1. } k \gets 1 \\
& \text{2. Randomly initialize a candidate solution } a_k \in \{0, 1\}^n. \\
& \text{3. \textbf{while} } a_k \neq a^* \, \textbf{do} \\
& \quad \text{4. Create a copy } a_k' \text{ of } a_k. \\
& \quad \text{5. Flip each bit in } a_k' \text{ with probability } p \in (0, 1). \\
& \quad \text{6. \textbf{if} } d(a_k', a^*) < d(a_k, a^*) \, \textbf{then} \\
& \quad \quad \triangleright \text{ where \( d(a, b) \) computes the Hamming Distance.} \\
& \quad \quad \text{7. } a_{k+1} \gets a_k' \\
& \quad \text{8. \textbf{else}} \\
& \quad \quad \text{9. } a_{k+1} \gets a_k \\
& \quad \text{10. \textbf{end if}} \\
& \text{11. } k \gets k + 1 \\
& \text{12. \textbf{end while}}
\end{aligned}
$$

- What are EAs used for?
	- Evolutionary Algorithms (EAs) are mostly used for optimisation
	- They are ==global random search== algorithms
- What is optimisation?
	- $f: M \to \mathbb{R}, \, f(x) \to \min$
	- $f:$ is objective function
		- High-dimensional
		- Non-linear, multimodal
		- Discontinuous, noisy, dynamic
	- $M \subseteq M_1 \times M_2 \times \dots \times M_n$ heterogeneous
	- Restrictions possible over $M,f(x)$
- How do we classify optimisation algorithms?
	- Direct
		- EA
	- First order
		- Gradient method
	- Second order
		- Newton method
- What is black box optimisation?
- What are iterative optimisation heuristics?
	- At every iteration
		- Choose direction
			- Gradient
			- Random
		- Determine step size
			- 1-D optimisation
			- Random
			- Self-adaptive (learning)
- What are theoretical statements about EA?
	- Global convergence with probability one
		- $\Pr\left(\lim_{t \to \infty} x_t \in X^*\right) = 1$
	- Convergence velocity
		- $\varphi = E f^{t+1}_{\text{best}} - f^t_{\text{best}}$
		- Typically, convex objective functions
- What is No Free Lunch (NFL) theorem?
	- All optimisation algorithms perform equally well iff. performance is averaged over all possible optimisation problems
- What is global minima?
	- $f^* :=f(x^*)$
	- $\forall x \in D : f^* \leq f(x)$
- What is local minima?
	- $\mathbf{x'} : U_\varepsilon(\mathbf{x'}) = \{\mathbf{x} \in D \mid \|\mathbf{x} - \mathbf{x'}\| < \varepsilon\}$
	- $f^{'} :=f(x^{'})$
	- $\exists \varepsilon > 0 : \forall \mathbf{x} \in U_\varepsilon(\mathbf{x'}) : f' \leq f(\mathbf{x})$
- What is euclidean distance?
	- $\|x - y\| = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$
- What is unimodal?
	- $f$ is called unimodal, iff there is exactly one local (global) minimiser (maximiser)
	- Otherwise called multimodal
- What is hamming distance?
	- $\delta_H(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^n I(x_i \neq y_i) = \sum_{i=1}^n |x_i - y_i|$
	- Used in the case of discreet sets
- What is parameter fitting?

### 2: Evolutionary Algorithms

- What are Evolutionary Algorithms?
	- Genetic Algorithms
		- Canonical
		- Messy
		- Real-coded
		- Order-based
	- Evolution Strategies
		- (1+1)
		- (1,l)
		- (m,l)
		- Derandomised
		- CMA
	- Evolutionary Programming
	- Genetic Programming
- What are the key features of GA?
	- Discrete representations
	- Emphasis on crossover
	- No self-adaptation
	- Larger population sizes
	- Probabilistic selection
	- Theory focussed on schema processing
- What are the key features of ES?
	- Mixed-integer capabilities
	- Emphasis on mutation
	- Self-adaptation
	- Small population sizes
	- Deterministic selection
	- Theory focused on convergence speed
- What are individuals?
	- Candidate solutions forming a population
- What is reproduction?
	- Copying of individuals
- What is crossover?
	- Recombination
	- Two or more parents
	- One or more offspring
- What is mutation?
	- One parent
	- One offspring
- What is the quality measure of individuals?
	- Fitness function or Objective function
- What is the survival of the fittest principle?
- What is the mating of the fittest principle?
- What are the main components of EAs?
	- Representation of individuals: Coding 
	- Evaluation method for individuals: Fitness 
	- Initialisation procedure for 1st generation
	- Definition of variation operators (mutation, crossover)
	- Parent (mating) selection mechanism
	- Survivor (environmental) selection mechanism
	- Technical parameters
		- Mutation rates
		- Population size
		- Crossover rates
- What is generalised EA?
$$
\begin{aligned}
& \text{1. } t \gets 0 \\
& \text{2. Initialize } P(t) \\
& \text{3. Evaluate } P(t) \\
& \text{4. \textbf{while} Termination criterion not met \textbf{do}} \\
& \quad \text{5. } P'(t) \gets \text{ParentSelection}(P(t)) \\
& \quad \text{6. } P''(t) \gets \text{Variation}(P'(t)) \quad \triangleright \text{E.g., Recombination and Mutation} \\
& \quad \text{7. Evaluate } P''(t) \\
& \quad \text{8. } P(t+1) \gets \text{EnvironmentalSelection}(P''(t) \cup Q) \quad \triangleright Q \in \{\emptyset, P(t)\} \\
& \text{9. } t \gets t + 1 \\
& \text{10. \textbf{end while}}
\end{aligned}
$$
- What are the advantages of EAs?
	- Widely applicable, also in cases where no good solution techniques are available
		- Multimodalities, discontinuities, constraints
		- Noisy objective functions
		- Multiple criteria decision making problems
		- Implicitly defined problems (simulation models)
	- No presumptions w.r.t. search space
	- Low development costs, i.e., costs to adapt to new problems
	- The solutions of EAs have straightforward interpretations
	- Can run interactively, always deliver solutions
	- Self-adaptation of strategy parameters
- What are the disadvantages of EAs?
	- No guarantee for finding optimal solutions within a finite amount of time. This is true for all global optimisation methods
	- No complete theoretical basis (yet), but much progress is being made
	- Parameter tuning is sometimes based on trial and error
		- Solution: Self-adaptation of strategy parameters


### 3: Genetic Algorithms

- What are the main characteristics of GA?
	- Often binary search space, $\{0,1\}^l$
	- Mutation: Bit inversion with a small probability $p_m$
	- Emphasis on recombination/crossover
	- No environmental selection
	- Probabilistic mating selection (proportional etc.)
	- Constant strategy parameters
	- Parent and offspring population sizes are identical
- How do we represent canonical GAs?
	- $a\in\{0,1\}^l$
	- Genotype space: $\{0,1\}^l$ , bit strings of length $l$
	- Phenotype space: Problem-specific representation
	- Genotype --Decoding--> Phenotype
	- Genotype <--Encoding-- Phenotype
- Compare phenotype and genotype space.
	- Variation operators act on genotypes
	- Genotypes are decoded into phenotypes
	- Phenotypes are evaluated
	- Selection acts on phenotype evaluations
- How to solve a problem defined over real values?
	- Subdivide $a$ into $n$ segments of equal length
	- Decode each segment into an integer value
	- Map each integer linearly into a given real-valued interval
	- Phenotype space: $M = \prod_{i=1}^n [u_i, v_i] \subseteq \mathbb{R}^n \quad \text{with interval bounds: } u_i < v_i$
	- Genotype space: $\{0, 1\}^l \quad \text{with} \quad l = n \cdot l_x$
	- Decoding function: $h'(a) = [h_1(a_1, \dots, a_{l_x}), h_2(a_{1+l_x}, \dots, a_{2l_x}), \dots, h_n(a_{1+(n-1)l_x}, \dots, a_l)]$
		- $a_1', a_2', \dots, a_{l_x}' = a_{1+(i-1)l_x}, a_{2+(i-1)l_x}, \dots, a_{l + (i-1)l_x}$
		- $h_i(a_1', \dots, a_{l_x}') = u_i + \frac{v_i - u_i}{2^{l_x} - 1} \left( \sum_{k=1}^{l_x} a_i 2^{k-1} \right)$
- What are the types of crossovers?
	- 1-point crossover
	- 2-point crossover
	- n-point crossover
	- Uniform crossover
- What are crossover parameters?
	- $p_c \in [0,1]$
	- Chooses two individuals with probability $p_c$ for crossover
	- Typical values:
		- $p_{c} = 0.6$
		- $p_{c} = 0.95$
		- $p_{c} = [0.75,0.95]$
- What are mutation parameters?
	- $p_m=1/l$
	- Alter each gene with probability $p_m$
	- Should be between $1/l\le p_m\le1/2$
	- At least one bit on average should mutate
	- $p_m=1/2$ corresponds with random generation of offspring
- Compare exploration vs exploitation
	- Exploration: Discovering promising areas in the search space, i.e., gaining information on the problem
		- Crossover is explorative, it makes a big jump to an area somewhere ‘in between’ two (parent) areas
	- Exploitation: Optimising within a promising area, i.e., using information
		- Mutation is exploitative, it creates random small deviations, thereby staying near (i.e., in the area of) the parent
- What is binary representation and decoding function?
	- $h(a_1, \dots, a_l) = \sum_{i=0}^{l-1} a_{i+1} \cdot 2^i$
	- $p_m=1/l$
	- $f=h$
	- $P(|\Delta f| = 2^i) = \frac{1}{l}, \quad \forall i \in \{0, \dots, l-1\}$
	- $\Delta f = f(a) - f(a') = h(a) - h(a')$
		- $a$: Parent individual
		- $a'$: Mutated offspring
- What are selection mechanisms?
	- Fitness proportional selection or Roulette wheel technique
	- Assign to each individual a part of the roulette wheel (size proportional to its fitness) 
	- Spin the wheel $\mu$ times to select $\mu$ individuals
	- $p_i = \frac{f_i}{\sum_{j=1}^\mu f_j}$
- What are the disadvantages of Roulette wheel technique?
	- Functions $f$ and $f+c$ with constant $c$ handled differently
	- If all function values in a population are similar it becomes random selection
	- Requires positive $f$-values, maximisation 
	- Population size: $\mu$
- What are the advantages of scaling of objective function values (proportional selection with scaling)?
	- $f' = f - c$
		- $c$ can be the smallest function value in the population
	- $p_1' = \frac{f_i - c}{S_f - c \cdot \mu}, \quad \text{with} \quad S_f = \sum_{j=1}^\mu f_j$
	- $p_i' > p_i \iff f_i > \bar{f}$
	- $p_i' < p_i \iff f_i < \bar{f}$
		- Scaling increases selection probabilities of above average individuals
		- Decreases selection probabilities of below-average individuals
- What is an example genetic algorithm?

$$
\begin{aligned}
&\text{1. } t \gets 0 \\
&\text{2. } \text{Initialize}(P(t)) \\
&\text{3. } \text{Evaluate}(P(t)) \\

&\text{4. \textbf{while} Termination criterion not met \textbf{do}} \\
&\quad \text{5. } P'(t) \gets \text{MatingSelection}(P(t)) \\
&\quad \text{6. } P''(t) \gets \text{Crossover}(P'(t), p_c) \\
&\quad \text{7. } P'''(t) \gets \text{Mutate}(P''(t), p_m) \\
&\quad \text{8. } \text{Evaluate}(P'''(t)) \\
&\quad \text{9. } P(t+1) \gets P'''(t) \\
&\quad \text{10. } t \gets t + 1 \\
&\text{11. \textbf{end while}}
\end{aligned}
$$

- What were the dominating theories in GA from 1975-2000?
	- Schema theory, schema theorem
	- Building block hypothesis
	- Implicit parallelism
	- Two-armed bandit analogy
- What is today's theory on GA?
	- Theoretical analysis with stronger predictive capabilities
		- Time complexity
- What is a schema?
	- A schema $H\in\mathbb{B}^l$ is a partial instantiation of a string. Usually the uninstantiated elements are denoted by ‘\*', sometimes called the “don’t care” symbol or ‘wild card’. A schema defines a subset of $\mathbb{B}: H\in\{0,1,*\}$
	- $H=\{1,0,0,*,1,0,*,*,*\}$
	- Set of all instances of schema $H = (h_1, \dots, h_l)$
		- $I(H) = \{(a_1, \dots, a_l) \in \mathbb{B}^l \mid h_i \neq * \implies a_i = h_i\}$
- What is the order of a schema?
	- Order of the schema is the number of instantiated elements
		- $o(H) = |\{i \mid h_i \in \{0, 1\}\}|$
- What is the defining length of a schema?
	- Defining length of the schema is the length of the substring starting at the first and ending at the last instantiated element
		- $d(H) = \max\{i \mid h_i \in \{0, 1\}\} - \min\{i \mid h_i \in \{0, 1\}\}$
- What are some facts about schemata?
	- In total there are $3^l$ different schemata
	- Each chromosome (element of $\mathbb{B}^l$) is an instance of $2^l$ different schemata
	- There are at most $\mu\cdot 2^l$ schemata represented in a population of size $\mu$
- What is schema theorem?
	- $m(H, t+1) \geq m(H, t) \cdot \frac{f(H)}{\bar{f}} \cdot \left( 1 - p_c \frac{d(H)}{l - 1} \right) \cdot (1 - p_m)^{o(H)}$
		- $f$: to be maximised, $\bar{f}$: mean fitness in population  
		- $l$: length of the string  
		- $H$: a schema  
		- $d(H)$: defining length  
		- $o(H)$: order  
		- $p_m$: mutation rate  
		- $p_c$: crossover rate  
		- $f(H)$: (estimated) schema fitness  
		- $m(H, t)$: expected number of instantiations of $H$ in generation $t$  
	- Expected number of instantiations of $H$ selected for crossover
		- $m(H, t) \cdot \frac{f(H)}{\bar{f}}$
	- Probability that crossover does not occur within the defining length
		- $1 - p_c \frac{d(H)}{l - 1}$
	- Probability that the schema is not mutated
		- $(1 - p_m)^{o(H)}$
- What are the assumptions for exponential growth of building blocks?
	- Assume $H$ is a short, low-order, highly fit schema
	-  $f(H) > \bar{f} \quad \text{assumed:} \quad f(H) = \bar{f} + c$
	- Assume $H$ is not destroyed by crossover or mutation
	- Assume this remains valid for a number of generations
		-  $m(H, t+1) = m(H, t) \cdot \frac{\bar{f} + c}{\bar{f}} = m(H, t) \cdot (1 + c')$
	- For a number of generations this means
		- $m(H, t) = m(H, 0) \cdot (1 + c')^t$
		- This means exponential growth of $H$ in the population
- What are some facts about the implicit parallelism of GA?
	- A lot of different schemata are effectively processed in parallel by a Genetic Algorithm (individuals are instantiations of more than one schema)
	- Effectively processing of a schema by reproduction at the desirable exponentially increasing rate
- Why wouldn’t a schema be processed effectively?
	- Schema disruption by genetic operators
- How can you explain the power of GAs?
	- Implicit parallelism and the building block hypothesis were seen as explanations for the power of GAs
	- A small defining length, $d(H)$
	- Low order, $o(H)$
	- High estimated fitness, $f(H)$
- What are some criticisms of Holland '75?
	- "GAs are able to detect short, low order, and highly fit schemata and combine these into highly fit individuals"
	- Most of Holland’s approximations are only true for very large numbers (trials and population size)
	- Within finite populations, exponentially increasing the number of schema instances leads to entirely filling the population
	- Within finite populations, exponentially decreasing the number of schema instances leads to the complete elimination
	- Not all schemata are represented in a typical population
	- Schemata of large defining length are likely to be destroyed by crossover (even highly fit ones)
- What is the theory behind almost sure convergence?
	- $\lim_{t \to \infty} \Pr\{\mathbf{x}^* \in P(t)\} = 1$
	- $P(t)$: Population at time $t$ 
	- $\mathbf{x}^*$: Global optimum
	- $\max_{\mathbf{x} \in P(t)} f(\mathbf{x}) \geq \max_{\mathbf{x} \in P(t-1)} f(\mathbf{x}), \quad \text{e.g., through elitist selection.}$
	- Any point is accessible from any other point (i.e., with mutation, $p_m > 0$)
- What is the convergence velocity for a GA?
	- $\varphi = \mathbb{E}(f_{\max}(P(t+1)) - f_{\max}(P(t)))$
- What is the success probability?
	- $p_{\vec{a}}^+ = P\{f(m(\vec{a})) > f(\vec{a})\}$
- What is the $k$-step success probability ($0\leq k \leq k_{max}$)?
	- $p_{\vec{a}}^+(k) = P\{f(m(\vec{a})) = f(\vec{a}) + k\}$
- What is the convergence velocity for optimal mutation rate $p^*$?
	- $\varphi_{(1+1)}(l, \vec{a}, p) = \sum_{k=0}^{k_{\text{max}}} k \cdot p_{\vec{a}}^+(k)$
- Explain counting ones as a $(1+1)$-EA problem?
	- Mutation rate is $p$, $q = 1- p$
	- $f_a := f(\vec{a})$
	- $p_{\vec{a}}^0 = \sum_{i=0}^{\min\{f_a, l - f_a\}} \binom{f_a}{i} \binom{l - f_a}{i} p^{2i} q^{l - 2i}$
	- $p_{\vec{a}}^+(k) = \sum_{i=0}^{\min\{f_a, l - f_a - k\}} \binom{f_a}{i} \binom{l - f_a}{i + k} p^{2i + k} q^{l - 2i - k}$
		- $0\leq k\leq l-f_{a}$
	- $p_{\vec{a}}^-(k) = \sum_{i=0}^{\min\{f_a - k, l - f_a\}} \binom{f_a}{i + k} \binom{l - f_a}{i} p^{2i + k} q^{l - 2i - k}$
		- $0\leq k\leq f_{a}$
	- $i$: No. of mutations 1 → 0 (harmful ones)
	- $j$: No. of mutations 0 → 1 (useful ones)
	- $p^{0}: j = i, \quad p^{+}(k): j = k \quad in \quad p^{+}, \quad p^−(k): j = k \quad in \quad p$
- What is the convergence velocity for $(1+1)$-GA?
	- $\varphi_{(1+1)} = \sum_{k=0}^{l - f_a} k \cdot p_{\vec{a}}^+(k)$
- What is the approximation for optimum mutation rate?
	- $p^* \approx \frac{1}{2(f_a + 1) - l}$
- Explain the Markov-chain analysis?
	- $l+1$ states
		- $z_k = \{ f(\vec{a}) = l - k \} \quad (0 \leq k \leq l)$
	- Transition probabilities
		- $p_{ij} = P\{ f(m(\vec{a})) = l - j \mid f(\vec{a}) = l - i \}$
	- $p_{ij} = \begin{cases} p_{l-i}^+(i - j) & , \ i > j \quad \text{(Improvement)} \\ 1 - \sum_{k=1}^j p_{l-i}^+(k) & , \ i = j \quad \text{(Stagnation)} \\ 0 & , \ i < j \quad \text{(Worsening)} \end{cases}$
	- State 0 ($l$ bits are correct) is absorbing
	- Transient class of state
		- $\tau = \{ 1, \dots, l \}$
	- Absorption Times:
		- Transition Matrix
			- $\mathbf{P} = \begin{pmatrix} \mathbf{I} & \mathbf{0} \\ \mathbf{R} & \mathbf{Q} \end{pmatrix}$
			- $E_i(t) = \sum_{j \in T} n_{ij}$
			- $\mathbf{N} = (n_{ij}) = (\mathbf{I} - \mathbf{Q})^{-1} \quad (T: \text{transient states})$
			- $I$ denotes a unity matrix of appropriate size
			- $Q$ will be an $(l − 1) × (l − 1)$-matrix 
			- $E_{i}(t)$: Expected time to absorption if started in state $i$
	- Order of magnitude is $\mathcal{O}(l \cdot \ln l)$
- What are the effects of different mutation rates?
	- $p_m$ too large: Exponential complexity (Evolution → random search)
	- $p_m$ too small: Time to absorption almost constant
	- For the (1+1) algorithm, counting ones problem, $p = 1/l$
		- Runtime is $\mathcal{O}(l \cdot \ln l)$
	- Using a (slightly) too large $p$ will quickly cause exponential runtime
- What is the convergence velocity for $(1,\lambda)$-GA/$(1+\lambda)$-GA?
	- $\varphi_{(1^+,\lambda)} = \sum_{k=k_{\text{min}}}^{l - f_a} k \cdot P_{k' = k}(\lambda)$
	- $P_{k' = k}(\lambda)$ is the probability of $\lambda$ offsprings to realise an $k$-step “improvement” after the selection
		- “improvement” can be negative
	- $(1, \lambda)-GA : k_{min} = fa$
	- $(1 + \lambda)-GA : k_{min} = 0$
- What is the proof idea for $(1,\lambda)$-GA/$(1+\lambda)$-GA?
	- $\varphi_{(1^+,\lambda)} = \sum_{k=k_{\text{min}}}^{1 - f_a} k \cdot \sum_{i=1}^{\lambda} \binom{\lambda}{i} \cdot p_{k' = k}^i \cdot p_{k' < k}^{\lambda - i}$
	- $i=\{1, \dots,\lambda\}$ offspring might be the best
	- $\binom{\lambda}{i}$ cases, the remaining ones are worse
	- $p_{k' = k} = \begin{cases} p_a^+(k) & , \ k \geq 0 \\ p_a^-(-k) & , \ k < 0 \end{cases}$
	- $p_{k' > k} = \begin{cases} \sum_{i=k+1}^{l - f_a} p_a^+(i) & , \ k \geq 0 \\ \sum_{i=k+1}^{-1} p_a^-(-i) + \sum_{i=0}^{l - f_a} p_a^+(i) & , \ k < 0 \end{cases}$
	- $p_{k' < k} = 1 - p_{k' = k} - p_{k' > k}$
	- For growing selective pressure $\lambda$ 
		- Optimum mutation rate increases
- What is the convergence velocity for $(\mu,\lambda)$-GA/$(\mu+\lambda)$-GA?
	- $\varphi_{(\mu^+, \lambda)} = \frac{1}{\mu} \sum_{k=k_{\text{min}}}^{l - \bar{f}_a} k \cdot \sum_{\nu = \lambda - \mu + 1}^\lambda p_{\nu}(k)$
	- $p_v(k)$ is the probability for the offspring of rank $v$ to improve objective function value by $k$
	- $p_{\nu}(k) = \sum_{i=0}^{\nu - 1} \binom{\lambda}{\nu - i - 1} \sum_{j=0}^{\lambda - \nu} \binom{\lambda - (\nu - 1 - i)}{\lambda - \nu - j} \cdot p_{k' = k}^{i + j + 1} \cdot p_{k' < k}^{\nu - i - 1} \cdot p_{k' > k}^{\lambda - \nu - j}$
		-  $\nu - i - 1$ realisations smaller than $k$ ($i=0,1, \dots, \nu-1$)
		- $\lambda - \nu - j$ realisations larger than $k$ ($j=0,1, \dots, \lambda-\nu$)
		- $i + j + 1$ (remaining) equals $k$
		- $\binom{\nu - 1}{\nu - i - 1}$ possibilities for choosing individuals distance < $k$
		- $\binom{\lambda - (\nu - 1 - i)}{\lambda - \nu - j}$ possibilities for better ones

### 4: Evolution Strategies

- What are the basics of ES?
	- Mostly real-valued search space $\mathbb{R}^n$
		- Mixed-integer or discrete spaces
	- Emphasis on mutation
		- $n$-dimensional normal distribution
		- Expectation zero
	- Different recombination operators
	- Deterministic selection 
		- $(\mu,\lambda)$-selection where deterioration is possible
		- $(\mu+\lambda)$-selection where only improvements are accepted
		- $\lambda\gg \mu$, i.e. creation of offspring surplus
	- Self-adaptation of strategy parameters
- What is the algorithm for an ES?
$$
\begin{aligned}
&1. \ t \to 0 \\
&2. \ \textbf{Initialize}(P(t)) \\
&3. \ \textbf{Evaluate}(P(t)) \\
&4. \ \textbf{while} \ \text{Termination criterion not met} \ \textbf{do} \\
&\quad 5. \ P'(t) \leftarrow \text{Recombine}(P(t)) \\
&\quad 6. \ P''(t) \leftarrow \text{Mutate}(P'(t)) \\
&\quad 7. \ P'''(t) \leftarrow \text{Select}(P''(t) \cup Q) \quad \triangleright Q \in \{\emptyset, P(t)\} \\
&\quad 8. \ \textbf{Evaluate}(P'''(t)) \\
&\quad 9. \ P(t+1) \leftarrow P'''(t) \\
&\quad 10. \ t \leftarrow t + 1 \\
&11. \ \textbf{end while}
\end{aligned}
$$
- What are the remarks for an ES algorithms?
	- Recombination is applied to all individuals
	- $P(t)''$ has a size of $\lambda>\mu$, $P(t)$ has size $\mu$
	- Normally distributed variations (mutations), applied to all individuals
	- Selection of either $\mu+\lambda$ or $\mu,\lambda$
- What is a ES with $1/5$ rule?
	- Exogenous adaptation of step size $s$
	- $a=(x_{1}, \dots,x_{n})$
- What is a self-adaptive ES with single step size?
	- One step-size controls mutation of all search variables
	- $a=((x_{1}, \dots,x_{n}), \sigma)$
- What is a self-adaptive ES with individual step sizes?
	- One individual $\sigma_{i}$ per $x_{i}$
	- $a=((x_{1}, \dots,x_{n}), (\sigma_{1}, \dots, \sigma_{n}))$
- What is a self-adaptive ES with correlated mutation?
	- Individual step sizes
	- One correlation angle per coordinate pair
	- Mutation according to a multivariate Gaussian $\mathcal{N}(0,C)$
	- $a=\left( (x_{1}, \dots,x_{n}), (\sigma_{1}, \dots, \sigma_{n}),\left( \alpha_{1}, \dots, \alpha_{\frac{n(n-1)}{2}} \right) \right)$
- How does mutation work for ES?
	- It makes use of normally distributed variations
	- Probability density function
		- $p(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$
	- Expectation is typically zero ($\mu=0$)
	- Standard deviation $\sigma$ needs to be adapted
- Explain self-adaptive ES with one step size?
	- One $\sigma>0$ controls mutation for all $x_i$ 
	- Mutation each search variable with a Gaussian perturbation
	- Individual before mutation
		- $\mathbf{a} = \left( (x_1, \dots, x_n), \sigma \right)$
	- Individual after mutation
		- $\mathbf{a}' = \left( (x_1', \dots, x_n'), \sigma' \right)$
	- Step 1: Mutate the step size
		- $\sigma' = \sigma \exp(\tau_0 \mathcal{N}(0, 1))$
	- Step 2: Mutate search variables
		- $x_i' = x_i + \sigma' \mathcal{N}(0, 1) \quad \forall i \in [n]$
- What is the learning rate for single step size ES?
	- $\tau_{0}$ is the learning rate
	- Affects the speed of the $\sigma$-adaptation
	-  $\tau_{0}$ bigger means faster but less precise
	-  $\tau_{0}$ smaller means slower but more precise
	- According to recommendation of Schwefel
		- $\tau_0 = \frac{1}{\sqrt{n}}$
- Where does the offspring lie in single step size ES?
	- Hypersphere
	- Position is uniformly distributed
- What are the advantages and disadvantages of one step ES?
	- Advantages
		- Simple adaptation mechanism 
		- Self-adaptation usually fast and precise
	- Disadvantages
		- Bad adaptation in case of complicated contour lines
		- Bad adaptation in case of very differently scaled object variables
			- $-100<x_{i}<100$ vs $-1<x_{j}<1$ 
- Explain self-adaptive ES with individual step sizes?
	- One $\sigma_{i}$ per $x_{i}$
	- Individual before mutation
		- $\mathbf{a} = \left( (x_1, \dots, x_n), (\sigma_1, \dots, \sigma_n) \right)$
	- Individual after mutation
		- $\mathbf{a}' = \left( (x_1', \dots, x_n'), (\sigma_1', \dots, \sigma_n') \right)$
	- Step 1: Sample a global perturbation
		- $g \sim \mathcal{N}(0, 1)$
	- Step 2: Mutate the step size
		- $\sigma_i' = \sigma_i \exp\left( \tau' g + \tau \mathcal{N}(0, 1) \right) \quad \forall i \in [n]$
	- Step 3: Mutate search variables
		- $x_i' = x_i + \sigma_i' \mathcal{N}(0, 1) \quad \forall i \in [n]$
- What is the learning rate for individual step size ES?
	- $\tau$, $\tau'$ are learning rates
	- $\tau'$ is the global learning rate
		- $\mathcal{N}(0, \tau)$ has only one realisation
	- $\tau$ is the local learning rate
		- $\mathcal{N}(0, \tau)$ has n realisations
	- Suggested by Schwefel
		- $\tau' = \frac{1}{\sqrt{n}}$
		- $\tau = \frac{1}{\sqrt{2\sqrt{n}}}$
- Where does the offspring lie in single step size ES?
	- Hyperellipsoid
	- Position is equally distributed
- What are the advantages and disadvantages of individual step ES?
	- Advantages
		- Individual scaling of object variables
		- Increased global convergence reliability
	- Disadvantages
		- Slower convergence due to increased learning effort
		- No rotation of coordinate system possible
			- Required for badly conditioned objective function
- Explain self-adaptive ES with correlated mutations?
	- Individual step sizes
	- One rotation angle for each pair of coordinates
	- Mutation according to covariance matrix 
		- $\mathcal{N}(0, C)$
	- Individual before mutation
		- $\mathbf{a} = \left( (x_1, \dots, x_n), (\sigma_1, \dots, \sigma_n), (\alpha_1, \dots, \alpha_{n(n-1)/2}) \right)$
	- Individual after mutation
		- $\mathbf{a}' = \left( (x_1', \dots, x_n'), (\sigma_1', \dots, \sigma_n'), (\alpha_1', \dots, \alpha_{n(n-1)/2}') \right)$
	- Step 1: Sample a global perturbation
		- $g \sim \mathcal{N}(0, 1)$
	- Step 2: Mutate the step size
		- $\sigma_i' = \sigma_i \exp\left( \tau' g + \tau \mathcal{N}(0, 1) \right) \quad \forall i \in [n]$
	- Step 3: Mutate rotation angles
		- $\alpha_j' = \alpha_j + \mathcal{N}(0, \beta) \quad \forall j \in \left[ n(n-1)/2 \right]$
	- Step 4: Mutate decision variables
		- $\vec{x}' = \vec{x} + \sigma_i' \mathcal{N}(0, \mathbf{C}') \quad \forall i \in [n]$
		- New Covariance matrix $C'$ is computed from $\alpha_{j}'$ and $\sigma_{i}'$
- How do you create $\mathcal{N}(0,C')$?
	- Multiplication of uncorrelated mutation vector with $n(n-1)/2$ rotational matrices
	- $\mathbf{C}^{\frac{1}{2}} = \left( \prod_{i=1}^{n-1} \prod_{j=i+1}^{n} R(\alpha_{ij}) \right) \begin{bmatrix} \sigma_1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & \sigma_n \end{bmatrix}$
	- $\mathbf{C} = \mathbf{C}^{\frac{1}{2}} \mathbf{C}^{\frac{1}{2} \top}$
- What is a multivariate normal distribution?
	- $f_X(\mathbf{x}) = \frac{1}{(2\pi)^{\frac{n}{2}} |\mathbf{C}|^{\frac{1}{2}}} \exp \left( -\frac{1}{2} (\mathbf{x} - \boldsymbol{\mu})' \mathbf{C}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)$
	- $C_{ij} = \text{cov}(X_i, X_j) = E \left[ (X_i - \mu_i)(X_j - \mu_j) \right]$
- What is the learning rate for self-adaptive ES with correlated mutation?
	- $\tau$, $\tau'$, $\beta$ are learning rates
	- $\tau$, $\tau'$ as before
	- $\beta=\frac{\pi}{36} \approx 0.0873$, corresponds to 5 degrees
	- Out of boundary correction
		- $|\alpha_j'| > \pi \implies \alpha_j' \leftarrow \alpha_j' - 2\pi \cdot \text{sign}(\alpha_j')$
- What are the advantages and disadvantages self-adaptive ES with correlated mutation?
	- Advantages
		- Individual scaling of object variables
		- Rotation of coordinate system possible
		- Increased global convergence reliability
	- Disadvantages
		- Much slower convergence
		- Effort for mutations scales quadratically
		- Self-adaptation very inefficient
- How do you implement correlated mutation algorithm?
	- Input: The problem dimensionality $n$ and an individual to be mutated $\mathbf{a}$.  
	- Output: A correlated step-size vector $\boldsymbol{\sigma}$.  

$$
\begin{aligned}
&\text{1. } n_q \gets \frac{n(n-1)}{2} \\
&\text{2. } \boldsymbol{\sigma} \gets \mathcal{N}(0, \boldsymbol{\sigma}') \quad \triangleright \text{Initialize an uncorrelated mutation vector} \\
&\text{3. for } k = 1, \dots, n-1 \text{ do} \quad \triangleright \text{Correlate } \boldsymbol{\sigma} \text{ by repeated rotations} \\
&\quad 4. n_1 \gets n - k \\
&\quad 5. n_2 \gets n \\
&\quad 6. \text{for } i = 1, \dots, k \text{ do} \\
&\quad \quad 7. d_1 \gets \sigma_{n_1}, \, d_2 \gets \sigma_{n_2} \\
&\quad \quad 8. \sigma_{n_2} \gets d_1 \sin(\alpha'_{n_q}) + d_2 \cos(\alpha'_{n_q}) \\
&\quad \quad 9. \sigma_{n_1} \gets d_1 \cos(\alpha'_{n_q}) - d_2 \sin(\alpha'_{n_q}) \\
&\quad \quad 10. n_2 \gets n_2 - 1, \, n_q \gets n_q - 1 \\
&\quad 11. \text{end for} \\
&\text{12. end for}
\end{aligned}
$$
- What are the ideas behind mutation?
	- Biological model: Repair enzymes, mutator genes
	- No deterministic control: Strategy parameters evolve 
	- Indirect link between fitness and useful strategy parameter settings
	- $\sigma$, $\alpha$ are conceivable as an internal model of the local topology
- How does recombination work?
	- Only for $\mu>1$ 
	- Directly after selection
	- Iteratively generates $\lambda$ offspring
	- Input: An individual to be mutated $(\mathbf{x})$
$$
\begin{aligned}
&\text{1. for } i = 1, \dots, \lambda \text{ do} \\
&\quad 2. \text{Choose recombinant } r_1 \text{ uniformly at random from parent population} \\
&\quad 3. \text{Choose recombinant } r_2 \ne r_1 \text{ uniformly at random from parent population} \\
&\quad 4. \text{Offspring} \gets \textbf{recombine}(r_1, r_2) \\
&\quad 5. \text{Add offspring to offspring population} \\
&\text{6. end for}
\end{aligned}
$$
- What is discrete recombination?
	- Variable at position $i$ will be copied at random (uniformly distributed) from Parent 1 or Parent 2, position $i$
	- For global discrete recombination consider all parents
- What is intermediate recombination?
	- Variable at $i$ position is arithmetic mean of Parent 1 and Parent 2, position $i$
	- For global intermediary recombination consider all parents
- What is $(\mu+\lambda)$-selection?
	- $\mu$ parents produce $\lambda$ offspring by 
		- (Recombination +) (may be left out but mutation always exists)
		- Mutation
		- These $\mu+\lambda$ individuals will be considered together
		- The best $\mu$ out of $\mu+\lambda$ will be selected ("survive“)
			- Deterministic selection
		- This method guarantees monotony
			- Deteriorations will never be accepted
- What is $(\mu,\lambda)$-selection?
	- $\mu$ parents produce $\lambda\gg \mu$ offspring by
		- (Recombination +)
		- Mutation
	- $\lambda$ offspring will be considered alone
	- The $\mu$ best out of $\lambda$ offspring will be selected
		- Deterministic selection
	- The method doesn’t guarantee monotonicity
		- Deteriorations are possible
		- The best objective function value in the generation $t+1$ maybe worse than the best in the generation $t$
- What are the different selection methods?
	- $(1+1)$-ES: One parent, one offspring, 1/5-Rule
	- $(1, \lambda)$-ES: One Parent, $\lambda$ offspring
		- Example: (1,10)-Strategy
		- One step size / $n$ self-adaptive step sizes 
		- Mutative step size control 
		- Derandomised strategy
	- $(\mu , \lambda)$-ES: $\mu>1$ parents, $\lambda>1$ offspring
		- Example: (2,15)-Strategy
		- Includes recombination
		- Can overcome local optima
	- $(\mu +\lambda)$-ES
		- Elitist strategies
- What is the selective pressure of this method?
	- The "selective pressure“ of this method is very high
- How do we define selective pressure?
	- Takeover time $\tau*$
	- The number of generations until repeated application of selection completely fills the population with copies of the initially best individual
	- For $\mu, \lambda$-selection: 
		- $\tau*=\frac{\ln{\lambda}}{\ln{\frac{\lambda}{\mu}}}$
	- For a standard (15,100)-ES:
		- $\tau*\approx 2$
- Why self-adaptation?
	- No deterministic step size control rather we have evolution of step sizes
	- Biology
		- Repair enzymes, mutator-genes
	- Why should this work at all?
		- Indirect coupling
			- Step sizes – Progress
		- Good step sizes improve individuals
		- Bad ones make them worse
		- This yields an indirect step size selection
- What is Schwefel's '87 '92 claim?
	- Self-adaptation works without exogeneous control
	- By recombining/mutating the strategy parameters
	- By exploiting the implicit link between fitness and useful internal models
- What are the necessary conditions for self-adaptation?
	- Found by experiments
	- Generation of an offspring surplus, $\lambda>\mu$ 
	- $(\mu,\lambda)$-selection to guarantee extinction of misadapted individuals
	- A not too strong selective pressure, e.g., (15,100) where $\frac{\lambda}{\mu}=7$ (approx.)
	- Certainly, $\mu>1$ necessary
	- Recombination also on strategy parameters
		- Especially intermediary recombination
- How to design an empirical test?
	- With simple functions – check whether it works 
	- Functions with predictable optimal $\sigma_{i}$ values
	- Compare with optimal behaviour (if known)
	- Investigate impact of selection
- What are test functions for empirical tests?
	- One common step size $(n_{\sigma}=1)$
		- Sphere model
		- $f_1(\mathbf{x}) = \sum_{i=1}^n x_i^2$
	- Appropriate scaling of variables $(n_{\sigma}=n)$
		- $f_2(\mathbf{x}) = \sum_{i=1}^n i x_i^2$
	- A metric $(n_\sigma = n, n_\alpha = n(n-1)/2)$
		- $f_3(\mathbf{x}) = \sum_{i=1}^n \left( \sum_{j=1}^i x_j \right)^2$
- What are some observations from empirical tests?
	- Progress
		- $P_{g}=\log \sqrt{\frac{f_{min}(0)}{f_{min}(g)}}$
	- Counterintuitive: Elitist is a bad choice
	- Misadapted $\sigma$ might survive in an elitist strategy
	- Forgetting is necessary to prevent stagnation periods
- How can we test this at all empirically?
	- Need to know optimal step size
		- Only for very simple, convex objective functions
		- Here: Sphere model
			- $f(x)=\sum_{i=1}^n(x_{i}-x_{i}^*)^2$
		- Dynamic sphere model
			- Optimum locations changes occasionally
	- $\sigma_{opt}=c_{\mu,\lambda}\frac{R}{n}$
- What are some facts about self-adaptation?
	- Self-adaptation of one step size
		- Perfect adaptation
		- Learning time for back adaptation proportional $n$
		- Proofs only for convex functions
	- Individual step sizes
		- Experiments by Schwefel 
	- Correlated mutations
		- Adaptation much slower
- What are some experimental results for individual step sizes?
	- A $(\mu,100)$-ES with $\mu \in \{1, \dots,30\}$
	- $n_\sigma = n = 30$ and the optimal $\sigma_i \propto \frac{1}{\sqrt{i}}$ is known for ellipsoid model $f_2$
	- Optimum setting of $\sigma_{i}:\mu=1$ is best
	- Self adaptation: $\mu=12$ imperfect, diverse parents are as good as the optimal strategy
	- Individuals exchange information about their "internal models" by recombination
- What are some experimental results for covariance?
	- $(15,100)$-ES with $n_{\sigma}=n=10,n_{\alpha}=45$
	- Recombination
		- Intermediary on $x_i$ 
		- Global intermediary on $\sigma i$ 
		- None on $\alpha_{i}$ (covariances)
		- Covariances increase effectiveness in case of rotated coordinate systems
- What is the mutation vector?
	- $\Delta x = z = (z_1, \dots, z_n)$
	- $Z_1, \dots, Z_n : (0, \sigma)$, normally distributed random variables
	- $Z^2 = \sum_{i=1}^n Z_i^2$, is $\chi^2$-distributed
	- $S = \sqrt{Z^2}$ is a random variable: Length of mutation vector $z$
	- For large n: Offspring located on hypersphere with radius
		- $E(S) \approx \sigma \sqrt{n}, \quad V(S) = \frac{\sigma}{2}$
	- Variance independent of $n$
- What is convergence velocity?
	- Expectation of the distance towards the optimum covered per generation
	- $\varphi = E\left[ \| \mathbf{x}^* - \mathbf{x}_t \| - \| \mathbf{x}^* - \mathbf{x}_{t+1} \| \right]$
	- $\varphi = E\left[ | f(\mathbf{x}^*) - f(\mathbf{x}_t) | - | f(\mathbf{x}^*) - f(\mathbf{x}_{t+1}) | \right]$
- What is the convergence velocity theory for $(1+1)$-ES for linear model?
	- $Z_1' \sim \mathcal{N}(0, \sigma^2)$, $\quad Z_1 \sim \mathcal{N}(0, 1)$
$$
\begin{aligned} \varphi &= E(Z_1') \\ &= \sigma E(Z_1) \\ &= \sigma \int_0^\infty z_1 \phi(z_1) \, dz_1 \\ &= \frac{\sigma}{\sqrt{2\pi}} \int_0^\infty z_1 \exp\left( -\frac{z_1^2}{2} \right) \, dz_1 \\ &= \frac{\sigma}{\sqrt{2\pi}} \end{aligned}
$$
- What is the corridor model?
	- The corridor model is a simplified optimisation model often used in evolutionary strategies (ES) to analyse and understand convergence velocity and success probability.
	- $f(\mathbf{x}) = c \cdot x_1, \quad -b \leq x_2, \dots, x_n \leq b$
	- Results of analysis
		- $\varphi = \frac{\sigma}{\sqrt{2\pi}} \left( 1 - \frac{\sigma}{b\sqrt{2\pi}} \right)^{n-1}$
	- After normalisation of variables $\sigma' = \frac{\varphi n}{b}, \quad \sigma' = \frac{\sigma n}{b}$
		- $\sigma' \approx \frac{\sigma'}{\sqrt{2\pi}} \exp\left( -\frac{\sigma'}{\sqrt{2\pi}} \right), \quad \text{for } n \gg 1$
	- Success probability $\omega_e = P\left( f(\mathbf{x}') \leq f(\mathbf{x}) \right)$
		- $\omega_e \approx \frac{1}{2} \exp\left( -\frac{\sigma'}{\sqrt{2\pi}} \right), \quad \text{for } n \gg 1$
- What is the optimal standard deviation?
	- $\sigma'_{\text{opt}} = \sqrt{2\pi}$
- What is the maximum convergence velocity?
	- $\varphi'_{\text{max}} = \frac{1}{e}$
- What is the optimal success probability?
	- $\omega_{e_{\text{opt}}} = \frac{1}{2e}$
- What is the sphere model?
	- $f(\mathbf{x}) = \sum_{i=1}^n x_i^2 = r^2$
	- $z'^2 + x^2 = l^2 \\ \quad \quad = x^2 + (R - z')^2 = r^2 \\ \quad \quad = r^2 = l^2 + R^2 - 2Rz'$
	- $\varphi = E(R^2 - r^2) = E(2RZ' - l^2)$
	- $\varphi = E(2R\sigma Z - \sigma^2 n)$
	- $\varphi = 2R\sigma \int_{z_{\text{min}}}^\infty z \phi(z) \, dz - \sigma^2 n \int_{z_{\text{min}}}^\infty \phi(z) \, dz$
	- $\varphi = \frac{2R\sigma}{\sqrt{2\pi}} \exp\left( -\frac{\sigma^2 n^2}{8R^2} \right) - \sigma^2 n \left( 1 - \Phi\left( \frac{\sigma n}{2R} \right) \right)$
	- After normalisation of variables $\varphi \approx \frac{\varphi'}{2R}, \quad \varphi' = \frac{\varphi n}{R}, \quad \sigma' = \frac{\sigma n}{R}$
		- $\varphi' = \frac{\sigma'}{\sqrt{2\pi}} \exp\left( -\frac{\sigma'^2}{8} \right) - \frac{\sigma'^2}{2} \left( 1 - \Phi\left( \frac{\sigma'}{2} \right) \right)$
	- Success probability $\omega_e = 1 - \Phi\left( \frac{\sigma'}{2} \right)$
- What is the optimal standard deviation?
	- $\sigma'_{\text{opt}} \approx 1.224$
- What is the maximum convergence velocity?
	- $\varphi'_{\text{max}} \approx 0.2025$
- What is the optimal success probability?
	- $\omega_{e_{\text{opt}}} \approx 0.270$
- What is the 1/5-success rule?
	- $\omega_{e_{opt}}$ should be about 1/5. If $\omega_{e}$ — measured during execution of the $(1+1)$-ES
		- Is larger than 1/5, increase $\sigma$
		- If it is smaller than 1/5, decrease $\sigma$
	- $\sigma(t + n) = \begin{cases} \sigma(t) \cdot k, & \text{if } \omega_e < \frac{1}{5} \\ \sigma(t) / k, & \text{if } \omega_e > \frac{1}{5} \end{cases}$
	- Choice of $k \approx 0.82$
- What is the simple $(1+1)$-ES algorithm with 1/5 rule?
	- $\textbf{Require:} \text{A constant } 0.817 \leq c \leq 1, \text{ a window } n \in \mathbb{Z}^+.$
$$
\begin{aligned}
& 1.\ t \gets 0 \\
& 2.\ p_s \gets 0 \quad \triangleright \text{ Probability of successful mutation} \\
& 3.\ \text{Initialize}(P(t)) \quad \triangleright \{ \mathbf{x}(0) \} \in \mathbb{R}^n, \, \mathbf{x} = (x_1, \dots, x_n) \\
& 4.\ \text{Evaluate}(P(t)) : \{ f(\mathbf{x}(0)) \} \\
& 5.\ \textbf{while} \ \text{Termination criterion not met \textbf{do}} \\
& 6.\ \quad P'(t) \gets \text{Mutate}(P(t)) \quad \triangleright x_i' = x_i + \sigma(t) \cdot \mathcal{N}_i(0, 1), \ \forall i \in \{ 1, \dots, n \} \\
& 7.\ \quad \text{Evaluate}(P'(t)) : \{ f(\mathbf{x}'(t)) \} \\
& 8.\ \quad P(t+1) \gets \text{Select}_{(1+1)}(P(t) \cup P'(t)) \\
& 9.\ \quad t \gets t + 1 \\
& 10.\ \quad p_s \gets \left( p_s + \mathbb{1}_{f(P(t)) > f(P(t-1))} \right) / (t \% (n + 1)) \quad \triangleright \text{Update \( p_s \)} \\
& 11.\ \quad \textbf{if} \ t \% n = 0 \ \textbf{then} \\
& 12.\ \qquad \sigma(t) =
\begin{cases}
\sigma(t - n) / c, & p_s \geq \frac{1}{5} \\
\sigma(t - n) \cdot c, & p_s < \frac{1}{5}
\end{cases} \\
& 13.\ \qquad p_s \to 0 \quad \triangleright \text{Reset \( p_s \) for the new \( \sigma(t) \)} \\
& 14.\ \quad \textbf{else} \\
& 15.\ \qquad \sigma(t) \gets \sigma(t - 1) \\
& 16.\ \quad \textbf{end if} \\
& 17.\ \textbf{end while}
\end{aligned}
$$
- What is the disadvantage of 1/5 rule for $(1+1)$-ES?
	- Certainly a more local search method
	- 1/5-success rule may fail

### Q and A

- Which statement(s) are characteristics of evolutionary algorithms?
	- Evolutionary algorithms require no fitness gradient information of any kind to proceed
	- Evolutionary algorithms are easy to process in parallel and can escape from local minima where deterministic optimisation methods may fail
- Regarding exploration and exploitation in EAs, which statement(s) is/are correct?
	- Crossover operators have the ability to jump out of a local optimum
	- Mutation operators can search for an optimum near the parent
- Two state-of-the-art discrete problems are OneMax ( 𝑓𝑂𝑀(𝒙) = ∑ 𝑥𝑖 𝑛 𝑖=1 ) and BinaryValue (𝑓𝐵𝑉(𝒙) = ∑ 2𝑛−𝑖𝑛 𝑖=1 𝑥𝑖). Which statement(s) is/are correct regarding solving these two problems by EAs?
	- 𝑓𝑂𝑀(𝒙) and 𝑓𝐵𝑉(𝒙) have the same difficulty to optimise, as only the Hamming distance to the optimum determines the quality of search
- Given a parent population size 𝜇 and an offspring population size 𝜆. Suppose one and only one individual is initialised as an optimum at the 0th generation, what is the number of generations needed for the optimum to fill the whole population? (Mutation and crossover are not considered) 
	- (𝜇, 𝜆)-selection needs ln 𝜆 ln 𝜆/𝜇 generations
	- Proportional selection needs 𝜆lnλ generations
- To analyse a (1+1) genetic algorithm (GA) on a 𝑛-dimensional OneMax ( 𝑓𝑂𝑀(𝒙) = ∑ 𝑥𝑖 𝑛 𝑖=1 ), we denote a 𝑘-step success probability 𝑝𝒙 +(𝑘) = 𝑃{𝑓𝑂𝑀(𝑚(𝒙)) = 𝑓𝑂𝑀(𝒙) + 𝑘}, 𝑚(𝒙) is the solution candidate obtained from applying mutation on 𝒙. Which formula can present the convergence velocity of the (1+1) GA? 
	- 𝜑 = ∑ 𝑘 ∙ 𝑝𝒙 +(𝑘)
- Which statement(s) is/are true about discrete and intermediary recombination? 
	- Both of them are conserving common components of parent individuals.
	- The offspring generated by global intermediary recombination are the same.
	- Recombination produces new individuals by combining the information contained in two or more parents.
- Regarding 1/5 rule in (1+1)-ES, which following statement(s) is/are correct? 
	- The step size should be increased/decreased if the success probability is bigger/smaller than 1/5.
	- The number 0.2 roughly equals the optimal success probability in corridor and sphere models
- Which statement(s) is/are correct about self-adapted mutations (single step-size mutation, individual mutation, correlated mutation) in ES?
	- Correlation matrices used in correlated mutation must be positive definite.
	- For a decision vector with 𝑛 variables, single step-size and individual mutations have 1 and 𝑛 parameters, respectively.
	- An individual mutation operator can work efficiently on problems of differently scaled object variables, while a single step-size mutation cannot.
- Why is log-normal distribution used to update step size in ES?
	- A log-normal distribution can guarantee that the updated step size is a positive number
	- A log-normal distribution can guarantee the same probability to increase and decrease a step size
- Compared with “+” selection in ES, what statement(s) is/are true for “,” selection?
	- A mis-adapted strategy parameter will be eliminated
	- A deterioration may occur
	- The offspring population size 𝜇 > 1 is necessary
- Suppose the formula ∫ 𝑧𝑃𝐷𝐹(𝑧)𝑑𝑧 𝐴 𝐵 represents a convergency velocity of ES, what is/are the correct lower and upper integral domain(s)? (Hint: 𝑧 represents progress)
	- For (1,1)-ES: 𝐴 = ∞, 𝐵 = −∞
	- For (1+1)-ES: 𝐴 = ∞, 𝐵 = 0
- What are the differences between GA and ES?
	- GA emphasises the crossover operator, while ES emphasises on mutation
	- GA uses discrete representations, and ES is capable of dealing with mixed-integer variables
- Between (𝜇 + 𝜆)-ES and (𝜇, 𝜆)-ES selections, which statement(s) is/are reasonable regarding a choice of 𝜇 and 𝜆?
	- In (𝜇 , 𝜆)-ES selection, 𝜆 > 𝜇
	- In (𝜇 + 𝜆)-ES selection, 𝜇 / 𝜆 = 1
- Why is a normal distribution used in ES for continuous problems? 
	- Because it can maximise the unbiasedness
	- Because of its infinite support
	- Because the total probabilities of increasing and decreasing a decision variable are the same
- Which of the following step-size control mechanism(s) in ES is/are capable of self-adaption? (𝒩(0,1) is a realisation of a standard normal distribution, 𝒰(0,1) is a realisation of a uniform distribution, 𝛼, 𝜏, 𝜏′, 𝑎 are learning rates)
	- 𝜎′ = 𝜎(1 + 𝛼𝒩(0,1))
	- 𝜎𝑖′ = 𝜎𝑖 exp(𝜏′ + 𝜏𝒩(0,1))