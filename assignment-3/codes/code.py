# Hema Sri Cheekatla
# CS21BTECH11013

# importing libraries

import openpyxl
import pandas as pd
import numpy as np
from numpy import linalg as la
from numpy import random as rn
import matplotlib.pyplot as plt

def Probability(m, n):
	return float(m/n)
"""
	m = no. of favourable outcomes
	n = total no. of outcomes
"""

# Finding the Probability based on the data collected
# Reading the data from the excel sheet
data = pd.read_excel("../tables/Table.xlsx")
outcomes = list(data["Frequency"])
print("Obtained Probability:")
print(Probability(outcomes[0], sum(outcomes)))

N = sum(outcomes)

# Defining events
"""
	X = 0 --> Vehicle passed is a two-wheeler --> outcomes[0]
	X = 1 --> Vehicle passed is a three-wheeler --> outcomes[1]
	X = 2 --> Vehicle passed is a four-wheeler --> outcomes[2]

"""

# Randomly generating list 90 numbers containing the elements {0, 1, 2}
# each number represents an event as mentioned above

lst = np.random.randint(0, 3, size = 90)
# print(lst)

X_0 = np.count_nonzero(lst == 0)
X_1 = np.count_nonzero(lst == 1)
X_2 = np.count_nonzero(lst == 2)

print("Random Probability:")
print(Probability(X_0, N))
