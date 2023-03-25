import sys


class GridGraph:
    def __init__(self, grid):
        self.__grid = grid

    def islandCount(self):
        visited = set()
        count = 0
        for r in range(len(self.__grid)):
            for c in range(len(self.__grid[0])):
                if self.explore(r, c, visited):
                    count += 1
        return count

    def baseCondition(self, r, c, visited):
        rowInbound = True if 0 <= r < len(self.__grid) else False
        colInbound = True if 0 <= c < len(self.__grid[0]) else False
        if not rowInbound or not colInbound:
            return False
        if self.__grid[r][c] == 'W':
            return False
        if (r, c) in visited:
            return False
        return True

    def explore(self, r, c, visited):
        if not self.baseCondition(r, c, visited):
            return False
        pos = (r, c)
        visited.add(pos)
        self.explore(r - 1, c, visited)
        self.explore(r + 1, c, visited)
        self.explore(r, c - 1, visited)
        self.explore(r, c + 1, visited)
        return True

    def minimumIsland(self):
        visited = set()
        minSize = sys.maxsize
        for r in range(len(self.__grid)):
            for c in range(len(self.__grid[0])):
                size = self.exploreSize(r, c, visited)
                minSize = size if 0 < size < minSize else minSize
        return minSize

    def exploreSize(self, r, c, visited):
        if not self.baseCondition(r, c, visited):
            return 0
        pos = (r, c)
        visited.add(pos)
        size = 1
        size += self.exploreSize(r - 1, c, visited)
        size += self.exploreSize(r + 1, c, visited)
        size += self.exploreSize(r, c - 1, visited)
        size += self.exploreSize(r, c + 1, visited)
        return size
