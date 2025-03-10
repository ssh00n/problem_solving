def solution(n, left, right):
    answer = []
    left_row = left // n
    left_col = left % n
    right_row = right // n
    right_col = right % n
    for i in range(left_row, right_row+1):
        for j in range(n):
            if i == left_row:
                if j >= left_col:
                    answer.append((max(i, j)+1)
                                  else:
                                  continue
                                  else:
                                  answer.append((max(i, j)+1)
                                                if i == right_row and j == right_col:
                    break
    
    return answer