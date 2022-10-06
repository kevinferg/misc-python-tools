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
