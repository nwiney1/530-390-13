#1/usr/bin/env python
import improc.py
import matplotlib.pyplot as plt
#generating a histogram
#A array of values
#N = number of bins
def hist(A,N):
  n = len(n)
  mergesort(A)
  minA = A[0]
  maxA = A[N]
  diff = maxA - minA
  size_bin = diff / N
  counter = 0
  I = 0
  num_per_bin = np.zeros(N)
  tmp = min[A]
  bins = np.zeros(N)
  for i in range(N):
    tmp = tmp + size_bin
    bins[i] = tmp
      for j in range(n):
        if A[j] <= max_val:
          counter = counter + 1 
        else:
          num_per_bin[i] = counter
          counter = 0
          tmp = tmp + size_bin
          I = I + counter
  noralize = I
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


