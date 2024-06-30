#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
"""
1. Binary search until with find target
2. Iterate left and right until both left and right are not equal to target
3. return indeces
O(log n * n / 2)

1. Binary search for index directly left of number and directly right of number
O(2log n)
"""
from typing import List
class Solution:
    def search_left(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right        
        while True:
            print(f"{left}, {right}")
            mid = int((left + right) / 2)
            
            if left >= right:
                return left + 1
            
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Make sure target is inside nums
        if not (nums[0] <= target <= nums[-1]):
            return -1
            
        left = self.search_left(nums, target)
        
        if left == -1:
            return [-1, -1]
        
        return [left, 0]
        
# @lc code=end

