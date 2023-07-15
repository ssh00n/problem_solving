import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

N = int(input())
perms = permutations(range(1, N+1))
for perm in perms:
    print(' '.join(map(str, perm)))
    
    
# print(perms)
# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

# 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 
# 첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다. 

