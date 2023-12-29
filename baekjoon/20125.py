import sys

input = sys.stdin.readline

# approach
# 그래프 순회

# 그래프 순회
# 심장 찾기
# 심장으로부터 위 - 머리
# 심장으로부터 왼쪽 / 오른쪽 - 팔
# 심장으로부터 아래 - 허리
# 허리로부터 [y+1, x-1] : 왼쪽 다리
# 허리로부터 [y+1, x+1] : 오른쪽 다리


def find_heart(graph, n):
    heart = None
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "*":
                if (
                    (i + 1 < n)
                    and (j + 1 < n)
                    and (
                        graph[i - 1][j] == "*"
                        and graph[i + 1][j] == "*"
                        and graph[i][j - 1] == "*"
                        and graph[i][j + 1] == "*"
                    )
                ):
                    heart = (i, j)
                    break
    return heart


def get_arms(heart, graph):
    i, j = heart
    start_idx = None
    length = 0
    for idx, value in enumerate(graph[i]):
        if value == "*":
            if start_idx is None:
                start_idx = idx
            length += 1

    end_idx = start_idx + length - 1
    left_arm_length = j - start_idx
    right_arm_length = end_idx - j

    return left_arm_length, right_arm_length


def get_waist(heart, graph):
    i, j = heart
    start_idx = None
    length = 0
    column = [row[j] for row in graph]

    for idx, value in enumerate(column):
        if value == "*":
            if start_idx is None:
                start_idx = idx
            length += 1

    # Need validation
    end_idx = start_idx + length - 1
    waist = end_idx - i
    waist_end = (end_idx, j)
    return waist, waist_end


def get_legs(waist_end, graph):
    left_leg_length = 0
    right_leg_length = 0

    i, j = waist_end
    left_leg_start_idx = j - 1
    right_leg_start_idx = j + 1

    left_leg_column = [row[left_leg_start_idx] for row in graph[i + 1 :]]
    right_leg_column = [row[right_leg_start_idx] for row in graph[i + 1 :]]

    for element in left_leg_column:
        if element == "*":
            left_leg_length += 1

    for element in right_leg_column:
        if element == "*":
            right_leg_length += 1

    return left_leg_length, right_leg_length


n = int(input())
graph = [input().rstrip() for _ in range(n)]
heart = find_heart(graph, n)
left_arm, right_arm = get_arms(heart, graph)
waist, waist_end = get_waist(heart, graph)
left_leg, right_leg = get_legs(waist_end, graph)

print(f"{heart[0]+1} {heart[1]+1}")
print(f"{left_arm} {right_arm} {waist} {left_leg} {right_leg}")
