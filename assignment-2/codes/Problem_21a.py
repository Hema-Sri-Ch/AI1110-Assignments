# Name : Hema Sri Cheekatla
# CS21BTECH11013
# To find the value of x at where the marginal cost is minimum, given the cost function
# 2019 Paper, problem 21a - Assignment 2

# Python libraries for math
from sympy import *

x = symbols('x')
# cost function = x^3/3 - 45x^2 - 900x + 36
C = (x**3)/3 - 45*(x**2) - 900*x + 36 # C - Cost function given in the question

# Marginal cost is d/dx(cost function)

MC = diff(C, x) # MC - Marginal Cost
print("Marginal Cost function, MC = f(x) = {}".format(MC))

# To find where this marginal cost function is minimum consider its first derivative

d_MC = diff(MC, x) # d_MC - derivative of MC
print("f'(x) = {}".format(d_MC))
# Let us solve the first dirivative of marginal cost to obtain the value of x at where it is zero
# f'(x) = 0

c = solve(d_MC)
print("f'(x) = 0, at x =",c[0])

# If f"(c) > 0, then at x = c f(x) is minimum, that is marginal cost is minimum

dd_MC = diff(d_MC, x) #dd_MC - double derivative of MC
print("f\"(x) = {}".format(dd_MC))

value = dd_MC.subs(x,c[0]) # value - f"(c)
print("f\"(c) = {}".format(value))
if value > 0:
	print("Hense f\"(x) at x =", c[0], "is positive")
	print("Hence the marginal cost function is minimum at x = ",c[0])
print("The number of units to be produced to obtain minimum Marginal Cost is", c[0])
