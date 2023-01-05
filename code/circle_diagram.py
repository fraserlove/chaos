import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
dpi = 90 # Figure DPI

iter_colour = "#111111" # Iteration Colour
iter_alpha = 0.5 # Iteration Alpha Value
rigid = True

figure, ax = plt.subplots()

ax.add_artist(plt.Circle((0, 0), 1, fill=False, color='#444444', lw=2, alpha=1))

if rigid:
    x0 = 0.7435 # Size of initial angle
    nmax = 10 # Number Of Iterations to Perform
    for i in range(nmax):
        ax.plot([0, np.cos(i * x0)], [0, np.sin(i * x0)], c=iter_colour, alpha=iter_alpha, lw=1.5)
        ax.annotate('$f^{}(x)$'.format(i), (np.cos(i * x0), np.sin(i * x0)), (1.35 * np.cos(i * x0) - 0.225, 1.2 * np.sin(i * x0) - 0.05), 'data', fontsize=25)
else:
    x0 = 0.12 # Size of initial angle
    nmax = 10 # Number Of Iterations to Perform
    for i in range(nmax):
        x0 *= 2
        ax.plot([0, np.cos(x0)], [0, np.sin(x0)], c=iter_colour, alpha=iter_alpha, lw=1.5)
        ax.annotate('$f^{}(x)$'.format(i), (np.cos(x0), np.sin(x0)), (1.35 * np.cos(x0) - 0.225, 1.2 * np.sin(x0) - 0.05), 'data', fontsize=25)


a = -1.1
b = 1.1

#ax.set_xlim(a, b)
#ax.set_ylim(a, b)
ax.set_xticks(np.arange(a, b))
ax.set_yticks(np.arange(a, b))
ax.set_aspect('equal')
ax.set_axis_off()

plt.savefig('./images/{}_circle.pdf'.format('rigid' if rigid else 'doubling'), dpi=dpi * 10, bbox_inches='tight')