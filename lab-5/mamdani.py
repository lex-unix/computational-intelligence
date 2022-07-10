import numpy as np
from sympy import Point, Line, Float
import matplotlib.pyplot as plt
import matplotlib.patches as patches


a1 = [100, 200, 30, 40, 1]
a2 = [200, 300, 20, 60, 1]
b1 = [140, 240, 30, 40, 1]
b2 = [240, 320, 50, 40, 1]
c1 = [50, 100, 10, 30, 1]
c2 = [100, 150, 20, 50, 1]
intitial_values = [220, 200]

set1 = [a1, b1, c1]
set2 = [a2, b2, c2]


def get_coordinate(xp, fp, x):
    y = np.interp(x, xp, fp)
    return y


def find_line(s, x):
    if x in range(s[0], s[1] + 1):
        return [s[0], s[1]], [s[-1], s[-1]]
    elif x in range(s[0] - s[2], s[0] + 1):
        return [s[0] - s[2], s[0]], [0, s[-1]]
    else:
        return [s[1], s[1] + s[3]], [s[-1], 0]


def find_intersections(s, alpha):
    line1 = [[0, s[-1]], [s[0] - s[2], s[0]]]
    line2 = [[0, s[-1]], [s[1] + s[3], s[1]]]
    return get_coordinate(*line1, alpha), get_coordinate(*line2, alpha)


def expand_coordinates(s):
    return [[s[2], 0], [s[0], s[-1]], [s[1], s[-1]], [s[3], 0]]


def get_z(z1, z2):
    z = []
    z.append([min(z1[0][0], z2[0][0]), 0])
    flag = True
    i = 1
    while i != 3:
        if z1[i][0] in range(int(z2[i - 1][0]), int(z2[i][0] + 1)):
            if z1[i][1] > z2[i][1] and flag:
                z.append([z1[i][0], z1[i][1]])
                flag = False
                continue
            else:
                p1 = Point(z1[i][0], z1[i][1])
                p2 = Point(z1[i + 1][0], z1[i + 1][1])
                p3 = Point(z2[i - 1][0], z2[i - 1][1])
                p4 = Point(z2[i][0], z2[i][1])
                line1 = Line(p1, p2)
                line2 = Line(p3, p4)
                intersection = line1.intersection(line2)
                points = intersection[0]
                x, y = float(Float(points.x)), float(Float(points.y, 2))
                z.append([x, y])

        if z1[i][0] < z2[i][0] and z1[i][1] > z2[i][1]:
            z.append([z1[i][0], z1[i][1]])
        else:
            z.append([z2[i][0], z2[i][1]])

        i += 1

    z.pop()
    z.append(z2[-2])
    z.append(z2[-1])
    return z


def polygon_area(xs, ys):
    return 0.5 * (np.dot(xs, np.roll(ys, 1)) - np.dot(ys, np.roll(xs, 1)))


def polygon_centroid(xs, ys):
    xy = np.array([xs, ys])
    c = np.dot(xy + np.roll(xy, 1, axis=1),
               xs * np.roll(ys, 1) - np.roll(xs, 1) * ys
               ) / (6 * polygon_area(xs, ys))
    return c


alphas1 = []
for i in range(len(set1) - 1):
    for value in intitial_values:
        line = find_line(set1[i], value)
        alpha = get_coordinate(*line, value)
        alphas1.append(alpha)


alphas2 = []
for i in range(len(set2) - 1):
    for value in intitial_values:
        line = find_line(set2[i], value)
        alpha = get_coordinate(*line, value)
        alphas2.append(alpha)

intersection1 = find_intersections(c1, np.min(alphas1))
intersection2 = find_intersections(c2, np.min(alphas2))

z1 = [intersection1[0], intersection1[1],
      c1[0] - c1[2], c1[3] + c1[1], np.min(alphas1)]
z2 = [intersection2[0], intersection2[1],
      c2[0] - c2[2], c2[3] + c2[1], np.min(alphas2)]


z1_expanded = expand_coordinates(z1)
z2_expanded = expand_coordinates(z2)

z = get_z(z1_expanded, z2_expanded)
z_points = list(zip(*z))
x, y = z_points
z0 = polygon_centroid(x, y)

print(z0)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_ylim(0, 1)
ax.set_xlim(0, 500)

ax.add_patch(patches.Polygon(xy=z,
             label='Z', color='r', fill=False))

plt.plot(z0[0], 0, 'go', label='Z0')

plt.title('Mamdani fuzzy inference system')
plt.xlabel('x coordinates')
plt.ylabel('Probabily')

plt.legend()
plt.show()
