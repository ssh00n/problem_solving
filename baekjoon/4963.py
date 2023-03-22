import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


while True:
    w, h = map(int, input().split())
    if w==h==0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    visited = [[False]*w for _ in range(h)]
    
    def dfs(x, y):
        dx = [0, 0, 1, -1, 1, -1, 1, -1]
        dy = [1, -1, 0, 0, 1, 1, -1, -1]
        visited[x][y] = True
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx in range(h) and ny in range(w):
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    dfs(nx, ny)
        return 1
    
    res = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                res += dfs(i, j)
                
    print(res)