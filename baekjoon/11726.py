import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# n = width, 2 = height
# [2x1, 1x2]
#
# n = 1 -> 1x2 = 1
# n = 2 -> 1x2*2, 2x1*2 = 2
# n = 3 -> 1x2*3, 1x2+2x1*2, 2x1*2+1x2, = 3

n = int(input())

# tabulation
dp_table = {1 : 1,
            2 : 2}

def rec_tile(n):
    
    for i in range(3, n+1):
        if i >= 10007:
            dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 10007
        else:
            dp_table[i] = dp_table[i-1] + dp_table[i-2]
        
    return dp_table[n]
            
print(rec_tile(n))