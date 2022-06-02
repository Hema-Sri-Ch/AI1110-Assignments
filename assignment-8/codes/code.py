# CS21BTECH11013, Hema Sri Cheekatla
# Assignment-8, Probability and Random Variables
# Graphs

# importing libraries
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([0,10])
y1 = np.array([1, 1])
y2 = np.array([-1, -1])

X = np.array([0,10,10,0])
Y = np.array([1,1,-1,-1])


plt.plot(x1, y1)
plt.plot(x1, y2)

plt.fill_between(X, Y, color = "green", alpha = 0.3)

plt.axhline(y=0, color = "black")
plt.axvline(x=0, color = "black")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.grid()
plt.savefig("../images/Graph")
plt.show()

plt.plot(x1, x1)
x2 = np.array([0,-10])
plt.plot(x2, x1)

X1 = np.array([0, -10, 10, 0])
Y1 = np.array([0, 10, 10, 0])

plt.fill_between(X1, Y1, color = "green", alpha = 0.3)


plt.axhline(y=0, color = "black")
plt.axvline(x=0, color = "black")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.grid()
plt.savefig("../images/Graph2")
plt.show()
