import sys

n = int(sys.stdin.readline())

solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()

# [-99, -2, -1, 4, 98]
# [-99, -74, -11, -6, -1, 3, 6, 44, 56]


left = 0
right = n - 1
min_diff = abs(solutions[-1] + solutions[0])
res1 = solutions[0]
res2 = solutions[-1]

while left < right:
    
    if abs(solutions[left]) == abs(solutions[right]):
        res1 = solutions[left]
        res2 = solutions[right]
        break
    
    elif abs(solutions[left]) > abs(solutions[right]):
        two_sum = abs(solutions[left] + solutions[right])
        if two_sum < min_diff:
            min_diff = two_sum
            res1 = solutions[left]
            res2 = solutions[right]
        left += 1
    
    else: # abs(solutions[left] < abs(solutions[right]))
        two_sum = abs(solutions[left] + solutions[right])
        if two_sum < min_diff:
            min_diff = two_sum
            res1 = solutions[left]
            res2 = solutions[right]
        right -= 1

print(f"{res1} {res2}")