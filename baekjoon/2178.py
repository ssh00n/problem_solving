import sys
from collections import deque

input = sys.stdin.readline

# 0, 0 에서 출발하여 N-1, M-1의 위치로 이동할 때 지나야 하는 최소 칸의 수

n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]
count = 0
visited = [[False]*m for _ in range(n)]

def escape_maze(maze):
    shortest = -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    row = len(maze)
    col = len(maze[0])
    visited[0][0] = True
    queue = deque()
    queue.append([0, 0, 1])

    while queue:
        cur_x, cur_y, cur_len = queue.popleft()
        if cur_x == n-1 and cur_y == m-1:
            shortest = cur_len
            break
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                if maze[next_x][next_y] == "1" and not visited[next_x][next_y]:
                    queue.append([next_x, next_y, cur_len + 1])
                    visited[next_x][next_y] = True
    return shortest

result = escape_maze(maze)
print(result)


         
# for i in range(n):
#     for j in range(m):
#         if maze[i][j] == "1" and not visited[i][j]:
#             res.append(bfs(i, j))
            



