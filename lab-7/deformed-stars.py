import random
import operator
from individ import Individ, a, b, n


step_size = .1
e = .0001

epoch = 0
popultaion_t = [Individ() for x in range(n)]
while True:
    popultaion_z = []

    for individ in popultaion_t:
        new_individ = individ.x + random.random() * step_size

        if new_individ < a:
            new_individ += (b - a)
        elif new_individ > b:
            new_individ += (a - b)

        new_individ = Individ(new_individ)
        popultaion_z.append(new_individ)

    population_s = []
    i = [x for x in range(n)]
    j = [x for x in range(n)]
    random.shuffle(i)
    random.shuffle(j)

    for k in range(n):
        new_individ = (popultaion_z[i[k]].x + popultaion_z[j[k]].x) / 2
        new_individ = Individ(new_individ)
        population_s.append(new_individ)

    population = popultaion_t + popultaion_z + population_s

    sorted_population = sorted(population, key=operator.attrgetter('fitness'))

    popultaion_t = sorted_population[:n]

    epoch += 1

    if abs(popultaion_t[0].fitness - popultaion_t[1].fitness) < e:
        break

print(f'Epoch {epoch}')
print(f'x = {popultaion_t[0].x:.3f}')
print(f'fitness = {popultaion_t[0].fitness:.3f}')
