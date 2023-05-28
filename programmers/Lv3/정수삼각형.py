# 정수 삼각형
# 1) 양 끝일 때 : upper + current
# 2) 양 끝이 아닐 때 : max(upper left, upper right) + current

def solution(triangle):
    height = len(triangle)
    dp = [[0]*i for i in range(1, height+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, height):
        for j in range(len(triangle[i])):
            if i == j:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    answer = max(dp[-1])
    return answer