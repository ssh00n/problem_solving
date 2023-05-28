# Approach
# 연결 요소의 개수를 구하는 문제이다.
# visited == False일 때 BFS를 호출하면서 연경 요소 count

from collections import deque

def solution(n, computers):
    
    # 각 컴퓨터 : 0 ~ n-1의 정수
    def bfs(start_node):
        q = deque()
        q.append(start_node)
        visited[start_node] = True
        
        while q:
            cur_node = q.popleft()
            for i in range(len(computers[cur_node])):
                if computers[cur_node][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append(i)
        return 1
    
    visited = [False]*(n)
    answer = 0
    for computer in range(len(computers)):
        if not visited[computer]:
            answer += bfs(computer)
        
    
    return answer

