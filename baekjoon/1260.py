import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s] = graph.get(s, []) + [e]
    graph[e] = graph.get(e, []) + [s]

# print(graph)
visited = []

def dfs(cur_v):
    visited.append(cur_v)
    for v in sorted(graph[cur_v]):
        if v not in visited:
            dfs(v)
    return visited
            
def bfs(start_v):
    visited = [start_v]
    queue = deque([start_v])
    while queue:
        cur_v = queue.popleft()
        for v in sorted(graph[cur_v]):
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

print(*dfs(v))
print(*bfs(v))