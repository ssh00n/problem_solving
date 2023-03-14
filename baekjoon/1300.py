# 1300 k번째 수
# n <= 10^5
# k <= min(10^9, n^2)
# A = [n][n]
# B = [n*n]
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        count = 0
        
        for i in range(1, n+1):
            count += min(mid//i, n)
        
        if count >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

print(binary_search(k, 1, n*n))

# A = [[(i+1)*(j+1) for j in range(n)] for i in range(n)]
# B = sum(A, [])
# B.sort()
# print(B[k+1])
# 이분 탐색을 통해 목표한 idx에 접근


# A = [[0]*n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         A[i][j] = (i+1) * (j+1)

# for i in range(n):
#     for j in range(n):
#         print(A[i][j], end=' ')
#     print()
# print(B)
