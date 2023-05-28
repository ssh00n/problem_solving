# Approach
# 예시를 분석하여 일반화 해보기
# ex) s = 27, n = 5
# 5 + 5 + 5 + 6 + 6이 최적해를 갖는다(모든 수가 같을 때 exponentially increase)
# 즉, s//n *(n - (s%n)) -> 5 * (5 -2)
# (s//n + 1) * (n - (n-s%n )) -> 5 * (5-(5-2))

# s = 짝수, n = 짝수 / n = 홀수
# s = 홀수, n = 짝수 / n = 홀수
# 모든 경우에 대해 일반화 가능한 optimal solution이 된다.

def solution(n, s):
    answer = []
    if s // n < 1:
        answer.append(-1)
    else:
        for _ in range(n-(s%n)):
            answer.append(s//n)
    
        for _ in range(n-(n-s%n)):
            answer.append(s//n+1)
        
    # result = (s//n)*(n-(s%n)) + (s//n+1)*(n-(n-s%n))
     
    return answer