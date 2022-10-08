import numpy as np
import matplotlib.pyplot as plt

import radar

rmax = 8
r_ticks = np.arange(1, rmax, 1)
r_vals = [7, 6, 4, 1, 6, 2]
labels = [f"Stat {1 + n}" for n in range(len(r_vals))]

plt.figure()

radar.plot_web(r_ticks, len(r_vals))   # Plot background "web" gridlines
radar.plot_star(r_vals)                # Plot "star" data
radar.polar_labels(labels, rmax)       # Add category labels at angles

plt.axis("equal")
plt.axis("off")
plt.savefig("star.png", bbox_inches="tight")
plt.close()