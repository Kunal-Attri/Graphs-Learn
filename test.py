from DirectedGraph import DirectedGraph
from GridGraph import GridGraph
from UndirectedGraph import UndirectedGraph


def get_edges():
    edges = set()
    noOfEdges = int(input("No of edges: "))
    for _ in range(noOfEdges):
        edges.add(tuple(input().split()))
    return edges


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

g = GridGraph(grid)
print(g.minimumIsland())

