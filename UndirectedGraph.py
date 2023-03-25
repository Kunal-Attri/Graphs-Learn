from Graph import Graph


class UndirectedGraph(Graph):
    def __init__(self, edges=None, adjacency_map=None):
        super().__init__()
        if edges is not None:
            self.build_adjacency_map(edges)
        elif adjacency_map is not None:
            self._graph = adjacency_map

    def build_adjacency_map(self, edges) -> None:
        for edge in edges:
            self._graph[edge[0]] = self._graph.get(edge[0], set())
            self._graph[edge[0]].add(edge[1])
            self._graph[edge[1]] = self._graph.get(edge[1], set())
            self._graph[edge[1]].add(edge[0])
