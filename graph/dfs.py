n, s = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
used = [[0] for x in range(len(graph))]


def dfs(v, clr):
    used[v] = 3 - clr
    for u in graph[v]:
        if used[u] == 0:
            dfs(u, used[v])
        if used[u] == used[v]:
            return 0


for j in range(len(graph)):
    if not used[j]:
        dfs(j)


print(dfs(s-1))
print(res)
print(len(used))