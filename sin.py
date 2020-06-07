import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
fig = plt.figure(tight_layout=True)  #tight_layout会自动调整子图参数，使之填充整个图像区域
plt.plot(x,y)
def update_points(num):
    point_ani.set_data(x[num], y[num])
    return point_ani, #逗号一定加上，否则动画不能正常显示


point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")
# 开始制作动画
ani = animation.FuncAnimation(fig, update_points, np.arange(0, 100), interval=100, blit=True)
# ani.save('sin_test2.gif', writer='imagemagick', fps=10)

#第1个参数fig：即为我们的绘图对象.
# 第2个参数update_points：更新动画的函数.
# 第3个参数np.arrange(0, 100)：动画帧数，这需要是一个可迭代的对象。
# interval参数：动画的时间间隔。
# blit参数：是否开启某种动画的渲染
plt.show()