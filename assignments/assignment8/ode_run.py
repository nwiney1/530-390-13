#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import ode
import pde

#problem 1
# Poisson problem
Lx = 10
Ly = 4
Nx = 25
Ny = 25

#dx = Lx/(Nx-1)
#dy = Ly/(Ny-1)
dx = 0.1
dy = 0.1

d2dx2 = 1/(dx*dx)

T = np.zeros(Nx*Ny)
f = np.zeros(Nx*Ny)

# set forcing
i = np.floor(0.5*Nx)
j = np.floor(0.5*Ny)
f[i + j*Nx] = 1

# boundary conditions
for j in range(Ny):
  i = 0
  T[i+j*Nx] = 1
  i = Nx-1
  T[i+j*Nx] = 0
for i in range(Nx):
  j = 0
  T[i+j*Nx] = 0
  j = Ny-1
  T[i+j*Nx] = 0

# Jacobi iteration
T = pde.jacobi(T,f,dx,Nx,Ny,1000)

# check error
# (build matrix)
nx = Nx - 2
ny = Ny - 2
A = np.zeros([nx*ny,nx*ny])
for q in range(nx*ny):
  for p in range(nx*ny):
    if p == q:
      A[p,q] = -4*d2dx2
    elif p == q-1:
      A[p,q] = 1*d2dx2
    elif p == q+1:
      A[p,q] = 1*d2dx2
    elif p == q-nx:
      A[p,q] = 1*d2dx2
    elif p == q+nx:
      A[p,q] = 1*d2dx2

# boundary conditions
for q in range(nx*ny):
  for p in range(nx*ny):
    if p % nx == nx-1 and q % ny == 0:
      A[p,q] = 0
    if p % nx == 0 and q % ny == ny-1:
      A[p,q] = 0

#plt.imshow(A,interpolation="none")
#plt.show()

# pull out the interior
T_int = np.zeros(nx*ny)
f_int = np.zeros(nx*ny)
for j in range(ny):
  for i in range(nx):
    T_int[i+j*nx] = T[(i+1) + (j+1)*Nx]
    f_int[i+j*nx] = f[(i+1) + (j+1)*Nx]

# (calculate error) ** DOES NOT WORK FOR NONZERO BOUNDARY CONDITIONS **
b_tilde = pde.Au(A,T_int)
norm = pde.norm2(pde.bsc(f_int,b_tilde))
#print(norm)

# plot
T_plot = np.zeros([Nx,Ny])
f_plot = np.zeros([Nx,Ny])
for j in range(Ny):
  for i in range(Nx):
    T_plot[i,j] = T[i+j*Nx]
    f_plot[i,j] = f[i+j*Nx]

x = np.zeros([Nx+1,Ny+1])
y = np.zeros([Nx+1,Ny+1])
for j in range(Ny+1):
  for i in range(Nx+1):
    x[i,j] = -0.5*dx + i*dx
    y[i,j] = -0.5*dy + j*dy

plt.pcolormesh(x,y,T_plot,edgecolors="black")
plt.colorbar()
plt.show()
