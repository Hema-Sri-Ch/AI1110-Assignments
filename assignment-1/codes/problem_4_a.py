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

# y cordinates are obviously 0s since we are plotting integers on real axis
y = list()
while k > 0:
	y.append(0)
	k = k - 1
plt.scatter(set, y, c = "blue")

plt.xlabel('real - axis')

# limitting x axis since we are getting integral solutions between -4 and 4
plt.xlim(-6, 6)
# we can neglect y axis since we just need points on x axis
plt.ylim(0,0.5)
plt.title('My pointing graph')
plt.savefig("../images/Figure_1.png")
plt.show()
print('Done!')
