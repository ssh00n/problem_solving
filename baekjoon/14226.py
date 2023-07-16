import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

# BOJ 14226 이모티콘
# 연산
# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
# 3. 화면에 있는 이모티콘 중 하나를 삭제

# S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값?
# BFS

# 1. 화면에 있는 정보 복사 -> 클립보드 
# 2. 클립보드 -> 화면에 붙여넣기
# 3. 화면에 있는 이모티콘 삭제

def emoticon(N):
    q = deque()
    visited = [[-1] * (N+1) for _ in range(N+1)]
    
    q.append((1, 0))
    visited[1][0] = 0

    
    
    while q:
        s, c = q.popleft()
        
        if visited[s][s] == -1:
            visited[s][s] = visited[s][c] + 1
            q.append((s, s))
        
        if (s + c) <= N and visited[s + c][c] == -1:
            visited[s + c][c] = visited[s][c] + 1
            q.append((s + c, c))
            
        if s - 1 >= 0 and visited[s - 1][c] == -1:
            visited[s - 1][c] = visited[s][c] + 1
            q.append((s - 1, c))
    return min([i for i in visited[N] if i != -1])        



def main():
    N = int(input())
    print(emoticon(N))



main()