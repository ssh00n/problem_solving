import sys
from collections import deque

input = sys.stdin.readline

def bfs(i, j):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    visited[i][j] = True
    q.append((i, j))
    
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx in range(m) and ny in range(n):
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return 1


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    result = 0
    graph = [[0]*n for _ in range(m)]
    visited = [[False]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                res = bfs(i, j)
                result += res
    print(result)
    
    