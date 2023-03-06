from itertools import permutations
import sys


def solution():
    n = int(sys.stdin.readline())
    matrix = []

    for i in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    paths = list(permutations(range(n)))

    res = 999999999

    for path in paths:
        if matrix[path[-1]][path[0]] == 0:
            continue
        
        sum = 0
        flag = False
        
        for i in range(n-1):
            if matrix[path[i]][path[i+1]] == 0:
                flag = True
                break
            
            sum += matrix[path[i]][path[i+1]]
            
            if sum >= res:
                flag = True
                break
        if flag:
            continue
        
        sum += matrix[path[-1]][path[0]]
        res = min(res, sum)

    print(res)
solution()