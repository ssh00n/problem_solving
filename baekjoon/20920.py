import sys
from collections import Counter

input = sys.stdin.readline

# abcdefghijklmnopqrstuvwxyz
# Approach
# 우선순위 역순으로 정렬을 수행한다.

n, m = map(int, input().split())
vocas = []
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        vocas.append(word)


counter = Counter(vocas)

result = list(set(vocas))
result.sort()  # 3: 알파벳 사전 순
result.sort(key=lambda x: len(x), reverse=True)  # 2. 해당 단어의 길이 순
result.sort(key=lambda x: counter[x], reverse=True)  # 1. 자주 나오는 단어 순

print("\n".join(result))
