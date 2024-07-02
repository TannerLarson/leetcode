#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Three functions:
        - Check row
        - Check column
        - check box
        
        A row/col/box is valid:
        1. Loop through list, add each character to a set
        2. If any number already exists in the set, return false
        3. Otherwise return true
        """
        rows = board
        columns = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]
        
        for i_row in range(9):
            for i_col in range(9):
                current_value = rows[i_row][i_col]
                columns[i_col].append(current_value)
                boxes[(i_row // 3) * 3 + i_col // 3].append(current_value)
                
        print(f"Rows: {rows}")
        print(f"Columns: {columns}")
        print(f"Boxes: {boxes}")
        
        return self.rows_are_valid(rows) and self.rows_are_valid(columns) and self.rows_are_valid(boxes)
        
    def rows_are_valid(self, rows: List[List[str]]) -> bool:
        for row in rows:
            values = set()
            for char in row:
                if char != "." and char in values:
                    return False
                values.add(char)
        return True
        
# @lc code=end

