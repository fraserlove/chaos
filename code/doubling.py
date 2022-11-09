import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
# Figure dpi
dpi = 90

def plot(f, a, b, s):
    x = np.arange(a, b + s, s)
    fig = plt.figure(figsize=(300/dpi, 300/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    y = []
    xp = []
    for i in range(len(x)): y.append(f(x[i]))
    for i in range(len(x)): xp.append(1/2)

    ax.plot(x[:len(x) // 2], y[:len(y) // 2], c='#444444', lw=1.4)
    ax.plot(x[len(x) // 2:], y[len(y) // 2:], c='#444444', lw=1.4)
    ax.plot(xp, y, c='#444444', lw=1, alpha=0.4, linestyle='dashed')

    ax.annotate('$s_i = l$', (1/4, 0), (1/4 - 0.1, -0.09), 'axes fraction')
    ax.annotate('$s_i = r$', (3/4, 0), (3/4 - 0.1, -0.09), 'axes fraction')
    ax.annotate('$\\frac{1}{2}$', (1/2, 0), (1/2 - 0.015, -0.1), 'axes fraction')
    ax.set_xlim(a, b)
    ax.set_ylim(min(y), max(y))
    ax.set_xticks(np.arange(min(x), max(x)+1, 1))
    ax.set_yticks(np.arange(min(y), max(y)+1, 1))
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')

    plt.savefig('./images/doubling.pdf'.format(a, b), dpi=dpi * 10, bbox_inches='tight')

def f(x):
    return np.mod(2 * x, 1)

plot(f, 0, 1, 0.0001)