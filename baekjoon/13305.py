import sys
input = sys.stdin.readline

n = int(input())
distance = [0] + list(map(int, input().split()))
price = list(map(int, input().split()))

stack = [[price[0], distance[0]]]
# print(stack[-1][0]) # price
# print(stack[-1][1]) # distance

dist = 0
cost = 0
for p, d in zip(price, distance):
    if p >= stack[-1][0]:
        dist += d
    else: # p <= stack[-1][0]
        dist += d
        cost += (dist * stack[-1][0])
        stack.pop()
        stack.append([p, d])
        dist = 0
else:
    cost += (dist * stack[-1][0])
    
print(cost)


    