from collections import deque


class Graph:
    """Класс Graph представляет собой абстракцию неориентированного графа, который состоит из вершин и ребер

    В граф передаются вершины и ребра графа.

    Атрибутами класса являюся вершина, ребро и массив для хранения графа

    Класс Graph хранит граф ввиде списков смежности, подкласс представляет граф ввиде матрицы смежности """

    def __init__(self, vertex, edge):
        """Конструктор класса Graph хранит количество вершин, количество ребер, список смежности графа"""

        self.vertex = vertex
        self.edge = edge
        self.graph = [[] for _ in range(vertex)]

    def add_edge(self, u, v):
        """Метод для добавления связи между переданными вершинами

        В метод передается вершины и ребера графа. Вершины и ребра переводятся в индексацию с нуля

        Метод добавляет ребро в список текущей вершины

        Метод работает только для списков ребер"""

        u -= 1
        v -= 1
        self.graph[u].append(v)
        return self.graph

    def dfs(self, start, clr):
        """Метод для поиска компонент связности, циклов, пути между вершинамии и проверка двудольности графа

        Метод принимает стартову вершину и ее цвет, который отвечает за посещенность

        Массив used 0 для непосещеннх вершин, 1 для посещенных вершин, 2 для вершин без исходящих ребер

        Метод не будет работать для взвешенного графа"""

        used = [0]*self.vertex

        def dfs1(s, clr):
            used[s] = 3 - clr
            for u in self.graph[s]:
                if used[u] == 0:
                    dfs1(u, used[s])
                if used[u] == used[s]:
                    return 0

        for j in range(self.vertex):
            if not used[j]:
                dfs1(j, used[j])
        return len(used)

    def bfs(self, start):
        """Метод для нахождения кратчайшего расстояния между вершинами, изолированных вершин

        В метод передается стартовая вершина

        В методе объявляем очередь, в которую положим начальную вершину. В массиве dist добавляем 0 -
        расстояние до начальной вершины. В цикле объявлем первую вершину посещенной и проверяем соседей
        этой вершины. Если смежные вершины не посещены, считаем расстояние до этой вершины

        Метод не работает для взвешенного графа"""

        queue = deque()
        used = [0]*self.vertex
        dist = [10**10]*self.vertex
        queue.append(start)
        dist[start] = 0
        while len(queue) != 0:
            v = queue.popleft()
            used[v] = 1
            for u in self.graph[v]:
                if used[u] == 0:
                    queue.append(u)
                    dist[u] = dist[v] + 1
        return dist

    def dijkstra(self, start, end):
        """Метод для определения кратчайшего пути от начальной вершины графа ко всем остальным

        В граф передается стартовая вершина.

        В массиве dist для стартовой вершины объявляем значение 0, для всех остальных бесконечность.
        Проводим релаксацию ребер. Далее идет условие проверки на то, достижима ли вершина, если нет
        то выходим из алгоритма. Проверяем соседей текущей вершины. Объявляем вершину посещенной

        Метод не работет для отрицательных ребер"""

        for j in range(self.edge):
            v, u, w = map(int, input().split())
            v -= 1
            u -= 1
            self.graph[v].append([u, w])
        dist = [10**10]*self.vertex
        used = [0]*self.vertex
        dist[start] = 0
        for i in range(self.vertex):
            v = 0
            min_dist = 10**10
            for j in range(self.vertex):
                if used[j] == 0 and dist[j] < min_dist:
                    v = j
                    min_dist = dist[j]
            if v == -1:
                return
            for edge in self.graph[v]:
                u = edge[0]
                w = edge[1]
                if dist[u] > dist[v] + w:
                    dist[u] = dist[v] + w
            used[v] = 1
        return dist, dist[end]



class Matrix(Graph):
    """Класс Matrix наследуется от класса Graph, представляет собой абстракцию неориентированного графа, состоящего из вершина и ребер

    В граф передаются вершины и ребра графа.

    Атрибутами класса являюся вершина, ребро и массив для хранения графа

    Класс Matrix принимает граф в виде матрицы смежности и хранит в виде списка ребер"""

    def __init__(self, vertex, edge):
        """Конструктор класса Matrix наследуется от конструктора Graph"""

        super().__init__(vertex, edge)

    def add_edge(self, lst):
        """Метод представляет граф из матрицы смежности в список смежности"""

        for x in range(self.vertex):
            for y in range(self.edge):
                if lst[x][y] == 1:
                    self.graph[x].append(y)
                    print("hihi")
        return self.graph

    def dfs(self, start, clr):
        """Метод наследуется от класса Graph"""

        super().__init__(start, clr)

    def bfs(self, start):
        """Метод наследуется от класса Graph"""

        super().__init__(start)

    def dijkstra(self, start, end):
        """Метод наследуется от класса Graph"""

        super().__init__(start, end)