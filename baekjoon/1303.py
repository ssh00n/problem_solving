import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline


# 문제
# 전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 
# 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 
# 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.
# N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가?
# 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

# 입력
# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 
# 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 
# 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

# 출력
# 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다. -> W 병사의 위력, B 병사의 위력

N, M = map(int, input().split())
graph = [input().rstrip() for _ in range(M)]


def find_soldiers(start_y, start_x, target):
    q = deque()
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q.append((start_y, start_x))
    visited[start_y][start_x] = True
    soldiers = 1

    while q:
        cur_y, cur_x = q.popleft()
    
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if next_y in range(M) and next_x in range(N):
                if graph[next_y][next_x] == target and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    q.append((next_y, next_x))
                    soldiers += 1
    
    return soldiers

ally_groups = []
enemy_groups = []

for target in ['W', 'B']:
    visited = [[False] * N  for _ in range(M)]
    for y in range(M):
        for x in range(N):
            if graph[y][x] == target and not visited[y][x]:
                if target == 'W':
                    ally_groups.append(find_soldiers(y, x, target))
                else:
                    enemy_groups.append(find_soldiers(y, x, target))

print(sum(i**2 for i in ally_groups), sum(i**2 for i in enemy_groups))