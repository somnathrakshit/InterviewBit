# Author : Somnath Rakshit

def coverPoints(X, Y):
    sum = 0
    for i in range(len(X) - 1):
        sum += max(abs(X[i + 1] - X[i]), abs(Y[i + 1] - Y[i]))
    return sum


X = [0, 1, 1]
Y = [0, 1, 2]
print(coverPoints(X, Y))
