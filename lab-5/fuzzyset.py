import matplotlib.pyplot as plt
import matplotlib.patches as patches


def get_h(h1, h2):
    return min(h1, h2)


def get_alpha(alpha1, alpha2, h, h1, h2):
    return h * (alpha1 / h1 + alpha2 / h2)


def get_beta(beta1, beta2, h, h1, h2):
    return h * (beta1 / h1 + beta2 / h2)


def get_lower_modal(m1, m2, alpha1, alpha2, alpha):
    return m1 + m2 - alpha1 - alpha2 + alpha


def get_upper_modal(m1, m2, beta1, beta2, beta):
    return m1 + m2 + beta1 + beta2 - beta


def add_sets(a, b):
    h = get_h(a[-1], b[-1])
    alpha = get_alpha(a[2], b[2], h, a[-1], b[-1])
    beta = get_beta(a[3], b[3], h, a[-1], b[-1])
    lower_modal = get_lower_modal(a[0], b[0], a[2], a[2], alpha)
    upper_modal = get_upper_modal(a[1], b[1], a[3], b[3], beta)

    return [lower_modal, upper_modal, alpha, beta, h]


a = [470, 470, 0, 0, 1]
b = [385, 520, 0, 50, 1]
c = [300, 300, 100, 0, .8]
d1 = [0, 0, 0, 0, .2]
d2 = [385, 385, 0, 200, .8]
f1 = [0, 0, 0, 0, .8]
f2 = [380, 390, 10, 20, .2]

scenarios = []

s = add_sets(a, b)
s = add_sets(s, c)
s = add_sets(s, d1)
s = add_sets(s, f1)

scenarios.append(s)

s = add_sets(a, b)
s = add_sets(s, c)
s = add_sets(s, d2)
s = add_sets(s, f1)

scenarios.append(s)

s = add_sets(a, b)
s = add_sets(s, c)
s = add_sets(s, d2)
s = add_sets(s, f2)

scenarios.append(s)

s = add_sets(a, b)
s = add_sets(s, c)
s = add_sets(s, d1)
s = add_sets(s, f2)

scenarios.append(s)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim(1000, 2400)
ax.set_ylim(0, 1)

colors = ['b', 'r', 'g', 'y']
for i, (s, color) in enumerate(zip(scenarios, colors), 1):
    x = [s[0] - s[2], s[1] + s[3], s[1], s[0]]
    y = [0, 0, s[-1], s[-1]]

    ax.add_patch(patches.Polygon(xy=list(zip(x, y)),
                 color=color, label='S' + str(i), fill=False))


plt.title('Investment approximation')
plt.xlabel('Money')
plt.ylabel('Probability')

plt.legend()
plt.show()
