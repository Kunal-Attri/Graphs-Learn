from queue import Queue


def breadthFirstTraverse(graph, source):
    order = []
    que = Queue()

    if source in graph:
        que.put(source)
    else:
        return order

    while que.qsize() > 0:
        current = que.get()
        order.append(current)
        for neighbour in graph.get(current, {}):
            que.put(neighbour)
    return order


#  a -> c
#  ↓    ↓
#  b    e
#  ↓
#  d -> f
g = {
    'a': {'b', 'c'},
    'b': {'d'},
    'c': {'e'},
    'd': {'f'},
    'e': {},
    'f': {}
}

print(breadthFirstTraverse(g, 'a'))
