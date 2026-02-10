---
tags:
  - academic
aliases:
  - linear algebra
title: linear algebra
description: fundamentals of linear algebra
parent nodes:
  - "[[mathematics]]"
child nodes:
---

## Key Concepts

#### What is a *vector*?
A *vector* is a representation of a quantity which has both magnitude (size) and direction.
A *vector* can be represented as an ordered array of numbers called *components*.
For example, in a 2-dimensional space, a vector can be represented as shown below. Here $x$ and $y$ are the magnitudes of the x-axis (horizontal direction) and y-axis (vertical direction), respectively.
$$ 
\vec v = (x, y) 
$$
#### What is a *matrix*?
A *matrix* is a representation of a vector.
A $n \times m$ matrix has $n$ rows and $m$ columns. 
#### What is a *coordinate system*?
A coordinate system is a way to translate between vectors and sets of numbers.
#### What is a *scalar*?
A *scalar* is a real number that scales the magnitude of the vector without changing its direction. 
$$ 
c \times \vec v = c\vec v 
$$
$$
c \times 
\begin{bmatrix} x \\
y
\end{bmatrix} 
= 
\begin{bmatrix} cx  \\
cy
\end{bmatrix} 
$$
#### How does *vector addition* work?
Given,
$$ 
\vec v_1  = 
\begin{bmatrix} x_1  \\
y_1
\end{bmatrix} \hspace{0.5cm} and \hspace{0.5cm} 
\vec v_2  = 
\begin{bmatrix} x_2  \\
y_2
\end{bmatrix} 
$$
$$ 
\vec v_1 \pm \vec v_2  = 
\begin{bmatrix} x_1 \pm x_2  \\
y_1 \pm y_2 
\end{bmatrix} 
$$
#### What are *basis vectors*?
The *basis vectors* are unit vectors in each direction of a co-ordinate system.
For example, in a 2-dimensional system the *basis vectors* would be as shown below,
$$ 
\hat{i} , \hspace{0.5cm} \hat{j} 
$$
#### What is *basis* of a vector space?
The *basis* of a vector space is a set of *linearly independent* vectors that *span* the entire space.
#### What is *linear combination* of two vectors?
Given, 
$$ 
\vec v \hspace{0.5cm} and \hspace{0.5cm} \vec w 
$$
$$ 
a\vec v \pm b\vec w 
$$
#### What is *span* of two vectors?
The *span* of two vectors is the set all linear combinations of the given vectors.
The *span* of most 2-dimensional vectors is the entire sheet of 2-dimensional space unless they are both in the same/opposite direction (they line up).
#### What does *linearly dependent* mean?
A vector which lies in the span of other vectors, i.e. a vector which can be represented as the sum of the other vectors is said to be *linearly dependent* to the other vectors.
$$ 
\vec u = a\vec v + b\vec w 
$$
#### What does *linearly independent* mean?
A vector which adds another dimension to the span is said to be *linearly independent* of the other vectors.
$$ 
\vec u \neq a\vec v + b\vec w 
$$
$$ 
a\vec v + b\vec w + c\vec u = 0, \hspace{0.5cm} 
a = b = c = 0 
$$
#### What is a *linear transformation*?
A *linear transformation* is a function that a) keeps all lines as lines b) keeps the origin the same, i.e. the grid lines of the co-ordinate system will remain parallel and evenly spaced.
$$ 
\vec v = a\hat i + b\hat j 
$$
$$ 
Tranformed (\vec v) = aTrasformed(\hat i) + bTransformed(\hat j) 
$$
$$ 
Tranformed (\hat i) = 
\begin{bmatrix} a  \\
c
\end{bmatrix} \hspace{0.5cm} and \hspace{0.5cm} Tranformed (\hat j) = 
\begin{bmatrix} b  \\
d
\end{bmatrix}
$$
$$ 
\begin{bmatrix} a & b  \\
c & d
\end{bmatrix} 
\begin{bmatrix} x  \\
y
\end{bmatrix} = x 
\begin{bmatrix} a  \\
c
\end{bmatrix} + y 
\begin{bmatrix} b  \\
d
\end{bmatrix} = 
\begin{bmatrix} ax & by  \\
cx & dy
\end{bmatrix} 
$$
A transformation $L$ is linear if it satisfies the following, 
1. **Additivity**
$$ 
L(\vec u + \vec v) = L(\vec u) + L (\vec v) 
$$
2. **Scaling** 
$$ 
L(c\vec u) = cL(\vec u) 
$$
#### What is *matrix multiplication*?
$$ 
\begin{bmatrix} a & b  \\
c & d
\end{bmatrix} 
\begin{bmatrix} u & v  \\
w & x
\end{bmatrix} = 
\begin{bmatrix} au + bw & av + bx  \\
cu + dw & cv + dx
\end{bmatrix} 
$$
$$ 
M_1 \times M_2 \neq M_2 \times M_1 
$$
Matrix multiplication is **Associative**,
$$ 
A(BC) = (AB)C 
$$
#### What is *determinant* of a matrix?
The factor by which a linear transformation scales any area is called its *determinant*.
If the *determinant* is negative then that means there is an inversion of orientation of space.
$$ det(
\begin{bmatrix} a & b  \\
c & d
\end{bmatrix}
) = ad - bc 
$$
$$ 
det(
\begin{bmatrix} a & b & c  \\
d & e & f  \\
g & h & i
\end{bmatrix}
) = a \times det(
\begin{bmatrix} e & f  \\
h & i
\end{bmatrix}
) - b \times det(
\begin{bmatrix} d & f  \\
g & i
\end{bmatrix}
) + c \times det(
\begin{bmatrix} d & e \\
g & h
\end{bmatrix}
) 
$$
$$ 
det(M_1 \times M_2) = det(M_1) \times det(M_2) 
$$
#### What is a *linear system of equations*?
Given, $A$ is the **Constant Matrix**
$$
\begin{align}
a_{1}x + b_{1}y + c_{1}z = v_{1} \\
a_{2}x + b_{2}y + c_{2}z = v_{2} \\
a_{3}x + b_{3}y + c_{3}z = v_{3} \\
\end{align}
$$
$$
A = 
\begin{bmatrix}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{bmatrix}
\hspace{0.5cm} and \hspace{0.5cm}
\vec{x} = 
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$
$$
A \vec{x} = 
\begin{bmatrix}
v_{1} \\
v_{2} \\
v_{3}
\end{bmatrix}
$$
#### What is *identity matrix*?
A matrix with ones on its diagonal and zeros elsewhere is called an *identity matrix* ($I$). 
  For example,
