import sys
input = sys.stdin.readline

# logic
# 3x3 행렬로 뒤집어야 하므로
# 먼저 3x3씩 Sliding 하면서 한 행 또는 한 열이 같은지 확인한다.
# 행 비교 -> 같으면 아래로, 다르면 열 비교 -> 옆으로 이동


n, m = map(int, input().split())

matrix_a = [list(map(str, input().rstrip())) for _ in range(n)]
matrix_b = [list(map(str, input().rstrip())) for _ in range(n)]

def column(matrix, i):
    return [row[i] for row in matrix]

def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if matrix_a[i][j] == '0':
                matrix_a[i][j] = '1'
            else:
                matrix_a[i][j] = '0'

def compare_row(x, y):
    if matrix_a[x][y:y+3] == matrix_b[x][y:y+3]:
        return 1
    else:
        return 0
    
def compare_column(x, y):
    if column(matrix_a[x:x+3], y) == column(matrix_b[x:x+3], y):
        return 1
    else:
        return 0

count = 0
    
for i in range(n):
    for j in range(m):
        if compare_row(i, j):
            continue
        else:
            reverse(i, j)
            count += 1
        
    



