import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

# 각 사람의 덩치 순위 계산
ranks = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

# 결과 출력
print(' '.join(map(str, ranks)))
