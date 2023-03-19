import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1) ]
visited = [False] * (n+1)
res = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
def bfs(x):
    
    visited[x] = True
    q = deque()
    q.append([x, 0])
    while q:
        cur_v, cur_count = q.popleft()
        if cur_count == k:
            res.append(cur_v)
        for v in graph[cur_v]:
            if not visited[v]:
                visited[v] = True
                q.append([v, cur_count+1])
    if cur_count < k:
        res.append(-1)

    return sorted(res)
    

print('\n'.join(map(str, bfs(x))))
