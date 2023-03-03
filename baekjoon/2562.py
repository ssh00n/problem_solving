import sys

numbers = []
for _ in range(9):
    numbers.append(int(sys.stdin.readline()))

print(max(numbers))
print(numbers.index(max(numbers))+1)