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

# Midpoint higherOrder
for i in range(n):
  k1y = gy(x[i], y[i], z[i])
  k1z = gz(x[i], y[i], z[i])
  k2y = gy(x[i] + (h / 2), y[i] + (k1y * (h / 2)), z[i] + (k1z * (h / 2)))
  k2z = gz(x[i] + (h / 2), y[i] + (k1y * (h / 2)), z[i] + (k1z * (h / 2)))
  phy = k2y
  phz = k2z
  x[i + 1] = x[i] + h
  y[i + 1] = y[i] + (h * phy)
  z[i + 1] = z[i] + (h * phz)

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