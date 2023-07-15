import sys
from itertools import combinations

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

# logic
# anta [ ] tica 사이에 들어가는 문자를 parsing한다
# anta, tica는 반드시 포함되기 때문에 [a, c, i, n, t] 는 default

# k < 5이면, result = 0

# dictionary에서 value가 가장 높은 순으로 (k - 5)개 만큼 추가한다
# -> 최적해가 아님
# 단순히 하나의 문자를 추가하는 것보다, 공통 부분 문자열이 많은 것을 우선순위로 추가하는게 최적해
# 단어당 포함 여부를 확인하는 것이 좋을듯

# rc, hello, car
# 두 번 포함되면 한번만 센다. set!!

# 위 풀이는 문제에 대한 해답을 보장할 수 없음
# 26개의 알파벳에 대해 모든 조합을 고려해서 제일 많은 조합을 배워야함

# -------------------------------------------------------------------------


n, k = map(int, input().split())
words = [set(input().rstrip()) for _ in range(n)]
if k < 5:
    print(0)
    sys.exit(0)
elif k == 26:
    print(n)
    sys.exit(0)

alphabets = [chr(i) for i in range(97, 123) if chr(i) not in ['a', 'c', 'i', 'n', 't']]
result = 0

for comb in combinations(alphabets, k-5):
    literate = set(list('antic') + list(comb))
    count = 0
    for word in words:
        if word.issubset(literate):
            count += 1
    result = max(result, count)

print(result)

# print(words)    
# d = dict()
# result = 0

# for word in words:
# alphabets = [chr(i) for i in range(97, 123) if chr(i) not in ['a', 'c', 'i', 'n', 't']]
# result = 0

# for comb in combinations(alphabets, k-5):
#     literate = set(list('antic') + list(comb))
#     count = 0
#     for word in words:
#         if word.issubset(literate):
#             count += 1
#     result = max(result, count)

# print(result)
#     target = word[4:-4]
#     for s in set(target):
#         if s not in d:
#             d[s] = 1
#         else:
#             d[s] += 1

# # print(d)

# sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# k -= 5

# for key in sorted_dict.keys():
#     if k == 0:
#         break
#     if key not in literate:
#         literate.add(key)
#         k -= 1

# # print(literate)
# for word in words:
#     target = word[4:-4]
#     result += set(target).issubset(literate)
        

# print(result)

