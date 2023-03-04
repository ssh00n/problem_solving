import sys
import math

N, K = map(int, sys.stdin.readline().split())

arr = [True for i in range(N+1)]
count = 0
check_remove = []

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i] == True:
        j = 1
        while i * j <= N:
            print(i * j)
            arr[i * j] = False
            count += 1
            if count == K:
                print(i*j)
                break
            j += 1
            

