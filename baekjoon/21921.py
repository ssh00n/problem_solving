import sys
from collections import deque

input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

q = deque()
visitors_in_period = 0
max_visitors = 0
max_count = 0

for i in range(N):
    visitor = visitors[i]
    q.append(visitor)
    visitors_in_period += visitor

    if i >= X - 1:
        if visitors_in_period > max_visitors:
            max_visitors = visitors_in_period
            max_count = 1
        elif visitors_in_period == max_visitors:
            max_count += 1

        visitors_in_period -= q.popleft()

# Least Recently Used Algorithm


if max_visitors:
    print(max_visitors)
    print(max_count)
else:
    print("SAD")
