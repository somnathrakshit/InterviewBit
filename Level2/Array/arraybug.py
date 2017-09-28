# Author : Somnath Rakshit

def rotateArray(a, b):
    ret = []
    for i in range(len(a)):
        ret.append(a[(i + b)%len(a)])
    return ret

a= [1, 2, 3, 4, 5, 6]
b=5
print(rotateArray(a,b))