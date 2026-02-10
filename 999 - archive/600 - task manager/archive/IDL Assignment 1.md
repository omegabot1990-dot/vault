---
tags:
  - academic
  - idl
description: assignment one for IDL
due date: 2024-11-10
start date: 2024-10-25
end date: 2024-11-14
status: Archive
importance level: important
urgency level: not urgent
task type: distil
story points: 
parent nodes: 
child nodes: 
recurrent:
---
# NEED TO CATCH UP
Links: [Docs](https://docs.google.com/document/d/1tG19S-RBs1BCHhRWdJnBnFGtFtDNZHQv-oqXSOyeDS4/edit#heading=h.13fo8yvo49g3) 

[[deep_learning_assignment_one.pdf]]

## Experiments

1. MNIST
	1. Metrics	
	2. Layers
	3. Activations
	4. Initialisations
	5. Optimisers
	6. Regularisers

## Results

#### Layers

> Layers: 1, Neurons: 10, Epochs: 10

```
Test loss: 0.2438032031059265
Test accuracy: 0.9302999973297119
Test precision: 0.9439885020256042
Test recall: 0.920199990272522
Test top-K categorical accuracy: 0.9951000213623047
Test mean squared error: 0.010528499260544777
```

> Layers: 1, Neurons: 10, Epochs: 20

```
Test loss: 0.22163449227809906
Test accuracy: 0.9390000104904175
Test precision: 0.9481881260871887
Test recall: 0.9315000176429749
Test top-K categorical accuracy: 0.9965000152587891
Test mean squared error: 0.00945283193141222
```

- Doubling the epochs only showed a slight increase in accuracy of ~1%

> Layers: 1, Neurons: 20, Epochs: 10

```
Test loss: 0.17500679194927216
Test accuracy: 0.95169997215271
Test precision: 0.9586206674575806
Test recall: 0.9452000260353088
Test top-K categorical accuracy: 0.9976999759674072
Test mean squared error: 0.007680268958210945
```

- Doubling the number of neurons increased the accuracy by about ~2%

> Layers: 1, Neurons: 50, Epochs: 10

```
Test loss: 0.0968627855181694
Test accuracy: 0.9718999862670898
Test precision: 0.9762192368507385
Test recall: 0.9688000082969666
Test top-K categorical accuracy: 0.9994000196456909
Test mean squared error: 0.004330483730882406
```

- Increasing the neurons from 10 to 50 increased the accuracy by ~4%

> Layers: 2, L1: 10, L2: 10, Epochs: 10

```
Test loss: 0.23749643564224243
Test accuracy: 0.9327999949455261
Test precision: 0.9452195167541504
Test recall: 0.9214000105857849
Test top-K categorical accuracy: 0.9957000017166138
Test mean squared error: 0.010264994576573372
```

- Adding a new layer did not make much of a difference to the accuracy

> Layers: 2, L1: 10, L2: 10, Epochs: 20

```
Test loss: 0.22345326840877533
Test accuracy: 0.9375
Test precision: 0.9468269348144531
Test recall: 0.9294999837875366
Test top-K categorical accuracy: 0.9966999888420105
Test mean squared error: 0.009612875059247017
```

> Layers: 2, L1: 20, L2: 10, Epochs: 10

```
Test loss: 0.1752960979938507
Test accuracy: 0.9502000212669373
Test precision: 0.9585407972335815
Test recall: 0.9433000087738037
Test top-K categorical accuracy: 0.998199999332428
Test mean squared error: 0.0076533714309334755
```

> Layers: 2, L1: 10, L2: 20, Epochs: 10

```
Test loss: 0.2029501050710678
Test accuracy: 0.9423999786376953
Test precision: 0.9527647495269775
Test recall: 0.933899998664856
Test top-K categorical accuracy: 0.9973999857902527
Test mean squared error: 0.008937104605138302
```

> Layers: 3, L1: 10, L2: 10, L3: 10, Epochs: 10

```
Test loss: 0.2904787063598633
Test accuracy: 0.9172999858856201
Test precision: 0.9326606392860413
Test recall: 0.9057999849319458
Test top-K categorical accuracy: 0.9945999979972839
Test mean squared error: 0.012611188925802708
```

> Layers: 3, L1: 20, L2: 10, L3: 10, Epochs: 10

```
Test loss: 0.14490242302417755
Test accuracy: 0.9578999876976013
Test precision: 0.9638127684593201
Test recall: 0.953499972820282
Test top-K categorical accuracy: 0.9979000091552734
Test mean squared error: 0.006349713541567326
```

> Layers: 3, L1: 10, L2: 10, L3: 20, Epochs: 10

```
Test loss: 0.22090618312358856
Test accuracy: 0.9369000196456909
Test precision: 0.9468909502029419
Test recall: 0.9289000034332275
Test top-K categorical accuracy: 0.9961000084877014
Test mean squared error: 0.009699106216430664
```

> Layers: 3, L1: 20, L2: 20, L3: 20, Epochs: 10

```
Test loss: 0.14551028609275818
Test accuracy: 0.9567999839782715
Test precision: 0.9634467363357544
Test recall: 0.9514999985694885
Test top-K categorical accuracy: 0.998199999332428
Test mean squared error: 0.0065310243517160416
```

> Layers: 3, L1: 50, L2: 25, L3: 10, Epochs: 10

```
Test loss: 0.1037573590874672
Test accuracy: 0.9714000225067139
Test precision: 0.9743486642837524
Test recall: 0.9685999751091003
Test top-K categorical accuracy: 0.9993000030517578
Test mean squared error: 0.0045462376438081264
```

> Layers: 2, L1: 50, L2: 25, Epochs: 10

```
Test loss: 0.09056785702705383
Test accuracy: 0.9722999930381775
Test precision: 0.975764274597168
Test recall: 0.970300018787384
Test top-K categorical accuracy: 0.9993000030517578
Test mean squared error: 0.004260252695530653
```

> Layers: 2, L1: 50, L2: 50, Epochs: 10

```
Test loss: 0.10807005316019058
Test accuracy: 0.9695000052452087
Test precision: 0.9725655913352966
Test recall: 0.9678000211715698
Test top-K categorical accuracy: 0.9991999864578247
Test mean squared error: 0.004716948140412569
```

> Layers: 2, L1: 100, L2: 75, Epochs: 10

```
Test loss: 0.07764901220798492
Test accuracy: 0.9781000018119812
Test precision: 0.979252278804779
Test recall: 0.9769999980926514
Test top-K categorical accuracy: 0.9998000264167786
Test mean squared error: 0.003424893133342266
```

> Layers: 2, L1: 200, L2: 120, Epochs: 10

```
Test loss: 0.07957062870264053
Test accuracy: 0.9807000160217285
Test precision: 0.9816761612892151
Test recall: 0.980400025844574
Test top-K categorical accuracy: 0.9994999766349792
Test mean squared error: 0.003105627605691552
```

> Layers: 2, L1: 300, L2: 200, Epochs: 10

```
Test loss: 0.08631500601768494
Test accuracy: 0.9812999963760376
Test precision: 0.981496274471283
Test recall: 0.9812999963760376
Test top-K categorical accuracy: 0.9998999834060669
Test mean squared error: 0.0030793510377407074
```

> Layers: 2, L1: 500, L2: 350, Epochs: 10

```
Test loss: 0.08898917585611343
Test accuracy: 0.9800999760627747
Test precision: 0.9804843664169312
Test recall: 0.9797000288963318
Test top-K categorical accuracy: 0.9998999834060669
Test mean squared error: 0.0032298858277499676
```

#### Activations

> Layers: 2, L1: 300, L2: 200, Epochs: 10

> L1: tanh, L2: tanh

```
Test loss: 0.06428603082895279
Test accuracy: 0.9797000288963318
Test precision: 0.9819403886795044
Test recall: 0.9786999821662903
Test top-K categorical accuracy: 0.9997000098228455
Test mean squared error: 0.003040277399122715
```

> L1: tanh, L2: relu

```
Test loss: 0.07761719077825546
Test accuracy: 0.9796000123023987
Test precision: 0.9802743792533875
Test recall: 0.9789999723434448
Test top-K categorical accuracy: 0.9997000098228455
Test mean squared error: 0.0032880741637200117
```

> L1: leaky relu, L2: leaky relu

```
Test loss: 0.07757598161697388
Test accuracy: 0.9810000061988831
Test precision: 0.9817708134651184
Test recall: 0.9801999926567078
Test top-K categorical accuracy: 1.0
Test mean squared error: 0.0030086578335613012
```

> L1: elu, L2: elu

```
Test loss: 0.0709763616323471
Test accuracy: 0.9810000061988831
Test precision: 0.9824613928794861
Test recall: 0.9803000092506409
Test top-K categorical accuracy: 0.9998000264167786
Test mean squared error: 0.002992040943354368
```

#### Initialisations

> Layers: 2, L1: 300, L2: 200, Epochs: 10

> Glorot

```
Test loss: 0.09305544197559357
Test accuracy: 0.9805999994277954
Test precision: 0.9813776612281799
Test recall: 0.9801999926567078
Test top-K categorical accuracy: 0.9998000264167786
Test mean squared error: 0.0032494976185262203
```

> He

```
Test loss: 0.07477743923664093
Test accuracy: 0.9824000000953674
Test precision: 0.9833717346191406
Test recall: 0.9817000031471252
Test top-K categorical accuracy: 0.9998000264167786
Test mean squared error: 0.0028018320444971323
```

> Random Normal (mean = 0, sd = 0.05)

```
Test loss: 0.07988206297159195
Test accuracy: 0.9815000295639038
Test precision: 0.9826791882514954
Test recall: 0.9815000295639038
Test top-K categorical accuracy: 0.9998000264167786
Test mean squared error: 0.002964798826724291
```

> Random Normal (mean = 0, sd = 0.1)

```
Test loss: 0.08943638950586319
Test accuracy: 0.9794999957084656
Test precision: 0.98017817735672
Test recall: 0.9790999889373779
Test top-K categorical accuracy: 0.9998999834060669
Test mean squared error: 0.0033740501385182142
```

> Orthogonal (gain = 1.0)

```
Test loss: 0.07817064225673676
Test accuracy: 0.9822999835014343
Test precision: 0.9828794598579407
Test recall: 0.9817000031471252
Test top-K categorical accuracy: 0.9998000264167786
Test mean squared error: 0.0028929589316248894
```

> Orthogonal (gain = 2.0)

```
Test loss: 0.0848960429430008
Test accuracy: 0.9811000227928162
Test precision: 0.9816798567771912
Test recall: 0.9805999994277954
Test top-K categorical accuracy: 0.9998000264167786
Test mean squared error: 0.0031458712182939053
```

#### Optimisers

> Layers: 2, L1: 300, L2: 200, Epochs: 10
> Initialiser: Orthogonal

> Adam, $\alpha$ = 0.001

```
Test loss: 0.08890875428915024
Test accuracy: 0.9779000282287598
Test precision: 0.9787702560424805
Test recall: 0.977400004863739
Test top-K categorical accuracy: 0.9997000098228455
Test mean squared error: 0.003617183305323124
```

> Adam, $\alpha$ = 0.005

```
Test loss: 0.14048105478286743
Test accuracy: 0.9742000102996826
Test precision: 0.9755486249923706
Test recall: 0.9735000133514404
Test top-K categorical accuracy: 0.9984999895095825
Test mean squared error: 0.004267182666808367
```

> Adam, $\alpha$ = 0.0001

```
Test loss: 0.0932369977235794
Test accuracy: 0.9717000126838684
Test precision: 0.9764017462730408
Test recall: 0.9682000279426575
Test top-K categorical accuracy: 0.9993000030517578
Test mean squared error: 0.0043295519426465034
```

> SGD, $\alpha$ = 0.01, momentum = 0.9

```
Test loss: 0.0788249596953392
Test accuracy: 0.9757000207901001
Test precision: 0.9788668751716614
Test recall: 0.9726999998092651
Test top-K categorical accuracy: 0.9997000098228455
Test mean squared error: 0.0037609406281262636
```

> SGD, $\alpha$ = 0.1, momentum = 0.9

```
Test loss: 0.09324391186237335
Test accuracy: 0.9768999814987183
Test precision: 0.9781628847122192
Test recall: 0.9764999747276306
Test top-K categorical accuracy: 0.9995999932289124
Test mean squared error: 0.003643510863184929
```

> SGD, $\alpha$ = 0.05, momentum = 0.9

```
Test loss: 0.062350042164325714
Test accuracy: 0.9832000136375427
Test precision: 0.9840745329856873
Test recall: 0.9825000166893005
Test top-K categorical accuracy: 0.9997000098228455
Test mean squared error: 0.0026637455448508263
```

> RMSProp, $\alpha$ = 0.001

```
Test loss: 0.07757742702960968
Test accuracy: 0.9814000129699707
Test precision: 0.9819819927215576
Test recall: 0.9810000061988831
Test top-K categorical accuracy: 0.9998999834060669
Test mean squared error: 0.003113008802756667
```

> RMSProp, $\alpha$ = 0.01

```
Test loss: 0.2711627781391144
Test accuracy: 0.9639999866485596
Test precision: 0.9663620591163635
Test recall: 0.9624000191688538
Test top-K categorical accuracy: 0.9980999827384949
Test mean squared error: 0.005998213309794664
```

> RMSProp, $\alpha$ = 0.005

```
Test loss: 0.18158793449401855
Test accuracy: 0.9779999852180481
Test precision: 0.9782847762107849
Test recall: 0.9775999784469604
Test top-K categorical accuracy: 0.9993000030517578
Test mean squared error: 0.0038646801840513945
```

#### Regularisers

> Layers: 2, L1: 300, L2: 200, Epochs: 10
> Initialiser: Orthogonal
> Optimiser: SGD, $\alpha$ = 0.05, momentum = 0.9

> Dropout = 0.5

```
Test loss: 0.07986593246459961
Test accuracy: 0.9758999943733215
Test precision: 0.9795569181442261
Test recall: 0.9726999998092651
Test top-K categorical accuracy: 0.9991999864578247
Test mean squared error: 0.0036631638649851084
```

# Summary

## Introduction

This document utilises Keras, a high-level deep-learning framework developed on TensorFlow, to define and train neural networks. Keras streamlines the development of intricate models, thereby making it particularly suitable for constructing and training neural networks. A Multilayer Perceptron (MLP) constitutes a fully connected network comprising a minimum of three layers—input, hidden, and output—for classification and regression purposes. In contrast, a Convolutional Neural Network (CNN) is specifically designed to analyse images and videos, where convolutional layers effectively capture spatial patterns. This assignment aims to compare MLP and CNN architectures, adjust hyperparameters, and assess their performance.
## Task 1

Task 1 consists of two parts:

1. **Part 1**: Using the MNIST dataset of handwritten digits, explore two Keras examples with an MLP and a CNN to build basic neural networks.

2. **Part 2**: 
   - **a)** Develop an MLP for the Fashion MNIST dataset (28x28 grayscale images, 10 classes) and apply the same model to the CIFAR-10 dataset (32x32 RGB images, 10 classes).
   - **b)** Build a CNN for Fashion MNIST and replicate it for CIFAR-10.

