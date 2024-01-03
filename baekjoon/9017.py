import sys
from collections import Counter

input = sys.stdin.readline

# approach
# leaderboard에 tie가 있을 때 5번째 선수의 score를 비교한다
# 4명이 먼저 들어오는 것이 최소를 보장하지 않는다

T = int(input())
for _ in range(T):
    N = int(input())  # 6 <= N <= 1000
    teams = list(map(int, input().split()))
    counter = Counter(teams)
    leaderboard = dict()
    bucket = dict()
    score = 1
    for team in teams:
        if counter[team] >= 6:
            if team not in bucket:
                bucket[team] = [team]
                leaderboard[team] = score
            else:
                if len(bucket[team]) < 4:
                    leaderboard[team] += score
                bucket[team].append(score)
            score += 1

    score_win = min(leaderboard.values())
    winner = -1
    fifth_score_min = N + 1
    for key, value in leaderboard.items():
        if value == score_win and winner == -1:
            winner = key
        if value == score_win and winner != -1:
            if bucket[key][4] < fifth_score_min:  # tie
                fifth_score_min = bucket[key][4]
                winner = key

    print(winner)
