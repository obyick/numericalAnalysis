import numpy as np # numerical python
import matplotlib.pyplot as plt # collection of functions that make matplotlib work

# array
x = np.array([[0.], [1.5], [3.], [3.5]])
y = np.array([[2.0], [4.2], [2.5], [0.2]])

n = 2 # degree of the polynomial

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

VE = X@ac - y # find error vector

# calc quadratic error (1th and 2th)
EQ = np.transpose(VE)@VE
EQ2 = np.sum(VE**2)

# results
print(f'Impossible system coefficients matrix:\n{X}',
      f'Assembling the possible and determined system of x:\n{XtX}',
      f'Assembling the possible and determined system of y:\n{XtY}',
      f'a values:\n{ac}',
      f'Error vector:\n{VE}',
      f'Quadratic error (1th way):\n{EQ}',
      f'Quadratic error (2th way):\n[{EQ2}]', sep = ndln)

# graph information
plt.title(f'Degree {n} Polynomial Function')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()

plt.plot(x, y, 'o') # points plot

# g(x) plot
xg = np.linspace((np.min(x) - 0.2), (np.max(x) + 0.2), 100)
yg = 0
for i in range(n + 1):
  yg = yg + ((ac[i,0])*(xg**i))
plt.plot(xg, yg)

plt.show() # show everything in the same graph