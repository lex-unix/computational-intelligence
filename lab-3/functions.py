from math import sin, cos, exp, sqrt, pi

class Holder:
    MIN = -10
    MAX = 10
    RES = -19.2085

    def f(x, y):
        return -abs(sin(x) * cos(y) * exp( abs(1 - sqrt(x**2 + y**2) / pi) ) )


class GoldsteinPrice:
    MIN = -2
    MAX = 2
    RES = 3

    def f(x, y):
        part_one = int(1 + (x + y + 1)**2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6 * x * y + 3 * y**2))
        part_two = int(30 + (2 * x - 3 * y)**2 * (18 - 32 * x + 12 * x**2 + 48 * y - 36 * x * y + 27 * y**2))
        return part_one * part_two


class McCormick:
    MIN_X = -1.5
    MIN_Y = -3
    MAX = 4
    RES = -1.913
    def f(x, y):
        return sin(x + y) + (x - y)**2 - 1.5 * x + 2.5 * y + 1