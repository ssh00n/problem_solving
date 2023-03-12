import sys

n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))

list_a.sort()

m = int(sys.stdin.readline())
list_b = list(map(int, sys.stdin.readline().split()))


for i in list_b:
    left = 0
    right = len(list_a) - 1
    while left <= right:
        ptr = (left + right) // 2
        if i == list_a[ptr]:
            print(1)
            break
        elif i < list_a[ptr]:
            right = ptr -1
        elif i > list_a[ptr]:
            left = ptr + 1
    else:
        print(0)
