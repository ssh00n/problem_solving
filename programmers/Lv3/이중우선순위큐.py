# Approach
# python heapq 라이브러리를 이용(min_heap)
# min값과 max값을 번갈아가면서 pop해야 하므로 max heap도 필요하다
# 힙 두개를 관리하고, 한쪽 힙에서 pop이 발생하면 그 요소를 반대 힙에서 찾아서 remove

import heapq
def solution(operations):
    
    min_heap = []
    max_heap = []
    
    answer = []
    for operation in operations:
        instruction, num = operation.split()[0], int(operation.split()[1])
        if instruction == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, [-num, num])
        else:
            if min_heap:
                if num == 1:
                    evicted = heapq.heappop(max_heap)[1]
                    min_heap.remove(evicted)
                else:
                    evicted = heapq.heappop(min_heap)
                    max_heap.remove([-evicted, evicted])
                
    if min_heap:
        answer.append(heapq.heappop(max_heap)[1])
        answer.append(heapq.heappop(min_heap))
    else:
        answer = [0, 0]
    
    return answer