import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure
from scipy import integrate

x0 = np.array([1])
r = 1
k = 100
x_array = np.linspace(0, 15, 100)
zeros = np.zeros(len(x_array))
t0 = 0
tf = 10
t = np.linspace(t0, tf, 100)


def f(t, x):
    return r * x * (1 - x/k) 

dx = f(t, x_array)



fig=Figure(xlim=(t0, tf), x_label="Time (years)", y_label="Populaton")

fig.plot((t0, tf), (k, k), ls='--', lw=0.7, m='', c='k', label=f"Capacity = {k}")

for i in [10, 20, 40, 110, 120, 140]:
    x0 = np.array([i])
    results = integrate.solve_ivp(fun=f, t_span=(t0, tf), y0=x0, method="RK45", t_eval=t)
    x = results.y[0]
    fig.plot(t, x, label=f"$P_0$ = {i}", lw=0.7, ls='-', m='')



fig.legend(loc='lower right')

# fig.save('g4.2.svg')

# fig.line(x_array, dx, label='k=10, r=1')
# fig.quiver(x_array, zeros, dx, zeros)
# fig.legend()
# fig.save('g4.1.svg')