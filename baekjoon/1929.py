import sys
import math

M, N = map(int, sys.stdin.readline().split())

arr = [True for i in range(N+1)]

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= N:
            arr[i * j] = False
            j += 1

for i in range(M, N+1):
    if arr[i] and i!=1:
        print(i)

