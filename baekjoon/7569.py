import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque([])
res = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append([z, x, y])

def bfs():
    while queue:
        cur_z, cur_x, cur_y = queue.popleft()
        for i in range(6):
            next_z = cur_z + dz[i]
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0<=next_x<n and 0<=next_y<m and 0<=next_z<h and graph[next_z][next_x][next_y] == 0:
                graph[next_z][next_x][next_y] = graph[cur_z][cur_x][cur_y] + 1
                queue.append([next_z, next_x, next_y])
                
bfs()
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        res = max(res, max(j)) 


print(res-1)


# for z in range(h):      # i = 0, 1 (0 <= z <h)
#     for x in range(n):        # j = 0, 1, 2 (0 <= x < n)
#         for y in range(m):                # k = 0, 1, 2, 3, 4 (0 <= y < m)
#             print(graph[z][x][y], end=" ")
#         print()
#     print()