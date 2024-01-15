import sys
from collections import Counter

input = sys.stdin.readline


# 1. 같은 종류의 문자로 이루어져 있다.
# 2. 같은 문자는 같은 개수 만큼 있다

n_words = int(input())
standard = sorted(input().rstrip())
words = []
count = 0

for _ in range(n_words - 1):
    words.append(sorted(input().rstrip()))

# len(standard) == len(word)
# -> 비슷하려면 한 글자만 다른 경우
# len(standard) == len(word-1)
# -> 한 글자를 추가하는 경우
# len(standard) == len(word+1)
# -> 한 글자를 빼는 경우


def count_different_chars(str1, str2):
    counter = Counter(str1)
    counter2 = Counter(str2)
    for i in range(len(str2)):
        if str2[i] in counter and counter[str2[i]] > 0:
            counter[str2[i]] -= 1
            counter2[str2[i]] -= 1
    remaining_chars = list(counter.elements())
    remaining_chars2 = list(counter2.elements())

    if len(remaining_chars) == len(remaining_chars2) == 0:
        return 1
    elif len(remaining_chars) == len(remaining_chars2) == 1:
        return 1
    else:
        return 0


for word in words:
    if len(standard) == len(word):
        count += count_different_chars(standard, word)

    elif len(standard) == (len(word) - 1):
        original = word
        for i in range(len(word)):
            temp_word = original[:i] + original[i + 1 :]
            if temp_word == standard:
                count += 1
                break

    elif len(standard) == len(word) + 1:
        original = word
        for i in range(len(standard)):
            temp_word = original.copy()
            temp_word.extend(standard[i])
            temp_word = sorted(temp_word)
            if temp_word == standard:
                count += 1
                break

    else:
        pass

print(count)
