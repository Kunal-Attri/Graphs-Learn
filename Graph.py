from queue import Queue
from Stack import Stack
import random
import sys


class Graph:
    def __init__(self):
        self._graph = dict()

    def breadth_first_traversal(self, source) -> list:
        order = []
        que = Queue()

        if source in self._graph:
            que.put(source)
        else:
            return order

        while que.qsize() > 0:
            current = que.get()
            if current in order:
                continue
            else:
                order.append(current)
            for neighbour in self._graph.get(current, {}):
                if neighbour not in order:
                    que.put(neighbour)
        return order

    def depth_first_traversal(self, source) -> list:
        order = []

        if source in self._graph:
            stack = Stack(source)
        else:
            return order

        while stack.getSize() > 0:
            current = stack.pop()
            if current in order:
                continue
            order.append(current)

            for neighbour in self._graph.get(current, {}):
                if neighbour not in order:
                    stack.push(neighbour)
        return order

    def hasPath_bfs(self, src, dest) -> bool:
        que = Queue()
        que.put(src)
        visited = set()

        while que.qsize() > 0:
            current = que.get()
            if current == dest:
                return True

            if current in visited:
                continue
            visited.add(current)

            for neighbour in self._graph.get(current, {}):
                if neighbour not in visited:
                    que.put(neighbour)
        return False

    def hasPath_dfs(self, src, dest, visited=None) -> bool:
        if visited is None:
            visited = set()
        if src in visited:
            return False
        visited.add(src)

        if src == dest:
            return True

        for neighbour in self._graph.get(src, {}):
            if self.hasPath_dfs(neighbour, dest, visited):
                return True
        return False

    def connectedComponentsCount(self) -> int:
        count = 0
        nodes = set(self._graph.keys())
        visited = set()
        while nodes:
            component = self.depth_first_traversal(random.choice(list(nodes)))
            visited = visited.union(component)
            nodes = nodes.difference(visited)
            count += 1
        return count

    def largestComponentSize(self) -> int:
        largest = -sys.maxsize
        nodes = set(self._graph.keys())
        visited = set()

        while nodes:
            component = self.depth_first_traversal(random.choice(list(nodes)))
            visited = visited.union(component)
            nodes = nodes.difference(visited)

            largest = len(component) if len(component) > largest else largest
        return largest

    def shortestPath(self, src, dst) -> int:
        visited = set()
        que = Queue()

        if src == dst:
            return 0
        if (src in self._graph) and (dst in self._graph):
            que.put((src, 0))
        else:
            return -1

        while que.qsize() > 0:
            current = que.get()

            if current[0] == dst:
                return current[1]
            if current[0] in visited:
                continue
            visited.add(current[0])

            for neighbour in self._graph.get(current[0], {}):
                if neighbour not in visited:
                    que.put((neighbour, current[1] + 1))
        return -1
