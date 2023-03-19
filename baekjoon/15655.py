import sys
input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
stack = []

# 9 8 7 1 
# 1 7 8 9

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    for num in numbers:
        if not stack:
            stack.append(num)
            dfs()
            stack.pop()
            
        elif num not in stack and stack[-1] < num:
            stack.append(num)
            dfs()
            stack.pop()

dfs()