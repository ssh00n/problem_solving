import sys


input = sys.stdin.readline

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
edges = []
total = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
    
edges.sort(key=lambda x: x[2])
for edge in edges:
    a, b, cost = edge
    if find_parent(a) != find_parent(b):
        union_parent(parent, a, b)
        total += cost

print(total)

