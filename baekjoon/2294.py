import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [] # = dx
visited = [False] * (10001)

for _ in range(n):
    coins.append(int(input()))

def bfs(coins):
    q = deque()    
    visited[0] = 1
    q.append((0, 0))
    while q:
        cur, cur_count = q.popleft()
        if cur == k:
            return cur_count
        
        for coin in coins:
            nx = cur + coin
            if nx in range(len(visited)):
                if not visited[nx]:
                    visited[nx] = visited[cur] + 1
                    q.append((nx, cur_count+1))
    return -1

print(bfs(coins))
