import sys
N = int(sys.stdin.readline())

# nums = [int(sys.stdin.readline()) for _ in range(N)]

array = [0] * 10001

for i in range(N):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for _ in range(array[i]):
            sys.stdout.write(str(i)+'\n')