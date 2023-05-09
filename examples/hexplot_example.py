import numpy as np
import matplotlib.pyplot as plt
import hexgrid

# Generate hex grid
lims = [0,1]
num_y = 24
x, y = hexgrid.hexgrid(lims, lims, num_y) # hexgrid
c = np.random.rand(np.size(x))

# Create a plot
plt.figure(figsize=(5,5),dpi=100)
hexgrid.hexplot(x, y, c, s=200, cmap="Wistia") # hexplot
plt.xlim(lims)
plt.ylim(lims)
plt.axis("off")
plt.savefig("honeycomb.png", bbox_inches="tight")
plt.close()