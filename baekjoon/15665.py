import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))


stack = []

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
        
    for num in nums:
        if not stack:
            stack.append(num)
            dfs()
            stack.pop()
        elif stack[-1] <= num:
            stack.append(num)
            dfs()
            stack.pop()
        
dfs()