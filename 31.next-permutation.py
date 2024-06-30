#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse loop through nums
        
        # if next num
        
        """
        [1, 2, 3, 4]
        [1, 2, 4, 3]
        [1, 3, 2, 4]
        [1, 3, 4, 2]
        [1, 4, 2, 3]
        [1, 4, 3, 2]
        
        [2, 1, 3, 4]
        [2, 1, 4, 3]
        [2, 3, 1, 4]
        ...
        
        
        [2, 1, 3, 5]
        
        1. Loop through nums until we find one that is less than the previous
        
        2. also loop through a sorted version of nums
        
        """
        
# @lc code=end

