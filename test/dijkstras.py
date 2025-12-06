class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for row in range(vertices)]

    def min_dis(self, distance, visited):

        min = 1e7

        for v in range(self.V):
            if distance[v] < min and visited[v] == False:
                min = distance[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        distance = [1e7] * self.V
        distance[src] = 0
        visited = [False] * self.V

        for x in range(self.V):

            u = self.min_dis(distance, visited)

            visited[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and visited[v] == False and distance[v] > distance[u] + self.graph[u][v]):
                    distance[v] = distance[u] + self.graph[u][v]

        return distance[-1]

g = Graph(6)
g.graph = [[0, 1, 5, 0, 0, 0],
           [1, 0, 3, 10, 8, 0],
           [5, 3, 0, 0, 2, 0],
           [0, 10, 0, 0, 3, 2],
           [0, 8, 2, 3, 0, 7],
           [0, 0, 0, 2, 7, 0]        
           ]

print(g.dijkstra(0))