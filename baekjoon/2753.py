import sys

year = int(sys.stdin.readline().rstrip())

is_leap = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
print(int(is_leap))