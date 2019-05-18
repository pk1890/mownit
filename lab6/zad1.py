import numpy as np 
import matplotlib.pyplot as plt 
import array
import functools
import operator
import time
import bisect

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
    # print(inter)
    return inter



def CubicSplineInterp(xs, ys):
    b, c, d  = [], [], []
    dim = len(xs)  # dimension of x
    h = np.diff(xs)

    # calc coefficient c
    a = [y for y in ys]

    
    A = np.zeros((dim, dim))
    A[0, 0] = 1.0
    A[0, 1] = 0.0
    A[dim - 1, dim - 2] = 0.0
    A[dim - 1, dim - 1] = 1.0

    for i in range(dim - 1):
        if i != (dim - 2):
            A[i + 1, i + 1] = 2.0 * (h[i] + h[i + 1])     #macierz trójprzekatniowa h[i], 2h[i]+2h[i+1], h[i+1]
        A[i + 1, i] = h[i]
        A[i, i + 1] = h[i]  


    B = np.zeros(dim)
    for i in range(dim - 2):
        B[i + 1] = 3.0 *((a[i + 2] - a[i + 1]) / h[i + 1] - (a[i + 1] - a[i]) / h[i]) 
        
    c = np.linalg.solve(A, B)
    
    for i in range(dim - 1):
        d.append((c[i + 1] - c[i]) / (3.0 * h[i]))  # d = 1/3 delta c/delta x
        b.append((a[i + 1] - a[i]) / h[i] - h[i] * (c[i + 1] + 2.0 * c[i]) / 3.0)
    def readCubInterpData(X):
        Y = []
        for x in X: 
            if x < xs[0]:
                i = 0 
            elif x >= xs[-1]:
                i = dim-2
            else:
                i = bisect.bisect(xs, x) - 1
            
            dx = x - xs[i]
            Y.append(a[i] + b[i] * dx + c[i] * dx ** 2.0 + d[i] * dx ** 3.0)
        return Y

        
    return lambda x: readCubInterpData(x)
    

# x2 = lambda x: x*x
x2 = lambda x: x*x*np.sin(x*4) 
# x2 = lambda x: np.exp(x)

pts = np.linspace(-2, 2, 300)
interpPoints = np.linspace(-2, 2, 10)
fInterp = x2(interpPoints)
plt.plot(pts, x2(pts))
plt.plot(interpPoints, x2(interpPoints), 'rd')
start = time.time()
interpolate = readLinInterpData(linearInterp(interpPoints, fInterp), pts)
end = time.time()

print("Linear time: ", end-start)
plt.plot(pts, interpolate)

plt.show()


plt.plot(pts, x2(pts))
plt.plot(interpPoints, x2(interpPoints), 'rd')
start = time.time()
interpolate = polynomialInterp(interpPoints, fInterp)(pts)
end = time.time()

print("Polynomial time: ", end-start)
plt.plot(pts, interpolate)
plt.show()

plt.plot(pts, x2(pts))
plt.plot(interpPoints, x2(interpPoints), 'rd')
start = time.time()
interpolate = CubicSplineInterp(interpPoints, fInterp)(pts)
end = time.time()

print("Cubic time: ", end-start)
plt.plot(pts, interpolate)
plt.show()