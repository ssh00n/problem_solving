import sys

def check_vps(sequence):
    stack = []
    
    for s in sequence:
        if s == "(":
            stack.append('0')
        elif s == ")":
            if len(stack)==0:
                return "NO"
            stack.pop()
    
    if stack:
        return "NO"
    else:
        return "YES"

N = int(sys.stdin.readline())

sequences = []
for _ in range(N):
    sequences.append(sys.stdin.readline().rstrip())

for sequence in sequences:
    print(check_vps(sequence))