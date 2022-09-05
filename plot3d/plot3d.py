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

def xlabel(label):
    ax = plt.gca(projection='3d')
    ax.set_xlabel(label)

def ylabel(label):
    ax = plt.gca(projection='3d')
    ax.set_ylabel(label)

def zlabel(label):
    ax = plt.gca(projection='3d')
    ax.set_zlabel(label)
