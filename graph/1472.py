from collections import deque

n, m = map(int, input().split())
gr = [list(map(int, input().split())) for _ in range(n)]
level = [[-1] * m for _ in range(n)]


def bfs(v):
    q = deque([v])
    ans = 10 ** 10
    x, y = v
    level[x][y] = 0
    while q:
        x, y = q.popleft()
    i = y + 1
    while gr[x][i] == 0:
        i += 1
    else:
        if gr[x][i] == 2:
            i += 1

