import numpy as np # numerical python
import matplotlib.pyplot as plt # collection of functions that make matplotlib work

# function
def g(x, y):
  return -0.06 * np.sqrt(y)

# points
a = 0; b = 5; h = 1
X = a; Y = 3

# endline
ndln = '\n-------------------------------------------------------------------\n'

# auxiliary array
n = int(abs((b - a) / h))
x = np.zeros(n + 1)
y = np.zeros(n + 1)

# initial values
x[0] = X
y[0] = Y

# Euler
for i in range(n):
  k = g(x[i], y[i])
  x[i + 1] = x[i] + h
  y[i + 1] = y[i] + (h * k)

# output
for i in range(len(x)):
  print(f'{i}th Interation:\nx = {round(x[i])}, y = {round(y[i], 3)}',
        end = ndln)

# graphic
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('g(x)')
plt.plot(x, y, 'o')
plt.grid()
plt.show()