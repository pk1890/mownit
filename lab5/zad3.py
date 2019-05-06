
import numpy as np
import time
from scipy.integrate import quad
from numpy import log, sqrt



def F1(x):
    return  np.exp(-x**2)*(log(x))**2


def F2(x):
    return 1/(x**3-2*x-5)
def F3(x):
    return x**2*np.exp(-x)*np.sin(x)
    
def F4(x):
    return x*x/(np.exp(x) - 1) # na przedziale 0 do inf

def monteCarlo(f, a, b, size):
    x = np.random.uniform(a, b, size)
    start = time.time()
    vf = np.vectorize(f)
    end = time.time()
    print(end-start)
    mean = sum(vf(x)) / size
    return (b-a) * mean 


FFS = [(F1, 3, 10), (F2, 3, 4), (F3, 2, 3), (F4, 0.00001, 100)]
prec = 1000000
for (F, minim, maxim) in FFS:
    Int = quad(F, minim, maxim)
    print("\n\nNEXT FUNCTION, SCPIY: " ,Int)
    start = time.time()
    mc = monteCarlo(F,minim, maxim, prec)
    end = time.time()
    print("========================================Me: ",mc, "Error: ", Int - mc)
    print("Time elapsed: ", end-start)