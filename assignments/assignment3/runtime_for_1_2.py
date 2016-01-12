#!/usr/bin/env python

#assignment 1 runtime

import improc 
import numpy as np
import time
import Fibonacci
import matplotlib.pyplot as plt
n1 = 100
n2 = 1000
n3 = 10000

A1 = np.random.rand(n1)
A1_m = np.array(A1)
A2 = np.random.rand(n2)
A2_m = np.array(A2)
A3 = np.random.rand(n3)
A3_m = np.array(A3)
t0 = time.time()

improc.selectionsort(A1,n1)
t1_s = time.time()
improc.mergesort(A1_m,n1)
t1_m = time.time()
print(t1_s)
print(t1_m)
improc.selectionsort(A2,n2)
t2_s = time.time()
improc.mergesort(A2_m,n2)
t2_m = time.time()


improc.selectionsort(A3,n3)
t3_s = time.time()
improc.mergesort(A3_m,n3)
t3_m = time.time()

N = [n1, n2, n3]
t_s = [t1_s-t0, t2_s-t1_m, t3_s-t2_m]
print(t_s)
t_m = [t1_m-t1_s, t2_m-t2_s, t3_m-t3_s]
print(t_m)
plt.plot(N,t_s,N,t_m)
plt.show()

# assignment 2
F24 = Fibonacci. fibonacci(24)
print(F24)
