import sys

n, m = map(int, sys.stdin.readline().split())

# 1 ~ n까지 자연수 중 중복없이 m개를 고른 수열
stack = []
def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(1, n+1):
            if i not in stack:
                stack.append(i)
                dfs()
                stack.pop()
dfs()