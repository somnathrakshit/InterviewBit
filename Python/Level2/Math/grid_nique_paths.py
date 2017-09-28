# Author : Somnath Rakshit

def uniquePaths(m, n):
    grid = [[0] * (n + 1) for row in range(m + 1)]
    grid[1][1] = 1
    for i in xrange(1, len(grid)):
        for j in xrange(1, len(grid[0])):
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1]
    return grid[m][n]
