# Author : Somnath Rakshit

import math


def primesum(A):
    ans = [0, 0]
    A += 1
    a = [True] * A
    a[0] = a[1] = False
    
    for (i, isprime) in enumerate(a):
        if isprime:
            #yield i
            for n in range(i * i, A, i):
                a[n] = False
    ans = [0, 0]
    for i in range(1, A + 1):
        if a[i] and a[A - 1 - i]:
            ans[0] = i
            ans[1] = A - i - 1
            break
    return ans


A = 16777214
print(primesum(A))
