import sys

# 문제 분석
# lower case로 이루어진 N개의 단어가 들어오면
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로 
# 정렬 (중복 시 하나만 남기고 제거)

# 입력
# 단어의 개수 N (1 <= N <= 20,000)
# len(string) 문자열의 길이 <= 50
# 한줄에 단어 하나씩

# 접근 방법
# 20,000개의 길이의 리스트 (중복 시 하나만 남겨야 함)
# data = [] 에서 len(i)로 정렬

lst = sys.stdin.readlines()[1:]
lst = list(set(lst))
lst.sort()
lst.sort(key=len)
# print(lst)
print(''.join(lst))


# array.sort()
# array.sort(key = lambda x: len(x))
# for i in array:
#         sys.stdout.write(str(i)+'\n')