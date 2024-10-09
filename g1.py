import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

start, end = 0, 2 * np.pi
dim = 101
step = 5
    


x, y = np.meshgrid(np.linspace(start, end, dim), np.linspace(start, end, dim))
u1 = np.cos(x)
v1 = np.sin(y)
u2 = np.cos(x) * y
v2 = np.sin(x) * x

x_sliced = x[::step, ::step]
y_sliced = y[::step, ::step]
u1_sliced = u1[::step, ::step]
v1_sliced = v1[::step, ::step]
u2_sliced = u2[::step, ::step]
v2_sliced = v2[::step, ::step]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10, 5], dpi=600)


ax1.quiver(x_sliced, y_sliced, u1_sliced, v1_sliced, label=r"$u=cos(x)$, $v=sin(y)$")
ax1.set_xlabel("x (arb. units)")
ax1.set_ylabel("y (arb. units)")
ax1.tick_params(axis='both', which='both', direction='in')  
ax1.minorticks_on() 
ax1.legend()


ax2.quiver(x_sliced, y_sliced, u2_sliced, v2_sliced, label=r"$u=cos(x)*y$, $v=sin(x)*x$")
ax2.set_xlabel("x (arb. units)")
ax2.set_ylabel("y (arb. units)")
ax2.tick_params(axis='both', which='both', direction='in') 
ax2.minorticks_on()  
ax2.legend()


plt.tight_layout()
plt.savefig('g1.svg')
