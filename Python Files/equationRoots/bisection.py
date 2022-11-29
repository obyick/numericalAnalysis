import numpy as np # numerical python

a = 0.010; b = 0.015 # initial values to the first function
erro = 10**-5 # minimal error
itMax = 100 # maxima iteration

# main function
def f(x):
  return 1 - ((1 + x)**-48) - 35.48*x

def bisection(a, b, erro, itMax):
  it = 0
  x = a
  erro = 10**-5
  er = 1
  while(er >= erro and it < itMax):
    xold = x
    x = (a+b)/2
    er = np.abs((x-xold)/x)
    if(f(a)*f(x) < 0):
      b = x
    else:
      a = x
    it += 1
  return(x, er, it)

resbf = bisection(a, b, erro, itMax)
print(f"The algorithm, by the Bisection method in f(x), found the root approximately at [{round(resbf[0], 5)}], with [{resbf[2]}] iterations.")