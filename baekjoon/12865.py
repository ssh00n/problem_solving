import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# n = 물건 개수, k = knapsack capacity

things = [[0, 0]]
dp = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    things.append(list(map(int, input().split())))

for i in range(1, n+1):                  # i : 물건 개수, j = capacity
    for j in range(1, k+1):
        w = things[i][0]
        v = things[i][1]
        
        if w > j:                        # 현재 물건이 capacity보다 무거운 경우 -> 안 넣음
            dp[i][j] = dp[i-1][j]
        else:                             
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
                            
                            # 현재 물건이 capacity보다 가벼운 경우 -> capacity에서 물건 만큼의 무게를 빼고 현재 물건을 넣었을 경우와
                            # 넣지 않을 경우를 비교하여 큰 값을 취함
                    

print(dp[-1][-1])


# dictionay를 사용하는 경우

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cache = {0: 0}

for _ in range(N):
    curr_w, curr_v = map(int, input().split())
    temp = {}
    for w, v in cache.items():
        if curr_w + w <= K and curr_v + v > cache.get(curr_w + w, 0):
            temp[curr_w + w] = curr_v + v
    cache.update(temp)
print(max(cache.values()))