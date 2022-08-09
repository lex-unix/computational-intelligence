import random

GENOME_LENGTH = 2


class Individual:
    genome = []
    fitness = 0

    def __init__(self, function, genome=None):
        if genome is None:
            if hasattr(function, 'MIN'):
                self.genome = [random.uniform(
                    function.MIN, function.MAX) for _ in range(2)]
            else:
                x = random.uniform(function.MIN_X, function.MAX)
                y = random.uniform(function.MIN_Y, function.MAX)
                self.genome = [x, y]
        else:
            self.genome = genome
