import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 판다 모든 자리에서 해봐야 하고, dfs를 마치고 돌아와서 해당 칸에 카운트 기록하면 됨

dp = [[-1]*n for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    
    
    dp[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny in range(n) and nx in range(n):
            if graph[y][x] < graph[ny][nx]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
    
    return dp[y][x]

ans = 0
        
# for y in range(n):
#     for x in range(n):
#         ans = max(ans, dfs(y, x))

# print(ans)


# print(dfs(0, 0))
for y in range(0, 2):
    for x in range(0, 2):
        dfs(y, x)
    # print()

for i in range(n):
    for j in range(n):
        print(dp[i][j], end=' ')
    print()

