import numpy as np 
import math
import time

def min_plus(matrix: np.ndarray, other: np.ndarray):
    if(matrix.shape[0] != matrix.shape[1] != other.shape[0] != other.shape[1]) :
       print("macierz musi byc kwadratowa", matrix[1][0])
       exit()

    dim = matrix.shape[0]
    result = np.ndarray((dim, dim))

    for i in range (0, dim):
        for j in range (0, dim):
            minVal = matrix.item((i, 0)) + other.item((0, j))
            for k in range (1, dim):
                minVal = min(minVal, matrix.item(i, k) + other.item(k, j))
            result.itemset((i, j), minVal)

    return result
    
def shortest_path(matrix: np.ndarray):
    if(matrix.shape[0] != matrix.shape[1]) :
        print("macierz musi byc kwadratowa", matrix[1][0])
        exit()
    res = matrix
    for i in range(0, math.ceil(math.log2(matrix.shape[0]))):
        res = min_plus(res, res)
    return res

def floyd_warshall(matrix: np.ndarray):
    dim = matrix.shape[0]
    for k in range(0, dim):  
        for i in range(0, dim): 
            for j in range(0, dim): 
                matrix.itemset((i, j), min(matrix.item((i, j)) , matrix.item((i, k))+ matrix.item((k, j)))) 

    return matrix

I = np.infty
m = np.array([[0, I, 1, I],
                [2, 0, 5, 1],
                [I, 2, 0, 1],
                [8, I, 12, 0]])
print(m)
mm = min_plus(m, m)
#print (mm)
print(shortest_path(m))
print(floyd_warshall(m))

test = np.random.rand(100, 100)

for i in range(0, 100):
    test.itemset((i, i), 0)

start = time.time()
floyd_warshall(test)
end = time.time()


 
libtime = end-start
start = time.time()
shortest_path(test)
end = time.time()


shorttime = end-start


print("floyd time:", libtime, "mytime: ", shorttime)