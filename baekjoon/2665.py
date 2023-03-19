import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input().rstrip()))

q = deque()
q.append([0, 0, 0])
visited = [[False]*n for _ in range(n)]
visited[0][0] = True
deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
costs = [[1e9]*n for _ in range(n)]
costs[0][0] = 0


while q:
    cur_cost, cur_x, cur_y = q.popleft()
    if costs[cur_x][cur_y] < cur_cost:
        continue
    
    for delta in deltas:
        next_x = cur_x + delta[0]
        next_y = cur_y + delta[1]
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
                if grid[cur_x][cur_y] == "0":
                    next_cost = cur_cost + 1
                else:
                    next_cost = cur_cost
                    
                if next_cost >= costs[next_x][next_y]:
                    continue
                costs[next_x][next_y] = next_cost
                q.append([next_cost, next_x, next_y])

print(costs[n-1][n-1])
