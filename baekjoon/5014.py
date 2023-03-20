import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    # F : 건물의 층 수
    # S : 현재 위치
    # G : 목표 층
    # U : 한번에 올라갈 수 있는 층 수
    # D : 한번에 내려갈 수 있는 층 수

    F, S, G, U, D = map(int, input().split())
    visited = [0] * (F+1)
    visited[S] = 1
    if S == G:
        return 0
    
    deltas = [U, -D]
    q = deque()
    q.append((S))
    
    while q:
        cur = q.popleft()
        if cur == G:
            return visited[cur] - 1
        for delta in deltas:
            nx = cur + delta
            if nx in range(1, F+1) and not visited[nx]:
                visited[nx] = visited[cur] + 1
                q.append((nx))
                
    return "use the stairs"

print(bfs())
