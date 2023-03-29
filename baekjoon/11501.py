import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stock = list(map(int, input().split()))
    signal = stock[-1]
    profit = 0
    for i in range(len(stock)-1, -1, -1):
        if stock[i] < signal:
            profit += signal - stock[i]
        else:
            signal = stock[i]
    print(profit)