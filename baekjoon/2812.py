import sys
input = sys.stdin.readline

n, k = map(int, input().split())

number = list(map(int, input().rstrip()))

stack = []

# 1231234

# logic
# 1. 스택에 넣는다
# 2. stack[top] < number 이면, 스택의 숫자를 전체 숫자에서 빼준다
# 3. stack[top] >= number 이면, 스택에 숫자를 그대로 둔다

for i in range(len(number)):
    while stack and stack[-1] < number[i] and k > 0:
        stack.pop()
        k-= 1

    stack.append(number[i])


# print(''.join(map(str,stack[:-k])))
if k == 0:
    print(''.join(map(str,stack[:])))
else:
    print(''.join(map(str,stack[:-k])))
# k를 다 못쓰고 for 순회가 끝난 경우 -> 뒤에 k개를 제외해줌