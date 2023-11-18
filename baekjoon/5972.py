import sys
import heapq

with open("input.txt", "r") as file:
    input_data = iter(file.readlines())


def input():
    return next(input_data)


INF = sys.maxsize

V, E = map(int, input().split())
start = 1
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    x, y, weight = map(int, input().split())
    graph[x].append((y, weight))
    graph[y].append((x, weight))


def dijkstra(start):
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, cur = heapq.heappop(q)
        if dist[cur] < w:
            continue
        for next_node, next_w in graph[cur]:
            cost = w + next_w
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))


dist = [INF] * (V + 1)
dijkstra(start)

print(graph)

# ###############################################################
# for d in dist[1:]:
#     print(d if d != INF else "INF")

print(dist[V])
