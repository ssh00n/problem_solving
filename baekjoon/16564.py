import sys

n, k = map(int, sys.stdin.readline().split())

characters = []
for _ in range(n):
    characters.append(int(sys.stdin.readline()))

characters.sort()

left = characters[0]
right = left + k
res = 0

if n ==1:
    res = n + k
    
else:
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for i in range(n):
            if characters[i] <= mid:
                count += (mid - characters[i])
                
        if count == k:
            res = mid
            break
        
        elif count < k:
            res = mid
            left = mid + 1
            
        else:
            right = mid - 1
            
print(res)
