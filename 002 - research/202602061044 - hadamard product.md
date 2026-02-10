---
tags:
- math
aliases:
- Hadamard product
title: hadamard product
description: ''
parent nodes:
- '[[math]]'
published on: null
---

- The **Hadamard product** (also known as the <mark style="background: #BBFABBA6;">element-wise</mark> product) is an operation that takes two matrices of the <mark style="background: #BBFABBA6;">same dimensions</mark> and produces another matrix of the same dimensions
- For two matrices $A$ and $B$ of size $m \times n$, the Hadamard product $A \circ B$ is defined as:

> [!MATH] Hadamard Product
> $$(A \circ B)_{ij} = (A)_{ij}(B)_{ij}$$
> 
> #### Example ($2 \times 2$)
> $$
> \begin{bmatrix}
> a_{11} & a_{12} \\
> a_{21} & a_{22}
> \end{bmatrix}
> \circ
> \begin{bmatrix}
> b_{11} & b_{12} \\
> b_{21} & b_{22}
> \end{bmatrix}
> =
> \begin{bmatrix}
> a_{11}b_{11} & a_{12}b_{12} \\
> a_{21}b_{21} & a_{22}b_{22}
> \end{bmatrix}
> $$

- Key Properties
	* Commutative
		* $A \circ B = B \circ A$
	* Associative
		* $A \circ (B \circ C) = (A \circ B) \circ C$
	* Distributive
		* $A \circ (B + C) = A \circ B + A \circ C$
	* Identity
		* The identity is a matrix $J$ where all entries are $1$
