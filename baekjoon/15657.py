import sys

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
        if not stack:
            stack.append(num)
            dfs()
            stack.pop()
        
        else:
            if stack[-1] <= num:
                stack.append(num)
                dfs()
                stack.pop()
                

dfs()