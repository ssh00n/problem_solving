import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
budget = int(input())
result = 0

if sum(requests) <= budget:
    result = max(requests)
    print(result)
    exit(0)

start = 1
end = max(requests)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for request in requests:
        if request > mid:
            total += mid
        else:
            total += request
    
    if total > budget:
        end = mid - 1
    else:
        result = max(mid, result)
        start = mid + 1


print(result)