These exercises will deepen our understanding of initialisation, activation functions, optimisers, regularisation, and architectures.

#### Task 1.1

We undertook experiments utilising various metrics to comprehend the influence of architecture and hyperparameter tuning on the performance of Multi-Layer Perceptrons (MLP) and Convolutional Neural Networks (CNN). The metrics employed encompassed accuracy, precision, recall, top-k categorical accuracy, and mean squared error, thus providing valuable insights into the efficacy of each model.

Our initial experiments involved adjusting layers. For the MLP, increasing depth and width led to slight performance drops, likely due to the model’s increased complexity on simpler datasets. For the CNN, adding `Conv2D` layers before dense layers significantly improved performance by capturing spatial patterns more effectively. We tested multiple activation functions (`tanh`, `elu`, `leaky-relu`), observing minimal variation among them. Initialisations such as Glorot, He, and Orthogonal yielded close results within a 2% range. Among optimisers, SGD slightly outperformed others, with similar results from Adam and RMSProp. Dropout at 0.4 proved most effective for regularisation.

This experiment demonstrated the influence of architecture and hyperparameters on MLP and CNN models, enhancing our ability to tune networks for optimal performance across different tasks.

#### Task 1.2.a

This series of experiments investigates the performance impact of various neural network architectures and hyperparameter configurations on the Fashion MNIST and CIFAR-10 datasets. Employing a Multilayer Perceptron (MLP) approach, we assess three distinct configurations featuring varying activation functions, dropout rates, and optimisers. By applying these models to both datasets, our objective is to elucidate how architectural choices influence performance, especially when progressing from a simpler dataset (Fashion MNIST) to a more complex, higher-dimensional one (CIFAR-10).

