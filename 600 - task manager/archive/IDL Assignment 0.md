---
tags:
  - academic
  - idl
description: assignment zero for IDL
due date: 2024-09-27
start date: 2024-09-24
end date: 2024-09-26
status: Archive
importance level: important
urgency level: urgent
task type: execute
story points:
parent nodes:
  - "[[introduction to deep learning]]"
child nodes:
recurrent:
---
# NEED TO CATCH UP
![[deep_learning_assignment_zero_new.pdf]]
https://docs.google.com/document/d/1Ps7_VsauSX35vl8HzXQuBMORndf_jZjnOnRLh0tZ01c/edit

# Task 2

## Introduction

Alright, imagine you’re playing a game where you need to recognize different types of animals. Let’s say you have **10** different animals like dogs, cats, elephants, lions, etc. You need to figure out which animal is which just by looking at a picture.

### What is a Perceptron?

A **perceptron** is like a simple machine that tries to make decisions based on the information it gets. For example, if you show it a picture of a dog, it will try to say, "Hey, that’s a dog!" But what if you show it a picture of an elephant? It should say, "Nope, that’s not a dog."

Now, that’s good for figuring out if something **is or isn’t** a dog (this is called **binary classification**, where there are only two possible answers). But what if you need it to figure out all the different types of animals?

### Multi-Class Perceptron

A **multi-class perceptron** is like having **10 little perceptrons** working together. Each one is responsible for saying, "Is this a dog?" "Is this a cat?" "Is this an elephant?" and so on. Each perceptron is responsible for one animal.

So, when you show the multi-class perceptron a picture of an animal, all 10 perceptrons will think really hard and give you their answers. The one that shouts the loudest, saying "This is definitely my animal!" will be chosen. If the perceptron for "elephant" is the most confident, the machine will say, "This is an elephant."

### How Does It Work?

1. **Understanding the Input (Picture)**
    
    - Imagine the picture of an animal is broken down into lots of small pieces (pixels). Each pixel can give the machine some clues (like how bright or dark it is). So, for each picture, the machine gets a long list of clues (numbers) about what the picture looks like.
2. **The Perceptron Machine’s Brain**
    
    - The perceptron machine has a **brain** that is made up of **weights**. Think of these weights as little rules that the machine uses to figure out what animal the picture might be. Each animal has its own set of rules (weights).
3. **Making a Guess**
    
    - The machine looks at the picture’s clues and follows the rules (weights) for each animal. Then, it makes a **guess** for each animal about how likely it is that the picture matches that animal.
    - For example, it might guess: "This picture looks 20% like a dog, 70% like a cat, and 10% like an elephant."
4. **Choosing the Best Guess**
    
    - The machine then picks the guess that has the highest score. So, in the example above, since it thinks the picture looks 70% like a cat, it will say, "This is a cat!"
5. **Learning from Mistakes**
    
    - At first, the perceptron machine isn’t very smart. It makes a lot of mistakes. But here’s the cool part: Every time it makes a mistake, it learns from it.
    - Let’s say the machine saw a dog but guessed "cat" instead. The machine will realize that its **"dog rules" were too weak**, and the **"cat rules" were too strong**. So, it will adjust the rules to make the "dog rules" stronger and the "cat rules" weaker.
6. **Training the Machine**
    
    - You keep showing the machine lots of different pictures and keep letting it learn from its mistakes. Over time, it gets better and better at figuring out which animal is which. This process is called **training**.

### How Does the Machine Learn?

Let’s break down how the machine adjusts its rules:

- Each animal has its own **set of rules (weights)**.
- When the machine makes a mistake, it changes the rules. It will make the correct animal's rules stronger and the wrong guess’s rules weaker.
- This adjustment process helps the machine slowly become better at recognizing animals correctly.

### Why Do We Use Multiple Perceptrons?

For **binary classification** (like “dog or not dog”), you just need one perceptron. But for **multi-class problems** (like 10 different animals), you need multiple perceptrons—one for each class. That’s why it’s called a **multi-class perceptron**.

### How the Machine Decides in One Shot (Efficiency)

To make things faster, instead of asking each perceptron one by one (like a big classroom), we make the machine do it all at once:

- We put all the clues (numbers) from the picture in one big list (called a **matrix**).
- The machine has all the rules for all animals in another big list.
- The machine does one **big calculation** (matrix multiplication) to get guesses for all the animals at once.
- It then picks the best guess using the **argmax()** function, which just means finding the biggest number.

### Why Is This Cool?

- **It learns**: The machine starts off not knowing much, but by training (showing it lots of pictures), it gets smarter and better at guessing.
- **It’s fast**: Once it’s trained, the machine can guess really quickly.
- **It works for many classes**: Even though we’re talking about 10 animals, you could use it to recognize any number of different things.

### Comparing with Other Methods

- **Perceptron**: Tries to learn from mistakes and improve with each guess.
- **Other methods** (like distance-based): Measure how close something is to known examples. Perceptrons are often faster once trained and can handle larger datasets more efficiently.

### Summary

A **multi-class perceptron** is a simple machine that learns to recognize different classes (like animals) by training multiple perceptrons, one for each class. It guesses the class based on the clues it gets from the input, learns from mistakes by adjusting its rules, and gets better over time with more training.

# Multi-Class Perceptron Algorithm: Essential Math Concepts

---

## 1. Vectors and Matrices

### Vectors:
A **vector** is an ordered list of numbers. In the context of machine learning, a vector represents an input or a weight set.

For example, an input vector $\mathbf{x}$ could be:

