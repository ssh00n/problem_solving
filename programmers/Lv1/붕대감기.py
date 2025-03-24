def solution(bandage, health, attacks):
    t, x, y = bandage[0], bandage[1], bandage[2]
    
    curr_health = health
    attack_times = {time: damage for time, damage in attacks}
    
    curr_time = 1
    consecutive_success = 0
    
    max_time = attacks[-1][0]
    while curr_time <= max_time:
        # 몬스터 공격
        if curr_time in attack_times:
            curr_health -= attack_times[curr_time]
            consecutive_success = 0
        
        # 체력 회복
        else: 
            curr_health = min(curr_health + x, health)
            consecutive_success += 1
            if consecutive_success == t:
                curr_health = min(curr_health + y, health)
                consecutive_success = 0
        
        if curr_health <= 0:
            return -1
        
        curr_time += 1
        
    return curr_health
