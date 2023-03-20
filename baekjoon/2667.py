import sys
from collections import deque

input = sys.stdin.readline


# 5 <= n <= 25
n = int(input())
graph = []
for _ in range(n):
    graph.append(input().rstrip())

visited = [[False]*n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    count = 0
    
    while q:
        cur_x, cur_y = q.popleft()
        if graph[cur_x][cur_y] == "1" and visited[cur_x][cur_y]:
            count += 1
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx in range(n) and ny in range(n):
                if graph[nx][ny] == "1" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and not visited[i][j]:
            result.append(bfs(i, j))

print(len(result))
print('\n'.join(map(str, sorted(result))))