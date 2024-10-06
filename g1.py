import numpy as np
from matplotlib import pyplot as plt

x, y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
vx = np.cos(x)
vy = np.sin(y)
plt.figure(figsize=(6, 6), dpi=600)
plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
plt.xlabel('x')
plt.ylabel('y')
plt.title('Example of a quiver plot')
plt.quiver(x, y, vx, vy, pivot='mid', label='$v_x$ = cos($x$), $v_y$ = sin($y$)')
plt.legend()