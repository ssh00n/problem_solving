import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

cnt = 0
for i in range(len(coins)-1, -1, -1):
    if k == 0:
        break
    cnt += k // coins[i]
    k = k % coins[i]
    
    
print(cnt)
