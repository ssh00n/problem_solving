import sys

C = int(sys.stdin.readline())

for _ in range(C):
    user_input = list(map(int, sys.stdin.readline().split()))
    N = user_input[0]
    students = user_input[1:]    
    average = sum(students) // len(students)
    # print([a for a in A if a<X])
    over_avg = [student for student in students if student > average]
    
    result = len(over_avg)/len(students)*100
    print(f"{result:.3f}%")