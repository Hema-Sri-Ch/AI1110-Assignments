# Hema Sri Cheekatla
# CS21BTECH11013
# Solving minimun of a function using gradient descent algorithm

# importing libraries

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def f(x):
	return x*x - 90*x - 900

def dy_dx(x):
	return 2*(x-45)

xcoords = list()
ycoords = list()

xpts = np.linspace(-10, 100, 1000)
ypts = f(xpts)
# x_k = x_k - (0.25 * MC.subs(x, x_k))
x_k =  0

while dy_dx(x_k) < -0.000001 :
#	print(x_k)
	xcoords.append(x_k)
	ycoords.append(f(x_k))
	x_k = x_k - (0.05 * dy_dx(x_k))
	
print("The value of x at where the minimum for this function exists is nearly ",x_k)
# The Possible number of units to be produced for minimum marginal cost is the nearest positive integer that its tending to 
X = round(x_k)
print("Therefore, the number of units that are to be produced for minimum marginal cost is ", X)

plt.scatter(X, 0, color = "r")
plt.plot(xpts, ypts, color = "blue", label = "Marginal cost function")
plt.scatter(xcoords, ycoords, color = "red", label = "$x_k$")
plt.grid()
plt.axvline(x=X, linestyle = "--", color = "grey")
plt.axhline(y=0, color = "black")
plt.axvline(x=0, color = "black")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.text(40, 75, "x = 45")
plt.legend(loc = "upper right")
plt.savefig("../images/fig_1.png")
plt.show()
