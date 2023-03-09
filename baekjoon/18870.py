import sys

N = int(sys.stdin.readline())

x = list(map(int, sys.stdin.readline().split()))
    

# .index로 매번 찾으면 시간복잡도가 매우 높음
sorted_x = sorted(set(x))

# 정렬 후 큰 값의 개수를 log n 만에 구할 수 있는 알고리즘?
def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

for i in x:
    sys.stdout.write(str(binary_search(sorted_x, i))+" ")
    
# output = [sorted_x.index(i) for i in x]

# print(output)