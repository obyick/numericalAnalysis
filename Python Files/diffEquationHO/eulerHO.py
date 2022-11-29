import numpy as np # numerical python
import matplotlib.pyplot as plt # collection of functions that make matplotlib work

# functions
def gy(x, y, z):
  return z

def gz(x, y, z):
  m = 60
  c = 5
  k = 20
  return (-(c * z) - (k * y)) / m

# points
a = 0; b = 10; h = 0.5
X = a; Y = 1.2; Z = a

# endline
ndln = '\n-------------------------------------------------------------------\n'

# auxiliary array
n = int(abs((b - a) / h))
x = np.zeros(n + 1)
y = np.zeros(n + 1)
z = np.zeros(n + 1)

# initial values
x[0] = X
y[0] = Y
z[0] = Z

# Euler higherOrder
for i in range(n):
  ky = gy(x[i], y[i], z[i])
  kz = gz(x[i], y[i], z[i])
  x[i + 1] = x[i] + h
  y[i + 1] = y[i] + (ky * h)
  z[i + 1] = z[i] + (kz * h)

# output
for i in range(len(x)):
  print(f'{i}th Interation:\nx = {round(x[i])}, y = {round(y[i], 3)}, z = {round(z[i], 3)}',
        end = ndln)

# graphic
plt.plot(x, y, 'r')
plt.plot(x, z, 'g')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()
plt.show()