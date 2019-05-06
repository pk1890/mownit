
import numpy as np
import time
from scipy.integrate import quad
from math import log, sqrt

def ff(x):
    return 1/(sqrt(x)+1)

def rectangle(f, min, max, count):
    print("Metoda prostokątów")
    length = (max - min)
    h = length / count 
    xs = np.linspace(min, max, num=count, endpoint=False)
    Int = sum(map(
        lambda x : f(x) * h
        , xs[1::]))

    return Int

def trapeze(f, min, max, count):
    print("\nMetoda trapezów")
    length = (max - min)
    h = length / count 
    xs = np.linspace(min, max, num=count+1, endpoint=True)
    Int = sum(map(
            lambda x : (f(x) + f(x-h)) * h/2
            , xs[1::]))
    return Int


def F1(x):
    return  np.exp(-x**2)*(log(x))**2


def F2(x):
    return 1/(x**3-2*x-5)
def F3(x):
    return x**2*np.exp(-x)*np.sin(x)
    
def F4(x):
    return x*x/(np.exp(x) - 1) # na przedziale 0 do inf

    
FFS = [(F1, 3, 10), (F2, 3, 4), (F3, 2, 3), (F4, 0.00001, 100)]
prec = 100000
for (F, minim, maxim) in FFS:
    Int = quad(F, minim, maxim)
    print("\n\nNEXT FUNCTION, SCPIY: " ,Int)
    start = time.time()
    rec = rectangle(F,minim, maxim, prec)
    end = time.time()
    print("========================================Me: ", rec, "Error: ", Int - rec)
    print("Time elapsed: ", end-start)
    start = time.time()
    trap = trapeze(F, minim, maxim, prec)
    end = time.time()
    print("========================================Me: ", trap, "Error: ", Int - trap)
    print("Time elapsed: ", end-start)