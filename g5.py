import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure
from scipy import integrate

x0 = np.array([2, 4])

a = 4
b = 2
c = 1/3
d = 5

t0 = 0
tf = 10
t = np.linspace(t0, tf, 1000)


def f(t, x):
    rabbit, fox = x
    drabbit = a*rabbit - b*rabbit*fox
    dfox = c*rabbit*fox - d*fox
    
    return drabbit, dfox



results = integrate.solve_ivp(fun=f, t_span=(t0, tf), y0=x0, method="RK45", t_eval=t)
rabbit = results.y[0]
fox = results.y[1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10, 5], dpi=600)

ax1.plot(t, rabbit, label='Prey')
ax1.plot(t, fox, label='Predator')
ax1.set_xlabel("Time (years)")
ax1.set_ylabel("Population")
ax1.title.set_text("(a)")
ax1.tick_params(axis='both', which='both', direction='in')  
ax1.minorticks_on() 
ax1.legend(loc='upper right')


ax2.plot(rabbit, fox, color='k')
ax2.set_xlabel("Prey")
ax2.set_ylabel("Predator")
ax2.title.set_text("(b)")
ax2.tick_params(axis='both', which='both', direction='in') 
ax2.minorticks_on()  

# plt.savefig('g5.4.svg')
