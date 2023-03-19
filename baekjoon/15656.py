import sys
# from itertools import product as p

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

stack = []

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    for num in numbers:
        stack.append(num)
        dfs()
        stack.pop()

dfs()

# print(ans)
# print('\n'.join(ans))