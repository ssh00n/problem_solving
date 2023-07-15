import sys
sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')

input = sys.stdin.readline

sequence = input().rstrip()
cursor_idx = len(sequence)

n_commands = int(input())
commands = [input().split() for _ in range(n_commands)]


for command in commands:
    # print(f"before command : {sequence}, cursor: {cursor_idx}")
    if len(command) == 2:
        # print(f"command[0] : {command[0]}", end=' ')
        # print(f"command[1] : {command[1]}")
        temp = sequence
        sequence = temp[:cursor_idx] + command[1] + temp[cursor_idx:]
        cursor_idx += len(command[1])
    else:
        # print(f"command[0] : {command[0]}")
        if command[0] == 'L' and cursor_idx != 0:
            cursor_idx -= 1
        if command[0] == 'D' and cursor_idx != len(sequence):
            cursor_idx += 1
        if command[0] == 'B' and cursor_idx != 0:
            sequence = sequence[:cursor_idx-1] + sequence[cursor_idx:]
            cursor_idx -= 1
    
    # print(f"cursor_idx: {cursor_idx}, command: {command[0]}, after command: {sequence}")


print(sequence)