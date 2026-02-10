---
tags:
- note
aliases:
- Monte-Carlo Tree Search
title: monte-carlo tree search
description: ''
parent nodes:
- '[[monte carlo tree search]]'
published on: null
---

- [ ] What is Upper Confidence Bounds for Trees (UCT)?

---
- It is a [[202602020041 - heuristic|heuristic]] search algorithm for decision-making processes
- It builds a decision tree by iteratively sampling the search space through four phases to find optimal moves without exhaustive searching
	1. **Selection** 
		1. Starting at the root, the algorithm traverses the tree, selecting child nodes using a strategy that balances <mark style="background: #BBFABBA6;">exploration</mark> (trying new moves) and <mark style="background: #BBFABBA6;">exploitation</mark> (using known good moves)
	2. **Expansion** 
		1. Unless the node is terminal, one or more child nodes are added to the tree to expand it
	3. **Simulation (Rollout)** 
		1. A random, fast simulation is played out from the new node to estimate the potential value of that position
	4. **Backpropagation** 
		1. The simulation result (win/loss) is used to update the statistics (visits and scores) of the nodes traversed in the tree, moving back to the root
- **Balancing Act** 
	- MCTS manages the explore-exploit trade-off using methods like Upper Confidence Bounds for Trees (UCT)
- **Applications** 
	- Primarily used in complex, strategic, and turn-based games (e.g., AlphaGo)
- MCTS is particularly effective in scenarios where a heuristic evaluation function is difficult to define, as it relies on simulation results rather than static, pre-defined knowledge