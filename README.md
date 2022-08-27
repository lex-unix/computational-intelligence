# Computational Intelligence

## Table of content 
1. [Syllabus](#syllabus)
2. [Usage](#usage)
    * [Lab 1](#lab-1)
    * [Lab 2](#lab-2)
3. [Notes](#notes)

## Syllabus

The course consists of 7 labs:
* Lab 1 - Perceptron
* Lab 2 - Backpropagation algorithm
* Lab 3 - Genetic algorithm
* Lab 4 - Evolution strategies
* Lab 5 - Fuzzy inference systems
* Lab 6 - ANFIS
* Lab 7 - Deformed Stars method


## Usage

### Lab 1
Given the training set of $X$. Each element of $X$ is multiplied by the appropriate 
weight factor of $W$. The result is called activation $a$.

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
where $ \eta $ is learning rate.


Then find new value of $W$:
```math
w_{i}(n+1)=w_{i}(n)+\Delta_{i}, i= \overline{i,n} 
```


### Lab 2
There are multiple files for this lab. They are:
* Data generation - ```data.py```
* Data normalization - ```normalize.py```
* Backpropagation algorithm - ```backpropagation.py```

How to use it:
1. Generate data based on function you need to predict values for.
2. Normalize data.
3. Run backpropagation algorithm.


## Notes
**Be aware that Genetic Algorithm in Lab 3 is not correctly implemented and yet to be fixed**
