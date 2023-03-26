import sys
input = sys.stdin.readline

memo = {
    0 : [1, 0],
    1 : [0, 1],
    2 : [1, 1]
}
def fibonacci2(n):
    
    for i in range(3, n+1):
        if i not in memo:
            memo[i] = [memo[i-1][0]+memo[i-2][0], memo[i-1][1]+memo[i-2][1]]
    
    return memo[n]



T = int(input())

for _ in range(T):
    n = int(input())
    print(*fibonacci2(n))    



