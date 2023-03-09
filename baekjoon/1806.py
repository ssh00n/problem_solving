import sys

n, s = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))



right = 0
temp_sum = 0
result = 123456789
for left in range(n):
    while temp_sum < s and right < n:
        temp_sum += sequence[right]
        right += 1
    
    if temp_sum >= s:
        result = min(result, right - left)
    
    temp_sum -= sequence[left]

if result == 123456789:
    print(0)
else:
    print(result)

# def min_sequence(sequence):
#     for window in range(1, len(sequence)+1):
#         for i in range(len(sequence)):
#             if sum(sequence[i:i+window]) == s:
#                 return window
#     else:
#         return 0
# ans = min_sequence(sequence)
