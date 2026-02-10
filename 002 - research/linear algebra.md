---
tags:
  - moc

description: ''
parent nodes:
  - '[[math]]'
---

# linear algebra

## Key concepts (simplest → hardest)

### Objects + notation

- [ ] Scalar
- [ ] Vector (row vs column)
- [ ] Matrix
- [ ] Tensor (order/axes)
- [ ] Shape, indexing, slicing

### Basic operations (elementwise)

- [ ] Addition / subtraction
- [ ] Scalar multiplication
- [ ] Elementwise multiplication
	- [ ] Hadamard / elementwise product
- [ ] Transpose
- [ ] Symmetric matrix

### Reduction + aggregation

- [ ] Sum over all elements
- [ ] Sum over an axis
- [ ] Mean / average
- [ ] keepdims / non-reduction sum
- [ ] Cumulative sum

### Products

- [ ] Dot product / inner product
- [ ] Matrix–vector product
- [ ] Matrix–matrix multiplication

### Norms + distance

- [ ] Vector norms: ℓ1, ℓ2, ℓp
- [ ] Matrix norms: Frobenius norm
- [ ] Spectral norm (conceptual)

### Geometry of vectors

- [ ] Vectors as points vs directions
- [ ] Vector addition/subtraction (geometric)
- [ ] Dot product ↔ angle
- [ ] Orthogonality
- [ ] Cosine similarity

### Hyperplanes + linear models

- [ ] Hyperplane as decision boundary
- [ ] Half-spaces (>, < constraints)

### Linear transformations (matrices)

- [ ] Matrix as linear transformation
- [ ] Basis vectors and how a matrix acts on a basis
- [ ] Rotation / scaling / shear intuition

### Linear dependence + rank

- [ ] Linear combination
- [ ] Linear independence / dependence
- [ ] Column space intuition
- [ ] Rank

### Invertibility + solving systems

- [ ] Identity matrix
- [ ] Inverse matrix
- [ ] When an inverse exists (full rank)
- [ ] Numerical issues with inversion (stability)

### Determinant

- [ ] Determinant as area/volume scaling
- [ ] Determinant zero ↔ singular (non-invertible)

### Tensor contractions + Einstein notation

- [ ] Tensor contraction (generalized matrix multiplication)
- [ ] Einstein summation notation
- [ ] `einsum` as a unifying view of dot/matmul/trace

### Eigendecomposition

- [ ] Eigenvector / eigenvalue definition: Av = λv
- [ ] Characteristic equation: det(A − λI) = 0
- [ ] Eigendecomposition: A = W Σ W⁻¹ (when possible)
- [ ] Symmetric matrices: A = W Σ Wᵀ (orthogonal eigenvectors)
- [ ] Relationship to determinant (product of eigenvalues)
- [ ] Relationship to rank (nonzero eigenvalues)

### Eigenvalue intuition + tools

- [ ] Power iteration (principal eigenvector intuition)
- [ ] Gershgorin circle theorem (bounds/approximation)

## Resources

- [ ] [D2L — Linear Algebra (scalars → norms)](https://d2l.ai/chapter_preliminaries/linear-algebra.html)
- [ ] [D2L — Geometry & linear algebraic operations (angles, hyperplanes, rank, det, einsum)](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/geometry-linear-algebraic-ops.html)
- [ ] [D2L — Eigendecompositions](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/eigendecomposition.html)

- [ ] [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [ ] [MIT 18.06 Linear Algebra (Strang)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
