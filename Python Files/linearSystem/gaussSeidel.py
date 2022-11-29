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

K = np.eye(size) - np.linalg.inv(np.eye(size)*A)@A
w = np.linalg.inv(np.eye(size)*A)@b
x = np.zeros((size, 1))

for i in range(size):
  xold = np.copy(x)
  for j in range(size):
    x[j, 0] = K[j,:]@x + w[j, 0]
    erro = np.max(np.abs(x-xold)) / np.max(np.abs(x))
  print(f'\n{i+1}th Interation\n',
        f'x:\n{x}',
        f'\nDifference between x in the {i+1}th and {i}th interaction:\n{x - xold}',
        f'\nerror: [{erro}]\n',
        sep = '\n', end = ndln)