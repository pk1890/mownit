
import numpy as np
import time
from scipy.integrate import quad
from math import log, sqrt

def simpson(f, a, b):
    length = b-a
    h = length/10
    xs = np.linspace(a, b, num=6, endpoint=True)
    Int = sum(map(
            lambda x : (f(x) + 4*f(x-h) + f(x-2*h)) * (h/3)
            , xs[1::] ))

    return Int

def adaptive_simpson(f, a, b, err):
    m = (a+b)/2
    whole = simpson(f, a, b)
    left = simpson(f, a, m)
    right = simpson(f, m, b)

    if(abs(whole - left - right) > err):
        return(adaptive_simpson(f, a, m, err/2) + adaptive_simpson(f, m, b, err/2))
    else:
        return whole


def F1(x):
    return  np.exp(-x**2)*(log(x))**2


def F2(x):
    return 1/(x**3-2*x-5)
def F3(x):
    return x**2*np.exp(-x)*np.sin(x)
    
def F4(x):
    return x*x/(np.exp(x) - 1) # na przedziale 0 do inf

    


FFS = [(F1, 1, 3), (F2, 3, 4), (F3, 2, 3), (F4, 0.0001, 100)]
prec = 0.001
for (F, minim, maxim) in FFS:
    Int = quad(F, minim, maxim)
    print("\n\nNEXT FUNCTION, SCPIY: ", Int )
    start = time.time()
    adap = adaptive_simpson(F,minim, maxim, prec)
    end = time.time()
    print("========================================Me: ", adap, "Error: ", Int - adap)
    print("Time elapsed: ", end-start)