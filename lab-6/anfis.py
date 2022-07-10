import random
import numpy as np
import pandas as pd
from numpy.random import randn
from numpy import exp


l_rate = .0002
n_x = 3
n_rules = 3
epochs = 1000


def first_derivative(x, b, c):
    return 2 * (x - b) / c


def second_derivative(x, b, c):
    return 2 * (x - b)**2 / c**3


def activate(x, b, c):
    return exp(-((x - b)**2 / c**2))


def get_signal_products(activations):
    signal_product = np.array([])
    for i in range(N):
        prod = 1
        for j in range(n_rules):
            prod *= activations.T[i, j]

        signal_product = np.append(signal_product, prod)

    return signal_product


def correct_parameters(xs, error, activations, signal_product, defuzzys):
    summ = sum(np.multiply(signal_product, defuzzys))
    for n in range(len(data)):
        for i in range(n_x):
            prod = np.prod(
                activations[i], where=activations[i] != activations[i][n])

            a = 1 / sum(signal_product)
            b = defuzzys[n] - summ
            b *= prod
            derivative_1 = error * a * b * first_derivative(
                xs[i], param_b[i, n], param_c[i, n]) * activations[i, n]

            derivative_2 = error * a * b * second_derivative(
                xs[i], param_b[i, n], param_c[i, n]) * activations[i, n]

            param_b[i, n] -= l_rate * derivative_1
            param_c[i, n] -= l_rate * derivative_2

        derivative = error * signal_product[n] / sum(signal_product)
        A[n] -= l_rate * derivative
        B[n] -= l_rate * derivative
        C[n] -= l_rate * derivative


data = pd.read_excel('data/data-bp.xlsx')
N = len(data)

A = np.asarray([random.random() for x in range(len(data))])
B = np.asarray([random.random() for x in range(len(data))])
C = np.asarray([random.random() for x in range(len(data))])

param_b = np.asarray([randn(len(data)) + 30 for x in range(n_x)])
param_c = np.asarray([randn(len(data)) + 15 for x in range(n_x)])

errors = 0
for epoch in range(epochs):
    errors = 0
    prev_error = errors
    for k in range(len(data)):
        xs = data.loc[k, ['x1', 'x2', 'x3']].values.tolist()

        activations = np.array([])
        for i in range(n_x):
            for j in range(len(data)):
                activation = activate(
                    xs[i], param_b[i, j], param_c[i, j])

                activations = np.append(activations, activation)

        activations = activations.reshape(n_x, len(data))

        signal_products = get_signal_products(activations)

        normalized = np.asarray([w / sum(signal_products)
                                for w in signal_products])

        defuzzys = np.array([])
        for a, b, c in zip(A, B, C):
            defuzz = a * xs[0] + b * xs[1] + c * xs[2]
            defuzzys = np.append(defuzzys, defuzz)

        zs = np.multiply(normalized, defuzzys)
        z = sum(zs)
        y = data.at[k, 'y']
        error = z - y
        correct_parameters(xs, error, activations, signal_products, defuzzys)

        error = (z - y)**2
        errors += error

    data.sample(frac=1).reset_index(drop=True)
    print(f'Epoch {epoch}: {errors / len(data)}')

data = [[12, 21, 34],
        [14, 14, 14],
        [20, 20, 20]]
prediction = []

for k in range(3):

    xs = data[k]

    activations = np.array([])
    for i in range(n_x):
        for j in range(N):
            activation = activate(
                xs[i], param_b[i, j], param_c[i, j])

            activations = np.append(activations, activation)

    activations = activations.reshape(n_x, N)

    signal_products = get_signal_products(activations)

    normalized = np.asarray([w / sum(signal_products)
                            for w in signal_products])

    defuzzys = np.array([])
    for a, b, c in zip(A, B, C):
        defuzz = a * xs[0] + b * xs[1] + c * xs[2]
        defuzzys = np.append(defuzzys, defuzz)

    zs = np.multiply(normalized, defuzzys)
    z = sum(zs)
    prediction.append(z)

print(prediction)
