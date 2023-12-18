import sys
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    user_input = input().split()
    if user_input[0] == 'add':
        x = int(user_input[1])
        S.add(x)

    elif user_input[0] == 'remove':
        x = int(user_input[1])
        S.discard(x)

    elif user_input[0] == 'check':
        x = int(user_input[1])
        print(int(x in S))

    elif user_input[0] == 'toggle':
        x = int(user_input[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)

    elif user_input[0] == 'all':
        S = set(range(1, 21))

    elif user_input[0] == 'empty':
        S = set()