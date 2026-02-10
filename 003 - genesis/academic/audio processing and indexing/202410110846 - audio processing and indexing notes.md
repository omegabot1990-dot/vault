---
tags:
  - academic
  - api
aliases:
  - api notes
title: audio processing and indexing notes
description: notes for understanding audio processing and indexing lectures
parent nodes:
  - "[[audio processing and indexing]]"
child nodes: 
annotation-target:
---

## Cues

#### Analog and Digital Signals

- How does an Analog to Digital Conversion (ADC) system work?
   Analog Input -> Antialiasing Filter -> A/D Conversion -> Digita Processing -> Digital Output
- How to sample a sine wave?
   $$
   s_{k}(t) = \sin((f_{0} + kf_{sample})t), |k|\in \mathbb{N}
   $$
- What is the sampling theorem?
   A signal $s(t)$ with maximum frequency $f_{max}$ can be recovered, if sampled at frequency $f_s>2f_{max}$.
   Nyquist frequency (rate) $f_{N} = 2f_{max}$.
- What is bandwidth?
   Bandwidth indicates the width of a range in the frequency domain.
- What are negative frequencies?
   Consider a signal $s(t) = e^{i_{2}\pi f_{0}t}$, if $f_{0}<0$ then the signal rotates counter clockwise in the complex plane, this is a negative frequency.
   $$
   \begin{align}
e^{i_{2}\pi f_{0}t} = \cos(2\pi f_{0}t) + i\sin(2\pi f_{0}t) \\
\sin(2\pi f_{0}t) = \frac{e^{i_{2}\pi f_{0}t} - e^{-i_{2}\pi f_{0}t}}{2}  \\ \\
\cos(2\pi f_{0}t) = \frac{e^{i_{2}\pi f_{0}t} + e^{-i_{2}\pi f_{0}t}}{2} 
\end{align}   
   $$
- What is aliasing?
   Aliasing is a phenomenon in signal processing that occurs when a signal is sampled at a rate that is too low to capture its full detail, leading to distortion or misrepresentation of the signal.
- What is spectral replication?
  Spectral replication is a phenomenon that occurs when we sample a signal, and its frequency spectrum is repeated (or "replicated") at regular intervals. This happens as a direct consequence of the sampling process.
- What is under sampling?
  Under-sampling allows you to capture high-frequency bandpass signals using a lower sampling rate, reducing hardware requirements while avoiding aliasing. It uses spectral replication to reduce sampling frequency $f_s$ requirements.
  $$
  \frac{2f_{c} + B}{m + 1} \leq f_{s} \leq \frac{2f_{c} - B}{m + 1}
  $$
  Here, $f_c$ is the central frequency and $m \in \mathbb{N}$, selected so that $f_s > 2B$. 
- What is over sampling?
  Over-sampling is the process of sampling a signal at a rate much higher than the *Nyquist rate*, which is twice the highest frequency present in the signal. This is done for various reasons, such as improving signal quality, reducing noise, or simplifying the design of filters and other components in a digital signal processing system.
  $$
\begin{align}
f_{s} \gg 2f_{max} \\
f_{os} = 4^wf_{s}
\end{align}
  $$
  Where $f_{os}$ is the over sampling frequency and $w$ is the additional bits.
- What is quantisation?
  Quantisation is the process of rounding the continuous signal to the nearest discrete level. The size of each of these steps between digital levels is called the *quantisation step* or *resolution* and is given by:
  $$
q = \frac{V_{max}}{2^N}
$$
  Where $V_{max}$ is the maximum input voltage and $2^N$ is determined by the number of bits.
- What is quantisation error?
  Quantisation error is the difference between the actual analog signal and the nearest digital level that it is rounded to. Higher resolution means lower $e_q$.
  $$
  e_{q} \in [-0.5q, +0.5q] 
  $$

#### Short Time Fourier Transforms

- What are Dirichlet's conditions?
  1. $s(t)$ is piecewise continuous 
  2. $s(t)$ is piecewise monotonic
  3. $s(t)$ is absolutely integrable $\int_{0}^{T}|s(t)|dt < \infty$
