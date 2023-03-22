import sys
sys.setrecursionlimit(10**6)
# 10026. 적록색약
# R G B
# 적록색약 -> (RG) B

n = int(sys.stdin.readline())
graph = [list(input().rstrip()) for _ in range(n)]


    

def dfs(x, y, rg_weak):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(n) and ny in range(n) and not visited[nx][ny]:
            if graph[nx][ny] == graph[x][y] and rg_weak == 0:
                dfs(nx, ny, 0)
            elif graph[nx][ny] == graph[x][y] and rg_weak == 1:
                dfs(nx, ny, 1)
                
    return 1

visited = [[False]*n for _ in range(n)]
result1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result1 += dfs(i, j, 0)

# Red Green Weakness (R == G)
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"
            
visited = [[False]*n for _ in range(n)]
result2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result2 += dfs(i, j, 1)
            
print(f"{result1} {result2}")