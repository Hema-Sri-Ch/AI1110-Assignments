# CS21BTECH11013
# Hema Sri Cheekatla
# March 29, 2022
# 2018 Paper, Problem 4a
import matplotlib.pyplot as plt
import numpy as np

# 	-2+10x <= 13x+10 < 10x+24
# collecting the set of integers obeying the given expression
set = list()
n = -1000
k = 0
#checking the numbers from -1000 to 1000
# we can take any appropriate range
while n < 1001:
	a = -2 + 10*n
	b = 13*n + 10
	c = 24 + 10*n
	if a<=b and b<c:
		k = k + 1
		set.append(n)
	n = n + 1

# y cordinates for plotting points on real number line graph
# y cordinates are obviously 0s since we are plotting integers on real axis
y = list()
while k > 0:
	y.append(0)
	k = k - 1


x = np.linspace(-6, 6, 1000)
y_1 = -2 + 10*x
l1 = [10, -2]
plt.plot(x, y_1, 'b', label = "y1")
y_2 = 13*x + 10
l2 = [13, 10]
plt.plot(x, y_2, 'g', label = "y2")
y_3 = 24 + 10*x
l3 = [10, 24]
plt.plot(x, y_3, 'r', label = "y3")
plt.xlabel('x-axis')
plt.ylabel('y-axis')


""" the values of x that obey the inequality y1 <= y2 < y3 are
 the values at where the line y2 lies between y1 and y3
 since y2 intesects y1 at x = -4 and y3 at x = 14/3,
 the possible values of x are found to be the integers in the set [-4, 4.67]
 if y = mx + c consider the list [m,c] to find the intersection points
"""
def intersec(a,b,c,d):
	xi = (b-d)/(c-a)
	yi = a*xi + b
	return xi, yi
# (x1,y1) intersection point of y1 and y2
# (x2,y2) intersection point of y2 and y3
x1, y1 = intersec(l1[0], l1[1],l2[0], l2[1])
x2, y2 = intersec(l2[0], l2[1], l3[0], l3[1])
plt.fill_between(x,y_1,y_3, where=[(x>=x1) and (x<x2) for x in x], color = 'green', alpha=0.3, label = 'region at where y1 <= y2 < y3')

plt.scatter(x1, y1, c = 'black')
plt.axvline(x = x1, color = 'grey', linestyle = '--')

plt.scatter(x2, y2, c = 'black')
plt.axvline(x = x2, color = 'grey', linestyle = '--')
plt.axhline(y=0, color = 'black')
plt.axvline(x=0, color = 'black')
plt.scatter(set, y, c = "blue", label = "x co-ordinates in this region")

plt.grid()
plt.legend(loc = "upper left")
plt.title('Graph of corresponding lines')
plt.savefig("../images/Figure_1.png")
plt.show()

plt.scatter(set, y, c = "blue", label = "points in the given set")

plt.xlabel('real - axis')

# limitting x axis since we are getting integral solutions between -4 and 4
plt.xlim(-6, 6)
# we can neglect y axis since we just need points on x axis
plt.ylim(0,0.5)
plt.legend(loc = "upper left")
plt.title('Pointing graph')
plt.savefig("../images/Figure_2.png")
plt.show()
print('Done!')


