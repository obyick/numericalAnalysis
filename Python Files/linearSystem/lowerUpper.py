import numpy as np # numerical python

# arrays to test
A = np.array([[13, -3, 4],[1, 9, -5], [1, 1, 8]])
b = np.array([[-31],[-22],[-47]])

size = len(A) # size of A array

xsum = lsum = usum = 0 # auxiliares values to sum

# initial and cap error
erro = 1
eMax = 1E-2

# endline
ndln = '\n-------------------------------------------------------------------\n'

U = np.concatenate((A, b), 1)
L = np.eye(size, size)
x = np.zeros(size)

for i in range(size):
  p = U[i, i]
  for j in range(i + 1, size):
    fator = U[j, i] / p
    L[j][i] = fator
    U[j,:] = U[j,:] - fator * U[i,:]

for i in range(size):
  for j in range(size):
    A[i][j] = U[i][j]
    b[i] = U[i, size]
    
for i in range(size - 1, -1, -1):
  sum = 0
  for j in range(size - 1, -1, -1):
    sum = sum + (A[i][j]) * (x[j])
  x[i] = ((b[i] - sum) / (A[i][i]))

for i in range(size):
  xsum = xsum + x[i]
  for j in range(size):
    usum = usum + U[i, j]
    lsum = lsum + L[i, j]

print(f'L:\n{L}',
      f'U:\n{U}',
      f'LU:\n{L@U}',
      f'L + U + x(n) = [{xsum+usum+lsum}]',
      sep = ndln)