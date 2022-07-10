import random


class Individ:
    solutions = []
    fitness = 0

    def __init__(self, F, solutions=None):
        if solutions is None:
            x = random.uniform(F.MIN_X, F.MAX_X)
            y = random.uniform(F.MIN_Y, F.MAX_Y)
            self.solutions = [x, y]

        else:
            self.solutions = solutions
