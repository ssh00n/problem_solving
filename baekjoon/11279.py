import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []
# heapq.heappush(x)

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not max_heap:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap, (-x, x))
        
