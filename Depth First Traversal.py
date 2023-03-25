from Stack import Stack


# Iterative
def depthFirstTraverse(graph, source):
    order = []
    if source in graph:
        stack = Stack(source)
    else:
        return order
    while not stack.isEmpty():
        current = stack.pop()
        order.append(current)

        for neighbour in graph.get(current, {}):
            stack.push(neighbour)
    return order


# Recursive
# def depthFirstTraverse(graph, start):
#     print(start)
#     for neighbour in graph[start]:
#         depthFirstTraverse(graph, neighbour)


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

print(depthFirstTraverse(g, 'e'))
