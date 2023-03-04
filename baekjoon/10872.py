import sys

N = int(sys.stdin.readline())

def factorial(N):
    if N > 0:
        return N * factorial(N - 1)
    else:
        return 1

print(factorial(N))


