import sys
input = sys.stdin.readline

n = int(input())

predictions = [int(input()) for _ in range(n)]
predictions.sort()

rankings = [i for i in range(1, len(predictions)+1)]

result = [abs(a - b) for a, b in zip(predictions, rankings)]

print(sum(result))