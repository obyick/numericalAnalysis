import numpy as np # numerical python
import matplotlib.pyplot as plt # collection of functions that make matplotlib work

# points
x = np.array([[2.2], [3.3], [4.4], [5.5], [6.6], [7.7]])
y = np.array([[-2.8], [-10.8], [-5.9], [21.4], [41.4], [9.1]])
p = 5.2

# degree of the polynomial
n = 2
gp = n + 1

b = 2 # b(n) = t(n)

# endline
ndln = '\n-------------------------------------------------------------------\n'

# impossible system coefficients matrix
X = x**0
for i in range(1, n + 1):
  X = np.concatenate((X, x**i), 1)

# assembling the possible and determined system
XtX = (X.T)@X
XtY = (X.T)@y

ac = np.linalg.solve(XtX, XtY) # solve the system and determine values of a0, a1 and a2

# best point definition matrices
resx = np.zeros((gp))
resy = np.zeros((gp))
minx = np.copy(x) - p
miny = np.copy(y)

# sets the three coordinates closest to the point
for i in range(gp):
  for j in range(len(x)):
    if abs(minx[j]) == np.min(abs(minx)):
      resx[i] = minx[j] + p
      resy[i] = miny[j]
      minx[j] = 1E50
      break

# Lagrange
def interpolacaoLagrange(x, y, p):
  size = len(resx)
  s = 0
  for i in range(size):
      L = 1
      for j in range(size):
        if i != j:
          L *= (p - resx[j])/(resx[i] - resx[j])
      s += L * resy[i]
  return s
  
s = interpolacaoLagrange(x, y, p)

# results
print(f'g({np.round(p, 4)}): [{np.round(s, 2)}]', end = ndln)

# graph coordinates
xg = np.linspace((np.min(x)), (np.max(x)), 100)
yg = 0
for i in range(n + 1):
  yg = yg + ((ac[i,0])*(xg**i))

# graph plot
plt.title(f'Degree {n} Polynomial Function')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.axvline(p)
plt.axhline(s)
plt.grid()
plt.plot(x, y, 'o')
plt.plot(p, s, 'o')
plt.plot(xg, yg)
plt.show()