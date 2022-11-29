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

K = np.zeros((size, size))
W = np.zeros((size))
y = np.zeros((size))

for i in range(0, size):
  K[i,:] = A[i,:] / A[i][i]
  W[i] = b[i] / A[i][i]
  K[i][i] = 0

K = -K

for it in range(1, 1000):
  d = y
  y = (K@y) + W
  erro = max(abs(y - d)) / max(abs(y))
  print(f'{it}th Interation: {y}\nerror: [{erro}]{ndln}')
  if erro < eMax: break


print(f'Answer check: {np.round(A@y, 0)}')