# Author : Somnath Rakshit

def setZeroes(A):
    r = len(A)
    c = len(A[0])
    rows = [1] * r
    cols = [1] * c
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 0:
                rows[i] = 0
                cols[j] = 0
    for i in range(r):
        if rows[i] == 0:
            for j in range(len(A[i])):
                A[i][j] = 0
    for i in range(c):
        if cols[i] == 0:
            for j in range(len(A)):
                A[j][i] = 0
    return A


A = [[1, 0, 1, ],
     [1, 1, 1],
     [1, 1, 1]]

print(setZeroes(A))
