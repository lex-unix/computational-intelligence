import operator
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import randn
from functions import GoldsteinPrice, Holder, McCormick
from individ import Individ


LAMBDA = 100
MU = 20
STEP_SIZE = .1
F = GoldsteinPrice
N_EPOCH = 40
SCOPE = np.asarray([[F.MIN_X, F.MAX_X], [F.MIN_Y, F.MAX_Y]])


def in_scope(solution):
    for i in range(len(SCOPE)):
        if solution[i] < SCOPE[i, 0] or solution[i] > SCOPE[i, 1]:
            return False

    return True


def create_population():
    return [Individ(F) for x in range(LAMBDA)]


def fitness(individ, f):
    return f(individ.solutions[0], individ.solutions[1])


def select_best_parents(population):
    sorted_population = sorted(population, key=operator.attrgetter('fitness'))
    selected = [individ for i, individ in enumerate(
        sorted_population) if i < MU]
    return selected


def get_children(population):
    children = []
    for individ in population:
        possible_solution = None
        for _ in range(int(LAMBDA / MU)):
            while possible_solution is None or not in_scope(possible_solution):
                possible_solution = individ.solutions + randn(2) * STEP_SIZE
            child = Individ(F, possible_solution)
            children.append(child)

    return children


best_solution, best_fitness = None, 1000
errors = []

population = create_population()

for epoch in range(N_EPOCH):

    for individ in population:
        individ.fitness = fitness(individ, F.f)

    population = select_best_parents(population)

    for individ in population:
        if individ.fitness < best_fitness:
            best_solution, best_fitness = individ.solutions, individ.fitness

    errors.append(abs(F.RES - best_fitness))

    children = get_children(population)

    population = children

print(f'Final solutions {best_solution}\nFinal fitness {best_fitness}')

x = np.arange(0, N_EPOCH, 1)

plt.plot(x, errors)
plt.xlabel('К-сь ітерацій')
plt.ylabel('Помилка')

plt.show()
