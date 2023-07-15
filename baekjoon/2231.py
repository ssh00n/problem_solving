import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

N = int(input())
constructor = 0
# Logic
# target = N으로부터 i만큼 뺀 수
# sum_digit = target의 각 자릿수를 더한 값
# 1 ~ 1,000,000의 숫자에 대해 각 자릿수를 어떻게 더할 것인가?
# 간단하다, 숫자를 문자열로 반환한 뒤 길이를 받아서, 각 자릿수를 더하면 됨!

# target + suffix = N을 만족하는지 검사
# 만족하면 -> constructor

for i in range(1, N):
    sum_digit = 0
    target = N - i
    for s in str(target):
        sum_digit += int(s)
    
    if target + sum_digit == N:
        constructor = target

print(constructor)

# for i in range(1, N+1):
#     A = list(map(int, str(i)))
#     result = i + sum(A)
#     if result == N:
#         print(i)
#         break
#     if i == N:
#         print(0)

