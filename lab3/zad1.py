import numpy as np 
import math
# import scipy.misc

def derivative(F, x, eps):
    return((F(x) - F(x+eps))/(eps))

def bisect(F, min:float, max:float, accuracy:float, itNo:int):
    center = (max+min)/2
    if(abs(F(center)) < accuracy ):
        print("Used iterations:", itNo)
        return center
    else:
        if(F(center)*F(min) < 0):
            return bisect(F, min, center, accuracy, itNo+1)
        else:
            return bisect(F, center, max, accuracy, itNo+1)

Fa = lambda x: math.cos(x) * math.cosh(x) - 1
Fb = lambda x: 1/x - np.tan(x) #[0, 2pi] z badania przebiegu zmienności wiemy że jedno zero jesst w [0.5, 1] a drugie w [3, 4]
Fc = lambda x: 2**(-x) + math.exp(x) + 2 * math.cos(x) - 6

def newton_solve(F, min:float, max:float, accuracy:float, itLim: int):
    x_last = np.infty
    x = min
    i = 0
    while(abs(x - x_last) > accuracy and i < itLim):
        x_last = x
        x = x - (F(x) / derivative(F, x, 1e-10))
        i+=1
    return x


ACCURACY = 1e-10

print("FA=======")
print("Bisect: ", bisect(Fa, 3/2*math.pi, 2*math.pi, ACCURACY, 0))
print("Newton: ", newton_solve(Fa, 3/2*math.pi, 2*math.pi, ACCURACY, 10))


print("FB=======")
print(bisect(Fb, 0.5, 1, ACCURACY, 0))
print(bisect(Fb, 3, 4, ACCURACY, 0))

print("FC========")
print(bisect(Fc, 1, 3, ACCURACY, 0))

