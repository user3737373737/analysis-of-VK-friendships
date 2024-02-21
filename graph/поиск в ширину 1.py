from collections import deque

def bfs(start, d, used):  # v - стартовая вершина
    q = deque()
    q.append(start)
    d[start] = 0
    while len(q) != 0:
        v = q.popleft()
        used[v] = 1
        for u in graph[v]:
            if used[u] == 0:
                q.append(u)
                d[u] = d[v] + 1


num = int(input())
for i in range(num):
    n, m = map(int, input().split())
    graph = [[] for j in range(n)]

    for j in range(m):
        v, u = map(int, input().split())
        graph[v].append(u)

    start = int(input())

    d = [987654321] * n
    used = [0] * n
    bfs(start, d, used)

    print(*d)