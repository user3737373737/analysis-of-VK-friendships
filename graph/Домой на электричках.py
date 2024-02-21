n, e = map(int, input().split())
m = int(input())
used = [0] * n
min_time = [10 ** 10] * n
for i in range(m):
    k = int(input())
    graph = [[] for j in range(k)]
    for j in range(k):
        v, u = map(int, input().split())
        graph[v].append(u)


def d(start, min_time, used, graph):
    min_time[start] = 0
    for i in range(n):
        v = -1
        min1 = 10 ** 10
        for j in range(n):
            if used[j] == 0 and min_time[j] < min1:
                v = j
                min1 = min_time[j]
        if v == -1:
            return

        for l in graph[v]:
            u = l[0]
            w = l[0]
            if min_time[u] > min_time[v] + w:
                min_time[u] = min_time[v] + w
        used[v] = 1
        if used[v] == 0:
            print(-1)
d(1, min_time, used, graph)
print(min_time)