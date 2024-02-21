n, m = map(int, input().split())
graph = [[] for i in range(n)]
color = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    #graph[v].append(u)
    print(graph)

"""
Ввод графов

Матрица смежности:
graph = [list(map(int, input().split())) for i in range(n)]

Список смежности:
graph = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1 # если индексация с единицы
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
    
     def dfs(self, v, cur_color):
        color = [0] * self.vertex
        color[v] = cur_color
        for u in self.graph[v]:
            if color[u] == 0:
                dfs(u, 3 - cur_color)
            elif color[u] == color[v]:
                return
                
                
                

n, m = map(int, input().split())
color = int(input())
s = int(input())
end = int(input())
gr = Graph(n, m)
m = Matrix(n, m)
graph = [list(map(int, input().split())) for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    gr.add_edge(u, v)
print(*gr.bfs(s))
print(gr.dfs(s, color))
print(gr.dijkstra(s, end))
print(m.add_edge(graph))
"""