import sys

N = int(sys.stdin.readline())
T = []

def recursion(s, l, r):
    global count
    if l >= r:
        count += 1
        return [1, count]
    elif s[l] != s[r]:
        count += 1
        return [0, count]
    else:
        count += 1
        return recursion(s, l+1, r-1)
    
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)



for _ in range(N):
    T.append(sys.stdin.readline().rstrip())

for t in T:
    count = 0
    print(*isPalindrome(t))