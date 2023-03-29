import math
S = int(input())

res = 0
if S == 1:
    res = 1
    

for n in range(int(2*math.sqrt(2*S)), 0, -1):
    if n*(n+1) > 2*S:
        continue
    if n*(n+1) <= 2*S:
        res = n
        break
    
print(res)

# n*(n+1) < 2*S