import sys
import heapq

n = int(sys.stdin.readline())

heap = []
res = 0

for i in range(n):
    card = int(sys.stdin.readline())
    heapq.heappush(heap, card)
    
# 힙에서 가장 작은 수(두 수의 합 or 카드)를 찾고, 그 두개를 더해서 heap에 push
# 2 2 3 3 
if n == 1:
    print(0)
else:
    while heap:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        res += (a + b)
        heapq.heappush(heap, a+b)
        if len(heap)==1:
            break

    print(res)