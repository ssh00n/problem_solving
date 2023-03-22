import sys
input = sys.stdin.readline
# 2617. 구슬 찾기
# N(홀수)개의 구슬 1,2, ... N
# 구슬 중 무게가 전체의 중간인 ((N+1)/2)번째 구슬을 찾기
n, m = map(int, input().split())

# 현재 들어온 구슬보다 가벼운 리스트 
light = [[] for _ in range(n+1)]
# 현재 들어온 구슬보다 무거운 리스트
heavy = [[] for _ in range(n+1)]
mid = (n+1) //2


for _ in range(m):
    x, y = map(int, input().split())
    heavy[y].append(x)
    light[x].append(y)

def dfs(graph, v):
    global count
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(graph, i)

answer = 0        
for i in range(1, n+1):
    visited = [False] * (n+1)
    count = 0
    dfs(heavy, i)
    if count >= mid:
        answer += 1
    count = 0
    dfs(light, i)
    if count >= mid:
        answer += 1
        
print(answer)

