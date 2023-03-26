import sys
input = sys.stdin.readline


n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
dp = [[0]*(len(triangle[i])+1) for i in range(len(triangle))]
dp[0][0] = triangle[0][0]


for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))
