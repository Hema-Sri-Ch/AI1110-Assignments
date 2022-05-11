# Hema Sri Cheekatla, CS21BTECH11013
# Finding probability for a particular outcome,
	# which is the combination of outcomes of two independent events

# importing libraries

import numpy as np
from numpy import random as rn
import random
import itertools

# defining probability of independent events

def Prob_Independent_Events(X, Y):
	return X*Y

# declaring the values
Prob_of_X_0 = 1/2
Prob_of_X_1 = 1/2

Prob_of_Y_1 = 1/6
Prob_of_Y_5 = 1/6

Prob_sum_3 = Prob_Independent_Events(Prob_of_X_0, Prob_of_Y_1)
Prob_sum_12 = Prob_Independent_Events(Prob_of_X_1, Prob_of_Y_5)

print("Probability of sum shown up is 3 is ", Prob_sum_3)
print("Probability of sum shown up is 12 is ", Prob_sum_12)

""" Creating a list of touple(x, y) 
	where 	x = 0 -- coin shows 1
		x = 1 -- coin shows 6
		y = 0 -- die shows 1
		y = 1 -- die shows 2
		y = 2 -- die shows 3
		y = 3 -- die shows 4
		y = 4 -- die shows 5
		y = 5 -- die shows 6
"""
R = 5
N = 10
res = [divmod(ele, R + 1) for ele in random.sample(range((R - 2) * (R - 1)), N)]

# print(res)

# getting sum 3 --> m
# getting sum 12 --> n

m = res.count((0,1))
n = res.count((1,5))
print("Random Probability of getting sum 3 is ", m/N)
print("Random Probability of getting sum 12 is ", n/N)
