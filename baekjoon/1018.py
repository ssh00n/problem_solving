import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

# [0, 0] 인덱스가 B인 경우 -> 행, 열 모두 짝수번째 인덱스가 B, 홀수번쨰 인덱스 W
# [0, 0] 인덱스가 W인 경우-> 행, 열 모두 짝수번째 인덱스가 W, 홀수번째 인덱스 B


# 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 00 ~ 07, 00 02 04 06 == W
# 10 ~ 17, 11 13 15 17 == W
# 20 ~ 27, 20 22 24 26 == W
# 30 ~ 37, 31 33 35 37 == W
# 40 ~ 47, 40 42 44 46 == W


def check_repainting(start_r, start_c):
    count_repaintng = 0
    if board[start_r][start_c] == "W":
        for i in range(start_r, start_r + 8, 2):
            if not board[i][start_c] == "W":
                count_repaintng += 1

            for j in range(start_c + 2, start_c + 8, 2):
                if not board[i][j] == "W":
                    count_repaintng += 1

            for j in range(start_c + 1, start_c + 8, 2):
                if not board[i][j] == "B":
                    count_repaintng += 1

        for k in range(start_r + 1, start_r + 8, 2):
            if not board[k][start_c] == "B":
                count_repaintng += 1

            for j in range(start_c + 2, start_c + 8, 2):
                if not board[k][j] == "B":
                    count_repaintng += 1

            for j in range(start_c + 1, start_c + 8, 2):
                if not board[k][j] == "W":
                    count_repaintng += 1

    else:  # if board[start_r][start_c] == "B":
        for i in range(start_r, start_r + 8, 2):
            if not board[i][start_c] == "B":
                count_repaintng += 1

            for j in range(start_c + 2, start_c + 8, 2):
                if not board[i][j] == "B":
                    count_repaintng += 1

            for j in range(start_c + 1, start_c + 8, 2):
                if not board[i][j] == "W":
                    count_repaintng += 1

        for k in range(start_r + 1, start_r + 8, 2):
            if not board[k][start_c] == "W":
                count_repaintng += 1

            for j in range(start_c + 2, start_c + 8, 2):
                if not board[k][j] == "W":
                    count_repaintng += 1

            for j in range(start_c + 1, start_c + 8, 2):
                if not board[k][j] == "B":
                    count_repaintng += 1

    return count_repaintng


result = sys.maxsize
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        if board[i][j] == "W":
            w_case = check_repainting(i, j)
            board[i][j] = "B"
            b_case = check_repainting(i, j) + 1
            num_repainting = min(w_case, b_case)
            board[i][j] = "W"
        else:
            b_case = check_repainting(i, j)
            board[i][j] = "W"
            w_case = check_repainting(i, j) + 1
            num_repainting = min(w_case, b_case)
            board[i][j] = "B"

        result = min(result, num_repainting)

print(result)
