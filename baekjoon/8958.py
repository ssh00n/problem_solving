import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    ox = sys.stdin.readline()
    total = 0
    score=1
    
    for i in range(len(ox)):
        if ox[i] == "O":
            
            prev = score
            
            if ox[i-1] == "O":    
                score = prev + 1
                total += score
                prev = score
            else:
                total += score
        else:
            score=1
    print(total)
            