import sys
input = sys.stdin.readline


d = [[0]*15 for _ in range(15)]

def residents(k, n):
    if k == 0:
        return n
    if n == 1:
        return 1
    if d[k][n] == 0:
        d[k][n] = residents(k, n-1) + residents(k-1, n)
    
    return d[k][n]
    

    
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(residents(k, n))