**Experiment 1**: The inaugural model incorporates ReLU activations, a three-layer structure, HeNormal initialisation, and a 30% dropout rate. It is optimised using the Adam optimiser and aims to strike a balance between depth and regularisation.
**Experiment 2**: The subsequent model utilises ELU activations with a slightly reduced depth (three dense layers comprising 512, 256, and 128 nodes) alongside a 25% dropout rate with HeNormal initialisation. This model is optimised with RMSprop to examine the implications of a smoother gradient approach.
**Experiment 3**: We experiment with a larger model employing LeakyReLU activations in the final configuration. This model consists of 1024, 512, and 256 nodes per layer, accompanied by a higher dropout rate (40%) to mitigate overfitting. Optimised with Stochastic Gradient Descent (SGD) and momentum, it assesses the impact of a gradual, stabilised gradient descent on both datasets.

Each model was initially trained on the Fashion MNIST dataset, following which the same configurations were applied to CIFAR-10. To facilitate comparing performance across datasets, accuracy-related metrics (precision, recall, and top-k categorical accuracy) and error-related metrics (mean squared error) were thoroughly evaluated.

The experiments produced significant insights into the ways architectural choices affect performance on diverse datasets. The first model, characterised by ReLU activations and the Adam optimiser, performed effectively on Fashion MNIST but exhibited limited adaptability to the more complex CIFAR-10 data, likely due to the simpler activation and optimiser configurations. Conversely, utilising ELU and RMSprop, the second model displayed enhanced adaptability to CIFAR-10, manifesting a smoother convergence across epochs. Nevertheless, the third model, integrating LeakyReLU and SGD, yielded the most balanced performance, particularly on CIFAR-10, where the heightened complexity necessitated robust regularisation and meticulous gradient descent. In summary, this series of experiments accentuates the significance of regularisation, activation function selection, and optimiser tuning when transitioning from a simpler dataset to a more intricate one, such as CIFAR-10. 

