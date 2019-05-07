import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# def f(x, y): return x*y*y-x*6*np.sin(2*x*y)
# def f(x, y): return x*y*y-x
def f(x, y): return x*x*y*y


phi_m = np.linspace(0, 6, 100)
phi_p = np.linspace(0, 6, 100)

node_x = np.linspace(0, 6, 10)
node_y = np.linspace(0, 6, 10)

X,Y = np.meshgrid(phi_p, phi_m)
NX, NY = np.meshgrid(node_x, node_y)
NZ = f(NX, NY).T

Z = f(X, Y).T
fig = plt.figure(figsize=(14,6))

# `ax` is a 3D-aware axis instance, because of the projection='3d' keyword argument to add_subplot
bx = fig.add_subplot(1, 2, 2, projection='3d')
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)
p1 = ax.scatter(NX, NY, NZ, c='r')
p2 = bx.scatter(NX, NY, NZ, c='r')



def lineInterp(X, Y, Z):
    data = []
    for i in range(0, len(X)-1):
        for j in range(0, len(Y)-1):
            A = np.zeros((4, 4))
            for k in range (0, 4): A[0][k] = 1
            A[1][0] = X[i]
            A[1][1] = X[i]
            A[1][2] = X[i+1]
            A[1][3] = X[i+1]


            A[2][0] = Y[j]
            A[2][2] = Y[j]
            A[2][1] = Y[j+1]
            A[2][3] = Y[j+1]

            for k in range(4):
                A[3][k] = A[1][k] * A[2][k]

            B = np.zeros((1, 4))
            B[0][0] = Z[i][j]
            B[0][1] = Z[i][j+1]
            B[0][2] = Z[i+1][j]
            B[0][3] = Z[i+1][j+1]

            # print(A)

            C = np.linalg.solve(A.T, B.T)
            data.append((X[i], X[i+1], Y[j], Y[j+1], C))
    
    def fun(x, y):
        for (xmin, xmax, ymin, ymax, C) in data:
            if x < xmin or y < ymin or x > xmax or y > ymax: continue
            return C[0] + C[1] * x + C[2] * y + C[3] *x*y
    
    return lambda x, y: fun(x, y)

Zi = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        Zi[i][j] = lineInterp(node_x, node_y, NZ)(phi_m[i], phi_p[j])
bx.plot_surface(X, Y, Zi, color='g')
    
plt.show()