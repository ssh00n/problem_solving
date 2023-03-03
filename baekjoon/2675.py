import sys

T = int(sys.stdin.readline())


for _ in range(T):
    R, S = sys.stdin.readline().rstrip().split()
    for s in S:
        print(s*int(R), end='')
    print()