- What is the Fourier Series?
  A periodic function $s(t)$ that satisfies Dirichlet's conditions can be expressed as a Fourier series with harmonically related sine/cosine terms.
  $$ s(t) = a_0 + \sum_{k=1}^{\infty} \left[ a_k \cdot \cos(k \omega t) - b_k \cdot \sin(k \omega t) \right] $$
$$ a_0 = \frac{1}{T} \int_{0}^{T} s(t) \, dt $$
$$ a_k = \frac{2}{T} \int_{0}^{T} s(t) \cdot \cos(k \omega t) \, dt $$
$$ b_k = \frac{2}{T} \int_{0}^{T} s(t) \cdot \sin(k \omega t) \, dt $$
Here $a_0$ is the DC term.
- What is Gibbs phenomenon?
  Overshoot exits at each discontinuity.
- What is Discrete Fourier Series (DFS)?
  The DFS represents a periodic discrete-time signal as a sum of complex exponentials at different frequencies.

## Notes

#### Analog and Digital Signals

- Analog Signals
   Continuous function $F$ of a continuous variable $t$, $F(t)$.
- Digital Signals
   Discrete function $F_k$ of a discrete (sampling) variable $t_k$ with $k$ as an integer, $F_k = F(t_{k})$. 
   Function is sampled with sampling frequency $f_s$ where, $f_s = 1 / t_s$.
- Time and Frequency are two complimentary signal descriptions.
- ADC Parameters
	1. Resolution or number of bits
	2. Speed or sample rate
	3. SNR or Signal-to-noise ratio $\overline{SNR_{ideal}} = 6.02N + 1.76[dB]$
	4. SINAD or Signal-to-noise-and-distortion-rate $SINAD = \frac{P_{signal} + P_{noise} + P_{distortion}}{P_{noise} + P_{distortion}}$
	5. ENOB or Effective number of bits
- Complex Numbers
   $$
   \begin{align}
\mathbb{C} = \{c | c = a +ib, where\space a, b \in \mathbb{R}\} \\
|c| = \sqrt{a^2 + b^2} \\
c = r (\cos {\phi} + i\sin{\phi}) = re^{i\phi} \\
a = r\cos\phi  \\
b = r \sin\phi \\
r = |c| = \sqrt{a^2 + b^2} \\
\phi = \arctan\left( \frac{b}{a} \right)
\end{align}
   $$
- Fields
  A field in mathematics is a set of numbers (or elements) that follow specific rules for addition, subtraction, multiplication, and division.
  Rules:
  1. Commutativity
  2. Associativity
  3. Identity Elements 
    1. Addition
    2. Multiplication
  4. Inverse
    1. Addition
    2. Multiplication
- Vector Spaces
  Rules:
  1. Closure under Addition
  2. Closure under Scalar Multiplication
  3. Associativity of Vector Addition
  4. Commutativity of Vector Addition
  5. Existence of Additive Identity
  6. Existence of Additive Inverse
  7. Distributivity of Scalar Multiplication with Respect to Vector Addition
  8. Distributivity of Scalar Multiplication with Respect to Scalar Addition
  9. Associativity of Scalar Multiplication
  10. Existence of Scalar Identity
- Linear Dependance
  A set of vectors is said to be linearly dependent if at least one of the vectors in the set can be written as a linear combination of the other vectors in the set.
  $$
  c_{1}v_{1} + c_{2}v_{2} + \dots + c_{n}v_{n} = 0
  $$
  Where $c_{i} \in Scalars$ and $v_{i} \in Vectors$.
- Basis of a Vector Space
  Rules:
  1. Linearly Independent
  2. Spans the Vector Space
- Scalar Product, Orthogonality
  The scalar product, also known as the dot product, is an operation that takes two vectors and returns a scalar (a single number).
  Orthogonal means the vectors are perpendicular $u \cdot v = 0$.
