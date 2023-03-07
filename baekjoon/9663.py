import sys



N = int(sys.stdin.readline())

pos = [0] * N
flag_a = [False] * N
flag_b = [False] * ((2*N)-1)
flag_c = [False] * ((2*N)-1)
count = 0

def put():
    global count
    count += 1
    # for i in range(8):
    #     print(f'{pos[i]:2}', end='')
    # print()

def set(i):
    for j in range(N):
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+(N-1)]:
            pos[i] = j
            if i == (N-1):
                put()
                
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(N-1)] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(N-1)] = False
                

set(0)
print(count)
