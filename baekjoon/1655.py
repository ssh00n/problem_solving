import heapq
import sys
# 시간 초과 


n = int(sys.stdin.readline())

baekjoon = [int(sys.stdin.readline()) for _ in range(n)]

# heap = heapq.heapify(baekjoon)
heap = []
res = []

for i in range(1, n+1):
    for j in range(i):
        heapq.heappush(heap, baekjoon[j])
    
    for k in range((len(heap)-1) //2):
        heapq.heappop(heap)
    print(heapq.heappop(heap))
    
    while heap:
        heapq.heappop(heap)
