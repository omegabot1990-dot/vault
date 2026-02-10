---
tags:
  - academic
  - ea
description: assignment one for EA
due date: 2024-11-20
start date: 2024-11-14
end date: 2024-12-24
status: Archive
importance level: important
urgency level: urgent
task type: distil
story points: 
parent nodes: 
child nodes: 
recurrent:
---

[[evolutionary_algorithms_practical_assignment.pdf]]

Consider the following items:
• Which version of GA did you choose to implement?
• Explain briefly how you performed hyperparameter tuning.
• Was the tuning effective, based on what you see from the tuning results?
• Anything else you would do in the assignment?


## Report

### Introduction

- Which version of GA did you choose to implement?
- Explain briefly how you performed hyperparameter tuning.
- Was the tuning effective, based on what you see from the tuning results?
- Anything else you would do in the assignment?

The assignment is divided into two parts: the first focuses on genetic algorithms, and the second on evolutionary strategies. In the former half, we are trying to solve the F18 (Low Autocorrelation Binary Sequence, or LABS) and F23 (N-Queens) problems from the *Pseudo-Boolean optimisation* (PBO) problem set. We aim to develop a genetic algorithm that works well for both problems, and we are constrained by an evaluation budget of 5,000 runs for each. However, we have a tuning budget of 5,000,000 to find the best hyperparameters that suit both problems simultaneously. As for the latter half, we are trying to solve the F23 (Katsuura) problem from the *Black-box Optimisation Benchmark* (BBOB) problem set. Here, we aim to develop an evolutionary strategy, and similar to the last case, we have an evaluation budget of 5,000 runs. 

The implementation of our GA involved standard bitwise mutation with a mutation rate $p_{m}=0.02$, uniform crossover with a crossover rate of $p_{c}=0.3$, and tournament selection. Due to budget limitations, our population was restricted to ten, although it is between fifty and two hundred in most moderate complexity cases. We decided to go with uniform crossover after we ruled out point crossover since we wanted to focus more on exploration. Our intuition was based on the results of getting stuck in local minima several times. We also experimented with roulette-wheel selection, but we decided on tournament selection as we noticed it selected better offspring for the problem.

The purpose of tuning was to optimise both the F18 and F23 problems simultaneously (multi-objective optimisation), but we were also faced with early stopping criteria (limited budget). We chose an exhaustive grid-based search that explores all combinations of hyperparameters in the defined space. We normalise the scores for each by averaging the scores for ten runs. We divide F18 by 5.5 (the optimal case we could find on hyperparameter tuning), and we only pick the cases for F23 whose score is 7 (optimal case of 7 queens); this gives us a score between 0 and 1 for both, then we try to find the hyperparameter combination that maximises this for both. We use a value of 5.5 instead of 8.16 (optimal case for $n=50$, for the F18 problem), since we wanted to balance the scales, the F23 problem had fitness scores above 0.5 after the normalised approach in most cases.

We are content with the mutation and crossover strategies. Still, we tried other selection strategies, like roulette-wheel (proportional) selection, which seemed to work well for one but not the other. We believe further exploration of selection strategies could yield better results. Also, other multi-optimisation strategies, like random search with guided refinement or something more complex like Bayesian optimisation, can be used to refine the hyperparameter space rather than search the already created one. 

---

We have chosen a standard selection technique for our GA: the roulette wheel selection. We wanted to select the individuals most fit for reproduction based on the proportional probability of their fitness scores. We decided to go with uniform crossover after we ruled out point crossover since we wanted to focus more on exploration. Our intuition was based on the results of getting stuck in local minima several times. We have used a standard bit-flip mutation as the mutation operator. 

To tune the hyperparameters, we use a grid-based search method, trying each combination of population size, mutation rate, and crossover rate. First, we populate arrays with standard values for the three. Our objective is to find a balance between the hyperparameters that works well for both problems. As we know the optimum values for both, we normalised the average score and proceeded with the grid search to find the best values.

• Was the tuning effective, based on what you see from the results?

We are content with the mutation and crossover strategies, but we tried other selection strategies, like tournament selection, and they seemed to work well for one but not the other. We believe further exploration of selection strategies could yield better results.

### Algorithms

- Outline your algorithms, algorithm parameters, and settings used for those parameters. 
- You can explain the implementation in various ways, as long as you make them clear and understandable. If you prefer to explain your algorithm in pseudo-code, you could find an example algorithm. Please ensure the algorithm and the results are reproducible from your description. Note that if we cannot get the same results using the codes you submit, the PA grade is 0 You can fix the random seed during your experiment and provide it to us so that we can avoid the different results caused by randomisation. 

