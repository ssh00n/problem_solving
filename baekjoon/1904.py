import sys
input = sys.stdin.readline

n = int(input())

memo = [0]*(n+1)

if n == 1:
    memo[1] = 1
else:
    memo[1] = 1
    memo[2] = 2

for i in range(3, n+1):
    if i >= 15746:
        memo[i] = (memo[i-1] + memo[i-2]) % 15746
    else:
        memo[i] = memo[i-1] + memo[i-2]
    
print(memo[n])

# dp_table -> bottom-up : Out of memory
# dp_table = {1 : 1,
#             2 : 2}

# def zero_one_tile(n):
#     for i in range(3, n+1):
#         if i not in dp_table:
#             dp_table[i] = zero_one_tile(i-1) % 15746 + zero_one_tile(i-2) % 15746
        
#     return dp_table[n] % 15746

# print(zero_one_tile(n))

# top-down : Out of memory