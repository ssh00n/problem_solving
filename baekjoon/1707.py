# 1707. 이분 그래프

import sys
from collections import deque

input = sys.stdin.readline

k = int(input())

def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] == 0:
                visited[i] = -visited[cur]
                q.append(i)
            else:
                if visited[i] == visited[cur]:
                    return False
    return True


for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    flag = True
    
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    for i in range(1, v+1):
        if visited[i] == 0:
            if not bfs(i):
                flag= False
                break
            
    print("YES" if flag else "NO")
