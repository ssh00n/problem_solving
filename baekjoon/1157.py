import sys
# 알파벳 대소문자로 된 단어
# 가장 많이 사용된 알파벳 대문자로 출력
# 최대 길이 1,000,000
# O(n)
# 리스트 멤버십 테스트보다 set 멤버십 테스트가 훠어어얼씬 빠르다

voca = sys.stdin.readline().rstrip()

voca = sorted(voca.upper())
set_voca = set(voca)

cnt_list = []

for i in set_voca:
    cnt_list.append(voca.count(i))

count = 0
cnt_max = max(cnt_list)

for s, freq in zip(set_voca, cnt_list):
    if cnt_max == freq:
        count += 1
        ans = s

if count >= 2:
    print("?")
else:
    print(ans)


# ans = max(cnt_list)



# max_i = max(cnt_list)
# idx = cnt_list.index(max_i)
# ans = voca[idx]


# if max_i == cnt_list.count(max_i):
#     print(voca[idx])
    
# else:
#     print("?")




# dictionary를 이용한 접근

# for i in voca:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1


# max_freq = 0
# for key in count_dict.keys():
#     if count_dict[key] > max_freq:
#         max_freq = count_dict[key]
#         ans = key
        
# if count_dict.values().count(max_freq) > 1:
#     print("?")
# else:
#     print(ans)
    