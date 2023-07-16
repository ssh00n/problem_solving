import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

start = max(lectures)
end = sum(lectures)

# 접근 : 이진 탐색(binary search)
# start <= end인 동안 다음 과정을 반복한다
# mid 값을 구함
# mid값에 대해, 해당 값으로 M개의 블루레이를 나눌 수 있는지 검사한다
# 블루레이가 M개보다 작다면 -> end값을 줄인다(end = mid - 1)
# 블루레이가 M개보다 크다면 -> start값을 늘린다(start = mid + 1)

result = 0

while start <= end:
    mid = (start + end) // 2  # 중간점
    total = 0  # 블루레이에 담긴 강의의 길이 합계
    count = 1  # 필요한 블루레이의 개수

    # 현재의 mid 값이 블루레이 길이일 때, 블루레이를 총 몇 개 필요한지 계산
    for lecture in lectures:
        # 블루레이 길이를 초과할 경우
        if total + lecture > mid:
            count += 1  # 블루레이 개수 증가
            total = lecture  # 합계 초기화
        else:
            total += lecture
        
    if count > M:
        start = mid + 1
    
    else:
        end = mid - 1
        result = mid 
    


print(result)
    