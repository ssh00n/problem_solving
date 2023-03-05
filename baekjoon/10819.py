# 10819. 차이를 최대로

# N개의 정수로 이루어진 배열 A가 주어짐
# 배열에 들어있는 정수의 순서를 적절히 바꿔 다음 식의 최댓값을 구하기

import sys
from itertools import permutations

N = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().split()))

perms = permutations(nums)

candidates = []

for perm in perms:
    sum = 0
    for i in range(len(perm)-1):
        sum += abs(perm[i] - perm[i+1])
    candidates.append(sum)

print(max(candidates))            

# sum = 0

# array = []
# for i in range(len(nums)//2):
#     array.append(nums[i])
#     array.append(nums[N-i-1])

# for i in range(len(array)-1):
#     sum += abs(array[i] - array[i+1])

# print(array)
# print(sum)
# 0 5 1 4 2 3
# i n-1 n-1-i
