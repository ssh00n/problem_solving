# 2798. 블랙잭

# 카드의 합 <= 21
# 카드의 합을 최대한 크게 만들기
# 각 카드에는 양의 정수
# N장의 카드 중 3장의 카드를 골라 M을 넘지 않으면서 최대한 가깝게 만들기

# 입력
# 1. 카드의 개수  3 <= N <= 100, 10 <= M <= 300,000
# 2. 카드에 쓰여 있는 수  <= 100,000

# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력

# 접근 방법
# 주어진 숫자들에서 카드 3개의 조합을 모두 만들고
# 조합의 합이 M에 가장 가까운 조합 선택
# 합 출력

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, sys.stdin.readline().split()))
candidates = combinations(nums, 3)

sum_candidates = sorted([sum(i) for i in candidates])

min_diff = 300001
for candidate in sum_candidates:
    diff = M - candidate
    if diff < min_diff and diff >= 0:
        min_diff = diff
        # print(min_diff)
        result = candidate
            
print(result)

