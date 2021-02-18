import numpy as np
import matplotlib.pyplot as plt

#Other good resources: https://youtu.be/UO98lJQ3QGI
#plot line style: https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle



x=np.arange(0,6,0.1)
y1=np.sin(x)
y2=2.*np.cos(x)

Width=4*2
Height=3*2

plt.clf()

plt.figure(figsize=(Width,Height),dpi=96)

plt.plot(x,y1,'r:',label='sin')   #red dot='r.', red line='r-', red dashline='r--'...
plt.plot(x,y2,'b:',label='cos')
plt.xlim(-1,6)	#set the limit for the x axis
plt.ylim(-2,1.5)	#set the limit for the y axis
plt.xlabel(r'$x$',fontsize=10)
plt.ylabel(r'$sin(x)$',fontsize=10)
plt.title('Collisional Dependence',fontsize=20)
plt.legend()	#show the legend
plt.show()		#show the plot
plt.savefig('Output_plot.png')#save the 
