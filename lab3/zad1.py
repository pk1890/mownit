import numpy as np 
import math
from matplotlib import pyplot as plt
# import scipy.misc

def derivative(F, x, eps):
    return((F(x+eps) - F(x))/(eps))

def bisect(F, min:float, max:float, accuracy:float, itNo:int):
    center = (max+min)/2
    if(abs(F(center)) < accuracy ):
        print("Used iterations bisect:", itNo)
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
    
    print("Used iterations Newton:", i)
    return x

def euler_solve(F, min:float, max:float, accuracy:float, itLim: int):
    x1 = min
    x2 = max
    i = 0
    while(abs(x2-x1) > accuracy and i < itLim):
        x3 = (F(x2)*x1-F(x1)*x2)/(F(x2)-F(x1))
        x1 = x2
        x2 = x3
        i+=1   
    print("Used iterations Euler :", i)
    return x3


ACCURACY = 1e-12

print("FA=======")
print("Bisect: ", bisect(Fa, 3/2*math.pi, 2*math.pi, ACCURACY, 0))
print("Newton: ", newton_solve(Fa, 3/2*math.pi, 2*math.pi, ACCURACY, 10))
print("Euler : ", euler_solve(Fa, 3/2*math.pi, 2*math.pi, ACCURACY, 10))


print("FB==(1)=====")
print("Bisect: ", bisect(Fb, 0.5, 1, ACCURACY, 0))
print("Newton: ", newton_solve(Fb, 0.5, 1, ACCURACY, 20))
print("Euler : ", euler_solve(Fb, 0.5, 1, ACCURACY, 20))
print("FB==(2)=====")
print("Bisect: ", bisect(Fb, 3, 4, ACCURACY, 0))
print("Newton: ", newton_solve(Fb, 3, 4, ACCURACY, 20))
print("Euler : ", euler_solve(Fb, 3, 4, ACCURACY, 20))

print("FC========")
print("Bisect: ", bisect(Fc, 1, 3, ACCURACY, 0))
print("Newton: ", newton_solve(Fc, 1, 3, ACCURACY, 20))
print("Euler : ", euler_solve(Fc, 1, 3, ACCURACY, 20))
