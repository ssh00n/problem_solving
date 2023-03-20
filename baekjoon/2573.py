import sys
from collections import deque
input = sys.stdin.readline

# 2573. 빙산
# 바다(0)로 둘러싸여 있는 빙산(x>0)은 해마다 0과 인접한 개수만큼 그 크기가 줄어든다
# BFS로 1보타 큰 영역을 탐색하고, 주변에 0이 있을 경우 그 개수만큼 1씩 감소시켜준다
# BFS가 호출되는 개수가 1번 -> 2번으로 감소하는 최초의 시간(년)을 출력

def solution():
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    def iceberg(i, j):
        visited = [[False]*m for _ in range(n)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        q = deque()
        visited[i][j] = True
        q.append((i, j))
        
        while q:
            cur_x, cur_y = q.popleft()
            if graph[cur_x][cur_y] > 0:
                count = 0
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]         
                    if next_x in range(n) and next_y in range(m):
                        if graph[next_x][next_y] == 0 and not visited[next_x][next_y]:
                            count += 1
                        elif graph[next_x][next_y] > 0 and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
                if count > graph[cur_x][cur_y]:
                    graph[cur_x][cur_y] = 0
                    visited[cur_x][cur_y] = True
                else:
                    graph[cur_x][cur_y] = graph[cur_x][cur_y] - count
                    visited[cur_x][cur_y] = True
        # for i in range(n):
        #     for j in range(m):
        #         print(graph[i][j], end=' ')
        #     print()
                
        return 1    

    def count_ice(i, j):
        visited = [[False]*m for _ in range(n)]
        count = 0
        def bfs(i, j):
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            q = deque()
            visited[i][j] = True
            q.append((i, j))
            
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if next_x in range(n) and next_y in range(m) and not visited[next_x][next_y]:
                        if graph[next_x][next_y] > 0:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y)) 
            return 1
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0 and not visited[i][j]:
                    count += bfs(i, j)
        return count

    def count_years():
        visited = [[False]*m for _ in range(n)]
        years = 0
        num_ice = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0 and not visited[i][j]:
                    years += iceberg(i, j)
                    num_ice = count_ice(i, j)
                    if num_ice >=2:
                        return years
        return 0

    print(count_years())

solution()
