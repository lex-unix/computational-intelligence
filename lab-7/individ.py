import random
from math import sqrt, cos, log


a = -5
b = 5
n = 50


class Individ:
    x = 0
    fitness = 0

    def __init__(self, x=None):
        if x is None:
            self.x = random.uniform(a, b)
        else:
            self.x = x

        self.getFitness()

    def getFitness(self):
        x = self.x
        numerator = 100 * sqrt(100 - x**2) * cos(x**2) * cos(x)
        denominator = (x**2 + 10) * log(100 - x**2)
        self.fitness = numerator / denominator
