import sys

input = sys.stdin.readline

N, new_score, P = map(int, input().split())

if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))

    for i in range(N):
        if new_score >= scores[i]:
            rank = i + 1
            break
        else:
            rank = i + 2

    if rank <= P and (N < P or scores[-1] < new_score):
        print(rank)
    else:
        print(-1)
