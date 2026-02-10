---
tags:
  - idl
  - academic
aliases:
  - understanding deep learning
title: understanding deep learning - notes
description: notes for understanding deep learning book
parent nodes:
  - "[[introduction to deep learning]]"
child nodes:
---


## Cues

#### Chapter 1

1. What is the *temporal credit assignment* problem?
   In reinforcement learning, the reward may occur some time after the action is taken, so associating the reward with the action may not be straightforward.

#### Chapter 2

1. What is *structured* or *tabular* data?
   Data of a predetermined or fixed size of which the elements are always ordered similarly.

#### Chapter 3

1. With the ReLU activation function, what is the nature of the output?
   $D$ hidden units have, at most $D$ joints and so is a piecewise linear function with at most $D+ 1$ linear regions.
2. How many linear regions can a model with $D_{i}$ dimensions and $D_{i}$ hidden units divide the input space with $D_{i}$ hyperplanes?
   $2^{D_{i}}$ linear regions
3. What is *dying ReLU* problem?
   The ReLU function has the disadvantage that its derivative is zero for negative inputs. If all the training examples produce negative inputs to a given ReLU function, then we cannot improve the parameters feeding into this ReLU during training. The gradient with respect to the incoming weights is locally flat, so we cannot “walk downhill.” This is known as the dying ReLU problem.



## Notes

#### Chapter 1

- Machine learning can be coarsely divided into,
	1. Supervised learning
	2. Unsupervised learning
	3. Reinforcement learning
- *Regression* problems have a continuous output rather than a *Classification* problem that deals with category assignment
	1. *Multivariate regression* predicts more than one number
	2. *Multi-class classification* predicts more than one category
		1. The model returns a vector of size $N$ containing the probabilities of $N$ categories
- AI and Ethics
	1. Bias and fairness
	2. Explainability
	3. Weaponising AI
	4. Concentrating power 
	5. Existential risk

#### Chapter 2

- Supervised Learning
   We need a model $f[\bullet]$, which takes input $x$ and returns $y$, i.e. $y=f[x]$.
   Computing prediction $y$ from the input $x$ is called *inference*.
   The model also contains *parameters* $\phi$, which determines the relationship between input and output.
   $$
   y=f[x, \phi]
   $$
   *Learning* or *training* a model is attempting to find parameter $\phi$ that make sensible output predictions from the input. We learn these parameters using a training dataset off $I$ pairs of input and output examples $\{x_{i}, y_{i}\}$.
   We quantify the degree of mismatch with the *loss* $L$, this is a scalar value that summarises how poorly the model predicts the training outputs from their corresponding inputs for parameters $\phi$.
   We can treat the loss as a function $L[\phi]$ of these parameters. When we train the model, we are seeking parameters $\hat{\phi}$ that minimise this loss function:
   $$
   \hat{\phi} = \underset{\phi}{argmin}[L[\phi]]
   $$
- 1D Linear Regression
   A 1D linear regression model describes the relationship between input x and output y  as a straight line:
   $$
   \begin{align}
y = f[x, \phi] \\
= \phi_{0} + \phi_{1}x
\end{align}
   $$
   This model has two parameters $\phi=[\phi_{0},\phi_{1}]^T$ , where $\phi_{0}$ is the y-intercept of the line and $\phi_{1}$ is the slope.
   The *loss* is the mismatch captured by the deviation between the model predictions $f[x_{i}, \phi]$ (height of the line at xi) and the ground truth outputs $y_{i}$. We quantify the total mismatch, *training error* or *loss* as the sum of the squares of these deviations for all $I$ training pairs.
   $$
   \begin{align}
L[\phi] = \sum_{i=1}^{I}(f[x_{i}, \phi] - y_{i})^2 \\
= \sum_{i=1}^{I}(\phi_{0} + \phi_{1}x_{i} - y_{i})^2
\end{align}
   $$
   Since the best parameters minimise this expression, we call this a least-squares loss.
   $L[\phi]$ is the *loss* function or the *cost* function. The goal is to find the parameters $\hat{\phi}$ that minimises this quantity:
   $$
   \begin{align}
\hat{\phi} = \underset{\phi}{argmin}[L[\phi]] \\
= \underset{\phi}{argmin}[\sum_{i=1}^{I}(f[x_{i}, \phi] - y_{i})^2] \\
= \underset{\phi}{argmin}[\sum_{i=1}^{I}(\phi_{0} + \phi_{1}x_{i} - y_{i})^2]
\end{align}
   $$

#### Chapter 3

- Shallow Neural Network
   Example with three hidden units: The function $f[x]$ maps a scalar input $x$ to a scalar output $y$ and has ten parameters $\phi = \{\phi_{0}, \phi_{1}, \phi_{2}, \phi_{3}, \theta_{10}, \theta_{11}, \theta_{20}, \theta_{21}, \theta_{30}, \theta_{31}\}$ :
   $$
   \begin{align}
y = f[x, \phi] \\
= \phi_{0} + \phi_{1}a[\theta_{10} + \theta_{11}x] + \phi_{2}a[\theta_{20} + \theta_{21}x] + \phi_{3}a[\theta_{30} + \theta_{31}x]
\end{align}
   $$
   The hidden units are $h_{1}$, $h_{2}$ and $h_{3}$.
   $$
   \begin{align}
