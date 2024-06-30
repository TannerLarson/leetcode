#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
from typing import List

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 1):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Exit if we've hit the target
            if closest == target:
                return closest
            
            i_left = i + 1
            i_right = len(nums) - 1
            while i_left < i_right:
                # print(f"{i}, {i_left}, {i_right}")
                s = nums[i_left] + nums[i_right] + nums[i]
                if abs(target - s) < abs(target - closest):
                    closest = s
                    
                if s < target:
                    i_left += 1
                else:
                    i_right -= 1
        return closest
                
                
        
        
# @lc code=end

