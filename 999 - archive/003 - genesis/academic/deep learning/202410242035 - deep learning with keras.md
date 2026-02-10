---
tags:
  - academic
  - idl
aliases:
  - deep learning with keras
title: deep learning with keras
description: assignment one for IDL
parent nodes:
  - "[[introduction to deep learning]]"
child nodes:
annotation-target:
---

# References

1. [Metrics](https://keras.io/api/metrics/)
2. [Layers](https://keras.io/api/layers/)
3. [Activations](https://keras.io/api/layers/activations/)
4. [Loss Function](https://keras.io/api/losses/)
5. [Initialisers](https://keras.io/api/layers/initializers/)
6. [Optimisers](https://keras.io/api/optimizers/)
7. [Regularisers](https://keras.io/api/layers/regularizers/)
8. [Datasets](https://keras.io/api/datasets/)

# Cues

- What is a **confusion matrix**?
   A **confusion matrix** is a performance measurement tool for classification algorithms, particularly in supervised learning. It summarises a model's predictions by comparing the actual class labels to the predicted class labels. The matrix provides insight into how many predictions were correct and where the errors occurred, giving a detailed performance breakdown for each class.
   - **True Positives (TP)**: The number of instances where the actual class was positive and the model predicted positive.
   - **False Positives (FP)**: The number of instances where the actual class was negative, but the model incorrectly predicted positive (a Type I error).
   - **False Negatives (FN)**: The number of instances where the actual class was positive, but the model incorrectly predicted negative (a Type II error).
   - **True Negatives (TN)**: The number of instances where the actual class was negative and the model correctly predicted negative.
- What is **accuracy**?
  The ratio of correctly predicted instances (both positive and negative) to the total cases.
  $$
  Accuracy = \frac{TP + TN}{TP + TN+FP+FN}
  $$
- What is **precision**?
  The ratio of correctly predicted positive instances to all predicted positives. This metric helps to measure how many of the predicted positive instances were actually positive.
  $$
  Precision = \frac{TP}{TP+FP}
  $$
- What is **recall**?
  The ratio of correctly predicted positive instances to all actual positive instances. This metric helps to measure how well the model is capturing positive instances. (Sensitivity or True Positive Rate)
  $$
  Recall = \frac{TP}{TP + FN}
  $$
- What is **F1 score**?
  A harmonic mean of Precision and Recall, providing a single score that balances both.
  $$
  F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
  $$
- What is **Top-k Categorical Accuracy**?
  Top-k accuracy is the fraction of predictions where the correct label is among the top-k predicted labels. For example, top-3 accuracy would consider a prediction correct if the true label is within the model's top 3 predicted labels.
- What is **logarithmic loss**?
  Logarithmic loss measures how far predicted probabilities are from the true class labels.
- What is loss?
  In machine learning, **loss** measures how well a model’s predictions align with the actual target values. It quantifies the error between the model’s predictions and the true labels. During training, the model aims to minimise this loss, adjusting its weights to improve prediction accuracy.
  **Guides Model Learning**: Loss provides the gradient information the optimiser uses to adjust the model’s weights.
  **Helps in Convergence**: Lowering the loss means the model’s predictions are getting closer to the true values, indicating it is learning effectively.
  **Evaluate Model Performance**: Monitoring loss (training and validation) can help detect overfitting or underfitting and understand how well the model generalises.
- What is **Categorical Cross-Entropy Loss**?
  Measures the difference between the predicted probability distribution and the true class distribution.
  Commonly used in multi-class classification (like MNIST digit classification).
- What is **Mean Squared Error (MSE)**?
  Mean squared error calculates the average squared difference between predicted and actual values.

# Notes

## Batch Size

**Changing the batch size** can affect the model's training process and potentially the final model weights. Here's how:

### 1. **Impact on Weight Updates**:

- **Batch size** determines how often the model's weights are updated during training.
- With a **smaller batch size**, the model updates the weights more frequently because each batch is smaller, and the model performs weight updates after processing each batch.
- With a **larger batch size**, the model updates the weights less frequently since it processes more data before each weight update.

#### Example:

- If you have 1,000 training samples:
    - With a batch size of 32, the model will perform 31 updates per epoch (1000/32 = 31).
    - With a batch size of 128, the model will perform only 8 updates per epoch (1000/128 = 8).

### 2. **Effect on Gradient Estimation**:

- The weights are updated based on the gradients of the loss function. When the batch size is smaller, the gradient estimates are computed using fewer samples, which makes them more **noisy**. This can result in weight updates that vary more significantly from one step to the next, potentially leading to faster exploration of the loss landscape but with less stability.
- When the batch size is larger, the gradient estimates are more **accurate** because they are computed from more samples, making the updates smoother and more stable. However, this might slow down the convergence and cause the model to get stuck in local minima.

### 3. **Generalisation and Overfitting**:

- **Smaller batch sizes** often introduce more randomness during training due to the noisier gradient updates. This can act as a form of regularisation, which may help prevent overfitting and improve the model’s ability to generalise to unseen data.
- **Larger batch sizes** produce smoother and more stable weight updates. Still, they might overfit the training data since the model might find it easier to "memorise" the data without the noise introduced by smaller batches.

### 4. **Convergence Speed**:

- **Smaller batch sizes** generally result in faster updates, meaning that the model's weights are updated more often, which can lead to faster convergence, at least early in training. However, it might also introduce instability, causing the training process to take longer to converge fully.
- **Larger batch sizes** lead to fewer weight updates, slowing the convergence, but the updates might be more reliable and stable. This can result in slower but more stable convergence.

### 5. **Effect on Memory and Computation**:

- **Smaller batch sizes** require less memory because fewer data points are processed at once. This allows you to fit larger models or use higher-resolution data.
- **Larger batch sizes** require more memory (especially for large datasets) because more data is processed simultaneously. You may run into memory limitations, especially if you're using GPUs.

### 6. **Final Model Weights**:

- The model's final weights may differ depending on the batch size because the number of updates and the nature of the gradient updates are different.
- Due to the different learning dynamics (more frequent, noisier updates vs. less frequent, smoother updates), training with a small batch size might cause the weights to converge differently than training with a large batch size.

### Trade-offs:

- **Smaller batch size**:
    - Pros: More frequent updates, potentially faster initial learning, better generalisation, and less memory are required.
    - Cons: Noisier gradient updates, more variability, possible instability, longer overall training time.
- **Larger batch size**:
    - Pros: Smoother, more stable updates, faster convergence in terms of the number of epochs, and less noisy gradients.
    - Cons: Can require more memory, less frequent updates, possibly slower learning early on, and potential for overfitting.

### Conclusion:

Yes, changing the **batch size** affects how often the model's weights are updated, the nature of those updates (noisier vs. smoother), and the overall learning dynamics, which in turn can lead to different final model weights. The choice of batch size is a trade-off between stability, generalisation, and computational efficiency.

---

## Layers

Changing the layers or architecture of a model for an MNIST digit classification task can significantly impact the model's performance, learning efficiency, and generalisation ability. Here’s how architectural modifications influence the model:

### 1. **Adding More Layers**:

- **Deeper Architectures**: Adding more layers, especially if they are **hidden layers** in a dense neural network, allows the model to learn more complex features and hierarchical representations of the data.
- **Impact on MNIST**: Adding too many layers can lead to overfitting for a relatively simple dataset like MNIST because MNIST images (28x28 grayscale digits) don’t require extremely deep models to capture relevant patterns. However, adding more layers than a simple shallow network can improve accuracy by enabling the model to learn more nuanced features.
- **Example Change**:
    - A simple model: One hidden layer.
    - Deeper model: Three to five hidden layers with increasing/decreasing neuron counts, allowing for more complex pattern recognition.

### 2. **Increasing or Decreasing Neurons per Layer**:

- **Increasing Neurons**: As the number of neurons increases, each layer’s capacity to capture information grows, which can improve the model’s accuracy on training data.
- **Decreasing Neurons**: Fewer neurons make the model smaller, less computationally intensive, and potentially faster but may reduce the model’s ability to capture complex relationships.
- **Impact on MNIST**: Since MNIST is relatively simple, using too many neurons can lead to overfitting and increased computation time without meaningful performance gains. Finding a balanced number of neurons (e.g., 128 or 256 per layer in dense layers) can offer a good trade-off for accuracy and speed.

### 3. **Convolutional Layers vs. Dense Layers**:

- **Convolutional Layers**: For image data, using convolutional layers (CNNs) instead of fully connected (dense) layers generally yields better performance because convolutional layers capture spatial hierarchies and patterns (edges, shapes, etc.).
- **Impact on MNIST**: Replacing dense layers with convolutional layers helps the model understand the spatial arrangement of pixels, which is crucial for classifying digits. A typical architecture for MNIST could use two or three convolutional layers followed by a dense layer for classification, which would significantly improve performance over a fully connected architecture.

```
# Original Dense Layer Model
model.add(keras.layers.Dense(128, activation='relu'))

# Convolutional Model
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(keras.layers.MaxPooling2D((2, 2)))
```

### 4. **Adding Pooling Layers**:

- **Pooling Layers**: Pooling layers (like max pooling) reduce the spatial dimensions of feature maps, which helps reduce the number of parameters and makes the model less prone to overfitting.
- **Impact on MNIST**: Pooling helps retain important features while reducing unnecessary detail, making the model more computationally efficient without sacrificing performance. For MNIST, adding a couple of max pooling layers after convolutional layers can improve both accuracy and efficiency.

### 5. **Regularisation Layers (Dropout and Batch Normalisation)**:

- **Dropout Layers**: Dropout randomly "drops" a fraction of neurons during training, which helps reduce overfitting by forcing the model to be more resilient.
- **Batch Normalisation**: Normalises the inputs to each layer, helping the model train faster and more stably.
- **Impact on MNIST**: Adding dropout layers between dense layers or after convolutional layers can prevent overfitting, particularly if the model is deep. Batch normalisation can improve convergence speed and stabilise training.

```
model.add(keras.layers.Dropout(0.5))  # Dropout rate of 50%
model.add(keras.layers.BatchNormalization())
```

### 6. **Using Different Activation Functions**:

- **Activation Functions**: The choice of activation functions (ReLU, sigmoid, tanh, etc.) affects the model’s ability to learn complex patterns.
- **Impact on MNIST**: ReLU is commonly used in hidden layers to prevent the vanishing gradient problem and allow faster convergence. Sigmoid and softmax activations are typically used in the output layer for binary and multi-class classification, respectively. Switching to ReLU (instead of sigmoid or tanh) in hidden layers can improve training efficiency and performance on MNIST.

### 7. **Skip Connections (for Deeper Models)**:

- **Skip Connections**: Used in architectures like ResNet, skip connections allow the model to bypass certain layers, which helps mitigate issues like the vanishing gradient problem in deeper networks.
- **Impact on MNIST**: While generally unnecessary for shallow networks, skip connections can help if you experiment with deeper architectures for MNIST. They allow deeper models to learn effectively without the risk of gradients diminishing too early.

### Summary: Key Architectural Considerations for MNIST

For MNIST, you don’t need an extremely deep or complex architecture, as it is a relatively simple classification task. A balanced approach, such as combining convolutional layers with pooling and dropout layers, can help improve the model's performance without overfitting. Convolutional layers and max pooling are highly effective for image data, while dropout helps improve generalisation. Here’s a sample architecture that works well for MNIST:

```
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))  # For 10 classes in MNIST
```

This architecture efficiently captures spatial features, reduces overfitting, and works well for image-based tasks like MNIST.

---

## Activations

For the MNIST digit classification task, the choice of activation functions plays a crucial role in the model's learning and performance. Here's a rundown of the most commonly used activation functions for MNIST and why they are useful:

### 1. **ReLU (Rectified Linear Unit)**:

- **Definition**: ReLU outputs the input value directly if it’s positive and outputs zero otherwise: 
  $$
  \text{ReLU}(x) = \max(0, x)
  $$
- **Usage in MNIST**: ReLU is widely used in the **hidden layers** of neural networks for MNIST classification. It introduces non-linearity while helping to avoid the vanishing gradient problem, enabling faster training and better convergence.
- **Why it’s useful**: ReLU speeds up training and generally improves performance by allowing networks to learn complex patterns. It also reduces computational cost compared to other activations, such as sigmoid or tanh.

```
model.add(Dense(128, activation='relu'))
```

### 2. **Softmax**:

- **Definition**: Softmax is an activation function that converts raw model outputs into probabilities for multi-class classification. It produces a vector of values between 0 and 1 that sum to 1: 
  $$
  \text{Softmax}(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}}​​
  $$
  
- **Usage in MNIST**: Softmax is typically used in the **output layer** for multi-class classification tasks like MNIST, where each digit (0–9) represents a separate class.
- **Why it’s useful**: Softmax ensures the model’s output represents probabilities, allowing the model to make a clear choice among multiple classes.

```
model.add(Dense(10, activation='softmax'))  # 10 classes for MNIST digits 0–9
```

### 3. **Tanh (Hyperbolic Tangent)**:

- **Definition**: Tanh maps inputs to a range between -1 and 1: 
  $$
  \text{Tanh}(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
  $$
- **Usage in MNIST**: Tanh can be used in hidden layers as an alternative to ReLU, though it's less common for image classification tasks like MNIST.
- **Why it’s useful**: Tanh activation is centered around zero, which helps when dealing with data centered around the mean. It can sometimes work well in hidden layers to introduce smooth gradients and help with convergence, though it's generally slower than ReLU and can lead to vanishing gradients in deep networks.

```
model.add(Dense(128, activation='tanh'))
```

### 4. **Leaky ReLU**:

- **Definition**: Leaky ReLU is a variant of ReLU that allows a small, non-zero gradient for negative input values, preventing units from dying during training: 
  $$
\text{Leaky ReLU}(x) = 
\begin{cases} 
x & \text{if } x > 0 \\ 
\alpha x & \text{if } x \leq 0 
\end{cases}
$$

  
  ​ where $\alpha$ is a small constant, typically 0.01.
- **Usage in MNIST**: Leaky ReLU can be applied in the hidden layers, especially if there’s a risk of neurons becoming inactive (dead ReLUs).
- **Why it’s useful**: It helps avoid the "dying ReLU" problem, where neurons stop learning due to zero gradients. Leaky ReLU can improve learning in deeper networks.

```
from keras.layers import LeakyReLU
model.add(Dense(128))
model.add(LeakyReLU(alpha=0.01))
```

### 5. **ELU (Exponential Linear Unit)**:

- **Definition**: ELU is another ReLU variant that introduces a smooth curve for negative inputs, which can improve the learning process:
  $$
  \text{ELU}(x) =
\begin{cases}
x & \text{if } x > 0 \\
\alpha (e^x - 1) & \text{if } x \leq 0
\end{cases}
  $$
- **Usage in MNIST**: ELU can be used in hidden layers for improved convergence and learning efficiency, especially in deeper networks.
- **Why it’s useful**: ELU reduces the vanishing gradient problem and speeds up convergence by providing non-zero gradients for negative inputs. It can perform better than ReLU in some cases, particularly on noisy data.

```
from keras.layers import ELU
model.add(Dense(128))
model.add(ELU(alpha=1.0))
```

### Summary of Activation Functions for MNIST

- **ReLU**: Generally the best choice for hidden layers in MNIST due to its simplicity and efficiency.
- **Softmax**: Essential in the output layer for multi-class classification to produce class probabilities.
- **Tanh**: Can be used in hidden layers but is less common due to potential vanishing gradient issues in deep networks.
- **Leaky ReLU**: Useful in hidden layers if you're concerned about dead neurons; allows some gradient for negative values.
- **ELU**: Another alternative to ReLU for hidden layers; can improve performance in deeper networks by offering smoother gradients for negative values.

In most cases for MNIST, a simple model with **ReLU in hidden layers** and **Softmax in the output layer** performs well, offering a good balance between training speed and accuracy.

---

## Loss Functions

For the MNIST digit classification task, which involves multi-class classification (10 classes, digits 0–9), choosing the loss function is crucial for effective training. Here’s a breakdown of suitable loss functions:

### 1. **Categorical Cross-Entropy**

- **Best for**: Multi-class classification with one-hot encoded labels.
- **Definition**: Categorical cross-entropy measures the difference between the true label distribution (one-hot encoded) and the predicted probability distribution from the model.
- **Why Use It**: It’s the standard choice for multi-class classification tasks like MNIST, as it encourages the model to output high probabilities for the correct class while minimising incorrect ones.

```python
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```
- **Input Labels**: Labels need to be **one-hot encoded** (e.g., `[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]` for digit "2").

### 2. **Sparse Categorical Cross-Entropy**

- **Best for**: Multi-class classification where labels are not one-hot encoded (i.e., labels are integers representing each class).
- **Definition**: Sparse categorical cross-entropy works similarly to categorical cross-entropy but allows for integer rather than one-hot encoded format labels.
- **Why Use It**: This is convenient when the labels are provided as integers (0–9 for MNIST), avoiding the need to one-hot encode them.

```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```
- **Input Labels**: Labels should be integers representing the class (e.g., `2` for the digit "2").

### 3. **Binary Cross-Entropy** (if using binary or multi-label approach)

- It is best for binary classification or when MNIST is framed as multiple binary tasks (e.g., detecting a specific digit vs all others).
- **Definition**: Binary cross-entropy measures the difference between predicted and true binary labels for each output neuron.
- **Why Use It**: If you are framing MNIST as a binary problem (e.g., "Is this a 5 or not?"), binary cross-entropy can be effective. However, this is less common than treating MNIST as a multi-class problem.

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```
- **Input Labels**: Binary format for each digit detection (1 for the target class, 0 for others).

### Choosing Between `Categorical Cross-Entropy` and `Sparse Categorical Cross-Entropy`

- **Categorical Cross-Entropy**: Use this if your labels are one-hot encoded (e.g., `[0, 0, 1, 0, ...]`).
- **Sparse Categorical Cross-Entropy**: Use this if your labels are integers (e.g., `0`, `1`, ..., `9`). This avoids the need to one-hot encode labels and performs equally well.

### Why Not Use Mean Squared Error (MSE) or MAE?

- **MSE or MAE** are typically used for regression tasks and are unsuitable for multi-class classification problems like MNIST. They don't provide the model with meaningful gradients for probabilities in classification.

### Summary

For a standard MNIST model:

- **Use `categorical_crossentropy`** if labels are one-hot encoded.
- **Use `sparse_categorical_crossentropy`** if labels are integer-encoded.

Either approach will help the model learn efficiently, but `sparse_categorical_crossentropy` is often preferred for simplicity when labels are in integer format.

---

## Initialisers

In neural networks, **initialisers** determine the initial values of the weights before training begins. Proper initialisation can help the model converge faster and avoid issues like vanishing or exploding gradients. Here are some common initialisers that are well-suited for the MNIST dataset:

### 1. **Glorot (Xavier) Initialisation**
   - **Best for**: Deep networks with ReLU, tanh, or linear activation functions.
   - **Definition**: Sets initial weights based on a uniform or normal distribution, scaled to keep the variance of activations across layers constant.
   - **Why Use It**: Glorot initialisation is widely used as a general-purpose initialiser and is effective for shallow and moderately deep networks, including fully connected (dense) networks used in MNIST.
   - **Example**:
     ```python
     from tensorflow.keras.initializers import GlorotUniform
     model.add(Dense(128, activation='relu', kernel_initializer=GlorotUniform()))
     ```

### 2. **He Initialisation**
   - **Best for**: Networks using ReLU and its variants (like Leaky ReLU and ELU) in the hidden layers.
   - **Definition**: He initialisation scales weights by $\sqrt{\frac{2}{\text{number of input units}}}$ and can use uniform or normal distribution.
   - **Why Use It**: He initialisation helps counteract the vanishing gradient problem, making it especially useful for deeper networks with ReLU activations. It’s very effective on image data like MNIST, as it allows better signal propagation through the network.
   - **Example**:
     ```python
     from tensorflow.keras.initializers import HeUniform
     model.add(Dense(128, activation='relu', kernel_initializer=HeUniform()))
     ```

### 3. **Lecun Initialisation**
   - **Best for**: Networks using `tanh` activation, though it can also be effective for `sigmoid` activation.
   - **Definition**: Scales weights by $\sqrt{\frac{1}{\text{number of input units}}}$ and is based on a normal or uniform distribution.
   - **Why Use It**: Lecun initialisation is designed to work well with `tanh`, which is sometimes used for image classification tasks when ReLU isn't optimal. It helps to prevent saturation of `tanh` units, which can slow down training.
   - **Example**:
     ```python
     from tensorflow.keras.initializers import LecunNormal
     model.add(Dense(128, activation='tanh', kernel_initializer=LecunNormal()))
     ```

### 4. **Random Normal or Random Uniform**
   - **Best for**: General-purpose initialiser; can be used in simpler models or as a baseline.
   - **Definition**: Initialises weights from a normal or uniform distribution, typically with a mean of 0 and a small standard deviation.
   - **Why Use It**: Random normal or uniform initialisation can be helpful for experimenting, but it’s usually less effective for deep networks as it lacks the specific scaling that Glorot or He initialisers provide.
   - **Example**:
     ```python
     from tensorflow.keras.initializers import RandomNormal
     model.add(Dense(128, activation='relu', kernel_initializer=RandomNormal(mean=0.0, stddev=0.05)))
     ```

### 5. **Orthogonal Initialisation**
   - **Best for**: Deep networks, especially recurrent networks, though it can sometimes improve convergence in other architectures.
   - **Definition**: Initialises weights as an orthogonal matrix, helping preserve gradient norms through layers, which can be particularly helpful in maintaining signal flow in deep networks.
   - **Why Use It**: Although it's less common in CNNs or shallow networks, orthogonal initialisation can sometimes improve convergence stability in dense or convolutional layers with deeper architectures.
   - **Example**:
     ```python
     from tensorflow.keras.initializers import Orthogonal
     model.add(Dense(128, activation='relu', kernel_initializer=Orthogonal(gain=1.0)))
     ```

### Summary of Recommendations for MNIST
- **ReLU Activation**: Use **He initialisation** (e.g., `HeUniform`).
- **Tanh Activation**: Use **Lecun initialisation** (e.g., `LecunNormal`).
- **General-purpose**: **Glorot initialisation** works well in most cases, especially for shallower networks.

For a typical MNIST model with ReLU activations in hidden layers and a softmax output, **He initialisation** for hidden layers and **Glorot initialisation** as a general-purpose choice are highly effective and should yield good results.

---

## Optimisers

For training a model on the MNIST dataset, the choice of optimiser significantly impacts how quickly and effectively the model converges. Since MNIST is a relatively simple dataset, many optimisers perform well, but certain optimisers are particularly well-suited for improving training speed and stability. Here are the best optimisers to try for MNIST:

### 1. **Adam (Adaptive Moment Estimation)**
   - **Description**: Adam combines the advantages of other popular optimisers, AdaGrad and RMSprop, by adapting the learning rate individually for each parameter and using momentum.
   - **Why Use It**: Adam is widely used in practice because it converges quickly and works well for most tasks, including MNIST. It adapts learning rates, making it easier to use without much hyperparameter tuning.
   - **Recommended Settings**: The default settings (`learning_rate=0.001`, `beta_1=0.9`, `beta_2=0.999`) generally work well.
   - **Example**:
     ```python
     from tensorflow.keras.optimizers import Adam
     model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
     ```

### 2. **SGD with Momentum (Stochastic Gradient Descent with Momentum)**
   - **Description**: Standard SGD updates weights by applying the same learning rate to each parameter, but adding **momentum** helps accelerate convergence and reduce oscillations in the gradient path.
   - **Why Use It**: SGD with momentum can work well for MNIST, especially with a carefully tuned learning rate. It may converge slower than Adam, but with momentum, it achieves good accuracy on simpler datasets.
   - **Recommended Settings**: Try a learning rate between `0.01` and `0.1` with momentum around `0.9`.
   - **Example**:
     ```python
     from tensorflow.keras.optimizers import SGD
     model.compile(optimizer=SGD(learning_rate=0.01, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])
     ```

### 3. **RMSprop**
   - **Description**: RMSprop (Root Mean Square Propagation) scales the learning rate based on a moving average of the squared gradients, which helps stabilise network updates with noisy gradients.
   - **Why Use It**: RMSprop effectively handles complex network gradients, which can help on more challenging datasets. It often performs similarly to Adam on MNIST.
   - **Recommended Settings**: The default learning rate (`0.001`) typically works well.
   - **Example**:
     ```python
     from tensorflow.keras.optimizers import RMSprop
     model.compile(optimizer=RMSprop(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
     ```

### 4. **AdaGrad (Adaptive Gradient Algorithm)**
   - **Description**: AdaGrad adapts the learning rate for each parameter based on the history of gradients, allowing it to perform smaller updates for parameters that receive larger gradients.
   - **Why Use It**: AdaGrad is particularly useful for sparse data. While it’s less common for image tasks like MNIST, it can work well if the data is sparse or the initial learning rate is set carefully.
   - **Recommended Settings**: The default learning rate (`0.01`) works in many cases but can be lowered if it converges too quickly.
   - **Example**:
     ```python
     from tensorflow.keras.optimizers import Adagrad
     model.compile(optimizer=Adagrad(learning_rate=0.01), loss='categorical_crossentropy', metrics=['accuracy'])
     ```

### 5. **Nadam (Adam with Nesterov Momentum)**
   - **Description**: Nadam is a variant of Adam that incorporates Nesterov momentum, which adjusts the momentum term for better performance, particularly in deep networks.
   - **Why Use It**: Nadam can converge faster than Adam sometimes and may yield better accuracy on tasks like MNIST.
   - **Recommended Settings**: Use the default learning rate of `0.002`, which is slightly higher than the Adam default.
   - **Example**:
     ```python
     from tensorflow.keras.optimizers import Nadam
     model.compile(optimizer=Nadam(learning_rate=0.002), loss='categorical_crossentropy', metrics=['accuracy'])
     ```

### 6. **Adamax (Variant of Adam)**
   - **Description**: Adamax is a variant of Adam based on the infinity norm, which is more stable in some cases where Adam may become unstable.
   - **Why Use It**: It can be particularly helpful for datasets with higher dimensional data or noisy gradients, though it performs similarly to Adam for MNIST.
   - **Recommended Settings**: A default learning rate of `0.002` generally performs well.
   - **Example**:
     ```python
     from tensorflow.keras.optimizers import Adamax
     model.compile(optimizer=Adamax(learning_rate=0.002), loss='categorical_crossentropy', metrics=['accuracy'])
     ```

### Summary of Recommendations
For MNIST, **Adam** and **SGD with momentum** are generally the most effective choices:

- **Adam**: Good default optimiser for most tasks, performing well on MNIST with minimal tuning.
- **SGD with Momentum**: Often yields competitive accuracy with Adam but may require more tuning (learning rate and momentum).
- **RMSprop**: A strong alternative to Adam, especially for more complex models.
- **Nadam**: Slightly faster convergence than Adam sometimes due to Nesterov momentum.

Adam will be the best starting point in most cases due to its adaptability and efficiency, but experimenting with **SGD with momentum** and **Nadam** can also yield good results on MNIST.

---

## Regularisers

Regularisation techniques help prevent overfitting in neural networks by controlling the model's complexity. Regularisation is often beneficial to improve generalisation for the MNIST dataset, which is a relatively simple dataset, especially if you’re using a more complex model than necessary for the task. Here are the best regularisers to use for MNIST:

### 1. **Dropout**
   - **Description**: Dropout randomly "drops" (sets to zero) a fraction of neurons in a layer during each training iteration. This forces the model to learn redundant representations and prevents reliance on specific neurons.
   - **Why Use It**: Dropout is one of the most effective regularisation techniques for dense (fully connected) layers and convolutional layers. It’s especially useful for preventing overfitting in slightly deeper networks or when the model achieves high accuracy on training data but struggles to generalise.
   - **Recommended Settings**: A dropout rate of `0.2` to `0.5` works well for MNIST.
   - **Example**:
     ```python
     from tensorflow.keras.layers import Dropout
     model.add(Dense(128, activation='relu'))
     model.add(Dropout(0.5))  # Drops 50% of neurons during training
     ```

### 2. **L2 Regularization (Ridge Regularization)**
   - **Description**: L2 regularisation adds a penalty equal to the squared magnitude of weights to the loss function, encouraging the model to keep weights small, which can help with generalisation.
   - **Why Use It**: L2 regularisation is effective for dense layers, as it reduces the risk of large weights and helps prevent overfitting. It’s suitable for MNIST when using dense layers or even in convolutional layers for more complex architectures.
   - **Recommended Settings**: Typical values range from `0.001` to `0.0001`.
   - **Example**:
     ```python
     from tensorflow.keras.regularizers import l2
     model.add(Dense(128, activation='relu', kernel_regularizer=l2(0.001)))
     ```

### 3. **L1 Regularization (Lasso Regularization)**
   - **Description**: L1 regularisation adds a penalty equal to the absolute magnitude of weights, promoting sparsity by driving some weights to zero. This can help in pruning unnecessary connections, making the model simpler.
   - **Why Use It**: While less common than L2, L1 can be helpful if you want to introduce sparsity in your model. For MNIST, L1 is useful if you’re interested in building a lightweight or sparse model with fewer active weights.
   - **Recommended Settings**: Common values range from `0.001` to `0.0001`.
   - **Example**:
     ```python
     from tensorflow.keras.regularizers import l1
     model.add(Dense(128, activation='relu', kernel_regularizer=l1(0.001)))
     ```

### 4. **L1_L2 Regularisation (Elastic Net)**
   - **Description**: Combines L1 and L2 regularisation, adding both absolute and squared weight penalties to the loss function.
   - **Why Use It**: L1_L2 regularisation offers the benefits of both sparsity (from L1) and weight decay (from L2), making it more flexible. It can be useful if you want the advantages of both L1 and L2 regularisation.
   - **Recommended Settings**: Set L1 and L2 values, typically around `0.001`.
   - **Example**:
     ```python
     from tensorflow.keras.regularizers import l1_l2
     model.add(Dense(128, activation='relu', kernel_regularizer=l1_l2(l1=0.001, l2=0.001)))
     ```

### 5. **Batch Normalisation**
   - **Description**: While not strictly a regulariser, batch normalisation normalises inputs to each layer, helping to stabilise and accelerate training.
   - **Why Use It**: Batch normalisation can reduce overfitting by adding a small amount of noise during training and making the network more robust. It also helps by allowing the use of higher learning rates and reducing the need for other regularisers.
   - **Example**:
     ```python
     from tensorflow.keras.layers import BatchNormalization
     model.add(Dense(128, activation='relu'))
     model.add(BatchNormalization())
     ```

### Choosing Regularisers for MNIST
For MNIST, you likely don’t need heavy regularisation, but a combination of **Dropout** and **L2 regularisation** works effectively for most architectures. Here’s a recommended setup:

1. **Dropout**: Use Dropout layers (with `0.2`–`0.5` dropout rate) after dense layers to prevent overfitting.
2. **L2 Regularisation**: Add L2 regularisation on dense or convolutional layers with a small factor (`0.001` or `0.0001`) to prevent large weights.

### Example Architecture with Dropout and L2 Regularisation
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.regularizers import l2

model = Sequential()
model.add(Dense(128, activation='relu', kernel_regularizer=l2(0.001), input_shape=(784,)))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
```

### Summary
- **Best Regularisers for MNIST**: **Dropout** and **L2 regularisation**.
- **Dropout** helps prevent overfitting by adding noise to the network and forcing redundant feature learning.
- **L2 Regularisation** reduces large weights, promoting simpler models.
- **Batch Normalisation** can benefit stability and training speed, though it’s often used instead of traditional regularisers in some setups.

This combination should help improve generalisation and prevent overfitting for MNIST.

## CNN

A **CNN (Convolutional Neural Network)** is a type of deep learning model primarily used for analysing and processing visual data, such as images and videos. CNNs are particularly powerful for image recognition and classification tasks because they can automatically learn to detect features (such as edges, textures, and shapes) directly from raw pixel data. 

### Key Components of a CNN Model

1. **Convolutional Layers**:
   - The convolutional layer is the core building block of a CNN. It applies **filters (kernels)** to the input data, which slide over the image, performing element-wise multiplications and generating **feature maps**. 
   - Each filter detects specific features, like edges, textures, or patterns. The network learns which filters are most useful for detecting different image features during training.
   - **Example**: In a CNN for MNIST, a convolutional layer might detect edges of the digit shapes in the first few layers.

2. **Activation Function**:
   - After each convolution operation, an **activation function** is applied to introduce non-linearity. 
   - **ReLU (Rectified Linear Unit)** is the most commonly used activation in CNNs because it helps prevent the vanishing gradient problem and speeds up training.

3. **Pooling (Downsampling) Layers**:
   - Pooling layers reduce the spatial size of the feature maps, making the network computationally efficient and reducing the risk of overfitting.
   - The most common type is max pooling. This method takes the maximum value in each region, helping to retain the most prominent features.
   - Pooling layers maintain the most important information while reducing less important details, allowing the model to focus on high-level patterns.

4. **Fully Connected (Dense) Layers**:
   - After several convolutional and pooling layers, the data is typically flattened (converted into a 1D vector) and passed through one or more dense layers.
   - Dense layers act as a classifier and make the final predictions. They take the features extracted by convolutional layers and learn to associate them with specific max pooling classes.

5. **Output Layer**:
   - The output layer provides the final predictions. For classification, a **softmax** activation is typically used to produce probabilities for each class.

### Architecture of a Typical CNN
A basic CNN model often has the following architecture:

1. **Input Layer**: Takes in raw pixel data (e.g., 28x28 for MNIST).
2. **Convolutional + ReLU Layer(s)**: Extracts basic features like edges.
3. **Pooling Layer(s)**: Reduces spatial dimensions.
4. **Additional Convolutional + Pooling Layers**: Extract more complex patterns as you go deeper into the network.
5. **Flatten Layer**: Converts the 2D matrix into a 1D vector to connect with dense layers.
6. **Dense (Fully Connected) Layer(s)**: Learns to classify based on features extracted by previous layers.
7. **Output Layer**: Outputs probabilities for each class.

### Example CNN Architecture for MNIST
Here’s how a simple CNN for classifying MNIST digits might look in Keras:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))  # 32 filters, 3x3 kernel
model.add(MaxPooling2D((2, 2)))  # Downsamples by 2x2
model.add(Conv2D(64, (3, 3), activation='relu'))  # More filters for deeper features
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())  # Converts 2D feature maps to 1D vector
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))  # 10 output classes for digits 0-9
```

### Why CNNs Are Effective for Image Data
- **Local Feature Detection**: By using small filters, CNNs can capture local patterns in the input images, such as edges and textures, and gradually build up to more complex features.
- **Parameter Efficiency**: By sharing weights (using the same filter across the image), CNNs reduce the number of parameters compared to fully connected networks, making them more efficient and less prone to overfitting.
- **Hierarchical Feature Learning**: As you move deeper into the network, CNNs can learn hierarchical features, starting with simple edges and moving on to complex shapes and objects.

### Applications of CNNs
CNNs are used in many applications beyond basic image classification:
- **Image Recognition and Classification** (e.g., handwritten digit recognition with MNIST, object detection).
- **Image Segmentation** (e.g., medical imaging to segment tumours).
- **Face Recognition** (e.g., facial feature detection).
- **Video Analysis** (e.g., action recognition in videos).
- **Natural Language Processing** (e.g., text classification, using 1D convolutions).

In summary, CNNs are powerful neural networks designed to automatically and effectively extract visual features from images. They are a top choice for computer vision tasks like MNIST classification.

# Summary