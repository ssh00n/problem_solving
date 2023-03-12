# 2110. 공유기 설치
# N개의 수직선 좌표에서
# C개를 좌표를 선택하여
# 가장 인접한 두 좌표 사이의 거리가 최대가 되도록 함

import sys

n, c = map(int, sys.stdin.readline().split())
houses = []

for _ in range(n):
    houses.append(int(sys.stdin.readline()))

houses.sort()

start = 1
end = houses[-1] - houses[0]
result = 0


while start <= end:
    mid = (start + end) // 2
    prev = houses[0]
    count = 1
    
    for i in range(1, len(houses)):
        if houses[i] >= prev + mid:
            prev = houses[i]
            count +=1
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)