#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


"""
Trivial solution:
1. For each number
2. Calculate all possible volumes for all other numbers to the right
3. Record the biggest
4. If a bigger value is found, update biggest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i_left in range(len(height)):
            for i_right in list(range(len(height)))[i_left + 1:]:
                area = min(height[i_left], height[i_right]) * (i_right - i_left)
                max_area = max(area, max_area)
                
        return max_area

O(n!) = really bad

Better solution:
1. Have two pointer indexes, both starting at either end
2. Calculate the volume between these two, replacing max if bigger
3. Move index with shorter height in. Move left if same


[3, 3, 1, 1]

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i_left = 0
        i_right = len(height) - 1
        
        while True:
            area = (i_right - i_left) * min(height[i_right], height[i_left])
            print(area)
            max_area = max(max_area, area)
            if i_left == i_right:
                return max_area
            if height[i_left] <= height[i_right]:
                i_left += 1
            else:
                i_right -= 1
                
        
# @lc code=end
