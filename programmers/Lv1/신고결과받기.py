def solution(id_list, report, k):
    user_indices = {name: idx for idx, name in enumerate(id_list)}
    reported_dict = { name: set() for name in id_list }

    for rep in report:
        reporter, reported = rep.split()
        reported_dict[reported].add(reporter)
            
    answer = [0] * len(id_list)
                
    for reported, reporters in reported_dict.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[user_indices[reporter]] += 1
                
    return answer