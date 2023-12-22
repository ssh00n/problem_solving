import sys
input = sys.stdin.readline


N, K = map(int, input().split())
nations = []

# apporach
# 2d array -> sort lambda x[0], x[1], x[2]

for _ in range(N):
    nation_num, gold, silver, bronze = map(int, input().split())
    nations.append([nation_num, gold, silver, bronze])


nations.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

rank = 1
nations[0].append(rank)
if nations[0][0] == K:
    print(nations[0][-1])
    exit(0)


for i in range(1, N):
    prev_nation = nations[i-1]
    curr_nation = nations[i]

    nation_num = curr_nation[0]
    
    if prev_nation[1:4] == curr_nation[1:4]:
        curr_nation.append(rank)
        
    else:
        rank = i+1
        curr_nation.append(rank)
    
    if nation_num == K:
        print(curr_nation[-1])
        break
    