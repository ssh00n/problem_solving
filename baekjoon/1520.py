import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# logic
# 출발 지점 : (0, 0)
# 도착 지점 : (n-1, n-1)
# graph 탐색하면서(DFS) 현재 숫자보다 낮은 위치로 이동한다.
# (n-1, n-1)에 도착했으면 count += 1

m, n = map(int, input().split())

dp = [[None]*n for _ in range(m) ]
graph = [list(map(int, input().split())) for _ in range(m)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    if r == m-1 and c == n-1:
        return 1
    
    if dp[r][c] is not None:
        return dp[r][c]
    
    dp[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr in range(m) and nc in range(n):
            if graph[r][c] > graph[nr][nc]:
                dp[r][c] += dfs(nr, nc)
    
    return dp[r][c]
                

res = dfs(0, 0)
print(res)
