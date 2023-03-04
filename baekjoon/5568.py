# 5568, 카드 놓기

import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card_list = []
candidates = []
res = []
for _ in range(n):
    card_list.append(sys.stdin.readline().rstrip())

perms = list(permutations(card_list, k))
candidates = []

for perm in perms:
    num = ''
    for i in range(k):
        num += perm[i]
    candidates.append(num)


candidates = set(candidates)
print(len(candidates))

