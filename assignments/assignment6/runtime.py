import numpy as np
#import histogram
import integrator as intr
import matplotlib as plt

N =100000
A = np.zeros(N)
b = 5
n = 10000
for i in range(N):
  A[i] = exponential(b)
histogram.hist(A,n)

problem 2
[w,Sw] = intr.monte_carlo_3d(intr.density,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[x,Sw] = intr.monte_carlo_3d(intr.xmoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[y,Sw] = intr.monte_carlo_3d(intr.ymoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[z,Sw] = intr.monte_carlo_3d(intr.zoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)

print(x/w,y/w,z/w)
print(7)

