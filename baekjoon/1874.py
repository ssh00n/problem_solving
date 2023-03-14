import sys

n = int(sys.stdin.readline())

targets = []
flag = 0

for _ in range(n):
    targets.append(int(sys.stdin.readline()))
    
stack = []
answer = []
current = 1


for target in targets:
    while current <= target:
        stack.append(current)
        answer.append("+")
        current += 1
        
    if stack[-1] == target:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
    
if flag == 0:
    for i in answer:
        print(i)