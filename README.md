# Computational Intelligence

## Table of content

1. [Syllabus](#syllabus)
2. [Labs](#usage)
   - [Lab 1](#lab-1)
   - [Lab 2](#lab-2)

## Syllabus

The course consists of 7 labs:

- [Lab 1](#lab-1) - **Perceptron**
- [Lab 2](#lab-2) - **Backpropagation algorithm**
- [Lab 3](#lab-3) - **Genetic algorithm**
- [Lab 4](#lab-4) - **Evolution strategies** & **Ant colony optimization algorithm**
- [Lab 5](#lab-5) - **Fuzzy inference systems**
- [Lab 6](#lab-6) - **ANFIS** (Adaptive Neuro-Fuzzy Inference System)
- [Lab 7](#lab-7) - **Deformed Stars method**

## Labs

### Lab 1

Given the training set of $X$. Each element of $X$ is multiplied by the appropriate weight factor of $W$. The result is called activation $a$.

Train model for such equation:

```math
(x_{1} \wedge x_{2}) \vee x_{3}
```

Activation function:

```math
Y = \begin{cases}
 1 & x \geq \theta \\
 0 & x < \theta
\end{cases}
```

If computed value is wrong, the difference between computed value $(Y)$ and real value $(T)$ is calculated:

```math
\delta = T - Y
```

To adjust weight first calculate:

```math
\Delta_{i}= \eta  \delta x_{i}
```

where $\eta$ is learning rate.

Then find new value of $W$:

```math
w_{i}(n+1)=w_{i}(n)+\Delta_{i}, i= \overline{i,n}
```

### Lab 2

Here we use sigmoid as activation function:

```math
f(x)= \frac{1}{1+ e^{-x} }
```

To get the computed values as closer to real as possible we need to minimize the cost function and find the new weights using gradient descent:

```math
E(w)= \sum_{i=1}^k \sum_{j=1}^m ( d_{ij} -  y^{2}_{ij} )^{2}
```

We can normalize input with such function:

```math
 x'= \frac{x-\min(x)}{\max(x)-\min(x)}
```

We test this network with 3, 6 and 10 neurons in hidden layer.

The test function is:

```math
\sin(x_{1}) + \sin(x_{2}) - \sin(x_{3})
```

There are multiple files for this lab. They are:

- Data generation - `data.py`
- Data normalization - `normalize.py`
- Backpropagation algorithm - `backpropagation.py`

How to use it:

1. Generate data based on function you need to predict values for.
2. Normalize data.
3. Run backpropagation algorithm.
