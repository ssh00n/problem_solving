import sys

n, b = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
c = 1000

def dot(mat_1, mat_2):
    result = [ [0]*len(mat_1) for _ in range(len(mat_1))]
    temp = 0
    for i in range(len(mat_1)):
        for j in range(len(mat_1)):
            for k in range(len(mat_1)):
                temp += mat_1[j][k]*mat_2[k][j]
            result[i][j] = temp % 1000
            
    return result

# def mat_mod(mat, c):
#     for i in range(len(mat)):
#         for j in range(len(mat)):
#             mat[i][j] = mat[i][j] % c
    
#     return mat
    # result[i][j] = mat[i] * mat[j]
    # mat[0][:] * mat[:][0]
    
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
    
ans = divide_conquer(A, 10)

for i in ans:
    print(*i)
# A_2 = dot(A, A)
# A_3 = dot(A_2, A)
# A_4 = dot(A_3, A)
# A_5 = dot(A_4, A)
# A_6 = dot(A_5, A)

# print(mat_mod(A_2, 1000))
# print(mat_mod(A_3, 1000))
# print(mat_mod(A_4, 1000))
# print(mat_mod(A_5, 1000))
# print(mat_mod(A_6, 1000))


# for i in range(3):
#     mat = dot_square(mat, mat)

# print(mat_mod(mat, 1000))




# mat[i][j] * mat[j][i]-> j= 0, 1, 2, 3, 4
# result[i][j] = mat[i][:] * mat[:][j]

# result[0][0] = mat[0][0]*mat[0][0] + mat[0][1]*mat[1][0] + mat[0][2]*mat[2][0] + mat[0][3]*mat[3][0]

# mat[0][0, 1, 2, 3, 4] * mat[0, 1, 2, 3, 4][0] -> result[0][0] = 2
# mat[0][0, 1, 2, 3, 4] * mat[0, 1, 2, 3, 4][1] -> result[0][1] = 0
# mat[0][0, 1, 2, 3, 4] * mat[0, 1, 2, 3, 4][2] -> result[0][2] = 0
# mat[0][0, 1, 2, 3, 4] * mat[0, 1, 2, 3, 4][3] -> result[0][3] = 0
# mat[0][0, 1, 2, 3, 4] * mat[0, 1, 2, 3, 4][4] -> result[0][4] = 2
