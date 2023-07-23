def solution(n,a,b):

    # n, a, b가 주어졌을 때 [1, 2, ..., n]
    # a, b를 2씩 나눠주면서 추적하여 2로 나눈 나머지와 몫을 이용해 layer 추적 -> 같으면 만남
    
    round = 1
    while a > 0 and b > 0:
        if (a//2 + a%2) == (b//2 + b%2):
            return round
        a = (a // 2 + a % 2)
        b = (b // 2 + b % 2)
        round += 1
