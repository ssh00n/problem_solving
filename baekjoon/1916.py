import sys
import heapq 
# from collections import deque

# 시간 초과

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
# visited = [False] *(n+1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
        
        
# print(graph)

start, end = map(int, input().split())
costs = [1e9 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])
    
while heap:
    cur_cost, cur_v = heapq.heappop(heap)
    if costs[cur_v] < cur_cost:
        continue
    # if cur_v == end and cur_cost < min_cost:
    #     min_cost = cur_cost
    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_v]:
            continue
        
        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])
        

print(costs[end])