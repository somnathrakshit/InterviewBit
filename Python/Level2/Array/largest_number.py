# Author : Somnath Rakshit

# Author : Somnath Rakshit

def largestNumber(A):
    A = list(A)
    def my_cmp(a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        if ab > ba:
            return 1
        elif ab < ba:
            return -1
        else:
            return 0
    
    A.sort(cmp=my_cmp, reverse=True)
    return ''.join(str(e) for e in A)


A = [8, 89]
print(int(largestNumber(A)))

