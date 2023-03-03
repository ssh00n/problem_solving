import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
count = 0

for number in numbers:
    if number == 1:
        continue    
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        count += 1 
            
        
print(count)
