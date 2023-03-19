import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
result = {"MIN_VALUE" : 1e9, "MAX_VALUE" : -1e9}

def divide(x, y):
    if x < 0 and y > 0:
        return -(-x // y)
    elif x > 0 and y < 0:
        return -(x // -y)
    else:
        return x // y

def dfs(i, cur_result, add, sub, mul, div):
    if i == n:
        result["MIN_VALUE"] = min(result["MIN_VALUE"], cur_result)
        result["MAX_VALUE"] = max(result["MAX_VALUE"], cur_result)
        return
    
    if add > 0:
        add -= 1
        dfs(i+1, cur_result+nums[i], add, sub, mul, div)
        add += 1
    
    if sub > 0:
        sub -= 1
        dfs(i+1, cur_result-nums[i], add, sub, mul, div)
        sub += 1
    
    if mul > 0:
        mul -= 1
        dfs(i+1, cur_result*nums[i], add, sub, mul, div)
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1, divide(cur_result, nums[i]), add, sub, mul, div)
        div += 1
    
dfs(1, nums[0], add, sub, mul, div)

print(result["MAX_VALUE"])
print(result["MIN_VALUE"])