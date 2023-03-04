import sys


def move(N, no, x, y):
    if no > 1:
        move(N, no-1, x, 6-x-y)
    
    if N <= 20:    
        print(x, y)    
    
    if no > 1:
        move(N, no-1, 6-x-y, y)
        

N = int(sys.stdin.readline())
print(2**N-1)
if N <= 20:
    move(N, N, 1, 3)
    