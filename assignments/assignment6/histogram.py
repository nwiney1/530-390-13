#1/usr/bin/env python
import numpy as np
import improc
import matplotlib.pyplot as plt
#generating a histogram
#A array of values
#N = number of bins
def hist(A,N):
  n = len(A)
  improc.mergesort(A,n)
  minA = A[0]
  maxA = A[N]
  diff = maxA - minA
  size_bin = diff / N
  counter = 0
  I = 0
  num_per_bin = np.zeros(N)
  max_val = minA + size_bin
  bins = np.zeros(N)
  i = 1
  bins[i] = max_val
  for j in range(n):
    if A[j] <= max_val:
      counter = counter + 1 
    else:
      num_per_bin[i] = counter
      counter = 0
      max_val = max_val + size_bin
      I = I + counter*size_bin
      if i < N-1:
        i = i + 1
      else:
        num_per_bin= num_per_bin 
  plt.plot(bins,num_per_bin)
  plt.show()
  return I  
#B = num_per_bin
#mergesort(B)
#C_hist = np.zeros(N,B[N])
#tmp1 = 0
#for k in range(N) 
#  C_hist[k,:] = A[tmp:tmp + num_per_bin[k]]
#  tmp = tmp + num_per_bin[k]


