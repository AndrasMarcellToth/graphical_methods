import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure
from scipy import integrate

rabbit = np.arange(0, 10, 1)
fox = np.arange(0, 10, 1)




a = 4
b = 2
c = 1/3
d = 1


t0 = 0
tf = 20
t = np.linspace(t0, tf, 100)



drabbit = a*rabbit - b*rabbit*fox
dfox = c*rabbit*fox - d*fox
    

x, y = np.meshgrid(rabbit, fox)
u, v = np.meshgrid(drabbit, dfox)



fig=Figure(x_label="Rabbit", y_label="Fox")




fig.quiver(x, y, u, v)
fig.streamplot(x, y, u, v)


fig.legend()



# fig.line(x_array, dx, label='k=10, r=1')
# fig.quiver(x_array, zeros, dx, zeros)
# fig.legend()