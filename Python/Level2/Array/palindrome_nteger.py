# Author : Somnath Rakshit

def isPalindrome(self, A):
    l=len(A)
    ans=True
    for i in range(l//2):
        if A[i] != A[l-i-1]:
            ans=False
            break
    if ans:
        return 1
    else:
        return 0