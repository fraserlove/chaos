import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
# Figure dpi
dpi = 70

h = 0.6

def plot(f, t, a, b, s):
    x = np.arange(a, b + s, s)
    fig = plt.figure(figsize=(300/dpi, 300/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    y = []
    yp = []
    for i in range(len(x)): y.append(f(x[i]))
    for i in range(len(x)): yp.append(t(x[i]))

    ax.plot(x, y, c='#444444', lw=1.4)
    ax.plot(x, [h for i in x], c='#444444', lw=1, alpha=0.4)
    ax.plot(x, x, c='#444444', lw=1, alpha=0.4)
    ax.plot(x, yp, c='#444444', lw=1.4, linestyle='dashed', alpha=0.7)

    ax.annotate('$h$', (x[0], h), (-0.06, h - 0.02), 'axes fraction')
    ax.set_xlim(a, b)
    ax.set_ylim(min(y), max(y))
    ax.set_xticks(np.arange(min(x), max(x)+1, 1))
    ax.set_yticks(np.arange(min(y), max(y)+1, 1))
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')

    plt.savefig('./images/truncated_tent.pdf'.format(a, b), dpi=dpi * 10, bbox_inches='tight')

def f(x):
    return min(h, 1 - 2 * np.abs(x - 1/2))

def t(x):
    return 1 - 2 * np.abs(x - 1/2)

plot(f, t, 0, 1, 0.0001)