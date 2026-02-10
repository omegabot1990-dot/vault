---
tags:
  - math
aliases:
  - Central Limit Theorem
title: central limit theorem
description:
parent nodes:
  - "[[202602072325 - distribution|Distribution]]"
annotation-target:
published on:
---

- It states that if you take enough samples from any distribution (no matter how weird, skewed, or messy it is), the mean of those samples will eventually form a [[202602072342 - normal distribution|Normal Distribution]] [^1][^2]
- Let $X_1, X_2, \dots, X_n$ be a sequence of [[202602092108 - independent and identically distributed|independent and identically distributed (IID)]] random variables with mean $\mu$ and variance $\sigma^2$. As $n$ becomes large ($n \to \infty$):

> [!MATH] Central Limit Theorem
> 
> $$\bar{X}_n \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$
> 
> - **$\bar{X}_n$**: The sample mean
> - **$\mathcal{N}$**: The Normal Distribution
> - **$\mu$**: The <mark style="background: #FF5582A6;">Population Mean</mark> (the true average of the underlying distribution)
> - **$\sigma^2$**: The <mark style="background: #FF5582A6;">Population Variance</mark> (the "spread" of the underlying distribution)
> - **$n$**: The sample size (usually $n \ge 30$ is considered "enough")

- <mark style="background: #BBFABBA6;">How it helps?</mark>
	- Work with the Unknown
		- You don't need to know the distribution of the population (e.g., "all humans")
		- You only need to know that your <mark style="background: #FF5582A6;">sample means</mark> will behave predictably

---

- The reduction in variance occurs because of the properties of the variance of a sum of independent variables:

> [!MATH] The Math Behind the Variance $\frac{\sigma^2}{n}$
> 
> 
> 1. **Linearity of Expectation**: 
>    $E[\bar{X}_n] = E\left[\frac{1}{n}\sum X_i\right] = \frac{1}{n} \sum E[X_i] = \frac{n\mu}{n} = \mu$
> 
> 2. **Variance of the Mean**: 
>    Since $Var(aX) = a^2Var(X)$, then:
>    $Var(\bar{X}_n) = Var\left(\frac{1}{n}\sum X_i\right) = \frac{1}{n^2} Var\left(\sum X_i\right)$
> 
> 3. **Summing Variances**:
>    Because the variables are IID, the variance of the sum is the sum of the variances:
>    $Var(\bar{X}_n) = \frac{1}{n^2} (n\sigma^2) = \frac{\sigma^2}{n}$


[^1]: [The Central Limit Theorem, Clearly Explained!!!](https://www.youtube.com/watch?v=YAlJCEDH2uY)
[^2]: [3Brown1Blue - But what is the Central Limit Theorem?](https://www.youtube.com/watch?v=zeJD6dqJ5lo&list=PLiAulSm0XXgvCGe63mrAkda9UQ9478YQv&index=7)
