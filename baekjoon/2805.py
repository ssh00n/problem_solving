import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

left = 0
right = max(trees)
ans = 0
while left <= right:
    h = (left + right) // 2
    total = 0
    for tree in trees:
        if tree > h:
            total += tree - h
    if total == m:
        ans = h
        break
    elif total < m:
        right = h - 1
    else:
        ans = h
        left = h + 1
print(ans)
        
            
# 10 15 17 20
# h = 15 
# 4 26 40 42 46
# h = 36
