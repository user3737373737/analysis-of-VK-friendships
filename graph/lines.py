from collections import deque

n = int(input())
used = [0 for _ in range(n)]
d = [10**10 for _ in range(n)]
graph = [list(map(str, input().split())) for i in range(n)]
q = deque()
point = 0
end = 0
O = 0
final = False
startx = 0
starty = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == '.':
            point = graph[i][j]
        elif graph[i][j] == 'X':
            end = graph[i][j]
        elif graph[i][j] == 'O':
            O = graph[i][j]
        elif graph[i][j] == '@':
            startx = i
            starty = j



def bfs(startx, starty, endx, endy, start, q, d):
    q.append(startx)
    q.append(starty)
    while len(q) != 0:
        startx = q.popleft()
        starty = q.popleft()
        if graph[startx][starty] == end:
            fianl = True