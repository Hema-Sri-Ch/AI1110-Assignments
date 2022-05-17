# Hema Sri Cheekatla, CS21BTECH11013
# AI1110 - Assignment - 5
# Plotting a pmf graph

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, stem
import numpy as np
import random
import itertools

# generating 4 integer tuples, (throwing pair of dice 4 times)
R = 5
N = 4

res = [divmod(ele, R+1) for ele in random.sample(range((R) * (R)), N)]
print(res)

# Checking for doublet
count = 0
for tpl in res:
	if tpl[0] == tpl[1]:
		count = count + 1

p = count/4;
print ("Hence the Random Probability is ", p)

# Plotting PMF
x = np.array([0, 1, 2, 3, 4])
y = np.array([625/1296, 125/324, 25/216, 5/324, 1/1296])


stem(x, y)
plt.xlabel("Values of Y")
plt.ylabel("Corresponding Probabilities")
plt.grid()
plt.savefig("../images/plot")
plt.show()
