import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
# Figure dpi
dpi = 90
nmax = 40

def plot(f, x0, a, b, s, mu = 0):
    x = np.arange(a, b + s, s)
    fig = plt.figure(figsize=(300/dpi, 300/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    ax.plot(x, f(x, mu), c='#222222', alpha=1, lw=2)
    ax.plot(x, x, c='#222222', alpha=1, lw=1)

    px, py = np.empty((2,nmax + 1,2))
    px[0], py[0] = x0, 0
    for n in range(1, nmax, 2):
        px[n] = px[n-1]
        py[n] = f(px[n-1], mu)
        ax.plot([px[n-1], px[n]], [py[n-1], py[n]], c='#666666', alpha=0.5, lw=1)
        px[n+1] = py[n]
        py[n+1] = py[n]
        ax.plot([px[n], px[n+1]], [py[n], py[n+1]], c='#666666', alpha=0.5, lw=1)

    ax.set_xlim(a, b)
    ax.set_ylim(a, b)
    ax.set_xticks(np.arange(a, b+1, 1))
    ax.set_yticks(np.arange(a, b+1, 1))
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')

    plt.savefig('./images/{}{}.pdf'.format(f.__name__, '_' + str(mu) if mu != 0 else ''), dpi=dpi * 10, bbox_inches='tight')

def logistic(x, mu):
    return mu * x * (1-x)

def tent(x, mu = 0):
    return 1 - 2 * np.abs(x - 1/2)

# Set x_0 = 0 for no cobweb plots
plot(tent, np.sqrt(2)/5, 0, 1, 0.0001, mu = 0)