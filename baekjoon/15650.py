N, M = map(int, input().split())

lst = []

def dfs():
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    else:
        for i in range(1, N+1):
            if not lst:
                lst.append(i)
                dfs()
                lst.pop()
            else:
                if i not in lst and i > lst[-1]:
                    lst.append(i)
                    dfs()
                    lst.pop()

dfs()