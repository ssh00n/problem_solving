import sys

# 남학생 : 스위치 번호가 자기가 받은 수의 배수 -> 상태를 바꿈(NOT 연산)
# 여학생 : 자기가 받은 수와 같은 번호의 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꿈


input = sys.stdin.readline

n = int(input())
switches = list(map(int, input().split()))
n_students = int(input())
students = [list(map(int, input().split())) for _ in range(n_students)]


def male(num):
    # [0 1 2 3 4 5 6 7] num 3 -> 2 5
    # [0 1 2 3 4 5 6 7] num 4 -> 3 7
    # [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14] num 3 -> 2 5 8 11 14

    for i in range(len(switches)):
        if (i + 1) % num == 0:
            switches[i] = int(not switches[i])


def female(num):
    target_idx = num - 1
    switches[target_idx] = int(not switches[target_idx])

    max_distance = min(target_idx, (n - 1 - target_idx))

    for i in range(1, max_distance + 1):
        if switches[target_idx - i] != switches[target_idx + i]:
            break

        switches[target_idx - i] = int(not switches[target_idx - i])
        switches[target_idx + i] = int(not switches[target_idx + i])


for student in students:
    if student[0] == 1:
        male(student[1])
    elif student[0] == 2:
        female(student[1])
for i in switches:
    print(i)


# if len(switches) <= 20:
#     print(" ".join(map(str, switches)))

# else:
#     for i in range((len(switches) // 20)):
#         print(" ".join(map(str, switches[i * 20 : (i + 1) * 20])))
