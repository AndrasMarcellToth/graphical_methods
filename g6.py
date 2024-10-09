import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure
from scipy import integrate

x0 = np.array([3, 3])


t0 = 0
tf = 30
t = np.linspace(t0, tf, 1000)

def f(t, x0):
    x, y = x0
    dx = y
    dy = -x + (1 - x**2) * y
    
    return dx, dy


# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10, 5], dpi=600)

# arr = np.linspace(-3, 3, 20)
# x, y = np.meshgrid(arr, arr)
# u = y
# v = -x + (1 - x**2) * y

# ax1.quiver(x, y, u, v)
# ax1.streamplot(x, y, u, v)
# ax1.set_xlabel("x (arb. units)")
# ax1.set_ylabel("y (arb. units)")
# ax1.title.set_text("(a)")
# ax1.tick_params(axis='both', which='both', direction='in')  
# ax1.minorticks_on() 


# results = integrate.solve_ivp(fun=f, t_span=(t0, tf), y0=x0, method="RK45", t_eval=t)
# x = results.y[0]
# y = results.y[1]

# ax2.plot(t, x, label='x(t)')
# ax2.plot(t, y, label='y(t)')
# ax2.set_xlabel("Time (s)")
# ax2.set_ylabel("Value")
# ax2.title.set_text("(b)")
# ax2.tick_params(axis='both', which='both', direction='in') 
# ax2.minorticks_on()  
# ax2.legend()



xi = np.linspace(-10, 10, 1000)
yi = xi / (1-xi**2)

fig, ax1 = plt.subplots(1, figsize=[8, 8], dpi=600)

for i in [[3, 3], [-2, 2], [0.1, 0.1], [0.5, 1], [3, 0.5], [4, 4]]:
    x0 = i
    results = integrate.solve_ivp(fun=f, t_span=(t0, tf), y0=x0, method="RK45", t_eval=t)
    x = results.y[0]
    y = results.y[1]
    ax1.plot(x, y, label=f"$x_0$ = {x0[0]}, $y_0$ = {x0[1]}")


ax1.plot(xi, np.zeros(len(xi)), color='k', ls='--', label='x-isocline')
ax1.plot(xi,yi, color='grey', ls='--', label='y-isocline')
ax1.set_xlabel("x (arb. units)")
ax1.set_ylabel("y (arb. units)")
ax1.tick_params(axis='both', which='both', direction='in')  
ax1.minorticks_on() 
ax1.legend(loc='lower right')
ax1.set_xlim([-3, 3])
ax1.set_ylim([-3, 3])
# plt.savefig('g6.2.svg')

















