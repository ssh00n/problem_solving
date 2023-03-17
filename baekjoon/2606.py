import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n_node = int(input())
n_edge = int(input())

graph = [[] for _ in range(n_node+1)]
for _ in range(n_edge):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n_node+1)
count = 0

def dfs(v):
    global count
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            count += 1
            dfs(i)


dfs(1)
print(count)