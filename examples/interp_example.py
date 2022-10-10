import numpy as np
import matplotlib.pyplot as plt

from interpolate import interp

# Grid/image data
xs = ys = np.linspace(0,1,3)
xydata = np.meshgrid(xs,ys)
z = np.array([[2,7,6],[9,3,1],[4,3,8]])


# Interpolate to random points
xy = np.random.rand(5000, 2)
c_smooth = interp(z, xy)
c_linear = interp(z, xy, smooth=False)


# Generate figure
def make_subplot(i, x, y, color, size, title):
    plt.subplot(1, 3, i)
    plt.title(title)
    plt.scatter(x, y, c=color, cmap='jet', s=size)
    plt.axis('equal')
    plt.axis('off')

plt.figure(figsize=(9,3))
make_subplot(1, xydata[0], xydata[1], z, 200, "Original Data")
make_subplot(2, xy[:,0], xy[:,1], c_linear, 3, "Linear")
make_subplot(3, xy[:,0], xy[:,1], c_smooth, 3, "Smooth")
plt.tight_layout()
plt.savefig("interpolated.png", bbox_inches="tight")
plt.close()