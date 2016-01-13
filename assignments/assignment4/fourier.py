#!/usr/bin/env python
import fft
import numpy as np
import matplotlib.pyplot as plt
import time
#import improc

PI = 2*np.arcsin(1)
N1 = 64
N2 = 512
L = 1
dt1 = L / (N1-1)
dt2 = L / (N2-1)
t1 = np.zeros(N1)
t2 = np.zeros(N2)
f1 = np.zeros(N1)
f2 = np.zeros(N2)
g1 = np.zeros(N1)
g2 = np.zeros(N2)
h1 = np.zeros(N1)
h2 = np.zeros(N2)

for i in range(N1):
  t1[i] = i*dt1
  f1[i] = i
  if t1[i] <= 0.1:
    g1[i] = 1
    h1[i] = 0
  elif t1[i] <= 0.4:
    g1[i] = 0
    h1[i] = 0
  elif t1[i] <= 0.6:
    g1[i] = 0
    h1[i] = 1
  else:
    g1[i] = 0
    h1[i] = 0

for j in range (N2): 
  t2[j] = j*dt2
  f2[j] = j
  if t2[j] <= 0.1:
    g2[j] = 1
    h2[j] = 0
  elif t2[j] <= 0.4:
    h2[j] = 0
    g2[j] = 0
  elif t2[j] <= 0.6:
    g2[j] = 0
    h2[j] = 1
  else:  
    h2[j] = 0
    g2[j] = 0
print("with N equal to " + str(N1))
print(fft.correlation(g1,h1))
print("with N equal to " + str(N2))
print(fft.correlation(g2,h2))
#fft.plot_c(f1[:0.5*N],[:N])

#ys = np.zeros(2*N)
#yf = np.zeros(2*N)


#sigma = PI / 16. / 2
#dsigma2 = 1. / (sigma*sigma)
#C = 1. / (np.sqrt(2.*PI)*sigma)
#I = 0
#for i in range(N):
#  x[i] = i*dx
#  f[i] = i
#  ys[2*i] = np.sin(x[i]) + np.sin(4.*x[i]) + np.random.rand(1)
#  ys[2*i+1] = 0
#  yf[2*i] = C * np.exp(-x[i]*x[i]*dsigma2*0.5)
#  yf[2*i] = yf[2*i] + C * np.exp(-(x[i-1]-L)*(x[i-1]-L)*dsigma2*0.5)
#  yf[2*i+1] = 0
#  I = I + yf[2*i]
#for i in range(N):
#  yf[2*i] = yf[2*i] / I
#  yf[2*i+1] = yf[2*i+1] / I

#fft.plot_c(x,ys)
#fft.plot_c(x,yf)
#conv = fft.convolution(ys,yf)
#fft.plot_c(x,conv)

#fft.plot_c(x,y)
#t0 = time.time()
#y = fft.fft_slow(y,1.)
#t1 = time.time()
#fft.plot_c(f[:0.5*N],y[:N])
#y = fft.fft_slow(y,-1.)
#fft.plot_c(x,y)
#
#t2 = time.time()
#fft.fft(y,1.)
#t3 = time.time()
#fft.plot_c(f[:0.5*N],y[:N])
#fft.fft(y,-1.)
#
#print("Fast = " + str(t3-t2))

#plt.plot(x,y)

#img = improc.rgb_to_gray_lum(improc.read("gilman-hall.jpg"))
#data_real = img[:,0,0]
#N = len(data_real)
#N2 = fft.pow2(N)
#x = np.zeros(N2)
#L = N
#L2 = N2
#data = np.zeros(2*N2)
#gaus = np.zeros(2*N2)

#sigma = 2.*PI
#dsigma2 = 1. / (sigma*sigma)
#C = 1. / (np.sqrt(2.*PI)*sigma)
#I = 0
#for i in range(N2):
#  x[i] = i
#  if i < N:
#    data[2*i] = data_real[i]
#    data[2*i+1] = 0
#  gaus[2*i] = C * np.exp(-x[i]*x[i]*dsigma2*0.5)
#  gaus[2*i] = gaus[2*i] + C * np.exp(-(x[i]-L2)*(x[i]-L2)*dsigma2*0.5)
#  gaus[2*i+1] = 0
#  I = I + gaus[2*i]
#for i in range(N2):
#  gaus[2*i] = gaus[2*i] / I

#data_slow = np.array(data)
#gaus_slow = np.array(gaus)

#t0 = time.time()
#conv_fast = fft.convolution(data,gaus)
#t1 = time.time()
#conv_slow = fft.convolution_slow(data_slow,gaus_slow)
#t2 = time.time()

#print("Fast: ", t2-t1, "Slow: ", t1-t0)

#plt.show()


