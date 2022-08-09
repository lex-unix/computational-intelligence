import random
import operator
import pandas as pd

from individual import Individual, GENOME_LENGTH
from functions import Holder, McCormick, GoldsteinPrice

INVERSION_CHANCE = .01
MUTATION_COUNT = None
MUTATION_CHANCE = .01
N = 40
F = Holder


def create_population():
    return [Individual(F) for _ in range(N)]


def fitness(data, f):
    return f(data[0], data[1])


def panmixia(population):
    A = random.choice(population)
    B = random.choice(population)

    return A, B


def mutation(Child):
    if random.random() < MUTATION_CHANCE:
        index = random.randint(0, GENOME_LENGTH - 1)
        if hasattr(F, 'MIN'):
            Child.genome[index] = random.uniform(F.MIN, F.MAX)
        else:
            Child.genome[index] = random.uniform(
                F.MIN_X, F.MAX) if index == 0 else random.uniform(F.MIN_Y, F.MAX)

    return Child


def inversion(Child):
    if random.random() < INVERSION_CHANCE:
        Child.genome = Child.genome[::-1]
    return Child


def new_individual(population):

    A, B = panmixia(population)

    index = random.randint(1, GENOME_LENGTH - 1)
    Child_1 = Individual(F, A.genome[:index] + B.genome[index:])
    Child_2 = Individual(F, B.genome[:index] + A.genome[index:])

    if random.random() < .5:
        return inversion(mutation(Child_1))
    else:
        return inversion(mutation(Child_2))


population = create_population()

for _ in range(25000):

    for individ in population:
        individ.fitness = (fitness(individ.genome, F.f))

    sorted_population = sorted(population, key=operator.attrgetter('fitness'))

    population = sorted_population[:int(N / 2) - 1]

    new_population = [new_individual(population) for x in range(N)]

    population = new_population


for individ in population:
    individ.fitness = (fitness(individ.genome, F.f))

sorted_population = sorted(population, key=operator.attrgetter('fitness'))

population = sorted_population[:int(N / 2) - 1]

for individ in population:
    print(individ.genome, individ.fitness)

data = {
    'Fitness': [individ.fitness for individ in population],
    'X': [individ.genome[0] for individ in population],
    'Y': [individ.genome[1] for individ in population]
}

df = pd.DataFrame(data)

df.index = [index for index in range(1, len(df) + 1)]

df.to_excel('data/goldsteinPrice.xlsx')
