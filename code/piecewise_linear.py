import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
# Figure dpi
dpi = 70

def plot_cobweb(f, a, b):
    """Make a cobweb plot.

    Plot y = f(x; r) and y = x for 0 <= x <= 1, and illustrate the behaviour of
    iterating x = f(x) starting at x = x0. r is a parameter to the function.

    """
    x = np.arange(a, b + 1, 1)
    fig = plt.figure(figsize=(300/dpi, 300/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    y = []
    for i in range(len(x)): y.append(f(x[i]))

    ax.plot(x, y, c='#444444', lw=1)

    # Annotate and tidy the plot.
    ax.set_xlim(a, b)
    ax.set_ylim(min(y), max(y))
    ax.set_yticks(np.arange(min(y), max(y)+1, 1))
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')

    plt.savefig('./images/piecewise_{}_{}.pdf'.format(a, b), dpi=dpi * 10, bbox_inches='tight')

def f(x):
    match x:
        case 0: return 2
        case 1: return 4
        case 2: return 3
        case 3: return 1
        case 4: return 0

plot_cobweb(f, 0, 4)