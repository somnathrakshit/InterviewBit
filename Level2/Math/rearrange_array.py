# Author : Somnath Rakshit

def arrange(A):
    l = len(A)
    for i in range(l):
        A[i] += (A[A[i]] % l) * l
    for i in range(l):
        A[i] //= l
    return A


A = [3, 2, 0, 1]
print(arrange(A))
