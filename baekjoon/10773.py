import sys

K = int(sys.stdin.readline())

stack = []

for _ in range(K):
    user_input = int(sys.stdin.readline())
    if user_input != 0:
        stack.append(user_input)
    else:
        stack.pop()

print(sum(stack))