import sys

input = sys.stdin.readline

for line in sys.stdin:
    a, b, c = map(int, line.split())
    if a == 0 and b == 0 and c == 0:
        break

    # check validity
    if a >= b + c or b >= a + c or c >= a + b:
        print("Invalid")
    else:
        # check type of triangle
        if a == b == c:
            print("Equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        else:
            print("Scalene")