import sys
from itertools import permutations

def solution():
    
    N = int(sys.stdin.readline())
    sequence = list(map(int, sys.stdin.readline().split()))
    operators = ['+', '-', '*', '/']
    counts = list(map(int, sys.stdin.readline().split()))
    op_list = [c for a, b in zip(operators, counts) for c in a * b]
    op_perms = permutations(op_list)

    res_list = []

    def divide(x, y):
        if x < 0 and y > 0:
            return -(-x // y)
        elif x > 0 and y < 0:
            return -(x // -y)
        else:
            return x // y

    for op_perm in op_perms:
        # print(op_perm)
        res = sequence[0]
        for i in range(len(op_perm)):
            if op_perm[i] == '+':
                res += sequence[i+1]
            elif op_perm[i] == '-':
                res -= sequence[i+1]
            elif op_perm[i] == '*':
                res *= sequence[i+1]
            else:
                res = divide(res, sequence[i+1])
            
            # print(res)
        res_list.append(res)

    print(max(res_list))
    print(min(res_list))

solution()