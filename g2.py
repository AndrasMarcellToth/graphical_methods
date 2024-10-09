import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

start, end = -2, 2
dim = 101
step = 5
q = 1

x, y = np.meshgrid(np.linspace(start, end, dim), np.linspace(start, end, dim))
z = q / (x**2 + y**2)

dx, dy = np.gradient(z)

x_sliced = x[::step, ::step]
y_sliced = y[::step, ::step]
dx_sliced = dx.T[::step, ::step]
dy_sliced = dy.T[::step, ::step]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10, 5], dpi=600)



ax1.contourf(x, y, z)
ax1.quiver(x_sliced, y_sliced, dx_sliced, dy_sliced, pivot='mid')
ax1.set_xlabel("x (arb. units)")
ax1.set_ylabel("y (arb. units)")
ax1.title.set_text("(a)")
ax1.tick_params(axis='both', which='both', direction='in')  
ax1.minorticks_on() 




ax2.contour(x, y, z)
ax2.quiver(x_sliced, y_sliced, dx_sliced, dy_sliced, pivot='mid')
ax2.set_xlabel("x (arb. units)")
ax2.set_ylabel("y (arb. units)")
ax2.title.set_text("(b)")
ax2.tick_params(axis='both', which='both', direction='in') 
ax2.minorticks_on()  


plt.savefig('g2.svg')

