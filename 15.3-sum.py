#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

"""
Trivial:
1. i, j, k
2. Add values at i and J
3. Increment k until we get to end of nums
4. Keep track of the times i + j + k == 0
5. increment j by one, put k right next to j

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        values = (nums[i], nums[j], nums[k])
                        result.add(tuple(sorted(values)))
        return sorted(result)

Idea:
1. Sort nums
2. i = 0, j = 1, k = len(nums)
3. 

{
    0: (2, -2), 
}
"""

# @lc code=start
from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Sort nums for faster computation
        nums.sort()
        # Loop through each num once
        for i in range(len(nums) - 1):
            # Because the list is sorted, duplicates will be adjacent to one another
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Create two more pointers i_left and i_right
            i_left = i + 1
            i_right = len(nums) - 1
            while i_left != i_right:
                # Calculate sum and target
                s = nums[i_left] + nums[i_right]
                target = nums[i] * -1
                
                # Check if we have a result
                if s == target:
                    result.append([nums[i], nums[i_left], nums[i_right]])
                
                # Incrementing i_left will always increase the sum. Therefore, 
                # if the sum is less than the target, we should increase i_left. 
                # Otherwise, increase i_right
                if s < target:
                    i_left += 1
                else:
                    i_right -= 1
                    
        # Remove duplicate triplets
        result = sorted({tuple(r) for r in result})
        return result
        
# @lc code=end

