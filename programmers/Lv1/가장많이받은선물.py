def solution(friends, gifts):
    n = len(friends)
    friend_to_idx = {friend: i for i, friend in enumerate(friends)}
    gift_matrix = [[0] * n for _ in range(n)]

    # 선물 기록 처리
    for gift in gifts:
        giver, receiver = gift.split()
        i = friend_to_idx[giver]
        j = friend_to_idx[receiver]
        gift_matrix[i][j] += 1

    gift_indices = [0] * n
    # 선물 지수 계산: 내가 준 선물 합 - 내가 받은 선물 합
    for friend, i in friend_to_idx.items():
        row_sum = sum(gift_matrix[i])
        col_sum = sum(row[i] for row in gift_matrix)
        gift_indices[i] = row_sum - col_sum

    # 다음 달 받을 선물 수 계산
    next_gifts = [0] * n
    for i in range(n):
        for j in range(i + 1, n):  # 한 쌍씩 비교 (i < j)
            # 두 사람 간 선물 기록이 다르면
            if gift_matrix[i][j] != gift_matrix[j][i]:
                if gift_matrix[i][j] > gift_matrix[j][i]:
                    next_gifts[i] += 1
                else:
                    next_gifts[j] += 1
            else:
                # 선물 기록이 같으면 선물 지수를 비교
                if gift_indices[i] > gift_indices[j]:
                    next_gifts[i] += 1
                elif gift_indices[i] < gift_indices[j]:
                    next_gifts[j] += 1
    answer = max(next_gifts)
    return answer