#### Task 1.2.b

In this series of experiments, we investigate the performance of three distinct Convolutional Neural Network (CNN) architectures applied to the Fashion MNIST and CIFAR-10 datasets. Each model configuration incorporates unique combinations of activation functions, optimisers, and regularisation techniques. By implementing these models on both datasets, we aim to elucidate how architectural designs and hyperparameter selections influence performance across varying levels of data complexity. 

**Experiment 1**: This model utilises ReLU activations and consists of two convolutional layers incorporating MaxPooling for down-sampling, followed by a fully connected layer with a dropout mechanism. The Adam optimiser is employed, with the objective of achieving rapid convergence accompanied by minimal regularisation. 

**Experiment 2**: This model builds upon the first by integrating BatchNormalisation after each convolutional layer to stabilise and expedite the training process. With three convolutional layers and a more extensive dense layer, the RMSprop optimiser, which maintains a decaying moving average of gradients for enhanced learning control, is utilised. 

**Experiment 3**: The final model employs LeakyReLU activations and incorporates L2 regularisation for each convolutional layer to mitigate overfitting. It also features an elevated dropout rate and utilises SGD with momentum, aiming to balance regularisation and stable, gradual optimisation.  

Each model is initially trained and evaluated on the relatively simpler Fashion MNIST dataset and subsequently tested on the more complex CIFAR-10 dataset. Performance is assessed using metrics such as accuracy, precision, recall, top-k categorical accuracy, and loss.

