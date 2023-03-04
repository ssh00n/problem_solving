import sys

N = int(sys.stdin.readline())

# 1065. 한수 찾기
# 한수 : 어떤 양의 정수 X의 각 자리가 등차수열을 이루는 수

if N <= 99:
    ans = N
    
else:
    ans = 99
    for i in range(100, N+1):
        if int(str(i)[1])-int(str(i)[0]) == int(str(i)[2])-int(str(i)[1]):
            ans += 1

print(ans)