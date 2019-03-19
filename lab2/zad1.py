import numpy as np 

import time

def solve(matrix :np.ndarray, vector: np.ndarray):
    if(matrix.shape[0] != matrix.shape[1]) :
       print("macierz musi byc kwadratowa", matrix[1][0])
       exit()

    if(vector.shape[1] != 1 and vector.shape[0] != matrix.shape[0]) :
       print("macierz musi byc kwadratowa", matrix[1][0])
       exit()

    # print(matrix)
    # print(np.linalg.inv(matrix))
    # print("====================")
    size = matrix.shape[0]
    result = np.identity(size)

    for column in range(0, size):
        for row in range(column, size):
            if matrix.item((row, column)) != 0:
                matrix[[column, row]] = matrix[[row, column]]
                result[[column, row]] = result[[row, column]]                 # zamien zawsze tak, aby bu
        value = matrix.item((column, column))
        for row in range(0, size):
            if(row == column): continue
            item = matrix.item((row, column))
            times = (item/value)
            for cell in range(0, size):
                curr = matrix.item((row, cell))
                matrix.itemset((row, cell), curr - (matrix.item(column, cell)*times))
                
                curr = result.item((row, cell))
                result.itemset((row, cell), curr - (result.item(column, cell)*times))

    for column in range (0, size):
        value = matrix.item((column, column))
        for row in range(0, size):
            matrix.itemset((column, row), matrix.item((column, row)) / value)
            result.itemset((column, row), result.item((column, row)) / value)

    
    # print( matrix)
    # print(result)

    
    return np.matmul(result, vector)
        # for i in range(0, size):
        # for row in range(0, size):

#print(np.matrix('1 3 2 ; 1 3 3 ').shape)
#solve(np.matrix('0 2 0 4 ; 0 0 0 3 ; 3 2 0 2 ; 0 2 3 4'))

dim = 600
m = 1000 * np.random.rand(dim, dim)
v = 1000 * np.random.rand(dim, 1)
print(m)

start = time.time()
reslib = np.linalg.solve(m, v)
end = time.time()

libtime = end-start

start = time.time()
myres = solve(m, v)
end = time.time()

mytime = end-start


print(reslib - myres)

print("lib time:", libtime, "mytime: ", mytime)




#matrix = [[-1, 2, 1, -1], [1, -3, -2, -1], [3, -1, -1, 4]]
# m = np.matrix('-1 2 1 ; 1 -3 -2  ; 3 -1 -1')

# print(solve(m))

# #print(np.matrix('1 3 2 ; 1 3 3 ').shape)
# solve(np.matrix('0 2 0 4 ; 0 0 0 3 ; 3 2 0 2 ; 0 2 3 4'))
