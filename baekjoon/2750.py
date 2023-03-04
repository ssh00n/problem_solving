import sys

N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for num in nums:
    print(num)

# nums = [int(sys.stdin.readline()) for _ in range(N)]

# for num in sorted(nums):
#     print(num)