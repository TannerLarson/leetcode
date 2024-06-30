#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
import copy
from typing import List, Tuple

class Grid:
    def __init__(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.num_col = len(grid)
        self.num_row = len(grid[0])

    def get(self, row: int, col: int) -> int:
        return self.grid[row][col]

    def set_value(self, row: int, col: int, value) -> None:
        self.grid[row][col] = value
        
    def show(self) -> None:
        for row in self.grid:
            print(row)

    def get_coord(self, coord: Tuple[int, int]) -> int:
        return self.grid[coord[0]][coord[1]]

    def get_surrounding_coords(self, row: int, col: int) -> List[Tuple[int, int]]:
        # print(f"starting: ({row}, {col})")
        coords = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
        filtered = list(filter(lambda coord: 0 <= coord[0] < self.num_row and 0 <= coord[1] < self.num_col, coords))
        # print(f"coords: {coords}")
        # print(f"Filtered: {filtered}")
        return filtered

    def adjacent_is_rotten(self, row: int, col: int) -> bool:
        coords = self.get_surrounding_coords(row, col)
        # Filter out empty and fresh oranges
        return list(filter(lambda coord: self.get_coord(coord) in (0, 1), coords))

    def no_adjacent(self, row: int, col: int) -> bool:
        return len(self.get_surrounding_coords(row, col)) == 0

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        input_grid = grid
        grid = Grid(input_grid)
        next_grid = Grid(input_grid)

        minute = 0
        while True:
            all_rotten = True
            for row in range(grid.num_row):
                for col in range(grid.num_col):
                    orange = grid.get(row, col)
                    if orange == 0:
                        continue
                    
                    if grid.no_adjacent(row, col):
                        return -1

                    if orange != 2:
                        all_rotten = False

                    if grid.adjacent_is_rotten(row, col):
                        next_grid.set_value(row, col, 2)
            minute += 1
            grid = copy.deepcopy(next_grid)
            if all_rotten:
                return minute
        
# @lc code=end
