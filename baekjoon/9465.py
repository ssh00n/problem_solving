import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    
    s1 = list(map(int, sys.stdin.readline().split())) # 첫 번째 줄
    s2 = list(map(int, sys.stdin.readline().split())) # 두 번째 줄

    for i in range(1, n):
        
        # idx 1 -> 이전 대각선의 스티커 값
        if i == 1:
            s1[1] += s2[0]
            s2[1] += s1[0]

        
        # max(두 칸 앞 스티커, 이전 스티커 값) + 현재 스티커의 값
        else:
            s1[i] = max(s2[i - 1], s2[i - 2]) + s1[i]
            s2[i] = max(s1[i - 1], s1[i - 2]) + s2[i]

    print(max(s1[n-1], s2[n-1]))