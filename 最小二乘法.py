# import matplotlib.pyplot as plt
# import numpy as np
# from fractions import Fraction
# fig = plt.figure(tight_layout=True)
# x=np.array([8,12,14,16])
# min=min(x)-3
# max=max(x)+3
# n=len(x)
# y=np.array([5,8,9,11])
# avg_x=sum(x)/len(x)
# avg_y=sum(y)/len(y)
# x_times_y=sum(x*y)
# x_2=sum(x**2)
# avg_x_avg_y=avg_x*avg_y
# avg_x_2=avg_x**2
# c=int((x_times_y-(n*avg_x_avg_y))*100)
# d=int((x_2-n*(avg_x_2))*100)
# b=Fraction(c,d)
# a=Fraction(avg_y)-Fraction(avg_x)*b
# graph_x=np.linspace(min,max,50)
# graph_y=b*graph_x+a
# plt.plot(graph_x,graph_y,color='red',linewidth=1.0,linestyle='--')
# plt.scatter(x, y, color='b')
# if (a>0):
#     plt.title("y="+str(b)+"x+"+str(a))
# elif(a==0):
#     plt.title("y="+str(b)+"x")
# else:
#     plt.title("y="+str(b)+"x"+str(a))
# plt.show()


#小数


import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
fig = plt.figure(tight_layout=True)
x=np.array([-5,0,4,7,12,15,19,23,27,31,36])
min=min(x)-3
max=max(x)+3
n=len(x)
y=np.array([156,150,132,128,130,116,104,89,93,76,54])
avg_x=sum(x)/len(x)
avg_y=sum(y)/len(y)
x_times_y=sum(x*y)
x_2=sum(x**2)
avg_x_avg_y=avg_x*avg_y
avg_x_2=avg_x**2
c=x_times_y-(n*avg_x_avg_y)
d=x_2-n*(avg_x_2)
# b=round(c/d)
b=c/d
# a=round(avg_y-(avg_x*b))
a=avg_y-(avg_x*b)
graph_x=np.linspace(min,max,50)
graph_y=b*graph_x+a
plt.plot(graph_x,graph_y,color='red',linewidth=1.0,linestyle='--')
plt.scatter(x, y, color='b')
if (a>0):
    plt.title("y="+"%.2f" %b+"x+"+"%.2f" %a)
elif(a==0):
    plt.title("y="+"%.2f" %b)
else:
    plt.title("y="+"%.2f" %b+"x"+"%.2f" %a)
plt.show()