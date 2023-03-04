import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    
    N = int(sys.stdin.readline())
    arr = [True for i in range(N + 1)]
    
    # 주어진 수에 대한 소수 리스트 만들기
    for i in range(2, int(math.sqrt(N)) + 1):
        if arr[i] == True: # i가 소수인 경우
            # i를 제외한 i의 모든 배수 지우기
            j = 2
            
            while i*j <= N:
                arr[i * j] = False
                j += 1
                
    prime_list = [i for i in range(2, N+1) if arr[i]]

    partitions = []
    for i in range(len(prime_list)):
        for j in range(len(prime_list)):
            if N == prime_list[i] + prime_list[j]:
                partitions.append([prime_list[i], prime_list[j]])
    
    # 가장 차가 작은 소수 조합 찾기
    min_diff = 9999
    for partition in partitions:
        diff = partition[0] - partition[1]
        if diff < 0:
            continue
        else:
            if diff < min_diff:
                min_diff = diff
                min_partition = sorted(partition)
                
    print(*min_partition)            
    