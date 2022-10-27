import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def figure(**kwargs):
    fig = plt.figure(**kwargs)
    ax = fig.add_subplot(111, projection='3d')
    return fig, ax

def surf(x, y, z, cmap=cm.coolwarm, linewidth=0, alpha=0.9, **kwargs):
    ax = plt.gca(projection='3d')
    ax.plot_surface(x, y, z, 
                    cmap=cmap, linewidth=linewidth, alpha=alpha, 
                    **kwargs)

def scatter(x, y, z, c='black', **kwargs):
    ax = plt.gca(projection='3d')
    ax.scatter(x, y, z, c=c, **kwargs)

    
def xlabel(label, **kwargs):
    ax = plt.gca(projection='3d')
    ax.set_xlabel(label, **kwargs)

def ylabel(label, **kwargs):
    ax = plt.gca(projection='3d')
    ax.set_ylabel(label, **kwargs)

def zlabel(label, **kwargs):
    ax = plt.gca(projection='3d')
    ax.set_zlabel(label, **kwargs)

    
def xlim(lims, **kwargs):
    ax = plt.gca(projection='3d')
    ax.set_xlim(lims, **kwargs)

def ylim(lims, **kwargs):
    ax = plt.gca(projection='3d')
    ax.set_ylim(lims, **kwargs)

def zlim(lims, **kwargs):
    ax = plt.gca(projection='3d')
    ax.set_zlim(lims, **kwargs)

def axis_equal():
    def get_midpt_and_range(lims):
        midpt = (lims[1] + lims[0])/2.
        span  = abs(lims[1] - lims[0])
        return midpt, span
        
    ax = plt.gca(projection='3d')
    x_m, x_r = get_midpt_and_range(ax.get_xlim3d())
    y_m, y_r = get_midpt_and_range(ax.get_ylim3d())
    z_m, z_r = get_midpt_and_range(ax.get_zlim3d())

    r = max([x_r, y_r, z_r])/2.
    ax.set_xlim3d([x_m - r, x_m + r])
    ax.set_ylim3d([y_m - r, y_m + r])
    ax.set_zlim3d([z_m - r, z_m + r])