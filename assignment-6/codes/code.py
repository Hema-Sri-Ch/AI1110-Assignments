# Hema Sri Cheekatla, CS21BTECH11013
# Plotting graph for time of arrivals

# Python libraries for plotting

import numpy as np
import matplotlib.pyplot as plt
import random

# Proving the Random Probability

# genrating 100 outcomes of arrivals
x = np.random.uniform(0, 60, 100)
y = np.random.uniform(0, 60, 100)
lst = list()

# print(x)
# print(y)

# verifying whether they meet or not
for i in range(100):
	# train comes first , x<y, and train waits for 10 minutes
	if x[i] < y[i]:
		if y[i] <= x[i] + 10:
			lst.append(1)
		else :
			lst.append(0)
	else :
	# bus comes first, x>y and bus waits for 26.83 minutes(we obtained in the solution)
		if y[i] > x[i] - 26.83:
			lst.append(1)
		else:
			lst.append(0)
			
# print(lst)
m = lst.count(1)
# print(m)
# we would get the probability arround 0.5
print("The Random Probability that the bus and train meet ", m/100)


# Plotting Graph
x1 = np.array([0, 50])
y1 = np.array([10, 60])
x2 = np.array([35, 60])
y2 = np.array([0, 25])
plt.plot(x1, y1, color = "blue")
plt.plot(x2, y2, color = "green")
plt.axhline(y=0, color = "black")
plt.axvline(x=0, color = "black")
plt.axhline(y=60, color = "black")
plt.axvline(x=60, color = "black")
X = np.array([0,0,35,60,60,50,0])
Y = np.array([10,0,0,25,60,60,10])
X1 = np.array([0, 50, 0, 0])
Y1 = np.array([10, 60, 60, 10])
X2 = np.array([35, 60, 60, 35])
Y2 = np.array([0, 0, 25, 0])
plt.fill_between(X,Y ,color = "green", alpha = 0.3)
plt.fill_between(X1,Y1 ,color = "yellow", alpha = 0.3)
plt.fill_between(X2,Y2 ,color = "yellow", alpha = 0.3)
plt.xlabel("x - time of arrival of train")
plt.ylabel("y - time of arrival of bus")
plt.grid()
plt.savefig("../images/graph")
# plt.show()
