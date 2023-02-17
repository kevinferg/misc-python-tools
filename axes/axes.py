import matplotlib.pyplot as plt

def draw_axes(xlim, ylim, reformat=True,
              frac = 1./40., color="black", linewidth=0.4, overhang=0.2):
    if reformat:
        plt.xlim(xlim)
        plt.ylim(ylim)
        plt.axis("off")

    ax = plt.gca()
    fig = plt.gcf()
    dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent().transformed(dps)
    width, height = bbox.width, bbox.height

    dx = xlim[1] - xlim[0]
    dy = ylim[1] - ylim[0]

    hw = frac*dy
    hl = frac*dx

    yhw = hw/dy * dx * height/width
    yhl = hl/dx * dy * width/height

    def add_arrow(x0, y0, lx, ly):
        ax.arrow(x0, y0, lx, ly, lw=lw, hwad_width=hw, head_length=hl, color=color,
                 overhang=overhang, length_includes_head=True, clip_on=False)

    add_arrow(xlim[0], 0.,  dx, 0.) # Right arrow
    add_arrow(xlim[1], 0., -dx, 0.) # Left arrow

    add_arrow(0., ylim[0], 0.,  dy) # Up arrow
    add_arrow(0., ylim[1], 0., -dy) # Down arrow


def label_axes(xlabel=r"$x$", ylabel=r"$y", **kwargs):
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    dx = (xlim[1] - xlim[0])/20.
    dy = (ylim[1] - ylim[0])/15.

    plt.text(xlim[1] - 2*dx, -dy, xlabel, **kwargs)
    plt.text(-dx, ylim[1] - 2*dy, ylabel, **kwargs)