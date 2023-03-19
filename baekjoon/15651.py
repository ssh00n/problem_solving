import sys

n, m = map(int, sys.stdin.readline().split())

stack = []

def dfs():
    if len(stack)==m:
        print(' '.join(map(str,stack)))
        
    else:
        for i in range(1, n+1):
            if not stack:
                stack.append(i)
                dfs()
                stack.pop()
            else:
                if i >= stack[-1]:
                    stack.append(i)
                    dfs()
                    stack.pop()

dfs()