import random
import pandas as pd

from math import exp


def sigmoid(s):
    return 1 / (1 + exp(-s))


def activate(X, W):
    summ = 0
    for x, w in zip(X, W):
        summ += w * x
    return sigmoid(summ)


def derevative(y):
    return (1 - y) * y


def create_network(n_d, n_hidden, n_y):
    network = []
    hidden_layer = [{'w': [random.random() for x in range(n_d)]}
                    for x in range(n_hidden)]
    output_layer = [{'w': [random.random() for x in range(n_hidden)]}
                    for x in range(n_y)]

    network.append(hidden_layer)
    network.append(output_layer)

    return network


def forwardpropagation(network, X):
    output = X
    for layer in network:
        new_output = []
        for neuron in layer:
            activation = activate(neuron['w'], output)
            neuron['y'] = activation
            new_output.append(neuron['y'])
        output = new_output

    return output


def backpropogation(network, D):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = []

        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0
                for neuron in network[i + 1]:
                    error += (neuron['delta'] * neuron['w'][j])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(neuron['y'] - D[j])

        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * derevative(neuron['y'])


def correct_weights(network, X, l_rate):
    for i in range(len(network)):
        new_X = X
        if i != 0:
            new_X = [neuron['y'] for neuron in network[i - 1]]

        for neuron in network[i]:
            for j in range(len(new_X)):
                neuron['w'][j] -= l_rate * neuron['delta'] * new_X[j]


def train(network, data, l_rate=0.8):
    e = .01
    while True:
        sum_error = 0
        for i in range(len(data)):
            X = data.loc[i, ['x1', 'x2', 'x3']].values.tolist()
            D = data.loc[i, ['d1', 'd2']].values.tolist()
            Y = forwardpropagation(network, X)
            backpropogation(network, D)
            correct_weights(network, X, l_rate)
            sum_error += sum([(d - y)**2 for d, y in zip(D, Y)]) / len(D)

        if sum_error / len(data) < e:
            break
        data.sample(frac=1).reset_index(drop=True)


def test(network, data):
    predictions = []
    for i in range(len(data)):
        X = data.loc[i, ['x1', 'x2', 'x3']].values.tolist()
        Y = forwardpropagation(network, X)
        predictions.append(Y)

    return predictions


data = pd.read_excel('data/normalized_data.xlsx')
data.drop(columns=['Unnamed: 0'], inplace=True)

network = create_network(3, 15, 2)

train(network, data.iloc[:30])

predictions_df = data.iloc[30:, :].copy(deep=True)
predictions_df.reset_index(drop=True, inplace=True)

predictions = test(network, predictions_df)


predictions_df.loc[:, ['y1']] = 0
predictions_df.loc[:, ['y2']] = 0

for i, prediction in enumerate(predictions):
    for j, y in enumerate(prediction):
        predictions_df.loc[i, ['y' + str(j + 1)]] = y

predictions_df.to_excel('data/prediction.xlsx')


# import numpy as np
# import matplotlib.pyplot as plt

# X = np.linspace(1, 10, 10)

# Y1 = np.arange(0, 10)
# Y2 = predictions

# plt.plot(X, Y1, X, Y2)

# plt.title('Dataset graph')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
