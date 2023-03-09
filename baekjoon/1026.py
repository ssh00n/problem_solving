import sys

# 1026. 보물
# N 크기의 배열 A, B(고정)
# A를 재배열 하여 S = A[0]*B[0] + ... + A[N-1]*B[N-1]
# S의 최솟값 출력

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


A.sort()
B.sort(reverse=True)


sum_seq = 0
for i in range(len(A)):
    sum_seq += B[i]*A[i]

print(sum_seq)
