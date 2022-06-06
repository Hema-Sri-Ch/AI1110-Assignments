# Hema Sri Cheekatla, CS21BTECH11013
# Assignment-9
# Plotting probability mass graphs

# importing libraries
import numpy as np
import matplotlib.pyplot as plt

x=[0, 0.4, 1, 1, 1, 0.6, 0, 0, 0]
y=[0, 0, 0, 0.6, 1, 1, 1, 0.4, 0]

x1=[0.4, 1]
y1=[0, 0.6]

x2=[0, 0.6]
y2=[0.4, 1]

xx = [0, 1]
yy = [0, 1]

Xx = [0, 0.4, 1, 1, 0.6, 0, 0]
Yy = [0, 0, 0.6, 1, 1, 0.4, 0]

X=[0, 1, 1, 0]
Y=[0, 0, 1, 1]


plt.scatter(X,Y, color="red")
plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(xx,yy)
plt.fill_between(Xx, Yy, color="green", alpha=0.3)

plt.text(0.2, 0.01, "r")
plt.text(-0.02, 0.2, "r")
plt.text(0.8, 1.01, "r")
plt.text(1.01, 0.8, "r")
plt.text(0.7, 0.01, "1-r")
plt.text(1.01, 0.3, "1-r")
plt.text(0.3, 1.01, "1-r")
plt.text(-0.02, 0.7, "1-r")

plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.grid()
plt.savefig("../images/plot1")
plt.show()

x=[0, 0.4, 0, 0]
y=[0, 0, 0.4, 0]

X=[1,0]
Y=[0,1]

plt.plot(x,y)
plt.scatter(x,y,color="red")
plt.fill_between(x, y,color="green", alpha=0.3)
plt.plot(X,Y,color="grey",linestyle="--")

plt.text(0.2, 0.01, "s")
plt.text(-0.02, 0.2, "s")

plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.grid()
plt.savefig("../images/plot2")
plt.show()

x=[0, 1, 1, 1, 0.4, 0, 0]
y=[0, 0, 0.4, 1, 1, 1, 0]

x1=[0, 1, 1, 0.4, 0, 0]
y1=[0, 0, 0.4, 1, 1, 0]

Xx=[1.4, 0]
Yy=[0, 1.4]

X=[1,0]
Y=[0,1]

plt.plot(x,y)
plt.scatter(x,y,color="red")
plt.fill_between(x1, y1,color="green", alpha=0.3)
plt.plot(X,Y,color="grey",linestyle="--")
plt.plot(Xx, Yy)

plt.text(0.7, 1.01, "2-s")
plt.text(1.02, 0.7, "2-s")

plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.grid()
plt.savefig("../images/plot3")
plt.show()
