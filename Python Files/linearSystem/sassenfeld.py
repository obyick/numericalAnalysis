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

K = np.eye(size) - (np.linalg.inv(np.eye(size) * A) @ A)
W = (np.linalg.inv(np.eye(size)*A) @ b)
beta = np.ones((size, 1))
x = np.copy(b)

line = 0
colunm = 0

for i in range(size):
  x = K@x + W
  beta[i,0] = K[i,:] @ beta
  line = line + abs(K[:,i])
  colunm = colunm + abs(K[i,:])

sass = np.max(abs(beta))

print(f'K:\n{K}', f'Beta:\n{beta}', f'Sassenfeld: [{sass}]',
      f'Line sum: [{np.max(abs(line))}]', 
      f'Colunm sum: [{np.max(abs(colunm))}]', 
      sep = ndln)