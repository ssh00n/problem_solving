# 2309. 일곱 난쟁이

# 일곱 난쟁이의 키의 합이 100
# 아홉 난쟁이의 키가 주어지고, 일곱 난쟁이의 키만 출력 

# 입력 9개의 숫자 중 7개로 합 100을 만족하는 수 찾기

# combination으로 모든 7개의 조합을 만들고 합이 100인 경우만 출력
# 오름차순으로 출력..

import sys
from itertools import combinations

heights = []

for _ in range(9):
    heights.append(int(sys.stdin.readline().rstrip()))

candidates = combinations(heights, 7)

for candidate in candidates:
    if sum(candidate) == 100:
        print(*sorted(candidate), sep='\n')
        break
    # print(sum(candidate))