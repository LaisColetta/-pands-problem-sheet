# Program that writes a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
#Author: Lais
#References: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/, https://matplotlib.org/stable/tutorials/introductory/customizing.html

import matplotlib.pyplot as plt
import numpy as np
import tkinter

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
# naming the y axis and adding space between text and plot
plt.ylabel('y - axis\n')
# giving a title to my graph, adding space between title and plot
plt.title ('Plot of the functions f(x)=x, g(x)=x2, h(x)=x3\n')
# shrinking current axis by 20% to fit legend on the right side
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#function to show the plot
plt.show
#funtion to save the plot
plt.savefig('Week08-Weeklytask')
