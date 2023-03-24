import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
dpi = 90 # Figure DPI

n = 8 # Number Of Iterations to Perform
res = 1000 # Resolution of function curve
iter_colour = "#231B94" # Iteration Colour
iter_alpha = 1 # Iteration Alpha Value
identity = True # Decide to Plot the Identity or not

def plot(f, x0=0, a=0, b=1, mu=0, h=0):

    x = np.linspace(a, b, res)
    if f.__name__ == 'piecewise':
        x = np.linspace(a, b, b - a + 1)

    y = np.zeros_like(x)
    
    # Add the function curve
    for i in range(len(x)):
        y[i] = f(x[i], mu, h)

    fig = plt.figure(figsize=(300/dpi, 300/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    if f.__name__ == 'doubling': # Removing continuity
        ax.plot(x[:int(len(x)/2)], y[:int(len(x)/2)], c='#444444', lw=2, alpha=1)
        ax.plot(x[int(len(x)/2):], y[int(len(x)/2):], c='#444444', lw=2, alpha=1)
    else: ax.plot(x, y, c='#444444', lw=2, alpha=1)

    if identity: ax.plot(x, x, c='#222222', lw=1, alpha=0.4)

    if x0:
        # Initialize the x and y arrays for the cobweb diagram
        x = x0
        y = f(x, mu, h)

        # Add the initial line
        ax.plot([x, x], [0, y], c=iter_colour, alpha=iter_alpha, lw=1.5)

        # Loop over n iterations to plot the cobweb diagram
        for i in range(n):
            ax.plot([x, y], [y, y], c=iter_colour, alpha=iter_alpha, lw=1.5)
            ax.plot([y, y], [y, f(y, mu, h)], c=iter_colour, alpha=iter_alpha, lw=1.5)
            x = y
            y = f(y, mu, h)

    if f.__name__ == 'truncated_tent':
        ax.plot(x, [h for i in x], c='#444444', lw=1, alpha=0.4)
        ax.plot(x, [tent(i, mu) for i in x], c='#444444', lw=1.4, linestyle='dashed', alpha=0.7)
        ax.annotate('$h$', (x[0], h), (-0.08, h - 0.02), 'axes fraction')

    ax.set_xlim(a, b)
    ax.set_ylim(a, b)
    ax.set_xticks(np.arange(a, b+1, 1))
    ax.set_yticks(np.arange(a, b+1, 1))
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')
    plt.axis('on')

    plt.savefig('./images/{}{}{}.pdf'.format(f.__name__, '_' + str(mu) if mu != 0 else '', '_' + str(x0) if x0 != 0 else ''), dpi=dpi * 10, bbox_inches='tight')

def logistic(x, mu = 0, h = 0):
    return mu * x * (1-x)

def tent(x, mu = 0, h = 0):
    return mu * min(x, 1-x)

def truncated_tent(x, mu = 0, h = 0):
    return min(h, mu * min(x, 1-x))

def doubling(x, mu = 0, h = 0):
    return (2 * x) % 1

def piecewise(x, mu = 0, h = 0):
    # For piecewise set delta = 1, a = 0, b = 4
    match x:
        case 0: return 2
        case 1: return 4
        case 2: return 3
        case 3: return 1
        case 4: return 0

# To Plot Iterates Set x0 /= 0
plot(logistic, x0 = 0.1, mu = 3)