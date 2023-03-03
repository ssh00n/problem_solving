import sys

x, y, w, h = map(int, sys.stdin.readline().split())

if x < abs(w-x):
    min_row = x
else:
    min_row = abs(w-x)

if y < abs(h-y):
    min_col = y
else:
    min_col = abs(h-y)
    
if min_row < min_col:
    result = min_row
else:
    result = min_col

print(result)