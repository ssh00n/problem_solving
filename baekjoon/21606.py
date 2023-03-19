import sys
sys.setrecursionlimit(1000000000)

def solution():

    input = sys.stdin.readline

    n = int(input())
    a = input()

    graph = [0]

    for _ in range(n):
        graph.append([])
    # graph = [[] for _ in range(n+1)]
    # print(graph)

    res = 0
    visited = [False] * (n+1)

    for i in range(n-1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        
        # 실내 - 실내
        if a[x-1] == "1" and a[y-1] == "1":
            res += 2

    def dfs(start, count):
        visited[start] = True
        for i in graph[start]:
            if a[i-1] == "0" and not visited[i]:
                count = dfs(i, count)
            elif a[i-1] == "1":
                count += 1
        return count

    for i in range(1, n+1):
        if not visited[i] and a[i-1] == "0":
            count = dfs(i, 0)
            res += count * (count - 1) # 실외의 인접한 실내들을 나열하는 수
    print(res)
solution()
