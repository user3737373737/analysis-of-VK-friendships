n, m = map(int, input().split())
graph = [[] for i in range(n)]
color = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def dfs(v, graph, color, cur_color):
    color[v] = cur_color
    for u in graph[v]:
        if color[u] == 0:
            dfs(u, graph, color, 3 - cur_color)
        elif color[u] == color[v]:
            print(0)
            exit(0)


for v in range(n):
    if color[v] == 0:
        dfs(v, graph, color, 1)

for i in range(len(color)):
    if color[i] == 1:
        print(i + 1, end=' ')

print()

for j in range(len(color)):
    if color[j] == 2:
        print(j + 1, end=' ')


"""
Алгоритм
1. Выбираем стартовую вершину
2. Запускаем функцию от стартовой вершины
    3. Помечаем вершину пройденной 
    4. Проходимся циклом по смежных вершинах стартовой вершины
    5. Если она не посещена, то вызываем функцию от этой вершины
6. Запускаем цикл от used чтобы пройтись по всем вершинам, так как могут быть компоненты связности
7. Если вершина не пройдена, запускаем цикл от этой вершины
"""

"""
Алгоритм с цветами для поиска цикла в неорентированном графе
Вместо списка visited заведём
список color, в котором будем
хранить 0 для непосещенных
вершин, а для остальных 1 или
2 — их цвет.
Алгоритм DFS для каждого
ребра будет проверять цвет его
конечной вершины.
Непосещённая вершина
красится в цвет, неравный цвету
текущей. Если вершина была
посещена, то ребро пропускается
если его концы разноцветные,
инече делается пометка, что
граф не является двудольным.
"""

"""
color = [0] * n
flag = True
def dfs(start):
    for v in g[start]:
    if color[v] == 0:
        color[v] = 3 - color[start]
        dfs(v)
    elif color[v] == color[start]:
        flag = False
for i in range(n):
    if color[i] == 0:
        color[i] = 1
        dfs(i)
"""