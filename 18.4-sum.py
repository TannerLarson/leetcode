#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        
        """
        target = 1
        [-2, -1, 0, 0, 1, 2]
        ll = 0 -> -2
        l  = 2 ->  0
        r  = 4 ->  1
        rr = 5 ->  2
        total = 1
        
        [-1,0,1,2], [-1,0,0,2]
        """
        print(nums)
        results = []
        # Four pointers, two starting on left, two starting on right
        ll = 0
        l_prev = 0
        l_next = 2
        l = 1
        r = len(nums) - 2
        r_next = len(nums) - 3
        r_prev = len(nums) - 1
        rr = len(nums) - 1
        
        while True:
            if l == ll or r == rr:
                break
            print(f"{ll}, {l}, {r}, {rr}")
            
            # Add values to result if they add up to target
            s = nums[ll] + nums[l] + nums[r] + nums[rr]
            if s == target:
                results.append([nums[ll], nums[l], nums[r], nums[rr]])
                
            # Check if we should break
            if (nums[l_next] == nums[r]) and ll == l_prev and rr == r_prev:
                break
                
            # If sum is less than target, increment a left pointer. Otherwise decrement a right pointer
            if s < target or abs(nums[l] - nums[l_next]) < abs(nums[r] - nums[r_next]):
                # if ll is equal to l_prev, increment l
                if ll != l_prev:
                    ll = l_prev
                    continue
                l_prev = l
                l = l_next
                while nums[l] == nums[l_next] and l_next < r - 1:
                    l_next += 1
                continue
            
            if s == target:
                continue
            
            if rr != r_prev:
                rr = r_prev
                continue
            r_prev = r
            r = r_next
            while nums[r] == nums[r_next] and r_next > l + 1:
                r_next -= 1
        
        results = {tuple(r) for r in results}
        return results
    
        
# @lc code=end

