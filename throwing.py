import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

v0=10
g=10
sin=3/5
cos=4/5
step=100
max=1.3
#Ctrl + Shift + Alt + j

x=v0*cos*np.linspace(0,max,step)
y=v0*sin*np.linspace(0,max,step)-0.5*g*np.linspace(0,max,step)**2+10
fig = plt.figure(tight_layout=True)  #tight_layout会自动调整子图参数，使之填充整个图像区域
plt.plot(x,y)

point_ani, = plt.plot(x[0], y[0], "ro")
def update_points(num):
    point_ani.set_data(x[num], y[num])
    return point_ani, #逗号一定加上，否则动画不能正常显示
plt.grid(ls="--")
ani = animation.FuncAnimation(fig, update_points, np.arange(0, 100), interval=100, blit=True)
plt.show()
