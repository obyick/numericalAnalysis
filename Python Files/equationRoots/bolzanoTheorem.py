import numpy as np # numerical python

a = 0.010; b = 0.015 # initial values to the first function

# main function
def f(x):
  return 1 - ((1 + x)**-48) - 35.48*x

# Bolzano theorem
if (f(a) * f(b) < 0):
  print("There's a root in the interval [a, b].")
elif (f(a) * f(b) == 0):
  print("Both [a, b] are roots.")
else:
  print("There isn't root in the interval [a, b].")