The experiments underscored the influence of CNN depth, normalisation, and activation functions on performance across datasets. The first model employing ReLU and Adam exhibited reasonable performance on Fashion MNIST but encountered difficulties with CIFAR-10, revealing constraints in generalising to more complex data. The second model, characterised by BatchNormalisation and RMSprop, demonstrated enhanced stability when applied to CIFAR-10, implying that normalisation facilitates handling higher-dimensional inputs. The third model, featuring LeakyReLU and regularisation, exhibited the most effective adaptability to CIFAR-10, particularly due to its robust regularisation and gradual optimisation through SGD. This study accentuates the significance of architectural choices and regularisation strategies when transferring models from simpler datasets to more intricate ones.  

## Task 1 Conclusion

This study conducted a comparative analysis of Multi-Layer Perceptron (MLP) and Convolutional Neural Network (CNN) architectures utilising the Fashion MNIST and CIFAR-10 datasets. The findings indicate that Convolutional Neural Networks significantly surpass Multi-Layer Perceptrons in performance when engaging with complex datasets such as CIFAR-10, attributable to their enhanced capacity for capturing spatial patterns. While Multi-Layer Perceptrons exhibited satisfactory performance on the less intricate Fashion MNIST dataset, they encountered considerable difficulties with CIFAR-10, even after undergoing hyperparameter tuning, thereby underscoring their limitations in handling high-dimensional image data. In contrast, Convolutional Neural Networks, particularly those incorporating dropout, L2 regularisation, and BatchNormalisation, demonstrated a commendable adaptability to CIFAR-10, effectively learning spatial dependencies. This observation reinforces the assertion that Convolutional Neural Networks are essential for tasks involving complex and structured data, highlighting the necessity for architectural choices that align with the dataset’s complexity. 

