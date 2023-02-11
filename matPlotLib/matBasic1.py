import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
y2=np.cos(x)
#y3=np.square(x)-2
plt.grid(True)
plt.xlabel('My X Values')
plt.ylabel('My Y Values')
plt.title('My first Graph')
plt.plot(x,y,'b-^',linewidth=3,markersize=6,label='sin(x)')
plt.plot(x,y2,'r-^',linewidth=3,markersize=6,label='cos(x)')
#plt.plot(x,y3,'g-^',linewidth=3,markersize=6,label='Green Line')
#plt.legend(loc='upper center')
plt.show()
