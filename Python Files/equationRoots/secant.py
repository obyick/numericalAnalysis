import numpy as np # numerical python

a = 0.010; b = 0.015 # initial values to the first function
erro = 10**-5 # minimal error
itMax = 100 # maxima iteration

# main function
def f(x):
  return 1 - ((1 + x)**-48) - 35.48*x

def secant(a, b, erro, itMax):
  it = 0
  er = 1
  xa = a
  x = b
  while(er >= erro and it < itMax):
    xb = xa
    xa = x
    x = xa-f(xa)*(xb-xa)/(f(xb)-f(xa))
    er = np.abs((x-xa)/x)
    it += 1
  return(x, er, it)

ressf = secant(a, b, erro, itMax)
print(f"The algorithm, by the Secant method in f(x), found the root approximately at [{round(ressf[0], 5)}], with [{ressf[2]}] iterations.")