import sys

W, H = map(int, sys.stdin.readline().split())

N = int(sys.stdin.readline())

row_lines = [0, H]
col_lines = [0, W]

for _ in range(N):
    axis, num_line =map(int, sys.stdin.readline().split())
    
    if axis == 0:
        row_lines.append(num_line)
    else:
        col_lines.append(num_line)

row_lines.sort()
col_lines.sort()

max_row = 0
max_col = 0


for i in range(len(row_lines)-1):
    diff_row = row_lines[i+1] - row_lines[i]
    if diff_row > max_row:
        max_row = diff_row

for j in range(len(col_lines)-1):
    diff_col = col_lines[j+1] - col_lines[j]
    if diff_col > max_col:
        max_col = diff_col

print(max_row*max_col)