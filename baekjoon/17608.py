import sys

N = int(sys.stdin.readline())
sticks = []

for _ in range(N):
    sticks.append(int(sys.stdin.readline()))



max_height = 0
count = 0
for i in range(len(sticks)-1, -1, -1):
    if sticks[i] > max_height:
        count += 1
        max_height = sticks[i] 

print(count)