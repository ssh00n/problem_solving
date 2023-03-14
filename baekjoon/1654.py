# 1654. 랜선 자르기

import sys

k, n = map(int, sys.stdin.readline().split())
cables = []

for _ in range(k):
    cables.append(int(sys.stdin.readline()))

cables.sort()
left= 1
right = cables[-1]

count = 0
res = []

while left <= right:
    mid = (left + right) // 2
    count = 0
    for cable in cables:
        count += (cable // mid)
    
    if count >= n:
        res.append(mid)
        left = mid + 1
    elif count < n:
        right = mid - 1

print(max(res))