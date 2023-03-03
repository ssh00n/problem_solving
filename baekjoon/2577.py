import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = str(A*B*C)

for i in range(10):
    print(result.count(f"{i}"))