import sys

N = int(sys.stdin.readline())
costs = list(map(int, sys.stdin.readline().split()))


costs.sort()
sum_cost = 0

for i in range(len(costs)):
    cost = 0
    j = len(costs)-i-1
    for j in range(j, -1, -1):
        cost += costs[j]
    
    sum_cost += cost

print(sum_cost)