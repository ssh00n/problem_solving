import sys

input = sys.stdin.readline

corrupted_num = input().strip()

n = 0
while len(corrupted_num):
    n += 1
    num = str(n)
    while len(num) and len(corrupted_num):
        if num[0] == corrupted_num[0]:
            corrupted_num = corrupted_num[1:]
        num = num[1:]
print(n)
