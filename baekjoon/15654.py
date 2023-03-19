import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
# [9, 8, 7, 1]
# [1, 7, 8, 9]

stack = []
def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
        
    for num in numbers:
        if num not in stack:
            stack.append(num)
            dfs()
            stack.pop()

dfs()