$$
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
, \hspace{0.5cm} 2 \times 2 \hspace{0.5cm} matrix
$$
$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
, \hspace{0.5cm} 3 \times 3 \hspace{0.5cm} matrix
$$
#### How to solve a linear system of equations for non-zero determinant?
==If $det(A) \neq 0$, then and only then does $A^{-1}$ exists.==
Given, 
$$
\begin{align}
A  \vec{x} = \vec{v}, \\
A^{-1} A \vec{x} = A^{-1} \vec{v} \\
\vec{x} = A^{-1} \vec{v}
\end{align}
$$
#### What is *inverse transformation*?
An *inverse transformation* is a function or operation that reverses the effect of another function or operation.
$$
AA^{-1}=I
$$
#### What is the *rank* of a transformation?
The number of dimensions of the output of a transformation is called its *rank*.
For a n-dimensional transformation, if the rank is n, then it is called a *full rank* transformation.
#### What is the *column space* or *column span* of a matrix?
The set of all possible outputs (of a transformation) for a given matrix is called the *column space* or *column span* of the matrix. i.e. The *column space* is the span of the columns of your matrix.
Zero **vector** is always included in the *column space*.
To be exact, **rank** would be the number of dimensions in the *column space*.
#### What is *null space* or *kernel* of the matrix?
The set of vectors that land on the origin for a non full rank transformation is called the *null space* or *kernel*.
==For a full rank transformation, the only vector that lands at the origin is the zero vector itself.==
For a linear system of equations, where the solution is a zero vector as shown below, the *null space* will give all the possible solutions to that system.
$$
A \vec{x} = 
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$
#### What is a *dot product* or *scalar product* or *inner product*?
The *dot product* is an operation that takes two equal length sequence of numbers and returns a single number. 
$$
\begin{bmatrix}
x_{1} \\
y_{1}
\end{bmatrix} 
\cdot
\begin{bmatrix}
x_{2} \\
y_{2}
\end{bmatrix}
= x_{1} x_{2} + y_{1} y_{2}
$$
$$
\vec{a} \cdot \vec{b} = a_{1}b_{1} + a_{2}b_{2} + \dots + a_{n}b_n
$$
$$
\vec{a} \cdot \vec{b} = a_{1}b_{1} + a_{2}b_{2} + \dots + a_{n}b_n
$$

When two vectors are,
  1. In the same direction then *dot product* is positive
  2. In the opposite direction then *dot product* is negative
  3. In perpendicular direction then 0

Geometrically, if $\theta$ is the angle between two vectors $\vec a$ and $\vec b$, where $\begin{Vmatrix}a\end{Vmatrix}$ and $\begin{Vmatrix}b\end{Vmatrix}$ are the magnitudes of the vectors $\vec a$ and $\vec b$, then the dot product is given by,  
$$
\vec{a} \cdot \vec{b} = 
\begin{Vmatrix}
a
\end{Vmatrix}
\begin{Vmatrix}
b
\end{Vmatrix}
\cos{\theta}
$$
Properties of *dot product* are as follows,
1. **Commutative**
$$
\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}
$$
2. **Distributive under addition**
$$
\vec{a} \cdot (\vec{b} + \vec{c}) = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}
$$
3. **Bilinear**
$$
c (\vec{a} \cdot \vec{b}) = (c \vec{a}) \cdot \vec{b} = \vec{a} \cdot (c \vec{b})
$$
  4. **Orthogonal**
     Two vectors are said to be orthogonal (i.e. the angle between them in 90$\degree$), if and only if their dot product is zero.
  
