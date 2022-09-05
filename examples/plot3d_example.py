import numpy as np
import matplotlib.pyplot as plt
import plot3d

vals = np.linspace(0, 1, 100)
x, y = np.meshgrid(vals, vals)
z = np.cos(8*x) + np.sin(10*y)

# Create a 3D figure
plot3d.figure(figsize=(6,4.5), dpi=80)
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

# Make a surface plot
plot3d.surf(x, y, z)

# Change axis names
plot3d.xlabel("x")
plot3d.ylabel("y")
plot3d.zlabel("cos(8x) + sin(10y)")

plt.savefig("surface.png", bbox_inches="tight")
plt.close()