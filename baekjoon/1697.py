import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    start, end = map(int, input().split())

    q = deque()
    q.append((start))
    visited = [False] * (100001)
    visited[start] = 1
    
    if start == end:
        return 0

    while q:
        cur_x = q.popleft()
        if cur_x == end:
            return visited[cur_x] - 1
        nx_list = [cur_x+1, cur_x-1, cur_x*2]
        for nx in nx_list:
            if nx in range(100001) and not visited[nx]:
                visited[nx] = visited[cur_x] + 1
                q.append((nx))
                
res = bfs()
print(res)