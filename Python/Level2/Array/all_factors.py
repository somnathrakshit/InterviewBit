# Author : Somnath Rakshit

def allFactors(A):
    import math
    factors = []
    n = int(math.ceil(math.sqrt(A)))
    for i in range(1, n + 1):
        a = 0
        b = 0
        if A % i == 0:
            a = i
            b = A / a
            factors.append(int(a))
            factors.append(int(b))
    factors = list(set(factors))
    factors.sort()
    return factors


N = 100
print(allFactors(N))
