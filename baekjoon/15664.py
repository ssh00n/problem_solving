import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False] * n

stack = []


def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    remember = 0
    for i in range(n):
        if not stack and remember != nums[i]:
            stack.append(nums[i])
            visited[i] = True
            remember = nums[i]
            dfs()
            stack.pop()
            visited[i] = False
            
        elif visited[i] == False and remember != nums[i] and stack[-1] <= nums[i]:
            stack.append(nums[i])
            visited[i] = True
            remember = nums[i]
            dfs()
            stack.pop()
            visited[i] = False

dfs()
