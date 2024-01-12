import sys

input = sys.stdin.readline

N, K = map(int, input().split())
table = input().rstrip()

mask_array = [0 for _ in range(N)]
count = 0
for i in range(len(table)):
    if table[i] == "P":
        start, end = i - K, i + K  # 햄버거를 탐색할 구간
        if start < 0:
            start = 0
        if end >= N:
            end = N - 1

        for j in range(start, end + 1):
            if table[j] == "H" and not mask_array[j]:
                mask_array[j] = 1
                count += 1
                break

print(count)