$$
\mathbf{x} = [x_1, x_2, \dots, x_d]
$$

where each $x_i$ is a feature (like a pixel value in an image) and $d$ is the number of features.

### Matrices:
A **matrix** is a two-dimensional array of numbers. In the multi-class perceptron, the weights for each class can be stored in a matrix $W$.

For example, if we have 10 classes and each input vector has 257 features (including the bias), the weight matrix $W$ could be of size $257 \times 10$:

$$
W = \begin{bmatrix}
w_{1,1} & w_{1,2} & \dots & w_{1,10} \\
w_{2,1} & w_{2,2} & \dots & w_{2,10} \\
\vdots & \vdots & \ddots & \vdots \\
w_{257,1} & w_{257,2} & \dots & w_{257,10}
\end{bmatrix}
$$

Each column in $W$ represents the weight vector for a class.

---

## 2. Dot Product (Inner Product)

The **dot product** of two vectors $\mathbf{a}$ and $\mathbf{b}$ is a scalar value calculated as:

$$
\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + \dots + a_d b_d
$$

In the perceptron, the dot product is used to compute the **score** for each class:

$$
\text{Score}_i = \mathbf{x} \cdot \mathbf{w}_i
$$

Where $\mathbf{x}$ is the input vector and $\mathbf{w}_i$ is the weight vector for class $i$.

---

## 3. Argmax Function

The **argmax** function finds the index of the largest value in a list. In the multi-class perceptron, after calculating the scores for each class, we use `argmax` to determine which class has the highest score:

$$
\hat{y} = \arg\max_{i} \mathbf{x} \cdot \mathbf{w}_i
$$

where $\hat{y}$ is the predicted class.

---

## 4. Weight Update Rule

When a mistake is made (i.e., when the predicted class $\hat{y}$ does not match the true class $y$), the weight vectors are updated as follows:

- **Decrease** the weights for the wrongly predicted class $\hat{y}$:

$$
\mathbf{w}_{\hat{y}} = \mathbf{w}_{\hat{y}} - \eta \mathbf{x}
$$

- **Increase** the weights for the correct class $y$:

$$
\mathbf{w}_y = \mathbf{w}_y + \eta \mathbf{x}
$$

where $\eta$ is the learning rate, which controls how much the weights are adjusted after each mistake.

---

## 5. Learning Rate ($\eta$)

The **learning rate** $\eta$ is a small positive constant that controls how big the weight updates are. A smaller $\eta$ means smaller, more gradual updates, while a larger $\eta$ speeds up learning but might overshoot the optimal solution.

Typical values for $\eta$ might be 0.01 or 0.001, but you need to experiment to find the best one.

---

## 6. Bias Term

The **bias** helps shift the decision boundary to better separate the classes. In the weight matrix $W$, an extra column is often used to represent the bias term.

### Bias Inclusion:
You append a 1 to the input vector $\mathbf{x}$, so it becomes $\mathbf{x}' = [x_1, x_2, \dots, x_d, 1]$. This allows the bias to be treated as part of the weight matrix:

$$
\mathbf{x} \cdot \mathbf{w}_i + b_i = [x_1, \dots, x_d, 1] \cdot [w_{1i}, w_{2i}, \dots, w_{di}, b_i]
$$

This simplifies weight updates, as the bias term is now incorporated into the same update rule.

---

## 7. Hinge Loss (Optional)

While the perceptron does not directly minimize a loss function, you might track a **hinge loss** to measure how well the model is performing:

$$
L = \max(0, 1 - \mathbf{w}_y \cdot \mathbf{x} + \mathbf{w}_{\hat{y}} \cdot \mathbf{x})
$$

The hinge loss is 0 if the correct class scores higher than any other class by a margin of 1. Otherwise, it penalizes the model based on how far off it is.

---

## 8. Matrix Multiplication

To make your algorithm efficient, you can compute the scores for all classes in a single matrix multiplication:

$$
Z = X W
$$

where:
- $X \in \mathbb{R}^{N \times d}$ is the matrix of inputs (with $N$ examples and $d$ features).
- $W \in \mathbb{R}^{d \times 10}$ is the weight matrix.
- $Z \in \mathbb{R}^{N \times 10}$ gives the scores for all classes for all input examples.

Then, for each row (each input example), use `argmax` to find the predicted class.

---

## 9. Accuracy Calculation

The **accuracy** measures how many predictions are correct. After you compute the predicted class $\hat{y}$ for each input, compare it to the true label $y$ and compute the accuracy as:

$$
\text{Accuracy} = \frac{\text{Number of correct predictions}}{\text{Total number of predictions}}
$$

---

## 10. Gradient Descent (Optional Extension)

If you want to extend the perceptron algorithm to something like **logistic regression** or **softmax regression**, you would use **gradient descent** to minimize a loss function. The gradient is the vector of partial derivatives of the loss function with respect to the weights, and you update the weights using the gradient:

$$
\mathbf{w}_i = \mathbf{w}_i - \eta \frac{\partial L}{\partial \mathbf{w}_i}
$$

where $L$ is the loss function (such as cross-entropy).

---

## Summary of Math Concepts

- **Vectors and Matrices**: Used to represent inputs and weights.
- **Dot Product**: To calculate the score for each class.
- **Argmax**: To find the class with the highest score.
- **Weight Update Rule**: Adjust weights when the model makes a mistake.
- **Learning Rate**: Controls the size of updates.
- **Bias**: Ensures flexibility in decision boundaries.
- **Matrix Multiplication**: For efficient computation of scores for all classes at once.
- **Accuracy**: To evaluate how well the model is performing.
