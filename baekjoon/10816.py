import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
integers = list(map(int, sys.stdin.readline().split()))


d = {}
for num in num_list:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

results = []
for integer in integers:
    if integer in d:
        results.append(d[integer])
    else:
        results.append(0)

print(*results)