---

We use the same algorithm for both problems F18 and F23. We use conditional statements to handle cases for initialisation as both have different $n$ values. We also have conditional termination criteria, as getting a fitness score of 7 means we can break the loop for the F23 problem. We use the same selection, crossover and mutation strategies for both.

### Hyper-parameter Tuning

- Describe the method and setting for the hyper-parameter tuning process.

Our aim was to find the optimal combination of hyperparameters for the PBO F18 and F23 problem sets. To this end, we first experimented with both problems individually and found values for population size, mutation rate, and crossover rate. The population size was limited to 30 at max because we had a limited budget. We tried standard mutation rates for both $n=50$ (F18) and $n=49$ (F23) problems by taking $\frac{1}{n}$ among others. We also wanted to have more exploratory capabilities, so we decided to go with a hyperparameter space with more crossover rates. After that, we followed the algorithm [] to do a grid-based search and find the best result that works for both problems.

### Experimental Results

- Description of the experiments and the results. Use the tables and figures generated from the IOHanalyzer. Make sure to present your results in a way that is convenient to the reader. Do not blindly include plots of all your experiments; try to combine information in figures and tables!

We had to optimise the F18 (LABS problem) with a dimension of 50 and F23 (N-Queens) problem) with a dimension of 49 from the PBO problem set for the first part. The GA is run 20 times independently on each and the average performance is found. The LABS problem is randomly initialised as a binary string with a length of 50. The N-Queens problem is initialised as a matrix of size 7x7 (binary vector) internally but is flattened to an integer array of 7 with integers 0 to 6 indicating the queens row in the column.
Although we could achieve an optimal solution of 7 for F23, we could only achieve an average value of 4.5 for F18, even when we ran the experiments exclusively on each other. On running the tuner, we were able to get a hyperparameter setting of $p_{c} = 0.3$, $p_{m} = 0.02$ and $\mu=10$ that gave us a fitness score of 4.39 for F18 and 4.9 for F23. For the N-Queens problem we also have an extra stopping criteria of $n=7$, since we find the optimal solution.

For the second task we had to design a Evolution Strategy on the F23 problem from BBOB suite (Katuura) with a dimension of 10. Here each solution is a real valued vector in $[-5, 5]^{10}$. We have choses a parent population size of $\mu=10$ and child population size of $\lambda=60$, where we follow $(\mu,\lambda)$-ES is used. We start by initialising each parent solution at random from $[-5, 5]$ uniformly for each dimension. The initial $\sigma$ (step-size) values are set to random values in the range $[0.04, 0.07]$. Here mutation is performed per-gene step-size adaptation, we also use discrete (gene-wise) recombination. Each offspring is created by selecting two parents at random and, for each gene, randomly choosing which parent to inherit from. After generating and mutating we evaluate all the offsprings and the best $\mu=10$ is selected for the new population, we ensure the population improves continuously this way. As for the F23 problem in the BBOB dataset we were able to get an average of 0.46.

F18 
ETV

The curve shows an increasing trend, indicating that the algorithm improves its best-so-far value as the number of function evaluations increases. The growth is gradual and smooth, suggesting that the genetic algorithm converges progressively toward better solutions.
EDCF
- The EDCF graph plateaus at 1, showing that a significant proportion of runs achieve similar target values. The sharp drop near specific target values indicates that certain thresholds are harder to achieve, reflecting the algorithm's performance constraints.
F23
ETV
- Similar to F18, the best-so-far value increases with more function evaluations, though the growth appears more uneven compared to F18. There is a steep increase toward the later stages, which may indicate delayed convergence or challenges in finding better solutions earlier.
EDCF
- The EDCF graph shows a more gradual decline compared to F18, suggesting variability in performance across different runs. The presence of smaller steps in the drop indicates that achieving higher target values is more difficult for F23 compared to F18.

F23 (BBOB)
The graph shows a clear decline in the best-so-far value over increasing function evaluations.
This indicates that the evolution strategy algorithm is minimising the target function (assuming a minimisation problem) over time.
The decline is steep initially, suggesting that the algorithm quickly improves the solution in the early stages, followed by slower improvement as evaluations increase.
Toward the right of the graph (at approximately 4×1044 \times 10^44×104 evaluations), the curve flattens out, indicating that the algorithm has likely converged or stagnated and is no longer finding better solutions.

