#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

# ---------------------- Loading files ------------------------ #
maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
randvar = np.loadtxt('tri.dat', dtype='double')

# --------------------- Calculating PDF ------------------------#
for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list


# ------------------- Theoretical Gaussian Distriburion -------------- #
def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)

# ------------------- Theoretical Triangular Distribution ------- #	
def tri_pdf(x):
	if (x >0 and x < 1):
		return x
	elif(x> 1 and x < 2):
		return 2-x
	elif(x == 1):
		return 1
	else:
		return 0
	

vec_gauss_pdf = scipy.vectorize(gauss_pdf)
vec_tri_pdf = np.vectorize(tri_pdf, otypes=[np.float])


# ---------------- Plotting Simulation and Theoreitcal plots -------------- #

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
#plt.plot(x,vec_gauss_pdf(x))#plotting the CDF
plt.plot(x, vec_tri_pdf(x))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

# -------------------------------- Saving Plots ------------------------------ #

#plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')

#plt.savefig('../figs/gauss_pdf.pdf')
#plt.savefig('../figs/gauss_pdf.eps')

plt.savefig('../figs/tri_pdf.pdf')
plt.savefig('../figs/tri_pdf.eps')

plt.show() #opening the plot window
