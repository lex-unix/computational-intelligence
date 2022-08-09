import random
import pandas as pd

from math import sin


def my_function(x1, x2, x3):
    return sin(x1) + sin(x2) - sin(x3)


X1 = [random.randint(0, 8) for x in range(40)]
X2 = [random.randint(1, 9) for x in range(40)]
X3 = [random.randint(-2, 6) for x in range(40)]
D = []

for x1, x2, x3 in zip(X1, X2, X3):
    D.append(my_function(x1, x2, x3))

data = {
    'x1': X1,
    'x2': X2,
    'x3': X3,
    'd1': D,
}

df = pd.DataFrame(data)

if df['d1'].is_unique:
    avrg = sum(D) / len(D)
    D2 = []
    for d in D:
        D2.append(0 if d < avrg else 1)
    df['d2'] = D2
    df['avrg'] = [avrg for x in range(len(df))]
    # df.to_excel('data.xlsx')
    print('Created file')
