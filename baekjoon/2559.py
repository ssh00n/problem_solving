import sys

n, k = map(int, sys.stdin.readline().split())

temps = list(map(int, sys.stdin.readline().split()))

cumulative_sum = [0]
temp = 0
for i in range(len(temps)):
    temp += temps[i]
    cumulative_sum.append(temp)

n_sum = []
if n == k:
    print(sum(temps))
else:
    for i in range(n-k+1):
        n_sum.append(cumulative_sum[i+k] - cumulative_sum[i])

    print(max(n_sum))
    

# max_sum = 0
# for i in range(len(temps)-k):
#     temp_sum = 0
#     for j in range(i, i+k):
#         temp_sum += temps[j]
    
#     if max_sum < temp_sum:
#         max_sum = temp_sum

# print(max_sum)