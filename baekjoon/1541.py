import sys
input = sys.stdin.readline

wo_bracket = list(input().rstrip().split('-'))

nums = []
s = 0
for i in wo_bracket[0].split('+'):
    s += int(i)
for i in wo_bracket[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)