#### What is *cross product* or *vector product*?
The *cross product* is a binary operation on two vectors in a three-dimensional space and it results in another vector that lies perpendicular to the plane containing the original vectors.
The direction of the resultant vector is determined by the right hand rule.
Given, 
$$
\vec{a} = 
\begin{bmatrix}
a_{1} \\
a_{2} \\
a_{3}
\end{bmatrix}
and \hspace{0.5cm} \vec{b} =
\begin{bmatrix}
b_{1} \\
b_{2} \\
b_{3}
\end{bmatrix}
$$
$$
\vec{a} \times \vec{b} = 
\begin{bmatrix}
a_{2}b_{3} - a_{3}b_{2} \\
-(a_{1}b_{3} - a_{3}b_{1}) \\
a_{1}b_{2} - a_{2}b_{1}
\end{bmatrix}
$$
$$
\begin{bmatrix}
v_{1} \\
v_{2} \\
v_{3}
\end{bmatrix}
\times
\begin{bmatrix}
w_{1} \\
w_{2} \\
w_{3}
\end{bmatrix}
= \det(
\begin{bmatrix}
\hat{i} & v_{1} & w_{1} \\
\hat{j} & v_{2} & w_{2} \\
\hat{k} & v_{3} & w_{3}
\end{bmatrix}
)
$$
$$
= \hat{i}(v_{2}w_{3} - v_{3}w_{2}) + \hat{j}(v_{3}w_{1} - v_{1}w_{3}) +\hat{k}(v_{1}w_{2} - v_{2}w_{1})
$$
Geometrically, the magnitude of the *cross product* between two vectors $\vec a$ and $\vec b$, i.e. $\begin{Vmatrix} {\vec{a} \times \vec{b}} \end{Vmatrix}$ is the area of the parallelogram formed by $\vec{a}$ and $\vec{b}$ ($\det(\begin{bmatrix}a_{1} & b_{1} \\ a_{2} & b_{2}\end{bmatrix})$) and its direction is ascertained by the right hand thumb rule when curling from $\vec{a}$ to $\vec{b}$.

Properties of *dot product* are as follows,
1. **Anti-commutativity**
$$
\vec{a} \times \vec{b} = - \vec{b} \times \vec{a}
$$
2. **Distributive under addition**
$$
\vec{a} \times (\vec{b} + \vec{c}) = \vec{a} \times \vec{b} + \vec{a} \times \vec{c}
$$
3. **Bilinear**
$$
c (\vec{a} \times \vec{b}) = (c \vec{a}) \times \vec{b} = \vec{a} \times (c \vec{b})
$$
4. **Zero if parallel**
	   If the two vectors are parallel or if one of the vectors is zero vector then the *cross product* is also zero vector.
#### What is a *dual vector*?
A *dual vector* is a linear functional form of a vector to its field of scalars.
#### What is *Cramer's Rule*?
*Cramer's Rule* is a theorem used to solve a system of linear equations with as many equations as unknowns, provided the system has a unique solution.
It makes use of determinants and is useful in the case of small systems.
$$
AX = B
$$
Where,
- $A$ is a $n \times n$ square matrix of coefficients 
- $X$ is a column vector of variables $[x_{1}, x_{2}, \dots, x_{n}]^T$
- $B$ is a column vector of constants $[b_{1}, b_{2}, \dots, b_{n}]^T$
- $\det (A) \neq 0$, i.e. the vector $A$ is invertible

To find the solution of each variable $x_{i}$, replace the i-th column of matrix $A$ with the column vector $B$, forming the the new vector $A_{i}$. Then
$$
x_{i} = \frac{\det(A_{i})}{\det(A)}
$$
For example,
$$
A = 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
, \hspace{0.5cm} X = 
\begin{bmatrix}
x_{1} \\
x_{2}
\end{bmatrix}
, \hspace{0.5cm} B =
\begin{bmatrix}
b_{1} \\
b_{2}
\end{bmatrix}
$$
$$
A_{1} = 
\begin{bmatrix}
b_{1} & a_{12} \\
b_{2} & a_{22}
\end{bmatrix} 
\hspace{0.5cm} and \hspace{0.5cm} A_{2} =
\begin{bmatrix}
a_{11} & b_{1} \\
a_{21} & b_{2}
\end{bmatrix}
$$
 $$
x_{1} = \frac{\det A_{1}}{\det A}, \hspace{0.5cm}
x_{2} = \frac{\det A_{2}}{\det A}
$$
#### How to change the basis?
$$
A^{-1}MA \vec{v}
$$


---
%% 
(resources:: Resources - 202407152046)
%%
> [!info] 2024-07-15
> > [!example] **Resources:**
> > - [3 Blue and 1 Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

