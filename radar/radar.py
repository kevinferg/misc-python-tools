import numpy as np
import matplotlib.pyplot as plt

def plot_polar(rs, thetas, fill=False, **kwargs):
    """Plot radius and angle data on polar axes
    Arguments:
    - rs: array of radius values
    - thetas: array of angle values, in radians
    - fill: Whether to fill in the polygon created by r and theta
    - **kwargs: pass in other arguments of plt.plot() or plt.fill()
    """
    fun = plt.fill if fill else plt.plot
    fun(rs*np.cos(thetas), rs * np.sin(thetas), **kwargs)

def theta_space(n, start_angle=np.pi/2, direction="CW"):
    """Get equally-spaced angles (in radians) around a circle
    Arguments:
    - n: Number of angles
    - start_angle: which angle to start with, in radians
    - direction: which direction to go, "CW" or "CCW"
    Returns: array of angle values
    """
    dir = -1 if direction == "CW" else 1
    thetas = start_angle + dir * np.linspace(0, 2*np.pi * np.double(n-1)/np.double(n), np.int(n))
    return thetas

def plot_web(rs, thetas, color = "gray", linewidth=0.5, zorder=-1):
    """Plot a spider-web type shape for a radar chart
    Arguments:
    - rs: radius grid line locations
    - thetas: Number of grid lines to space evenly, OR angles (in radians) of grid line locations
    - color: Color of lines
    - linewidth: Thickness of lines
    - zorder: Layer at which to plot (low value means behind other plots)
    """
    if type(thetas) is int:
        thetas = theta_space(thetas)

    dup_thetas = np.append(thetas, thetas[0])
    
    all_thetas = np.tile(dup_thetas,(len(rs)))
    all_rs = np.repeat(rs,(len(dup_thetas)))

    radial_thetas = np.repeat(thetas, 3)
    radial_rs = np.tile(np.array([0, np.max(rs), 0]),len(thetas))

    plot_polar(all_rs, all_thetas, c=color, linewidth=linewidth, zorder=zorder)
    plot_polar(radial_rs, radial_thetas, c=color, linewidth=linewidth, zorder=zorder)

def plot_star(rs, thetas = None, fill=True, color="red"):
    """Plot a star shape for a radar chart given radius data
    Arguments:
    - rs: radii for each category
    - thetas: Angle (in radians) grid line locations, defaults to evenly-spaced
    - fill: Whether to fill in the star
    - color: Color of lines and fill (fill color has transparency)
    """
    if thetas is None:
        thetas = theta_space(len(rs))
    dup_thetas = np.append(thetas, thetas[0])
    dup_rs = np.append(rs, rs[0])
    plot_polar(dup_rs, dup_thetas, fill=False,
               color=color, marker=".", markerfacecolor=color, linewidth=2.5, markersize=15)
    plot_polar(dup_rs, dup_thetas, fill=fill, facecolor=color, alpha=0.2)
    
def polar_labels(labels, r, thetas = None, **kwargs):
    """Place automatically-rotated angle data text labels
    Arguments:
    - labels: String labels
    - r: Radius at which to place labels
    - thetas: Angle locations (radians) to place labels, defaults to evenly-spaced
    - **kwargs: Additional arguments for plt.text(), e.g. fontsize=18
    """
    if thetas is None:
        thetas = theta_space(len(labels))

    for i in range(len((thetas))):
        t = thetas[i] % (2*np.pi)
        rotation = -90 + t * 180/np.pi + 180 * (t > np.pi)
        plt.text(r * np.cos(t), r * np.sin(t), labels[i], rotation = rotation,
                 horizontalalignment='center', verticalalignment='center', **kwargs)