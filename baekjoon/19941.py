import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(input())
cnt = 0
for i in range(N):
    if arr[i] != "P":
        continue
    for j in range(i - K, i + K + 1):
        if 0 <= j < N:
            if arr[j] == "H":
                arr[j] = "-"
                cnt += 1
                break
print(cnt)
