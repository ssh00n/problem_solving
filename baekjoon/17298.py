import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1]*n
for i in range(len(A)):
    while stack and stack[-1][1] < A[i]:
        result[stack[-1][0]] = A[i]
        stack.pop()
        
        
    stack.append([i, A[i]])
        

print(*result)    