- Fourier Coefficients 
  Fourier coefficients $a_{n}$​ and $b_{n}$​ allow us to decompose any periodic function into a series of sines and cosines.
    
#### Short Time Fourier Transforms

- Fourier Coefficient
  $$
  \begin{align}
h_{f}(t) = e^{-i_{2}\pi ft} = \cos(k\omega t) - i\sin(k\omega t), \omega=\frac{2\pi}{T} \\
v \cdot w = s(t) \cdot h_{f}(t), w \cdot w = 1 \space[orthonormal] \\
= \int s(t).e^{-i_{2}\pi ft} dt
\end{align}
  $$
- Fourier Series properties

|                    | Time(t)                                       | Frequency(f)                                             |
| ------------------ | --------------------------------------------- | -------------------------------------------------------- |
| Homogeneity        | $$ a \cdot s(t) $$                            | $$ a \cdot S(f) $$                                       |
| Additivity         | $$ s(t) + u(t) $$                             | $$ S(f) + U(f) $$                                        |
| Linearity          | $$ a \cdot s(t) + b \cdot u(t) $$             | $$ a \cdot S(f) + b \cdot U(f) $$                        |
| Time reversal      | $$ s(-t) $$                                   | $$ S(-f) $$                                              |
| Multiplication     | $$ s(t) \cdot u(t) $$                         | $$ \frac{1}{T} \int_{0}^{T} S(f - t) \cdot U(t) \, dt $$ |
| Convolution        | $$ \sum_{m=-\infty}^{\infty} s(m) u(t - m) $$ | $$ S(f) \cdot U(f) $$                                    |
| Time shifting      | $$ s(t - \tilde{t}) $$                        | $$ e^{- \frac{i 2 \pi f \tilde{t}}{T}} \cdot S(f) $$     |
| Frequency shifting | $$ e^{\frac{i 2 \pi m t}{T}} \cdot s(t) $$    | $$ S(f - m) $$                                           |

- Discrete Fourier Series (DFS)
  DFS Analysis:
  $$ 
\tilde{c_k} = \frac{1}{N} \sum_{n=0}^{N-1} s[n] \cdot e^{-\frac{j 2 \pi k n}{N}}
$$
  DFS Synthesis (Inverse Fourier Transform):
  $$ 
s[n] = \sum_{k=0}^{N-1} \tilde{c_k} \cdot e^{\frac{j 2 \pi k n}{N}}
$$
  Orthogonality in DFS:
  $$ 
\frac{1}{N} \sum_{n=0}^{N-1} e^{\frac{j 2 \pi n (k - m)}{N}} = \delta_{k,m}
$$
  Where $\delta$ is the Kronecker's Delta,
  $$ 
\delta_{ij} = 
\begin{cases}
1 & \text{if } i = j \\
0 & \text{if } i \neq j 
\end{cases}
$$

- Discrete Fourier Series Properties
  
|                    | Time (n)                                   | Frequency (k)                                  |
| ------------------ | ------------------------------------------ | ---------------------------------------------- |
| Homogeneity        | $$ a \cdot s[n] $$                         | $$ a \cdot S(k) $$                             |
| Additivity         | $$ s[n] + u[n] $$                          | $$ S(k) + U(k) $$                              |
| Linearity          | $$ a \cdot s[n] + b \cdot u[n] $$          | $$ a \cdot S(k) + b \cdot U(k) $$              |
| Multiplication     | $$ s[n] \cdot u[n] $$                      | $$ \frac{1}{N} \sum_{h=0}^{N-1} S(h) U(k-h) $$ |
| Convolution        | $$ \sum_{m=0}^{N-1} s[m] u[n - m] $$       | $$ S(k) \cdot U(k) $$                          |
| Time shifting      | $$ s[n - m] $$                             | $$ e^{- \frac{j 2 \pi k m}{N}} \cdot S(k) $$   |
| Frequency shifting | $$ e^{\frac{j 2 \pi h n}{N}} \cdot s[n] $$ | $$ S(k - h) $$                                 |


## Summary

- N/A