import sys

N = int(sys.stdin.readline())

d = {}

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x in d.keys():
        d[x].append(y)
    else:
        d[x] = [y]

sorted_x = sorted(d.keys())

for key in sorted_x:
    if len(d[key]) == 1:
        print(key, *d[key])
    else:
        d[key].sort()
        for i in range(len(d[key])):
            print(key, d[key][i])