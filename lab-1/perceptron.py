import random


def logicFunction(x1, x2, x3):
    return (x1 and x2) or x3


def activation(X, W, teta):
    summ = 0
    for x, w in zip(X, W):
        summ += x * w
    return 1 if summ >= teta else 0


def learn(X, T, W, teta, learning_rate):
    answer = True
    Y = activation(X, W, teta)
    if Y != T:
        answer = False
        error = T - Y
        teta = error * teta * learning_rate
        W_new = []
        for x, w in zip(X, W):
            W_new.append(w + learning_rate * error * x)
        W = W_new
    return W, teta, answer


X1 = [0, 1]
X2 = [0, 1]
X3 = [0, 1]
learning_rates = [0.2, 0.04, 0.08]
for rate in learning_rates:
    W = [random.random() for w in range(3)]
    teta = random.random()
    i = 1
    print(f'Learning rate {rate}')
    while True:
        teta_new = teta
        answers = []
        for x1 in X1:
            for x2 in X2:
                for x3 in X3:
                    X = [x1, x2, x3]
                    T = logicFunction(x1, x2, x3)
                    W, teta_new, answer = learn(X, T, W, teta_new, rate)
                    answers.append(answer)
        i += 1
        if False not in answers:
            break
    print(f'Final parameters on {i} iteration: teta - {teta_new}, W - {W}')
