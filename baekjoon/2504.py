import sys

sequence = sys.stdin.readline().rstrip()


stack = []


def is_correct(sequence):
    global stack
    
    for s in sequence:
        if s == "(":
            stack.append(")")
        elif s == "[":
            stack.append("]") 
        elif not stack or stack.pop() != s:
            return False
    return not stack

def get_score(sequence):
        global stack
        total = 0
        temp = 1
        
        for i in range(len(sequence)):
            
            if sequence[i] == "(":
                temp *= 2
                stack.append(")")
            elif sequence[i] == "[":
                temp *= 3
                stack.append("]")
                
            elif sequence[i] == ")":
                if sequence[i-1] == "(":
                    total += temp
                temp //= 2
                stack.pop()
            else: # sequence[i] == "]"
                if sequence[i-1] == "[":
                    total += temp
                temp //= 3
                stack.pop()
            
        return total

if not is_correct(sequence):
    print(0)
else:
    print(get_score(sequence))


