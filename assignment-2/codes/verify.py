# Hema Sri Cheekatla, CS21BTECH11013
# Verifying the solution of out problem 21a
# ICSE 12, 2019 paper

# Python libraries for math and graphics

import numpy as np
import sympy as sp

x = sp.symbols('x')
# cost function = x^3/3 - 45x^2 - 900x + 36
C = (x**3)/3 - 45*(x**2) - 900*x + 36 # C - Cost function given in the question

# Marginal cost is d/dx(cost function)

MC = sp.diff(C, x) # MC - Marginal Cost
print("Marginal Cost function, MC = f(x) = {}".format(MC))

# Defining the function that is to be plotted and verified
def f(c):
	return float(MC.subs(x, c))


# Finding the value of x at where MC is minimum
""" Valid x values are whole numbers since x represents the number of units that are being produced. Upto 150 is an optimal range that is being assumed here """
x_vals = np.arange(0, 150, 1)

min_val = 100000
min_xcoord = 100000
for i in x_vals:
	if f(i)<min_val:
		min_val = f(i)
		min_xcoord = i

print("The number of units that are to be produced to obtain the minimum Marginal cost is ",min_xcoord, "units")