The EDCF curve has a relatively sharp decline, showing that a large proportion of runs achieve similar target values.
The gradual steps in the decline suggest variability among runs, where some runs achieve slightly better results than others.
At the lower end of the target value axis, the graph plateaus, showing that few runs achieve the most optimal target value. This reflects the difficulty of the optimization problem or potential limitations of the evolution strategy algorithm.

### Discussions and Conclusions

- Summarize the results and conclude your report. If you would like to put the main conclusions discussions as lists in this part, you can see an example below.
1) We suggest using population size μ = x for the genetic algorithm to solve the problem.
2) The genetic algorithm benefits from small mutation rates in solving the NAS problem. (Just an example, this may not be the truth.)
3) We observe that the evolution strategy benefits from comma selection for solving the NAS problem. (Again, just an example).
- Tips: Please put the references in the file references.bib and cite them in the right line, like this 

### References



## Notes

Below is a comprehensive report summarizing the experimentation conducted in the provided code.

**1. Overview of the Experimentation Setup**

The primary objective of the code is to run a Genetic Algorithm (GA) on two distinct combinatorial optimization problems provided by the IOH profiler framework:

- **Problem F18** (LABS problem) with a dimension of 50.
- **Problem F23** (N-Queens problem) with a dimension of 49.

The GA is run for 20 independent trials (runs) on each problem. After all runs, the code outputs the average performance (i.e., the average best-found fitness values over the 20 runs for each problem).

**2. Algorithmic Components and Parameters**

- **Representation**:  
    For the LABS problem (F18), individuals are represented as binary strings of length 50. Each gene is a binary variable (0 or 1).  
    For the N-Queens problem (F23), individuals are represented as integer arrays of length 7, where each integer is a row-index of the queen in that particular column. Internally, the code uses a 7x7 identity matrix indexing trick (`np.eye(7, dtype=int)[parents[i]].flatten()`) to transform these indices into a 49-dimensional binary vector to evaluate the problem.
    
- **Population Initialization**:  
    For F18 (LABS), each individual in the population of size 10 is initialized randomly with 0/1 bits.  
    For F23 (N-Queens), each individual is initialized by choosing a placement for each of the 7 queens (an integer from 0 to 6 indicating the queen’s row in that column).
    
- **Population Size**:  
    The population size (`pop_size`) is fixed at 10.
    
- **Mutation Rate**:  
    A mutation rate (`mutation_rate`) of 0.02 is used.  
    For the LABS problem, mutation flips a bit (0 → 1 or 1 → 0) with probability 0.02 per gene.  
    For the N-Queens problem, mutation selects a position and sets it to a new random integer between 0 and 6 (representing a different row for the queen in that column) with probability 0.02 per gene.
    
- **Crossover Rate**:  
    The crossover rate (`crossover_rate`) is 0.3. With this probability, a pair of selected parents is recombined. The crossover operator is uniform, swapping each gene of the pair with a 50% chance.
    
- **Selection Methods**:  
    The code includes two selection methods:
    
    1. **Tournament Selection**: Used in the main loop to select parents for creating offspring. A tournament size of 5 is used. In each tournament, 5 individuals from the population are chosen randomly, and the one with the highest fitness is selected as a parent.
    2. **Roulette-Wheel Selection**: Defined in the code (as `mating_selection`), but it is commented out for the N-Queens run. The final code uses tournament selection (`tournament_selection`) in the actual runtime.
- **Stopping Criteria and Budget**:  
    The total evaluation budget is 5000 function evaluations per run. The algorithm stops either when the budget is reached or when a certain quality criterion is met. For the N-Queens problem, if a solution with fitness `≥ sqrt(n)` (in this case, `≥ 7` since `sqrt(49)=7`) is found, the run stops early. For the LABS problem, the code tries to maximize the fitness but does not have a special early termination criterion, other than the evaluation budget.
    

**3. Execution and Logging**

- **IOH Profiler Integration**:  
    The code integrates with IOH Profiler via `ioh.logger.Analyzer`, enabling detailed logging of performance data for subsequent analysis in IOHanalyzer.
    
- **Multiple Runs**:  
    Each problem (F18 and F23) is run 20 times independently. After each run, the problem is reset (`problem.reset()`) to ensure each run is independent of previous trials.
    
