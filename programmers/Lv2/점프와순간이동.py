def solution(n):
    ans = 0
    
    # k칸 앞으로 -> k만큼 건전지 소모 (TODO : minimize)
    # 현재까지 온 거리 x 2만큼 순간 이동
    
    # logic
    # 순간이동을 할 수 없으면 1씩 빼주면서 backtracking

    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            ans += 1
            n -= 1
        
    return ans