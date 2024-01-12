import sys

input = sys.stdin.readline

# approach : Dynamic Programming <- 지역해가 최적해를 보장하지 않음

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float("inf")] * 3 for _ in range(M)] for _ in range(N)]
# dp[r][c][d] -> (r, c)위치에 있고, 마지막으로 d 방향으로 이동했을 때의 최소 비용

for c in range(M):
    for d in range(3):
        dp[0][c][d] = space[0][c]

# prev_c = c - 1 if prev_d = 2
# prev_c = c if prev_d = 1
# prev_c = c + 1 if prev_d = 0
# [0, 1, 2]

# Graph Traversal
for r in range(1, N):
    for c in range(M):
        prev_c_list = [c + 1, c, c - 1]
        for d in range(3):
            for prev_d in range(3):  # prev_d = 0 or 1 or 2
                prev_c = prev_c_list[prev_d]
                if d != prev_d and prev_c in range(M):
                    dp[r][c][d] = min(
                        dp[r][c][d], dp[r - 1][prev_c][prev_d] + space[r][c]
                    )
min_cost = float("inf")
for c in range(M):
    for d in range(3):
        min_cost = min(min_cost, dp[-1][c][d])

print(min_cost)
