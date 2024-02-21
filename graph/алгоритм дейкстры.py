n = int(input())
d, v = map(int, input().split())
r = int(input())
gr = [list(map(int, input().split())) for i in range(n)]
INF = 10 ** 10
used = [False] * n
dist = [INF] * n
min_dist = 0
min_v = d
dist[min_v] = 0
while min_dist < INF:
    i = min_v
    used[i] = True
    for x in gr[i]:
        if x[0] >= dist[i] and x[1] < dist[x[2]]:
            dist[x[2]] = x[1]
    min_dist = INF
    for l in range(n):
        if not used[l] and dist[l] < min_dist:
            min_dist = dist[l]
            min_v = d

print(dist[v])

