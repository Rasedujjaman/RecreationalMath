import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Parametric heart
t = np.linspace(0, 2*np.pi, 1000)
x = 16 * (np.sin(t))**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# Normalize & scale
x = 1.5 * x / np.max(np.abs(x))
y = 1.5 * y / np.max(np.abs(y))

# Colors (MATLAB order reversed as in your code)
myColor = ['#F00','#F80','#FF0','#0B0','#00F','#50F','#A0F'][::-1]

# Plot setup
plt.figure(figsize=(6,6))
numOfHeart = 7
step = 1/numOfHeart

# Concentric hearts
for ii in range(1, numOfHeart+1):
    plt.plot(ii*step*x, ii*step*y, linewidth=2, color=myColor[ii-1])

# Cupid arrow
arrow = FancyArrowPatch((0.25, 0.25), (0.80, 0.80),
                        arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='k')
plt.gca().add_patch(arrow)

# Title
plt.text(-0.8, 1.3, 'Beauty of Math', fontsize=14)

# Axis settings
plt.axis('equal')
plt.xticks([])
plt.yticks([])
plt.gca().set_frame_on(True)
plt.gca().spines['top'].set_linewidth(2)
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().spines['left'].set_linewidth(2)
plt.gca().spines['right'].set_linewidth(2)

plt.savefig("heartShape.png") # save as PNG
# plt.show() # optional

