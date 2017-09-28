# Author : Somnath Rakshit

def plusOne(A):
    A.reverse()
    carry = 0
    A[0] += 1
    for i in range(len(A)):
        if carry == 1:
            A[i] += 1
            carry = 0
        
        if A[i] >= 10:
            A[i] %= 10
            carry = 1
    
    if carry == 1:
        A.append(1)
    A.reverse()
    A = [int(e) for e in list(''.join(str(e) for e in A).lstrip("0"))]
    return A


A = [9, 9, 9]
print(plusOne(A))
