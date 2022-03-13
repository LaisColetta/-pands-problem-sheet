# Program that writes a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
#Author: Lais
#References: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/,

import matplotlib.pyplot as plt
import numpy as np
#Plot of the function f(x)=x
x1 = np.array(range(0,4))
y1 = x1
plt.plot (x1, y1, color = 'r', label = 'f(x)=x')

#Plot of the function g(x)=x2
x2 = np.array(range(0,4))
y2 = x2 * 2 
plt.plot (x2, y2, color = 'b', label = 'g(x)=x2')

#Plot of the function h(x)=x3
x3 = np.array(range(0,4))
y3 = x3 * 3 
plt.plot (x3, y3, color = 'g', label = 'h(x)=x3')

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title ('Plot of the functions f(x)=x, g(x)=x2, h(x)=x3')
# show a legend on the plot
plt.legend(loc = 'upper left')
#function to show the plot
plt.show
#funtion to save the plot
plt.savefig('Week08-Weeklytask')
