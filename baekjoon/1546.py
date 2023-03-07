import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
new_scores = [100*(score/max(scores)) for score in scores]
print(sum(new_scores)/len(new_scores))