import sys
input = sys.stdin.readline

n = int(input())

dp_table = {1 : 1,
               2 : 1}
def fibonacci_bottomup(n):
    
    for i in range(3, n+1):
        if i not in dp_table:
            dp_table[i] = dp_table[i-1] + dp_table[i-2]
            
    return dp_table[n]

print(fibonacci_bottomup(n))