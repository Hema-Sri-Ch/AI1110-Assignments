#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy
import mpmath as mm
import math

#if using termux
import subprocess
import shlex
#end if

# ---------------------- Loading files ------------------------ #
x = np.linspace(-4, 4, 30)#points of the x axis 				--> for uni_cdf and gauss_cdf
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
#randvar = np.loadtxt('req.dat', dtype='double')
randvar = np.loadtxt('tri.dat', dtype='double')

# --------------------- Calculating CDF ------------------------#
for i in range (0, 30): 									# --> for uni_cdf and gauss_cdf									
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
# ------------------ Theoreticla Uniform Distribution ----------- #
def uni_cdf(x):
	if(x>1):
		return 1
	elif(x<0):
		return 0
	else:
		return x
		
vec_uni_cdf = np.vectorize(uni_cdf, otypes=[np.float])

# ------------------- Theoretical Gaussian Distriburion -------------- #
def q_gauss_cdf(x):
	return (mm.erfc(x/math.sqrt(2))/2)
	
def gauss_cdf(x):
	return(1-q_gauss_cdf(x))
	
vec_gauss_cdf = np.vectorize(gauss_cdf, otypes=[np.float])

# ------------------- Theoretical Logarithmic Distribution -------- #
def req_cdf(x):
    if(x < 0):
        return 0
    else:
        return (1 - math.exp(-x/2))
        
vec_req_cdf = np.vectorize(req_cdf, otypes=[np.float])

# ------------------- Theoretical Triangular Distribution ------- #
def tri_cdf(x):
	if (x < 0):
		return 0
	elif (x >= 0 and x < 1):
		return x*x/2
	elif (x>= 1 and x < 2):
		return 2*x - x*x/2 - 1
	else :
		return 1
		
vec_tri_cdf = np.vectorize(tri_cdf, otypes=[np.float])

# ---------------- Plotting Simulation and Theoreitcal plots -------------- #

plt.plot(x.T,err, 'o')#plotting the CDF
#plt.plot(x, vec_uni_cdf(x))#plotting theoretical CDF
#plt.plot(x, vec_gauss_cdf(x))
#plt.plot(x, vec_req_cdf(x))
plt.plot(x, vec_tri_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

# -------------------------------- Saving Plots ------------------------------ #
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')

#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')

#plt.savefig('../figs/req_cdf.pdf')
#plt.savefig('../figs/req_cdf.eps')

plt.savefig('../figs/tri_cdf.pdf')
plt.savefig('../figs/tri_cdf.eps')
plt.show() #opening the plot window
