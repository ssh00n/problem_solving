import sys
# 나머지의 순환 성질을 이용한 접근 -> 시간초과

a, b, c = map(int, sys.stdin.readline().split())

i = 0
circular = []

while i < b:
    a *= a        
    if a % c in circular:
        break
    else:
        circular.append(a%c)
    i += 1
ans = circular[(b % len(circular))-1]
    
print(ans)