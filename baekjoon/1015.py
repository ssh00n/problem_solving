import sys
from itertools import permutations
# P = (0, N-1)까지의 permutation

# A가 주어졌을때 P를 B[P[i]] = A[i] 와 같이 적용하여
# 만든 B가 오름차순이 되도록하는 수열 P 찾기

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

perms = permutations([i for i in range(0, N)])


# for perm in perms:
    