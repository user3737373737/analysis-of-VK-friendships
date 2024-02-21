n, s = map(int, input().split())
graph = [list(map(int, input().split())) for x in range(n)]
used = [False for i in range(len(graph))]


def dfs(v):
    used[v] = 1
    for u in g[v]:
        if used[u] == 0:
            dfs(u)
    used[v] = 2


dfs(s)
print(len(used))