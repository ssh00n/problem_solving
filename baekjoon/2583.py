import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

m, n, k = map(int, input().split())
grid = [[0]*(n) for _ in range(m)]
visited =[[False]*n for _ in range(m)]

for _ in range(k):
    sy, sx, ey, ex = map(int, input().split())
    for i in range(sx, ex):
        for j in range(sy, ey):
            grid[i][j] += 1


def dfs(x, y, count = 0):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[x][y] = True
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(m) and ny in range(n):
            if grid[nx][ny] == 0 and not visited[nx][ny]:
                count = dfs(nx, ny, count)
    return count
                
res = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0 and not visited[i][j]:
            res.append(dfs(i, j, 0))
print(len(res))
print(*sorted(res))