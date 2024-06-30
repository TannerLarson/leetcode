#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        target = 9
        nums[left]  = 8
        nums[mid]   = 2
        nums[right] = 4
        """
        # create three pointers, left, mid, right
        left = 0
        right = len(nums) - 1
        mid = None
        
        while True:
            # calculate new mid
            mid = int((right + left) / 2)
        
            # return target index if nums[mid/left/right] == target
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            # return -1 if right - left == 2
            if right - left <= 2:
                return -1
            
            # if target is between left and mid, set right equal to mid. Otherwise set left equal to mid
            if nums[mid] < nums[left]:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        
# @lc code=end

