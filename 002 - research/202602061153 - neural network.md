---
tags:
  - deep_learning
aliases:
  - Neural Network
title: neural network
description: ""
parent nodes:
  - "[[neural networks]]"
published on:
---

- [ ] What is MSE?

---
- A neural network is a machine learning [[202602010044 - model|model]] that stacks simple "neurons" in layers and learns pattern-recognising weights and biases from data to map inputs to outputs [^1]
- Neural networks are <mark style="background: #FF5582A6;">function approximators</mark> built from layers of interconnected units (neurons)
- Each layer applies an [[202602111417 - affine map|affine]] transformation followed by a nonlinear [[202602111400 - activation|activation]]
- Depth enables hierarchical feature learning from simple to complex patterns

![Deep Neural Networks](https://assets.ibm.com/is/image/ibm/ICLH_Diagram_Batch_01_03-DeepNeuralNetwork:16x9?fmt=png-alpha&dpr=on%2C2&wid=1536&hei=864)

- [[202602111314 - model parameters|Parameters]] are learned from data using backpropagation and gradient-based optimisation
- A neuron takes an input [[202602102054 - vectors|vector]] $\mathbf{x}$, applies [[202602111358 - weights and biases|weights]] $\mathbf{w}$ and a [[202602111358 - weights and biases|bias]] $b$, and passes the result through an [[202602111400 - activation|activation]] function $f$:

> [!MATH] Forward Pass
> $$z = \sum_{i=1}^{n} w_i x_i + b$$
> 
> The output (activation) is:
$$a = f(z)$$

- To measure how "wrong" the network is, we calculate the cost $C$ for $n$ samples:

> [!MATH] The [[202602010047 - objective function|Loss Function]] (Mean Squared Error)
$$C = \frac{1}{n} \sum_{i=1}^{n} (y_{true} - y_{pred})^2$$

- To update weights, we need the gradient of the [[202602010047 - objective function|cost function]] with respect to the weight
- We use the chain rule to find this derivative:

> [!MATH] [[202602111557 - backpropagation|Backpropagation]]
$$\frac{\partial C}{\partial w} = \frac{\partial C}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}$$

- Once the gradient is calculated, we update the weight using the Learning Rate ($\eta$), which is a [[202602111256 - hyperparameters|hyperparameter]]:

> [!MATH] The Update Rule (Gradient Descent)
> $$w_{new} = w_{old} - \eta \cdot \frac{\partial C}{\partial w}$$

- Common architectures include:
	- Multilayer Perceptrons (MLP)
	- Convolutional Neural Networks (CNNs)
	- Recurrent Neural Networks (RNNs)
	- [[202602102143 - transformer|Transformer]]
- Model quality depends on:
	- Architecture
	- Data quality
	- Optimisation
	- Regularisation choices


[^1]: https://www.ibm.com/think/topics/neural-networks#:~:text=A%20neural%20network%20is%20a%20machine%20learning%20model%20that%20stacks%20simple%20%22neurons%22%20in%20layers%20and%20learns%20pattern%2Drecognizing%20weights%20and%20biases%20from%20data%20to%20map%20inputs%20to%20outputs.