h_{1} = a[\theta_{10} + \theta_{11}x] \\
h_{2} = a[\theta_{20} + \theta_{21}x] \\
h_{3} = a[\theta_{30} + \theta_{31}x]
\end{align}
   $$
   So,
   $$
   y = \phi_{0} + \phi_{1}h_{1} + \phi_{2}h_{2} + \phi_{3}h_{3}
   $$
   Generalised: Case with $D$ hidden units,
   $$
   \begin{align}
h_{d} = a[\theta_{d0} + \theta_{d1}x] \\
y = \phi_{1} + \sum_{d=1}^D\phi_{d}h_{d}
\end{align}
   $$
   General equation for a shallow neural network $y=f[x, \phi$] that maps a multi-dimensional input $x \in \mathbb{R}^{D_{i}}$ to a multi-dimensional output $y \in \mathbb{R}^{D_{o}}$ using $h \in \mathbb{R}^D$ hidden units:
   $$
   \begin{align}
h_{d} = a \left[ \theta_{d0} + \sum_{i=1}^{D_{i}}\theta_{di}x_{i} \right] \\
y_{j} = \phi_{j0} + \sum_{i=1}^{D_{i}}\theta_{jd}h_{d}
\end{align}
   $$
- Rectified Linear Unit (ReLU)
   $$
   a[z] = ReLU[z] = 
   \begin{cases}
0, z<0 \\
z, z\geq 0
\end{cases}
   $$

#### Chapter 4

* Deep Neural Network
  Example: Deep neural network with two hidden layers:
  $$
  \begin{align}
\begin{bmatrix}
h_{1}  \\
h_{2} \\
h_{3}
\end{bmatrix} = a\begin{bmatrix}
\begin{bmatrix}
\theta_{10} \\
\theta_{20} \\
\theta_{30}
\end{bmatrix} + \begin{bmatrix}
\theta_{11} \\
\theta_{12} \\
\theta_{13}
\end{bmatrix}x
\end{bmatrix}, \\
\begin{bmatrix}
h_{1}'  \\
h_{2}' \\
h_{3}'
\end{bmatrix} = a\begin{bmatrix}
\begin{bmatrix}
\psi_{10} \\
\psi_{20} \\
\psi_{30}
\end{bmatrix} + \begin{bmatrix}
\psi_{11} && \psi_{12} && \psi_{13} \\
\psi_{21} && \psi_{22} && \psi_{23} \\
\psi_{31} && \psi_{32} && \psi_{33} \\
\end{bmatrix}\begin{bmatrix}
h_{1} \\
h_{2} \\
h_{3}
\end{bmatrix}
\end{bmatrix}, \\
y' = \phi_{0}' + \begin{bmatrix}
\phi_{1}' && \phi_{2}' && \phi_{3}'
\end{bmatrix}\begin{bmatrix}
h_{1}' \\
h_{2}' \\
h_{3}'
\end{bmatrix}
\end{align}
  $$
  In matrix notation, this becomes:
  $$
  \begin{align}
\mathbf{h} = a[\mathbf{\theta_{0}} + \mathbf{\theta} x] \\
\mathbf{h'} = a[\psi_{0} + \Psi \mathbf{h}] \\
y' = \mathbf{\phi_{0}'} + \mathbf{\phi'}\mathbf{h'}
\end{align}
  $$
  General formulation, vector of hidden layers at layer $k$ as $\mathbf{h_{k}}$, vector of biases that contribute to the hidden layer $k + 1$ as $\mathbf{\beta_{k}}$ and the wights that are applied to the $k^{th}$ layer and contribute to the $(k+1)^{th}$ layer as $\mathbf{\Omega_{k}}$, a general network $y = f[x, \phi]$ with $K$ layers can be written as,
  $$
  \begin{align}
h_{1} = a[\beta_{0} + \Omega_{0}\mathbf{x}] \\
h_{2} = a[\beta_{1} + \Omega_{1}\mathbf{h_{1}}] \\
\vdots \\
h_{K} = a[\beta_{K - 1} + \Omega_{K - 1}\mathbf{h_{K - 1}}] \\
\mathbf{y} = \beta_{K} + \Omega_{K}\mathbf{h_{K}}
\end{align}
  $$
  The parameters $\phi$ of this model comprise all of these wight matrices and bias vectors $\phi = \{\beta_{k}, \Omega_{k}\}_{k=0}^K$.
  If the $k_{th}$ layer has $D_{k}$ hidden units, then the bias vector $\beta_{k-1}$ will be of size $D_k$. The last bias vector $\beta_K$ has the size $D_0$ of the output. The first weight $\Omega_{0}$ has a size $D_{1} \times D_{i}$, where $D_i$ is the size of the input. The last weight matrix $\Omega_{K}$ is $D_{o} \times D_{K}$ and the remaining matrices $\Omega_{k}$ are $D_{k + 1} \times D_{k}$.
  The network as a single function:
  $$
  \mathbf{y} = \beta_{K} + \Omega_{K}a[\beta_{K-1} + \Omega_{K-1}a[\dots \beta_{2} + \Omega_{2}a[\beta_{1}] + \Omega_{1}a[\beta_{0} + \Omega_{0}\mathbf{x}]]]
  $$

## Summary