# Report (TODO)

### Introduction

We will use Keras/TensorFlow to define and train simple neural networks among the numerous deep-learning libraries. Keras is an open-source deep-learning framework that offers an intuitive interface for constructing and training neural networks. It operates on top of lower-level deep learning libraries such as TensorFlow and Theano, providing a high-level abstraction that simplifies the development of complex machine learning models. 

A Multilayer Perceptron (MLP) is a fully connected neural network characterised by at least three layers: an input layer, one or more hidden layers, and an output layer. MLPs serve as foundational models for both classification and regression tasks. 

In contrast, a Convolutional Neural Network (CNN) is specifically designed for processing and analysing images, videos, and data grids. Its convolutional layers enable the model to effectively capture spatial hierarchies and patterns within the data. 

Through this assignment, we aim to gain practical experience by comparing various MLP and CNN architectures, manually tuning hyperparameters, and assessing their impact on model performance. Ultimately, we will apply this knowledge to develop a complex CNN to address the “tell-the-time” challenge.

### Task 1

Task 1 is divided into two parts. The first part focuses on the MNIST dataset, which consists of handwritten digits. We will explore two Keras examples utilising an MLP and a CNN network to gain practical experience constructing simple neural networks. The second part builds on these insights and requires us to: a) develop an MLP network for the Fashion MNIST dataset (includes 28x28 2D grayscale images, categorised into ten classes) and apply the same configuration to the CIFAR-10 dataset (includes 32x32x3 RGB images, also divided into ten categories); and b) create a CNN network for the Fashion MNIST dataset and replicate that configuration for the CIFAR-10 dataset. These exercises helped us understand the use of various initialisation strategies, activation functions, optimisers, regularisers, and diverse architectures. 

