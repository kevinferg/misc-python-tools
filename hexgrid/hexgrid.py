import numpy as np
import matplotlib.pyplot as plt

def hexgrid(xlim, ylim, ynum):
    dy = (ylim[1] - ylim[0])/(ynum - 1.)/2.
    yvals = np.linspace(ylim[0], ylim[1]+dy, ynum)

    xnum = int(np.ceil((xlim[1] - xlim[0])/(dy*np.sqrt(3))))
    xvals = np.linspace(*xlim, xnum)

    x, y = np.meshgrid(xvals, yvals)
    y[:,1::2] += dy
    x, y = x.flatten(), y.flatten()

    return x, y

def hexplot(x, y, c, s = 100, edgecolors="black", linewidths = 2, **kwargs):
    plt.scatter(x, y, s = s, marker="H", c = c, edgecolors=edgecolors, linewidths=linewidths, **kwargs)