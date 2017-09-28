# Author : Somnath Rakshit

def titleToNumber(A):
    A = A[::-1].strip()
    sum = 0
    m = 0
    for i in A:
        i = ord(i) - 65 + 1
        sum += pow(26, m) * i
        m += 1
    return sum


A = "A"
print(titleToNumber(A))
