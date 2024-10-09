import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure
from scipy import integrate

w = 1
b = 0.5


t = np.linspace(-1, 1, 20)
x, v = np.meshgrid(t, t)

def dxdv(x, v):
    dx = v
    dv = -b*v - w**2 * x
    return dx, dv

def energy(x, v):
    return x**2 + v**2

dx, dv = [], []


for i in [0, 0.5, 2, 5]:
    b = i
    temp_x, temp_v = dxdv(x, v)
    dx.append(temp_x)
    dv.append(temp_v)
    


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=[10, 10], dpi=600)

ax1.quiver(x, v, dx[0], dv[0], pivot='mid')
ax1.streamplot(x, v, dx[0], dv[0])
ax1.title.set_text("(a)")
ax1.set_xlabel("Position (m)")
ax1.set_ylabel("Velocity (m/s)")
ax1.tick_params(axis='both', which='both', direction='in')  
ax1.minorticks_on() 

ax2.quiver(x, v, dx[1], dv[1], pivot='mid')
ax2.streamplot(x, v, dx[1], dv[1])
ax2.title.set_text("(b)")
ax2.set_xlabel("Position (m)")
ax2.set_ylabel("Velocity (m/s)")
ax2.tick_params(axis='both', which='both', direction='in')  
ax2.minorticks_on() 


ax3.quiver(x, v, dx[2], dv[2], pivot='mid')
ax3.streamplot(x, v, dx[2], dv[2])
ax3.title.set_text("(c)")
ax3.set_xlabel("Position (m)")
ax3.set_ylabel("Velocity (m/s)")
ax3.tick_params(axis='both', which='both', direction='in')  
ax3.minorticks_on() 


ax4.quiver(x, v, dx[3], dv[3], pivot='mid')
ax4.streamplot(x, v, dx[3], dv[3])
ax4.title.set_text("(d)")
ax4.set_xlabel("Position (m)")
ax4.set_ylabel("Velocity (m/s)")
ax4.tick_params(axis='both', which='both', direction='in')  
ax4.minorticks_on() 

plt.tight_layout()


plt.savefig('g3.svg')
