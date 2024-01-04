import sys

input = sys.stdin.readline

# approach
# 가로등을 놓는다. 길이 1부터 n 사이
# 이분 탐색


# 시작, 끝지점 체크
# lighted area 구간 사이에 간격이 발생하면 False


n = int(input())  # 굴다리의 길이
m = int(input())  # 가로등의 개수
location_lights = list(map(int, input().split()))  # 가로등의 위치

left = 0
right = n
height = max(n - location_lights[0], location_lights[0])

if m == 1:
    print(height)
    exit(0)

while left < right:
    mid = (left + right) // 2
    flag = True
    for i in range(m - 1):
        lighted_start = location_lights[i] - mid
        lighted_end = location_lights[i] + mid
        if i == 0 and lighted_start > 0:
            flag = False
            break
        if i == m - 2 and (location_lights[i + 1] + mid) < n:
            flag = False
            break

        next_lighted_start = location_lights[i + 1] - mid
        if lighted_end < next_lighted_start:
            flag = False
            break

    if flag:
        height = mid
        right = mid
    else:
        left = mid + 1

print(height)
