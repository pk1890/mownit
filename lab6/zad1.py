import numpy as np 
import matplotlib.pyplot as plt 
import array
import functools
import operator

def readLinInterpData(data, X):
    Y = []
    for i in range(0, len(X)):
        for (b, a, mi, ma) in data:
            if X[i] >= mi and X[i] <= ma:
                Y.append(a*(X[i]-mi) +b)
                break
    return Y


def linearInterp(X, Y):
    ret = []
    for i in range(0, len(X)-1):
        ret.append((Y[i], #b
             (Y[i+1]-Y[i])/(X[i+1]-X[i]), #a
             X[i], #min
             X[i+1])) #max
    print(ret)
    return ret

def polynomialInterp(X, Y):
    inter = np.poly1d([0])
    for i in range(0, len(Y)):
        ret = np.poly1d([1])
        for j in range(0, len(X)):
            if not j == i:
                ret = ret * np.poly1d([1/(X[i]-X[j]), -X[j]/(X[i]-X[j])])
        inter = inter + (Y[i] * ret)
    print(inter)
    return inter

def splineInterp(X, Y):
    

# x2 = lambda x: x*x
x2 = lambda x: x*x*np.sin(x*4) 
# x2 = lambda x: np.exp(x)

pts = np.linspace(-2, 2, 300)
interpPoints = np.linspace(-2, 2, 10)
fInterp = x2(interpPoints)
plt.plot(pts, x2(pts))
plt.plot(interpPoints, x2(interpPoints), 'rd')

plt.plot(pts, readLinInterpData(linearInterp(interpPoints, fInterp), pts))

plt.show()


plt.plot(pts, x2(pts))
plt.plot(interpPoints, x2(interpPoints), 'rd')
plt.plot(pts, polynomialInterp(interpPoints, fInterp)(pts))
plt.show()