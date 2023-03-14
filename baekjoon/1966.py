import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, target_idx = map(int, input().split())
    documents = list(map(int, input().split()))
    target = documents[target_idx]    
    q = deque([])

    count = 0 
    for i in range(len(documents)):
        q.append([i, documents[i]])
        
    if n == 1:
        print(1)
    else:
        while q:
            if q[0][1] < max(q, key=lambda x:x[1])[1]:
                temp = q.popleft()
                q.append(temp)
            else:
                out = q.popleft()
                count += 1 
                if out[0] == target_idx:
                    break
        print(count)
                
                
