# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.get_backend()
#green circle marks and dassed lines
plt.plot([1,2,3], [1,2,3], 'go--', label='line 1', linewidth=2)
plt.plot([1,2,3], [1,4,9], 'rs-',  label='line 2')#red square
plt.plot([2,3,4], [3,4,5], color='green', linestyle='dashdot', marker='o',
         markerfacecolor='blue', markersize=12)
plt.axis([0, 4, 0, 10])#Makes axis of this size
plt.legend()#Write legends



# create a new figure
plt.figure()

# plot the point (1.5, 1.5) using the circle marker
plt.plot(1.5, 1.5, 'o')
# plot the point (2, 2) using the circle marker
plt.plot(2, 2, 'o')
# plot the point (2.5, 2.5) using the circle marker
plt.plot(2.5, 2.5, 'o')

# get current axes
ax = plt.gca()
# get all the child objects the axes contains
print(ax.get_children())

##other examples

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(2,1,1) # two rows, one column, first plot

fig2 = plt.figure()
ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])

import numpy as np
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)


xtext = ax.set_xlabel('my xdata') # returns a Text instance
ytext = ax.set_ylabel('my ydata')





