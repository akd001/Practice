from util import time_it, print_matrix
from typing import List

hello = "yo!"

land_matrix = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

land_matrix2 = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

land_matrix3 = [
    [1, 1],
    [1, 0]
]

class Solution:

    def explore(self, x, y: int, grid: List[List[int]]) -> int:
        # print(f">>> exploring {x}, {y} with gridId {gridId}")
        # print_matrix(grid)
        if x < 0 or x >= len(grid) or \
            y < 0 or y >= len(grid[0]) or \
            grid[x][y] == 0:
            # print(f"<<< returning from {x}, {y}")
            return 0
        grid[x][y] = 0
        size = 1
        # print(f"Setting {x}, {y} to gridId {gridId}")
        # print_matrix(grid)
        # print(f"<<< returning from {x}, {y}")
        return 1 + self.explore(x-1,y, grid) \
            + self.explore(x,y+1, grid) \
            + self.explore(x,y-1, grid) \
            + self.explore(x+1,y, grid) 

    @time_it
    def islandCount(self, grid: List[List[int]]) -> int:
        # 1. traverse grid and pick traversal seed
        # 2. explore in all four directions iteratively until hitting a 0
        rows = len(grid)
        columns = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    count += 1
                    self.explore(i, j, grid)
        # print_matrix(grid)
        return count
    
    @time_it
    def largestSquare(self, grid: List[List[int]]):
        rows = len(grid)
        columns = len(grid[0])
        maxSquare = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    size = self.explore(i, j, grid)
                    maxSquare = max(maxSquare, size)
        return maxSquare
        

if __name__=="__main__":
    matrix = land_matrix
    sol = Solution()
    # print(sol.islandCount(matrix))
    print(sol.largestSquare(matrix))