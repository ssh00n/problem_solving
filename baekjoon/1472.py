import sys

n = list(sys.stdin.readline().rstrip())

print(*sorted(n, reverse=True), sep='')