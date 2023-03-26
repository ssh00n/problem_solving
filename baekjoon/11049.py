import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())

matrices = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*(n) for _ in range(n)]

def top_down_dp(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    if x == y:
        return 0
    
    if x + 1 == y:
        return matrices[x][0] * matrices[x][1] * matrices[y][1]
    
    for k in range(x, y):
        left = top_down_dp(x, k)
        right = top_down_dp(k+1, y)
        
        if dp[x][y] == -1 or dp[x][y] > left + right + matrices[x][0] * matrices[k][1] * matrices[y][1]:
            dp[x][y] = left + right + matrices[x][0] * matrices[k][1] * matrices[y][1]
            
    return dp[x][y]

print(top_down_dp(0, n-1))