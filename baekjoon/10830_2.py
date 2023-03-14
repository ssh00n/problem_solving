import sys

n, b = map(int, sys.stdin.readline().split())

A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))


def dot(mat_1, mat_2):
    result = [[0 for i in range(len(mat_1))] for _ in range(len(mat_1))]
    
    for i in range(len(mat_1)):
        for j in range(len(mat_1)):
            for k in range(len(mat_1)):
                result[i][j] += (mat_1[i][k]*mat_2[k][j])
            
            result[i][j] %= 1000
    return result

def divide_conquer(mat, b):
    if b == 1:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] %= 1000
        return mat
    
    x = divide_conquer(mat, b//2)
    
    if b % 2 != 0:
        return dot(dot(x, x), mat)
    else:
        return dot(x, x)

ans = divide_conquer(A, b)

for i in ans:
    print(*i)