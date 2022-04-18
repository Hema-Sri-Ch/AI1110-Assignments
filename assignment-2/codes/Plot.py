# Hema Sri Cheekatla, CS21BTECH11013
# Plotting a parabola. (Marginal cost function)
# ICSE 12, 2019 paper

# Python libraries for math and graphics

import numpy as np
import matplotlib.pyplot as plt


# Defining the function that is to be plotted
def f(x):
	return (x**2-90*x-900)

# Arranging the coordinates and plotting
xcoord = np.linspace(-60, 150, 1000)
ycoord = f(xcoord)
X = [0, 45, 45]
Y = [f(45), f(45), 0]
plt.plot(xcoord, ycoord, label = "marginal cost function", color = "blue")
plt.scatter(X, Y, color = "red")
plt.text(1,f(45)-500, "(0,-2925)")
plt.text(40,f(45)-500, "(45, -2925)")
plt.text(40,250, "(45, 0)")
plt.axhline(y=0, color = "black")
plt.axvline(x=0, color = "black")
plt.axhline(y=-2925, color = "dimgrey", linestyle = "--")
plt.axvline(x=45, color = "dimgrey", linestyle = "--")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(loc = "upper right")
plt.savefig("../images/fig_1.png")
plt.show()
