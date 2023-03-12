import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

result = []

def paper(x, y, n):
    color = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != data[i][j]:
                paper(x, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y, n//2)
                paper(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

paper(0, 0, n)
print(result.count(0))
print(result.count(1))