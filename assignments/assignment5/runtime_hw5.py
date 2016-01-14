#!/usr/bin/env python
import integrator as intr
import numpy as np
import matplotlib.pyplot as plt


# 1st problem
PI = 2.*np.arcsin(1)
a=0
b= 2*PI
N= 10
h = (a+b) / (N-1)
x = np.zeros(N)
y1 = np.zeros(N)
y2 = np.zeros(N)
y8 = np.zeros(N)
for i in range(N):
  x[i] = a + h*i
  y1[i] = np.sin(x[i])
  y2[i] = np.sin(2*x[i])
  y8[i] = np.sin(8*x[i]) 

print(intr.trap_d(x,intr.multiply(y1,y1)))
print(intr.trap_d(x,intr.multiply(y1,y2)))
print(intr.trap_d(x,intr.multiply(y2,y8)))
print(intr.trap_d(x,intr.multiply(y8,y8)))

#2nd problem
a2= 0
b2 = 1
N = [10, 100, 1000] 
N2 = len(N)
for i in range(N2):
  x = np.zeros(N[i])
  y = np.zeros(N[i])
  print("for N = " + str(N[i])) 
  print(intr.trap(intr.lin,a2,b2,N[i]))
  print(intr.trap(intr.quad,a2,b2,N[i]))
  print(intr.trap(intr.eleventhpow,a2,b2,N[i]))
  print(intr.trap(intr.twelfthpow,a2,b2,N[i]))
  print(intr.trap(intr.exp,a2,b2,N[i]))
 
#Gauss-Legendre quadrature
n = [1, 2, 6]
n2 = len(n)
for k in range(n2):
  [x,w] = intr.gauss_leg(a2,b2,n[k])
  print("for n = " + str(n[k]))
  print(intr.gauss_quad(intr.lin,x,w))
  print(intr.gauss_quad(intr.quad,x,w))
  print(intr.gauss_quad(intr.eleventhpow,x,w))
  print(intr.gauss_quad(intr.twelfthpow,x,w))
  print(intr.gauss_quad(intr.exp,x,w))
 
