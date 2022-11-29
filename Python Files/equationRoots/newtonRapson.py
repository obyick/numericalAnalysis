import numpy as np # numerical python

a = 0.010; b = 0.015 # initial values to the first function
erro = 10**-5 # minimal error
itMax = 100 # maxima iteration

# main function
def f(x):
  return 1 - ((1 + x)**-48) - 35.48*x

# derived main function
def df(x):
  return (48/((1+x)**49)) - 35.48

def newtonRalphson(a, erro, itMax):
  it = 0
  x = a
  er = 1
  while(er >= erro and it < itMax):
    xold = x
    x = x-f(x)/df(x)
    er = np.abs((x-xold)/x)
    it += 1
  return(x, er, it)

resnf = newtonRalphson(a, erro, itMax)
print(f"The algorithm, by the Newton Ralphson method in f(x), found the root approximately at [{round(resnf[0], 5)}], with [{resnf[2]}] iterations.")