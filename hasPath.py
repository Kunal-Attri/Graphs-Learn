from queue import Queue


# DFS
def hasPath(graph, src, dest):
    if src == dest:
        return True

    for neighbour in graph.get(src, {}):
        if hasPath(graph, neighbour, dest):
            return True
    return False


# BFS
# def hasPath(graph, src, dest):
#     que = Queue()
#     que.put(src)
#
#     while que.qsize() > 0:
#         current = que.get()
#
#         if current == dest:
#             return True
#
#         for neighbour in graph.get(current, {}):
#             que.put(neighbour)
#     return False


g = {
    'f': {'g', 'i'},
    'g': {'h'},
    'h': {},
    'i': {'g', 'k'},
    'j': {'i'},
    'k': {}
}

print(hasPath(g, 'f', 'j'))
