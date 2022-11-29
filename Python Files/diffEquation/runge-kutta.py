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

# RK4
for i in range(n):
  k1 = g(x[i], y[i])
  k2 = g(x[i] + (h / 2), y[i] + (k1 * (h / 2)))
  k3 = g(x[i] + (h / 2), y[i] + (k2 * (h / 2)))
  k4 = g(x[i] + h, y[i] + (k3 * h))
  phi = (k1 + (2 * k2) + (2 * k3) + k4) / 6
  x[i + 1] = x[i] + (h)
  y[i + 1] = y[i] + (h * phi)

# output
for i in range(len(x)):
  print(f'{i}th Interation:\nx = {round(x[i])}, y = {round(y[i], 3)}',
        end = ndln)

# output
it = 2 
print(f'k1 = {g(x[it], y[it])}',
      f'k2 = {g(x[it] + (h / 2), y[it] + (k1 * (h / 2)))}',
      f'k3 = {g(x[it] + (h / 2), y[it] + (k2 * (h / 2)))}',
      f'k4 = {g(x[it] + h, y[it] + (k3 * h))}',
      sep = ndln, end = ndln)

# graphic
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('g(x)')
plt.plot(x, y, 'o')
plt.grid()
plt.show()