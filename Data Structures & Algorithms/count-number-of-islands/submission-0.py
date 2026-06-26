from collections import deque

class Solution:
    def __init__(self):
        self.tracked: set[tuple[int]] = []
        self.grid: List[List[str]] = []


    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        n_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])): # grid[0] assumes all rows have same length
                if int(grid[i][j]) == 0 or (i,j) in self.tracked:
                    continue
                else:
                    n_islands += 1
                    self.track_island((i,j))
        
        return n_islands

    
    def track_island(self, start: tuple[int]):
        queue = deque([start])
        self.tracked.append(start)

        while len(queue) > 0:
            next_point = queue[0]
            new_neighbors = self.get_neighbors(next_point)
            new_neighbors = [neighbor for neighbor in new_neighbors if neighbor not in self.tracked]
            queue.extend(new_neighbors)
            self.tracked.extend(new_neighbors)
            queue.popleft()


    def get_neighbors(self, index: tuple[int]) -> list[tuple[int]]:
        i, j = index # separating items in index
        possible_neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        # returns masked neighbors - in grid remain
        return [n for n in possible_neighbors if self.valid_neighbor(n)]


    def valid_neighbor(self, index: tuple[int]) -> bool:
        i, j = index
        if 0 <= i < len(self.grid) and 0 <= j < len(self.grid[0]):
            return self.grid[i][j] == '1'
        
        return False






        