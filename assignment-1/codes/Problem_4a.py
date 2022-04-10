# Name: Hema Sri Cheekatla
# CS21BTECH11013
# To solve the system of linear equations and plot their graph
# 2018 Paper, problem 4a

# Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

"""
line 1 --> 10x-y = 2
line 2 --> 13x-y = -10
line 3 --> 10x-y = -24

We need to find the values of x at where line 1 <= line 2 < line 3
"""
# solving line1, line2 and line2, line3
A = np.array(([10, -1],[13, -1])) # coefficient matrix for line1 and line2
B = np.array(([10, -1],[13, -1])) # coefficient matrix for line3 and line2
d1 = np.array(([2, -10]))
d2 = np.array(([-24, -10]))
e1 = np.array(([0, 1]))
c1 = d1[0]
c2 = d1[1]
c3 = d2[0]
c4 = d2[1]
n1 = A[0,:]
n2 = A[1,:]
n3 = B[0,:]
n4 = B[1,:]

# Solving lines
# x is intersection point of line1 and line2
# y is intersection point of line3 and line2
x = LA.solve(A, d1)
y = LA.solve(B, d2)

# solutions of lines
print("The point of intersection of line 1 and line 2:")
print(x)
print("The point of intersection of line 2 and line 3:")
print(y)
#Generating line function from slope and a point
def line_dir_pt(m,A,k1,k2):
  len = 1000
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

# direction vectors
m1 = np.array(([1,10]))
m2 = np.array(([1,13]))

# points
x1 = c1/(n1@e1)
A1 = x1*e1 # A1 a point on line 1
x2 = c2/(n2@e1)
A2 = x2*e1 # A2 a point on line 2

x3 = c3/(n3@e1)
A3 = x3*e1 # A3 a point on line 3
x4 = c4/(n4@e1)
A4 = x4*e1 # A4 a point on line 4/line 2(both are same)
# Generating lines
L_1 = line_dir_pt(m1,A1, -6, 6)
L_2 = line_dir_pt(m2,A2, -6, 6)
L_3 = line_dir_pt(m1,A3, -6, 6)
# plotting lines
plt.plot(L_1[0,:], L_1[1,:], label = 'line 1 -> 10x-y-2')
plt.plot(L_2[0,:], L_2[1,:], label = 'line 2 -> 13x-y+10')
plt.plot(L_3[0,:], L_3[1,:], label = 'line 3 -> 10x-y+24')
# plt.xlim([-6,6])
# plotting intersecting points
root1 = x.T
root2 = y.T
plt.scatter(root1[0], root1[1])
plt.scatter(root2[0], root2[1])
"""The integral values of x satisfying the given inequation are the integers that lies between root1[0] and root2[0] """
set = list()
num = int(root1[0])
while num<root2[0]:
	set.append(num)
	num = num + 1
# set of integral values in the corresponding valid region
print("The set of integral values of x at where the given inequation satisfies are:")
print(set)
# Setting the axes and limits and shading the valid region
y1 = L_1[1,:]
y2 = L_3[1,:]
x = L_1[0,:]
plt.axhline(y=0, color = 'black')
plt.axvline(x=0, color = 'black')
plt.axvline(x=root1[0], color = 'grey', linestyle = '--')
plt.axvline(x=root2[0], color = 'grey', linestyle = '--')
plt.fill_between(x,y1,y2, where=[(x>=root1[0]) and (x<root2[0]) for x in x], color = 'green', alpha=0.3, label = 'region at where $L_1 $<=$ L_2 < L_3$')
plt.xticks(np.arange(-6,7,1))
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.savefig('../images/Figure_1.png')
plt.show()
