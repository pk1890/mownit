import numpy as np 

def doolitleLU(matrix: np.ndarray):
    if(matrix.shape[0] != matrix.shape[1]) :
        print("macierz musi byc kwadratowa", matrix[1][0])
        exit()

    # print(matrix)
    # print(np.linalg.inv(matrix))
    # print("====================")
    size = matrix.shape[0]
    result = np.copy(matrix)

    L = np.ndarray(matrix.shape)
    U = np.ndarray(matrix.shape)

    for col in range(0, size):
        if(matrix.item((col, col)) == 0):
            for row in range(col, size):
                if(abs(matrix.item((row, col))) > abs(matrix.item((col,col)))):
                    matrix[[col, row]] = matrix[[row, col]]
                    break
    print(L)
    print(U)
    print("++++++++++++++++++++++++++++=")

    print(0*L)
    print(0*U)
    for column in range(0, size):
        for row in range(column, size):
            sum = 0
            for i in range(0, column):
                sum += L.item((column, i)) * U.item((i, row))
            U.itemset((column, row), matrix.item(column, row) - sum)    
        for row in range(column, size):
            if(column == row):
                L.itemset((column, column), 1)
            else:
                sum = 0
                for i in range(0, row):
                    sum+= L.item((row, i)) * U.item((i, column))
                L.itemset((row, column), ((matrix.item(row, column) - sum )/ U.item((column, column))))    
    
    np.set_printoptions(suppress=True)

    print(matrix)
    np.set_printoptions(suppress=True)
    print(L)
    print(U)




np.set_printoptions(suppress=True)

doolitleLU(np.matrix('0 1 2 ; 4 5 6 ; 8 9 10'))  