import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * n



stack = []

def dfs():    
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    remember = 0
    for i in range(n):
        if not visited[i] and remember != numbers[i]:
            visited[i] = True
            stack.append(numbers[i])
            remember = numbers[i]
            dfs()
            visited[i] = False
            stack.pop()   
    
dfs()     
