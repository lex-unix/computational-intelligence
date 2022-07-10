import numpy as np
from numpy.random import random_sample
from distance import DISTANCE

epochs = 500
d = np.array(DISTANCE)
n_ants = 50
n_cities = len(d)
evaporation_rate = .7
alpha = 2
beta = 2

visibility = 1 / d
visibility[visibility == np.inf] = 0

pheromone = .1 * np.ones((n_ants, n_cities))

route = np.ones((n_ants, n_cities + 1))

for _ in range(epochs):
    route[:, 0] = 1

    for i in range(n_ants):
        temp_visibility = np.array(visibility)

        for j in range(n_cities - 1):
            location = int(route[i, j] - 1)
            temp_visibility[:, location] = 0

            pheromone_feat = np.power(pheromone[location, :], alpha)
            visibility_feat = np.power(temp_visibility[location, :], beta)

            numerator = np.multiply(pheromone_feat, visibility_feat)
            denominator = np.sum(numerator)

            probability = numerator / denominator

            cummulative = np.cumsum(probability)
            city = np.nonzero(cummulative > random_sample())[0][0] + 1

            route[i, j + 1] = city

    optimal_route = np.array(route)
    dist_cost = np.zeros((n_ants, 1))

    for i in range(n_ants):
        s = 0
        for j in range(n_cities - 1):
            current_city = int(optimal_route[i, j]) - 1
            next_city = int(optimal_route[i, j + 1]) - 1
            s += d[current_city, next_city]

        dist_cost[i] = s

    dist_min_index = np.argmin(dist_cost)
    dist_min_cost = dist_cost[dist_min_index]
    best_route = route[dist_min_index, :]

    elite_dist = 1 / dist_min_cost
    pheromone = (1 - evaporation_rate) * pheromone
    for i in range(n_ants):
        dt = 1 / dist_cost[i]
        for j in range(n_cities - 1):

            current_city = int(optimal_route[i, j]) - 1
            next_city = int(optimal_route[i, j + 1]) - 1
            pheromone[current_city, next_city] += dt
            for k in range(n_cities - 1):
                if optimal_route[i, j] - 1 == best_route[k] - 1:
                    if optimal_route[i, j + 1] - 1 == best_route[k + 1] - 1:
                        pheromone[current_city, next_city] += elite_dist
                        break
                    else:
                        break

total_distance = int(dist_min_cost[0]) + d[int(best_route[-2]) - 1, 0]
print('Optimal route: ', best_route)
print(f'Total distance: {total_distance}km')
