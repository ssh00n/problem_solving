import math
import sys


# 2 ≤ n ≤ 100
# 1 ≤ w ≤ 10
# 1 ≤ num ≤ n

input = sys.stdin.readline
n, w, num = map(int, input().split())


def solution(n, w, num):
    rows = math.ceil(n / w)
    arr = [[0] * w for _ in range(rows)]

    target_row = 0
    target_col = 0

    # box number 할당
    box_number = 1
    for i in range(rows):
        for j in range(w):
            if box_number == num:
                target_row = i
                target_col = j if i % 2 == 0 else w-j-1
            if box_number <= n:
                if i % 2 == 0:
                    arr[i][j] = box_number
                else:
                    arr[i][w-j-1] = box_number
                box_number += 1
    
    for row in arr:
        print(" ".join(map(str, row)))
    print(f"n : {n}, w : {w}, num: {num}")
    print(f"target_row : {target_row}")
    print(f"target_col : {target_col}")

    result = 0

    if arr[rows-1][target_col] == 0:
        result = rows - 1 - target_row
    else:
        result = rows - target_row

    return result


# print(solution(10, 3, 8))
# print(solution(10, 3, 7))

# print(solution(22, 6, 8))
# print(solution(13, 3, 6))
print(solution(n, w, num))


# target = [1][4]
#rows - target_row = 3

# rows - target_row
# if arr[rows-target_row][target_col] == 0 -> rows - target_row - 1
# else rows - target_row
# 박스 위치 찾고, 가장 바깥부터 꺼내기