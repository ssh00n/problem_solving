import sys

input = sys.stdin.readline

seq_a = input().rstrip()
seq_b = input().rstrip()

dp = [[0]*(len(seq_b)+1) for _ in range(len(seq_a)+1)]
result = []
for i in range(1, len(seq_a)+1):
    for j in range(1, len(seq_b)+1):
        if seq_a[i-1] == seq_b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
        