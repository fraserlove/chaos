import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
# Figure dpi
dpi = 50


def plot_bifurc(f, r0, x0, N, M):
    """Make a bifurcation diagram.

    Plot x against r for 0 <= x <= 1, where r is a parameter to the function and
    x is the output of f(x). Start from r and increase to 4. x0 is the initial value.
    N is the number of iterations and M is the number of iterations to plot.
    
    """
    r = np.linspace(r0, 4.0, N)
    fig = plt.figure(figsize=(600/dpi, 300/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    x = x0 * np.ones(N) 
    for i in range(N):  
        x = f(x, r)
        if i >= (N - M):
            ax.plot(r, x, c='k', ls='', marker=',', alpha=0.02, markersize=.02)

    ax.set_xlim(r0, 4.0)
    ax.set_ylim(0.0, 1.0)
    ax.set_xlabel('$\mu$')                               
    ax.set_ylabel('$x$')   
    #ax.set_title('$F_\mu(x) = \mu x(1-x)$')
    plt.set_cmap(plt.cm.viridis_r)    
    plt.savefig('./images/bifurcation_{:.2}.png'.format(r0), dpi=dpi * 10, bbox_inches='tight')

class AnnotatedFunction:
    """A small class representing a mathematical function.

    This class is callable so it acts like a Python function, but it also
    defines a string giving its latex representation.

    """

    def __init__(self, func, latex_label):
        self.func = func
        self.latex_label = latex_label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

# The logistic map, f(x) = rx(1-x).
func = AnnotatedFunction(lambda x,r: r*x*(1-x), r'$rx(1-x)$')

plot_bifurc(func, 2.8, 0.1, 100000, 1000)