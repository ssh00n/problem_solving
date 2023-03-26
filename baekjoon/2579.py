import sys
input = sys.stdin.readline

# 제한 조건
# 1. 계단은 한 번에 한 계단 or 두 계단씩
# 2. 연속된 세 개의 계단을 모두 밟을 수 없음
# 3. 마지막 도착 계단은 반드시 밟아야 함

# -> Subproblem 으로 분할
# Optimal Substructure

n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [0]*(n)

if len(stairs) <=2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1] 
    
    for i in range(2, n):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

    print(dp[-1])
    