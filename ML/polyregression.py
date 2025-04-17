import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
y=[100,90,80,60,60,55,60,60,65,70,70,75,76,78,79,90,99,99,100,103,156,185]

mymodel=np.poly1d(np.polyfit(x,y,3))
myline=np.linspace(1,22,100)
plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()