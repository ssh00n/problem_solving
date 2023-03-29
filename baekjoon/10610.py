import sys
input = sys.stdin.readline

n = input().rstrip()

int_array = sorted([int(x) for x in n], reverse=True)

if sum(int_array) % 3 == 0 and int_array[-1] == 0:
    res = ''.join(map(str, int_array))
    
else:
    res = -1
    
print(res)




