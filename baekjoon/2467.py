import sys

with open("input.txt", "r") as file:
    input_data = iter(file.readlines())


def input():
    return next(input_data)


N = int(input())
solutions = list(map(int, input().split()))


left = 0
right = N - 1


def find_pair_with_sum(arr):
    min_sum = float("inf")
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        abs_current_sum = abs(current_sum)
        if abs_current_sum < min_sum:
            min_sum = abs_current_sum
            min_pair = (arr[left], arr[right])

        if current_sum < min_sum:
            left += 1
        else:
            right -= 1

    return min_pair


print(" ".join(map(str, find_pair_with_sum(solutions))))
