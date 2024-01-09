import sys
from collections import deque

input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

q = deque()
visitors_in_period = 0
periods = dict()

for visitor in visitors:
    q.append(visitor)
    visitors_in_period += visitor
    if len(q) == X:
        if visitors_in_period not in periods:
            periods[visitors_in_period] = 1
        else:
            periods[visitors_in_period] += 1
        oldest_visitor = q.popleft()
        visitors_in_period -= oldest_visitor

# Least Recently Used Algorithm

max_visitors = max(periods.keys())

if max_visitors:
    print(max_visitors)
    print(periods[max_visitors])
else:
    print("SAD")
