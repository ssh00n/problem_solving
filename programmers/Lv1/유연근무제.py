def convert_to_minutes(time):
    """ time: ex) 958 -> 9시 58분 -> (9 * 60) + 58 = 540 + 58 = 598 """
    hour = time // 100
    minute = time % 100
    return hour * 60 + minute

def solution(schedules, timelogs, startday):
    n = len(schedules)
    qualified_members = [True] * n

    for i in range(n):
        # 출근 희망 시각 + 10분
        goal_minutes = convert_to_minutes(schedules[i]) + 10

        # 7일 동안 로그 확인
        for j in range(7):
            # 실제 요일 계산
            currentDay = (startday + j - 1) % 7 + 1
            if currentDay in [6, 7]:  # 토(6), 일(7) 건너뛰기
                continue
            
            # 실제 출근 시각(분 단위)
            arrival_minutes = convert_to_minutes(timelogs[i][j])

            # 지각 판정
            if arrival_minutes > goal_minutes:
                qualified_members[i] = False
                break 

    return sum(qualified_members)