- **Fitness Recording**:  
    During each run, the best solution found so far (`f_opt`) and corresponding vector `x_opt` are tracked. After all 20 runs, the code prints the average best fitness values achieved across all runs for both F18 and F23.
    

**4. Expected Outcomes and Analysis**

- **F18 (LABS Problem)**:  
    The LABS problem is a bitstring problem where the GA attempts to find a configuration with a high fitness value. The final printout after 20 runs is `f18_score/20`, indicating the average performance. A higher score suggests better average solutions found.
    
- **F23 (N-Queens Problem)**:  
    The N-Queens problem as defined here is likely to be solved when a configuration is found that places 7 queens on a 7x7 chessboard without attacking each other. The code checks if `f_opt >= sqrt(n) = 7` to identify a perfect or near-perfect solution. If this occurs, the run can stop early. The final `f23_score/20` also reports the average performance of the GA. A value close to 7 would mean near-perfect solutions were found regularly.
    
- **Comparing and Reporting Results**:  
    After completion, the printed line `f"{f18_score/20} {f23_score/20}"` gives a quick comparison of the GA’s average effectiveness on both problems. The user can then analyze the raw data using IOHanalyzer if desired.
    

**5. Conclusion and Potential Improvements**

The experimentation as set up provides a baseline GA performance for two problems. The chosen parameters (population size=10, mutation_rate=0.02, crossover_rate=0.3) might not be optimal, but they serve as a reference point. Since results are logged, further analysis of convergence and performance can be done offline.

Potential improvements could include:

- Tuning the mutation and crossover rates.
- Trying alternative selection strategies or mixing crossover operators.
- Adjusting population size or using adaptive mutation.
- Running more evaluations or analyzing the effect of early stopping criteria.

**6. Summary**

In summary, the experimentation involves running a basic GA on two test problems (LABS and N-Queens), each for 20 runs, recording performance, and printing average outcomes. The chosen parameters and operators provide a classical GA setup, and the outputs allow a basic assessment of the GA’s effectiveness under the given configurations.


Below is a comprehensive and detailed report summarizing the experimentation conducted in the provided code.

---

**1. Goal of the Experiment**

The experiment is designed to apply an Evolution Strategy (ES) on a test problem from the BBOB suite, specifically problem F23, with a dimension of 10. The objective is to observe the ES’s performance over multiple independent runs and gather statistics about its effectiveness. After running the ES for 20 independent runs, the code computes and reports average performance metrics.

---

**2. Algorithmic Details**

