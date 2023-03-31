import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


dp = [[None]*n for _ in range(n)]

dy = [1, 0]
dx = [0, 1]

def dfs(y, x):
    # 종료시점 도착
    if y == n-1 and x == n-1:
        return 1
    
    if dp[y][x] is not None:
        return dp[y][x]
        
    dp[y][x] = 0
    for i in range(2):
        ny = y + dy[i]*graph[y][x]
        nx = x + dx[i]*graph[y][x]
        if 0 <= ny < n and 0 <= nx < n:
            dp[y][x] += dfs(ny, nx)
            
    return dp[y][x]

print(dfs(0, 0))

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end=' ')
#     print()