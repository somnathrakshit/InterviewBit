# Author : Somnath Rakshit

def wave(A):
    A.sort()
    ans = []
    l = len(A)
    for i in range(0, l - 1, 2):
        ans.append(A[i + 1])
        ans.append(A[i])
    if l % 2 == 1:
        ans.append(A[-1])
    return ans


A = [1,3,7,10,5]
print(wave(A))
