# 백준 11725. 트리의 부모 찾기
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

vertices = [[0] for _ in range(n+1)]
parent = [0]*(n+1)
parent[1] = 0

q = deque()
q.append(1)

for _ in range(n-1):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)
    

while q:
    current = q.popleft()
    for v in vertices[current]:
        if parent[v] == 0:
            parent[v] = current
            q.append(v)

print('\n'.join(map(str, parent[2:])))