### Task 1.1

We started with metrics for this task, hoping to understand how architecture and hyperparameter tuning would affect them. We experimented with accuracy (the ratio of correctly predicted instances (both positive and negative) to the total cases), precision (the ratio of correctly predicted positive instances to all predicted positives), recall (the ratio of correctly predicted positive instances to all actual positive instances), top-k-categorical accuracy (the fraction of predictions where the correct label is among the top-k predicted labels), and mean squared error (mean squared error calculates the average squared difference between predicted and actual values), these will be referred to as “metrics” from now on. 

We then tried experimenting with layers, first with dense layers, making them wider and deeper. With the MLP network, we noticed that making the network either too wide or too deep caused the metrics to show a slight decrease in performance. This is because the dataset is relatively simple, and adding complexity to the network would work detrimentally to regularisation. With the CNN network, we saw that adding the `Conv2D` layers before the Dense helped increase performance; this could be because the convoluted layers help the model capture spacial hierarchies and patterns better and improve classification. We then experimented with activations with both networks. The MLP and CNN networks did not vary much with `tanh`, `elu` and `leaku-relu`. We also tried a mixture of multiple activations, and it showed similar results. We then experimented with Glorot, He, Random Normal (mean = 0, sd = 0.05), Random Normal (mean = 0, sd = 0.1), Orthogonal (gain = 1.0) and Orthogonal (gain = 2.0) initialisation strategies, all of the strategies gave results within a 2% difference. We experimented with Adam, SGD with momentum and RMSProp and got the best result with SGD, though we achieved similar results with all optimisers mentioned again within a 2% difference. We then moved on to testing Dropout, L1 and L2 and no Dropout, and we got the best results with Dropout of 0.4.

This experiment helped us understand how to manipulate different architectures and hyperparameters, how this gave different metrics, and how to create and tune MLP and CNN networks.

#### Task 1.1.a

On the Fashion MNIST dataset, we decided to undertake 25 epochs of training. Our first experiment involved a deep network with three layers: 512 neurons in the first two layers and 256 in the third. We also found that a dropout rate of 0.3 helped, so we used a standard Adam Optimiser with the default learning rate. For the second one, we decided to try a different activation and went with ELU; we reduced the dropout to 0.25 and stuck with the RMSProp optimiser from the MNIST example because it's good with classification tasks. Finally, we tried a deep and wide network with 1024 neurons in the first layers, dividing the number of neurons by half till the third layer; we went with a leaky ReLU activation coupled with an SGD optimiser for controlled learning.
We found that the first experiment resulted in an accuracy of ~89.3%, the second with ~86.8%, and the third with ~88.9% on testing. We notice that having more layers yields better results in this case, mostly because of the increase in complexity over the MNIST dataset that required fewer layers. Also, we see that removing the dropout decreases the accuracy along with other metrics. The leaky ReLU with wider layers helped capture the patterns more; the SGD optimiser helped get a better result, as seen in the previous example with MNIST. On using the first network to train on the CIFAR 10 dataset, we could only get an accuracy of ~41.4%, but we had a precision of around ~77.5%. 