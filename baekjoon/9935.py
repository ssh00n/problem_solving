import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline

stack = []


sequence = input().rstrip()  # 1 <= 문자열의 길이 <= 1,000,000 
bomb = list(map(str, input().rstrip()))  # 1 <= 폭발 문자열의 길이  <= 36

for s in sequence:
    stack.append(s)
    if stack[-(len(bomb)):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(map(str, stack)))
else:
    print('FRULA')