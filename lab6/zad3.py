
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# def f(x, y): return x*y*y-x*6*np.sin(2*x*y)
# def f(x, y): return x*y*y-x
def f(x, y, z): return x*x*y*y*z*z

CurrZ = 3

phi_m = np.linspace(0, 6, 100)
phi_p = np.linspace(0, 6, 100)
phi_r = np.linspace(0, 6, 100)

node_x = np.linspace(0, 6, 5)
node_y = np.linspace(0, 6, 5)
node_z = np.linspace(0, 6, 5)
X, Y= np.meshgrid(phi_p, phi_m)
NX, NY = np.meshgrid(node_x, node_y)
NZ = f(NX, NY, CurrZ).T

InterpX, InterpY, InterpZ = np.meshgrid(node_x, node_y, node_z)
InterpR = f(InterpX, InterpY, InterpZ)

Z1 = f(X, Y, CurrZ).T
fig = plt.figure(figsize=(14,6))

# `ax` is a 3D-aware axis instance, because of the projection='3d' keyword argument to add_subplot
bx = fig.add_subplot(1, 2, 2, projection='3d')
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z1, rstride=4, cstride=4, linewidth=0)
p1 = ax.scatter(NX, NY, NZ, c='r')
p2 = bx.scatter(NX, NY, NZ, c='r')



def lineInterp(X, Y, Z, R):
    data = []
    for i in range(0, len(X)-1):
        for j in range(0, len(Y)-1):
            for k  in range(0, len(Z) -1):
                A = np.zeros((8, 8))
                for l in range (0, 8): A[0][l] = 1

                for l in range(0, 8): A[1][l] = X[i] if l % 2 == 0 else X[i+1] 
                for l in range(0, 8): A[2][l] = Y[j] if l % 4 <  2 else Y[j+1]
                for l in range(0, 8): A[3][l] = Z[k] if l     <  4 else Z[k+1]
                for l in range(0, 8): A[4][l] = A[1][l]*A[2][l]
                for l in range(0, 8): A[5][l] = A[1][l]*A[3][l]
                for l in range(0, 8): A[6][l] = A[2][l]*A[3][l]
                for l in range(0, 8): A[7][l] = A[4][l]*A[3][l]


                B = np.zeros((1, 8))
                B[0][0] = R[i  ][j  ][k  ]
                B[0][1] = R[i+1][j  ][k  ]
                B[0][2] = R[i  ][j+1][k  ]
                B[0][3] = R[i+1][j+1][k  ]
                B[0][4] = R[i  ][j  ][k+1]
                B[0][5] = R[i+1][j  ][k+1]
                B[0][6] = R[i  ][j+1][k+1]
                B[0][7] = R[i+1][j+1][k+1]
                # print(A)

                C = np.linalg.solve(A.T, B.T)
                data.append((X[i], X[i+1], Y[j], Y[j+1], Z[k], Z[k+1], C))
    
    def fun(x, y, z):
        for (xmin, xmax, ymin, ymax, zmin, zmax, C) in data:
            if x < xmin or y < ymin or z < zmin or x > xmax or y > ymax or z > zmax: continue
            return C[0] +          \
                   C[1] * x   +    \
                   C[2] * y   +    \
                   C[3] * z   +    \
                   C[4] * x*y +    \
                   C[5] * x*z +    \
                   C[6] * y*z +    \
                   C[7] * x*y*z 

    
    return lambda x, y, z: fun(x, y, z)

Zi = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        Zi[i][j] = lineInterp(node_x, node_y, node_z, InterpR)(phi_m[i], phi_p[j], CurrZ)
bx.plot_surface(X, Y, Zi, color='g')
    
plt.show()