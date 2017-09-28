# Author : Somnath Rakshit

import math

def isPrime(n):
    if n == 2:
        return 1
    if n % 2 == 0 or n <= 1:
        return 0
    
    sqr = int(math.sqrt(n)) + 1
    
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return 0
    return 1


A = 2
print(isPrime(A))
