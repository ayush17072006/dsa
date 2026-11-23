class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.visited = [False] * vertices

    def add_edge(self, source, destination):
        self.adj[source][destination] = 1
        self.adj[destination][source] = 1

    def display_graph(self):
        print("\nAdjacency Matrix:")
        print(" ", *range(self.vertices))

        for i in range(self.vertices):
            print(i, self.adj[i])

    def dfs_util(self, vertex, traversal):
        self.visited[vertex] = True
        traversal.append(vertex)

        for neighbour in range(self.vertices):
            if self.adj[vertex][neighbour] == 1 and not self.visited[neighbour]:
                self.dfs_util(neighbour, traversal)

    def dfs(self, start_vertex):
        if start_vertex < 0 or start_vertex >= self.vertices:
            print("Invalid starting vertex.")
            return []

        self.visited = [False] * self.vertices
        traversal = []
        self.dfs_util(start_vertex, traversal)

        return traversal