- **Evolution Strategy (ES) Setup**:  
    The code implements a standard ES with the following characteristics:
    
    - **Representation**: Each solution is a real-valued vector in [−5,5]10[-5, 5]^{10}[−5,5]10.
        
    - **Population Size and Offspring Generation**: A (μ,λ)(\mu,\lambda)(μ,λ)-ES is used:
        
        - Parent population size: μ=10\mu = 10μ=10
        - Offspring population size: λ=60\lambda = 60λ=60
    - **Strategy Parameters**: Each individual maintains a vector of mutation step-sizes (σ\sigmaσ-values) for each gene.
        
    - **Initialization**:
        
        - The parent solutions are initialized uniformly at random within the range [−5,5][-5,5][−5,5] for each dimension.
        - The initial σ\sigmaσ-values (step-sizes) are set to random values in the range [0.04, 0.07].
    - **Mutation**: Mutation is performed using the standard ES approach with per-gene step-size adaptation:
        
        σi,j←σi,jexp⁡(τ′N0+τN(0,1)) \sigma_{i,j} \leftarrow \sigma_{i,j} \exp(\tau' N_0 + \tau N(0,1))σi,j​←σi,j​exp(τ′N0​+τN(0,1)) xi,j←xi,j+N(0,σi,j) x_{i,j} \leftarrow x_{i,j} + N(0,\sigma_{i,j})xi,j​←xi,j​+N(0,σi,j​)
        
        where N0∼N(0,1)N_0 \sim \mathcal{N}(0,1)N0​∼N(0,1) is a global Gaussian variable sampled once per generation, and N(0,1)N(0,1)N(0,1) is a locally sampled Gaussian. The parameters τ′\tau'τ′ and τ\tauτ are set according to standard ES rules:
        
        - τ=12n\tau = \frac{1}{\sqrt{2\sqrt{n}}}τ=2n​​1​
        - τ′=12n\tau' = \frac{1}{\sqrt{2n}}τ′=2n​1​ where n=10n=10n=10 is the dimension.
        
        After mutation, each gene is clipped to remain within the [-5,5] bounds.
        
    - **Recombination**: Discrete (gene-wise) recombination is employed. Each offspring is created by selecting two parents at random and, for each gene, randomly choosing which parent to inherit from. Similarly, the corresponding σ\sigmaσ-value is chosen from the same parent.
        
    - **Selection**: After generating and mutating λ=60\lambda=60λ=60 offspring, all offspring are evaluated, and the best μ=10\mu=10μ=10 are selected to form the new parent population. This is a (μ,λ)(\mu,\lambda)(μ,λ)-selection scheme, ensuring the population continuously improves or maintains the best found solutions.
        

---

**3. Problem and Objectives**

- **Problem**:  
    The problem chosen is F23 from the BBOB test suite, with dimension 10. BBOB problems are well-known, continuous benchmark functions commonly used for testing the performance of optimization algorithms.
    
- **Evaluation Budget**:  
    The code sets a budget of B=50000B = 50000B=50000 function evaluations. The run continues until this budget is exhausted or until a user-defined optimum criterion is met.
    
- **Optimality Criterion**: The code tracks the best fitness found so far (foptf_{\text{opt}}fopt​) and compares it with a known optimum (set as `optimum = 0` in the code). If the algorithm finds a solution with a fitness equal to or better than the known optimum, it can terminate early.
    

---

**4. Experimental Protocol**

- **Number of Runs**:  
    The algorithm is run independently 20 times on F23. Independent runs mean the optimization process restarts from scratch each time, re-initializing the population and strategy parameters and resetting the problem’s internal state.
    
- **Logging and Output**:
    
    - Each run prints the best fitness value found at termination.
    - After completing all 20 runs, the code calculates and prints an average metric: it subtracts a reference value (6.87, presumably a known baseline or shift) from each final solution’s fitness, sums these values, and then computes the average. This gives a measure of performance relative to a baseline.
    
    The code is also integrated with IOH Profiler’s logging framework (`ioh.logger.Analyzer`), which allows detailed recording of the performance trajectories for subsequent analysis in IOHanalyzer. All data is stored in a folder ("data/run"), which can be analyzed offline to investigate performance curves, speed of convergence, and other metrics.
    

---

**5. Expected Results and Interpretation**

- **Fitness Performance**:  
    As a continuous optimization problem, F23 may be challenging. The ES attempts to minimize the function. The reported final fitness values after each run indicate how close the algorithm got to the global optimum (0.0, as indicated by `optimum = 0`).
    
- **Average Results**: By running the algorithm 20 times, we can assess:
    
    1. **Convergence Consistency**: How much the final results vary run-to-run. High variance suggests the algorithm struggles to find good solutions reliably.
    2. **Mean Performance**: The final printed "Average" line provides a single aggregate statistic of performance relative to 6.87. If this average is negative and large in magnitude, it means the algorithm consistently found solutions better than 6.87. If it’s close to zero or positive, it means performance is around or worse than that baseline.
- **Budget Constraints**: With a large budget (50,000 evaluations), the ES should have enough opportunity to improve solutions. If convergence is slow or gets stuck, the algorithm may not significantly improve beyond a certain point.
    

**Potential Adjustments & Future Work**:

- Adjusting μ\muμ and λ\lambdaλ can affect exploration-exploitation balance.
- Experimenting with different recombination schemes (e.g., intermediate recombination) or using weighted recombination based on fitness.
- Tuning the step-size adaptation parameters, or implementing alternative adaptation strategies (like CMA-ES).
- Using multiple runs with different random seeds provides a robust statistical assessment. Additional runs or statistical tests (like a Mann-Whitney U test or Wilcoxon signed-rank test) could be performed to compare different strategies or parameter settings.

---

**6. Summary**

In this experiment, a standard (μ,λ)(\mu,\lambda)(μ,λ)-ES with dimension n=10n=10n=10 is applied to BBOB function F23. The code runs 20 independent trials, each up to a budget of 50,000 evaluations, storing performance data for post-hoc analysis. The results output both individual run performances and an overall average performance measure relative to a baseline. Such experimentation provides insights into the ES’s robustness, reliability, and effectiveness on a complex continuous optimization landscape.

The integrated IOH profiler logging ensures that full performance data can be analyzed later to understand convergence rates, compare different algorithmic variants, and guide future improvements in the algorithm’s design and parameterization.