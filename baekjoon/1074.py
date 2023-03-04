# 1074. Z (devide-conquer, recursive)
import sys

N, r, c = map(int, sys.stdin.readline())

# n번쨰 사각형 위치 확인,
# 사각형의 개수는 정해져 있음
# 2*N X 2*N

# N = 2 -> 4
# N = 3 -> 16
# N = 4 -> 64

# 사각형 개수 :  2**(2*N-2)
max_num = 2**N * 2**N
num_squares = 2**(2*N-2)

def visit():
    if n == 0:
        return 0
    
    visit(n+1)