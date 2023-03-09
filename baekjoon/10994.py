import sys

n = int(sys.stdin.readline())

x = 4 * n - 3
star = [[' ']*x for _ in range(x)]


def draw(n, idx):
    if n == 1:
        star[idx][idx] = "*"
        return
    
    l = 4 * n - 3
    
    for i in range(idx, idx+l):
        star[idx][i] = "*"
        star[idx+l-1][i] = "*"
        
        star[i][idx] = "*"
        star[i][idx+l-1] = "*"
    
    return draw(n-1, idx+2)

draw(n, 0)

for i in range(x):
    for j in range(x):
        print(star[i][j], end='')
    print()


# draw(x, 0)

# i = 0 , j = 0, 1, 2, 3, 4
# i = 1 , j = 0, 4
# i = 2 , j = 0, 4
# i = 3 , j = 0, 4
# i = 4 , j = 0, 1, 2, 3, 4

# i = 0, j = 0, 1, 2, 3, 4, 5, 6, 7, 8
# i = 1, j = 0, 8
# i = 2, j = 0, 8
# i = 3, j = 0, 8
# i = 4, j = 0, 8
# i = 5, j = 0, 8
# i = 6, j = 0, 8
# i = 7, j = 0, 8
# i = 8, j = 0, 1, 2, 3, 4, 5, 6, 7, 8