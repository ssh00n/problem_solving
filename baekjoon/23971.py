import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

row_participants = 1
col_participants = 1

rows_with_participants = (h + n) // (n + 1)
cols_with_participants = (w + m) // (m + 1)

result = rows_with_participants * cols_with_participants
print(result)